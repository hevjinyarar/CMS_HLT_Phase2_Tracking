#!/usr/bin/env python

from __future__ import print_function
import copy
import math
import array
import collections

import ROOT
ROOT.gROOT.SetBatch(True)
ROOT.PyConfig.IgnoreCommandLineOptions = True

import Validation.RecoTrack.plotting.plotting as plotting
import Validation.RecoTrack.plotting.trackingPlots as trackingPlots

_colorindex = 2000
_colortmp = {}
def makeColor(hexstr):
    r = int("0x"+hexstr[0:2], 16)
    g = int("0x"+hexstr[2:4], 16)
    b = int("0x"+hexstr[4:6], 16)
    
    global _colorindex
    global _colortmp

    _colorindex += 1
    _colortmp[_colorindex] = ROOT.TColor(_colorindex, r/255., g/255., b/255.)
    return _colorindex

iter_colors = dict(
    InitialStep         = makeColor("cde7ff"),
    HighPtTripletStep   = makeColor("b2d3f3")
)

class Files:
    def __init__(self, filesLegends):
        self._files = []
        self._legends = []
        self._styles = []
        for fl in filesLegends:
            self._legends.append(fl[1])
            self._styles.append(fl[2])
            if isinstance(fl[0], tuple):
                self._files.append([ROOT.TFile.Open(f) for f in fl[0]])
            else:
                self._files.append(ROOT.TFile.Open(fl[0]))

    def getFiles(self):
        return self._files

    def getHistos(self, name):
        ret = []
        for f in self._files:
            path = "DQMData/Run 1/"+name
            if isinstance(f, list):
                fil = f[0]
                #if "cutsRecoPt" in name:
                #    path = "DQMData/Run 1/"+name.replace("cutsRecoPt", "cutsReco")
                #    fil = f[1]
                obj = fil.Get(path)
            else:
                #if "cutsRecoPt" in name:
                #    path = "DQMData/Run 1/"+name.replace("cutsRecoPt", "cutsReco")
                obj = f.Get(path)
            if not obj:
                raise Exception("Object %s not found from %s" % (path, f.GetPath()))
            ret.append(obj)
        return ret

    def getLegends(self):
        return self._legends

    def getStyles(self):
        return self._styles

def applyStyle(h, color, markerStyle):
    h.SetMarkerStyle(markerStyle)
    h.SetMarkerColor(color)
    h.SetMarkerSize(1.2)
    h.SetLineColor(color)
    h.SetLineWidth(2)

#styles = [
##    lambda h: applyStyle(h, ROOT.kBlack, 34),
##    lambda h: applyStyle(h, ROOT.kBlue, 21),
##    lambda h: applyStyle(h, ROOT.kRed, 22),
##    lambda h: applyStyle(h, ROOT.kGreen, 20),
#    lambda h: applyStyle(h, ROOT.kBlack, 21),
#    lambda h: applyStyle(h, ROOT.kBlue, 20),
#    lambda h: applyStyle(h, ROOT.kRed, 22),
#    lambda h: applyStyle(h, ROOT.kGreen, 34),
#]

class Plot:
    def __init__(self, histos, legends, styles):
        self._histos = histos[:]
        self._legends = legends[:]
        self._styles = styles[:]

    def remove(self, i):
        del self._histos[i]
        del self._legends[i]
        del self._styles[i]

    def histos(self):
        return self._histos

    def setHistos(self, histos):
        if len(self._histos) != len(histos):
            raise Exception("Had %d histograms, was trying to set %d" % (len(self._histos), len(histos)))
        self._histos = histos

    def scale(self, scale):
        for h in self._histos:
            h.Scale(scale)

    def rebin(self, rebin):
        for h in self._histos:
            h.Rebin(rebin)

    def normalizeToUnitArea(self):
        for h in self._histos:
            if h is None:
                continue
            i = h.Integral()
            if i == 0:
                continue
            if h.GetSumw2().fN <= 0: # to suppress warning
                h.Sumw2()
            h.Scale(1.0/i)

    def draw(self, opt=""):
        self._isHist = ("hist" in opt.lower())

        for h, style in zip(self._histos, self._styles):
            style(h)
            if self._isHist:
                h.SetLineWidth(3)

            h.Draw("same"+opt)

    def addToLegend(self, legend, legendColumns):
        st = "LP"
        if self._isHist:
            st = "L"

        for h, label in zip(self._histos, self._legends):
            legend.AddEntry(h, label, st)

    def getXmin(self):
        if len(self._histos) == 0:
            return 0
        return min([h.GetXaxis().GetBinLowEdge(h.GetXaxis().GetFirst()) for h in self._histos])

    def getXmax(self):
        if len(self._histos) == 0:
            return 1
        return max([h.GetXaxis().GetBinUpEdge(h.GetXaxis().GetLast()) for h in self._histos])

    def getYmax(self):
        if len(self._histos) == 0:
            return 1
        return max([h.GetMaximum() for h in self._histos])

class PlotStack:
    def __init__(self):
        self._histos = []
        self._legends = []

    def add(self, histo, legend):
        self._histos.append(histo)
        self._legends.append(legend)

    def draw(self, opt=""):
        self._stack = ROOT.THStack()
        for h in self._histos:
            self._stack.Add(h)
        self._stack.Draw("nostack"+opt)#same

    def addToLegend(self, legend, legendColumns):
        st = "f"
        for h, label in zip(self._histos, self._legends):
            legend.AddEntry(h, label, st)



class PlotText:
    ## Constructor
    #
    # \param x       X coordinate of the text (in NDC)
    # \param y       Y coordinate of the text (in NDC)
    # \param text    String to draw
    # \param size    Size of text (None for the default value, taken from gStyle)
    # \param bold    Should the text be bold?
    # \param align   Alignment of text (left, center, right)
    # \param color   Color of the text
    # \param font    Specify font explicitly
    def __init__(self, x, y, text, size=None, bold=True, align="left", color=ROOT.kBlack, font=None):
        self.x = x
        self.y = y
        self.text = text

        self.l = ROOT.TLatex()
        self.l.SetNDC()
        if not bold:
            self.l.SetTextFont(self.l.GetTextFont()-20) # bold -> normal
        if font is not None:
            self.l.SetTextFont(font)
        if size is not None:
            self.l.SetTextSize(size)
        if isinstance(align, basestring):
            if align.lower() == "left":
                self.l.SetTextAlign(11)
            elif align.lower() == "center":
                self.l.SetTextAlign(21)
            elif align.lower() == "right":
                self.l.SetTextAlign(31)
            else:
                raise Exception("Error: Invalid option '%s' for text alignment! Options are: 'left', 'center', 'right'."%align)
        else:
            self.l.SetTextAlign(align)
        self.l.SetTextColor(color)

    ## Draw the text to the current TPad
    #
    # \param options   For interface compatibility, ignored
    #
    # Provides interface compatible with ROOT's drawable objects.
    def Draw(self, options=None):
        self.l.DrawLatex(self.x, self.y, self.text)        

## Class for drawing text and a background box
class PlotTextBox:
    ## Constructor
    #
    # \param xmin       X min coordinate of the box (NDC)
    # \param ymin       Y min coordinate of the box (NDC) (if None, deduced automatically)
    # \param xmax       X max coordinate of the box (NDC)
    # \param ymax       Y max coordinate of the box (NDC)
    # \param lineheight Line height
    # \param fillColor  Fill color of the box
    # \param transparent  Should the box be transparent? (in practive the TPave is not created)
    # \param kwargs       Forwarded to histograms.PlotText.__init__()
    def __init__(self, xmin, ymin, xmax, ymax, lineheight=0.05, fillColor=ROOT.kWhite, transparent=True, **kwargs):
        # ROOT.TPave Set/GetX1NDC() etc don't seem to work as expected.
        self.xmin = xmin
        self.xmax = xmax
        self.ymin = ymin
        self.ymax = ymax
        self.lineheight = lineheight
        self.fillColor = fillColor
        self.transparent = transparent
        self.texts = []
        self.textArgs = {}
        self.textArgs.update(kwargs)

        self.currenty = ymax

    def clone(self):
        return copy.deepcopy(self)

    ## Add text to current position
    def addText(self, text, yspace=0):
        self.currenty -= self.lineheight
        self.currenty -= yspace
        self.addPlotObject(PlotText(self.xmin+0.01, self.currenty, text, **self.textArgs))

    def replaceText(self, index, text):
        y = self.currenty + (len(self.texts)-1-index)*self.lineheight
        self.replacePlotObject(index, PlotText(self.xmin+0.01, y, text, **self.textArgs))

    def removeText(self, index):
        self.currenty += self.lineheight
        self.removePlotObject(index)

    ## Add PlotText object
    def addPlotObject(self, obj):
        self.texts.append(obj)

    def replacePlotObject(self, index, obj):
        self.texts[index] = obj

    def removePlotObject(self, index):
        del self.texts[index]

    ## Move the box and the contained text objects
    #
    # \param dx  Movement in x (positive is to right)
    # \param dy  Movement in y (positive is to up)
    # \param dw  Increment of width (negative to decrease width)
    # \param dh  Increment of height (negative to decrease height)
    #
    # \a dx and \a dy affect to both box and text objects, \a dw and
    # \dh affect the box only.
    def move(self, dx=0, dy=0, dw=0, dh=0):
        self.xmin += dx
        self.xmax += dx
        if self.ymin is not None:
            self.ymin += dy
        self.ymax += dy
        self.currenty += dy

        self.xmax += dw
        if self.ymin is not None:
            self.ymin -= dh

        for t in self.texts:
            t.x += dx
            t.y += dy

    ## Draw the box and the text to the current TPad
    #
    # \param options  Forwarded to ROOT.TPave.Draw(), and the Draw() of the contained objects
    def Draw(self, options=""):
        if not self.transparent:
            ymin = self.ymin
            if ymin is None:
                ymin = self.currenty - 0.02
            self.pave = ROOT.TPave(self.xmin, ymin, self.xmax, self.ymax, 0, "NDC")
            self.pave.SetFillColor(self.fillColor)
            self.pave.Draw(options)
        for t in self.texts:
            t.Draw(options)

def calculateEfficiency(tfile, num_name, denom_name, rebin=None):
    num = tfile.Get(num_name)
    denom = tfile.Get(denom_name)
    if not num:
        raise Exception("Did not find %s from %s" % (num_name, tfile.GetName()))
    if not denom:
        raise Exception("Did not find %s from %s" % (denom_name, tfile.GetName()))

    eff = num.Clone()
    den = denom.Clone()
    if rebin is not None:
        eff.Rebin(rebin)
        den.Rebin(rebin)
    eff.Divide(den)
    return eff
                               
def main():
    ROOT.gROOT.LoadMacro("tdrstyle.C")
    ROOT.setTDRStyle()
    ROOT.gROOT.LoadMacro("CMS_lumi_v2.C")

    ROOT.gStyle.SetTitleYOffset(1.0)
    ROOT.gStyle.SetPadGridX(True)
    ROOT.gStyle.SetPadGridY(True)

    stylePU0    = lambda h: applyStyle(h, ROOT.kBlack, 21) 
    stylePU200  = lambda h: applyStyle(h, ROOT.kViolet, 34)

    pileup0   = "v4"#"#LTPU#GT=0"
    pileup200 = "v6"#"#LTPU#GT=200"

    files = Files([

	#("DQM_v2.root",   "v2",  stylePU0),
	("DQM_v4.root",   "v4",  stylePU0),
        ("DQM_v6.root", "v6",stylePU200), 
        ])

    plotEffAndFake(files, "ttbar_pu200_phase2", pileup200)
    plotVertex    (files, "ttbar_pu200_phase2", pileup200)
    #plotPixelVertex    (files, "ttbar_pu200_phase2", pileup200)
    plotResol     (files, "ttbar_pu200_phase2", pileup200)
    plotColoredEff(files.getFiles()[0], "ttbar_pu0_phase2",    pileup0,   isPhase2 = True)
    plotColoredEff(files.getFiles()[1], "ttbar_pu200_phase2",  pileup200, isPhase2 = True)
    #plotDebug     (files, "ttbar_pu200_phase2")

#    plotTime([files0pu_time, filespu_time], "ttbar_phase0_phase1_vs_pu", [0, 35, 50, 70], ["2016", "2017"], [styleRun2, stylePhase1])
#    plotTime([files0pu_time, filespu_time, filescapu_time], "ttbar_phase0_phase1ca_vs_pu", [0, 35, 50, 70], ["2016", "2017", "2017 (CA)"], [styleRun2, stylePhase1, stylePhase1CA])

    # trackingOnly with DQM+validation enabled, 1 thread
    if False:
        peakrss = {
            "2016": {0: 1515.45,
                     35: 1820.23,
                     50: 2021.14,
                     70: 2375.56},
            "2017": {0: 1696.24,
                     35: 2110.91,
                     50: 2190.12,
                     70: 2674.59},
            "2017 (CA)": {0: 1697.5,
                          35: 2213.77,
                          50: 2413.3,
                          70: 2795.5},
        }
        
        # trackingOnly without DQM+validation, no output modules, 4 threads
        peakrss = {
            "2016": {0: 1278.68,
                     35: 1664.89,
                     50: 1888.64,
                     70: 2314.17},
            "2017": {0: 1435.69,
                     35: 2143.47,
                     50: 2525.84,
                     70: 2915.48},
            "2017 (CA)": {0: 1452.07,
                          35: 2266.03,
                          50: 2502.52,
                          70: 3051.34},
        }
        
        peakrss_v2 = {
            "2016": {0: 1267.67,
                     35: 1674.13,
                     50: 1853.39,
                     70: 2192.17},
            "2017": {0: 1434.75,
                     35: 2123.64,
                     50: 2335.03,
                     70: 2667.48},
            "2017 (CA)": {0: 1441.02,
                          35: 2191.23,
                          50: 2445.68,
                          70: 2729.58},
        }
        
        peakrss_trajectory = {
            "2017 90X IB": {0: 1445.08,
                         35: 2112.86,
                         50: 2320.14,
                         60: 2578.23},
            "2017 90X IB+#17098": {0: 1422.88,
                                   35: 1974.98,
                                   50: 2128.61,
                                   60: 2300.59},
        }
        
        plotMemory("ttbar_phase0_phase1_vs_pu", peakrss, ["2016", "2017"], [styleRun2, stylePhase1])
        plotMemory("ttbar_phase0_phase1ca_vs_pu", peakrss, ["2016", "2017", "2017 (CA)"], [styleRun2, stylePhase1, stylePhase1CA])
        
        plotMemory("90x_ttbar_phase1_vs_pu", peakrss_trajectory, ["2017 90X IB", "2017 90X IB+#17098"], [stylePhase1, stylePhase1CA])

#    printEffFake(files1, pileup)
#    print("With CA")
#    printEffFake(files1ca, pileup)

    printEffFake(files, pileup200)
   

################################################################################
################################################################################
################################################################################
def plotDebug(files, prefix):
    folder_dqm = "Tracking/Run summary/TrackParameters/"

    _common = {
#        "xmin": -3, "xmax": 3, "ymin": 0, "ymax": 1,
        "ymax": 5e-1,
        "legendDx": -0.27, "legendDy": -0.0, #"legendDw": legendDw,
        "ylog": True
    }

    plot = Plot(files.getHistos(folder_dqm+"generalTracks/GeneralProperties/TrackPErrOverP_ImpactPoint_GenTk"), files.getLegends(), files.getStyles())
    for h in plot._histos:
        h.Scale(1.0/h.Integral())
    drawPlot(prefix+"_dqm_perroverp", plot, ymin=1e-4, **_common)

    plot = Plot(files.getHistos(folder_dqm+"generalTracks/GeneralProperties/TrackPtErrOverPt_ImpactPoint_GenTk"), files.getLegends(), files.getStyles())
    for h in plot._histos:
        h.Scale(1.0/h.Integral())
    drawPlot(prefix+"_dqm_pterroverpt", plot, ymin=1e-5, **_common)

    plot = Plot(files.getHistos(folder_dqm+"generalTracks/GeneralProperties/TrackEtaErr_ImpactPoint_GenTk"), files.getLegends(), files.getStyles())
    for h in plot._histos:
        h.Scale(1.0/h.Integral())
    drawPlot(prefix+"_dqm_etaerr", plot, ymin=1e-8, **_common)

################################################################################
################################################################################
################################################################################
def plotEffAndFake(files, prefix, pileup, hasPU70=True, hasCA=True):
    folder_eff = "Tracking/Run summary/Track/hltPhase2CutsRecoHp_hltPhase2ingParticleRecoTrackAsssociation/"
    #folder_eff = "Tracking/Run summary/TrackFromPV/hltPhase2CutsRecoFromPVHp_hltPhase2ingParticleRecoTrackAsssociation/"
    folder_fake = "Tracking/Run summary/Track/hltPhase2CutsRecoPt09Hp_hltPhase2ingParticleRecoTrackAsssociation/"
    #folder_fake = "Tracking/Run summary/TrackFromPV/hltPhase2CutsRecoFromPVPt09Hp_hltPhase2ingParticleRecoTrackAsssociation/"

    isrun2 = ("run2" in prefix)
    isrun2real = isrun2 and (len(files.getFiles()) == 3)

    xmin = 0.33
    xmax = 0.87
    legendDw = -0.1
    if isrun2:
        legendDw = 0
        #legendDw = -0.1
    if isrun2real:
        legendDw = 0.25

    putext = ""
    if pileup is not None:
        putext = " (%s)" % pileup

    effbox = PlotTextBox(xmin, None, xmax, 0.31, transparent=False)
    effbox.addText("t#bar{t} event tracks%s"%putext)
    effbox.addText("p_{T} > 0.9 GeV, ^{}d_{0} < 2.5 cm")

    fakebox = PlotTextBox(xmin, None, xmax-0.04, 0.85, transparent=False)
    fakebox.addText("t#bar{t} event tracks%s"%putext)
    fakebox.addText("p_{T} > 0.9 GeV")


    # eta
    effbox_eta = effbox.clone()
    effbox_eta.replaceText(1, "p_{T} > 0.9 GeV")
    plot = Plot(files.getHistos(folder_eff+"effic"), files.getLegends(), files.getStyles())
    _common = {
        "xtitle": "Simulated track #eta",
        "xmin": -4.5, "xmax": 4.5, "ymin": 0, "ymax": 1, #3-->4.5
        "legendDx": -0.27, "legendDy": -0.4, "legendDw": legendDw,
        "customise": lambda: effbox_eta.Draw()
    }
    if isrun2real:
        _common["legendTextSize"] = 0.035
        _common["legendDx"] -= 0.05

    drawPlot(prefix+"_efficiency_eta", plot, ytitle="Tracking efficiency", **_common)
               
    _common["xtitle"] = "Track #eta"
    _common["ymin"] = 0
    _common["ymax"] = 0.4
    _common["legendDy"] = -0.2
    _common["customise"] = lambda: fakebox.Draw()

    plot = Plot(files.getHistos(folder_fake+"fakerate"),
                files.getLegends(), files.getStyles())
    drawPlot(prefix+"_fakerate_eta", plot, ytitle="Tracking fake rate", **_common)

    _common["ymax"] = 0.1
    #plot = Plot(files.getHistos(folder_fake+"duplicatesRate"),
    #            files.getLegends(), files.getStyles())
    #drawPlot(prefix+"_duprate_eta", plot, ytitle="Tracking duplicate rate", **_common)


    # phi
    effbox_phi = effbox.clone()
    effbox_phi.replaceText(1, "p_{T} > 0.9 GeV")
    plot = Plot(files.getHistos(folder_eff+"effic_vs_phi"), files.getLegends(), files.getStyles())
    _common = {
        "xtitle": "Simulated track #phi",
        "xmin": -3.5, "xmax": 3.5, "ymin": 0, "ymax": 1, 
        "legendDx": -0.27, "legendDy": -0.4, "legendDw": legendDw,
        "customise": lambda: effbox_phi.Draw()
    }
    if isrun2real:
        _common["legendTextSize"] = 0.035
        _common["legendDx"] -= 0.05

    drawPlot(prefix+"_efficiency_phi", plot, ytitle="Tracking efficiency", **_common)
               
    _common["xtitle"] = "Track #phi"
    _common["ymin"] = 0
    _common["ymax"] = 0.2
    _common["legendDy"] = -0.2
    _common["customise"] = lambda: fakebox.Draw()

    plot = Plot(files.getHistos(folder_fake+"fakerate_vs_phi"),
                files.getLegends(), files.getStyles())
    drawPlot(prefix+"_fakerate_phi", plot, ytitle="Tracking fake rate", **_common)

    _common["ymax"] = 0.1
    #plot = Plot(files.getHistos(folder_fake+"duplicatesRate_phi"),
    #            files.getLegends(), files.getStyles())
    #drawPlot(prefix+"_duprate_phi", plot, ytitle="Tracking duplicate rate", **_common)

    # pT
    effbox_pt = effbox.clone()
    effbox_pt.replaceText(1, "")
    effbox_pt.move(dx=0.05)
    fakebox_pt = fakebox.clone()
    fakebox_pt.removeText(1)
    plot = Plot(files.getHistos(folder_eff+"efficPt"), files.getLegends(), files.getStyles())
    _common = {
        "xtitle": "Simulated track p_{T} (GeV)",
        "xmin": 1e-1, "xmax": 2e2, "ymin": 0, "ymax": 1,
        "xlog": True,
        "legendDx": -0.22, "legendDy": -0.4, "legendDw": legendDw,
        "customise": lambda: effbox_pt.Draw()
    }
    if isrun2real:
        _common["legendTextSize"] = 0.035
        _common["legendDx"] -= 0.05
    drawPlot(prefix+"_efficiency_pt", plot, ytitle="Tracking efficiency", **_common)
               
    _common["xtitle"] = "Track p_{T} (GeV)"
    _common["ymin"] = 0
    _common["ymax"] = 0.6
    _common["legendDy"] = -0.2
    _common["customise"] = lambda: fakebox_pt.Draw()
    if isrun2real:
        _common["legendDx"] -= 0.05
        _common["legendDy"] += 0.06

    folder_fake_pt = folder_fake.replace("Pt09", "")
    plot = Plot(files.getHistos(folder_fake_pt+"fakeratePt"),
                files.getLegends(), files.getStyles())
    drawPlot(prefix+"_fakerate_pt", plot, ytitle="Tracking fake rate", **_common)

    _common["ymax"] = 0.1
    #plot = Plot(files.getHistos(folder_fake_pt+"duplicatesRate_Pt"),
    #            files.getLegends(), files.getStyles())
    #drawPlot(prefix+"_duprate_pt", plot, ytitle="Tracking duplicate rate", **_common)

    # sim vertex z
    plot = Plot(files.getHistos(folder_eff+"effic_vs_simpvz"), files.getLegends(), files.getStyles())
    _common = {
        "xtitle": "Simulated vertex z (cm)",
        "xmin": -30., "xmax": 30., "ymin": 0, "ymax": 1,
        "xlog": False,
        "legendDx": -0.22, "legendDy": -0.4, "legendDw": legendDw,
        "customise": lambda: effbox_pt.Draw()
    }
    if isrun2real:
        _common["legendTextSize"] = 0.035
        _common["legendDx"] -= 0.05
    drawPlot(prefix+"_efficiency_simpvz", plot, ytitle="Tracking efficiency", **_common)
               
    _common["xtitle"] = "Simulated vertex z (cm)"
    _common["ymin"] = 0
    _common["ymax"] = 1.0
    _common["legendDy"] = -0.2
    _common["customise"] = lambda: fakebox_pt.Draw()
    if isrun2real:
        _common["legendDx"] -= 0.05
        _common["legendDy"] += 0.06

    _common["ymax"] = 0.1
    #plot = Plot(files.getHistos(folder_fake_pt+"duplicatesRate_Pt"),
    #            files.getLegends(), files.getStyles())
    #drawPlot(prefix+"_duprate_pt", plot, ytitle="Tracking duplicate rate", **_common)

    # r
    effbox_r = effbox.clone()
    effbox_r.move(dy=0.6)
    effbox_r.replaceText(1, "p_{T} > 0.9 GeV")
    fakebox_r = fakebox.clone()
    fakebox_r.move(dy=-0.55, dx=0.1)
    plot = Plot(files.getHistos(folder_eff+"effic_vs_vertpos"), files.getLegends(), files.getStyles())
    _common = {
        "xtitle": "Sim. track prod. vertex radius (cm)",
        "xmin": 0, "xmax": 60, "ymin": 0, "ymax": 1,
        "legendDx": 0.1, "legendDy": -0.12, "legendDw": legendDw,
        "customise": lambda: effbox_r.Draw()
    }
    if isrun2:
        _common["legendDx"] = -0.35
        _common["legendDy"] = -0.55
    if isrun2real:
        _common["legendTextSize"] = 0.035
        _common["legendDx"] -= 0.05
        _common["legendDy"] -= 0.02
    if hasPU70 and hasCA:
        _common["legendDx"] -= 0.1

    drawPlot(prefix+"_efficiency_r", plot, ytitle="Tracking efficiency", **_common)

    #####################################
    # d0
    effbox_d0 = effbox.clone()
    effbox_d0.replaceText(1, "")
    effbox_d0.replaceText(0, "")
    plot = Plot(files.getHistos(folder_eff+"effic_vs_dxypv_zoomed"),files.getLegends(), files.getStyles()) #pv"),#_zoomed"), 
    _common = {
        "xtitle": "Simulated track dxy",
        "xmin": -1.2, "xmax": 1.2, "ymin": 0, "ymax": 1, #3-->4.5
        "legendDx": -0.35, "legendDy": -0.4, "legendDw": legendDw#,
        #"customise": lambda: effbox_d0.Draw()
    }
    if isrun2real:
        _common["legendTextSize"] = 0.035
        _common["legendDx"] -= 0.05

    drawPlot(prefix+"_efficiency_dxy", plot, ytitle="Tracking efficiency", **_common)

    # dz
    effbox_dz = effbox.clone()
    effbox_dz.replaceText(1, "")
    effbox_dz.replaceText(0, "")
    #effbox_dz.replaceText(1, "p_{T} > 0.9 GeV")
    plot = Plot(files.getHistos(folder_eff+"effic_vs_dzpv_zoomed"),files.getLegends(), files.getStyles())#pv"),#_zoomed"), files.getLegends(), files.getStyles())
    _common = {
        "xtitle": "Simulated track dz",
        "xmin": -1.5, "xmax": 1.5, "ymin": 0, "ymax": 1, #3-->4.5
        "legendDx": -0.1, "legendDy": -0.4, "legendDw": legendDw#,
        #"customise": lambda: effbox_dz.Draw()
    }
    if isrun2real:
        _common["legendTextSize"] = 0.035
        _common["legendDx"] -= 0.05

    drawPlot(prefix+"_efficiency_dz", plot, ytitle="Tracking efficiency", **_common)



    #######################################
    _common["xtitle"] = "Track PCA radius (cm)"
    _common["ymin"] = 0
    #_common["ymax"] = 0.6
    _common["ymax"] = 1
    _common["legendDy"] = -0.35
    _common["customise"] = lambda: fakebox_r.Draw()
    if isrun2:
        _common["legendDx"] = 0
    if isrun2real:
        _common["legendDx"] -= 0.25
        _common["legendDy"] -= 0.2
        fakebox_r.move(dy=0.2, dx=0.02)
    if hasPU70:
        _common["ymax"] = 1
        _common["legendDx"] -= 0.05
        fakebox_r.move(dy=0.0, dx=0.2, dw=-0.2)
        if hasCA:
            _common["legendDx"] += 0.07
            _common["legendDw"] += 0.1
            _common["legendDy"] -= 0.2
            fakebox_r.move(dy=0.2)
            

    plot = Plot(files.getHistos(folder_fake+"fakerate_vs_vertpos"),
                files.getLegends(), files.getStyles())
    drawPlot(prefix+"_fakerate_r", plot, ytitle="Tracking fake rate", **_common)

    _common["ymax"] = 0.1
    fakebox_r.move(dx=-0.2, dy=0.4)
    if hasPU70:
        fakebox_r.move(dx=0.1)
    #plot = Plot(files.getHistos(folder_fake+"duplicatesRate_vertpos"),
    #            files.getLegends(), files.getStyles())
    #drawPlot(prefix+"_duprate_r", plot, ytitle="Tracking duplicate rate", **_common)


################################################################################
################################################################################
################################################################################
def plotColoredEff(phase1file, prefix, pileup, isPhase2 = False):
    #folder_track = "DQMData/Run 1/Tracking/Run summary/Track/cutsReco%s_trackingParticleRecoAsssociation/"
    #folder_track = "DQMData/Run 1/Tracking/Run summary/Track/cutsReco%sHp_trackingParticleRecoAsssociation/"
    folder_track = "DQMData/Run 1/Tracking/Run summary/Track/hltPhase2CutsReco%sByOriginalAlgoHp_hltPhase2ingParticleRecoTrackAsssociation/"
    iterations = [
        "InitialStep",
        "HighPtTripletStep"#,
    ]

    if isPhase2 :
        iterations = [
            "InitialStep",
            "HighPtTripletStep"
            ]

    legendLabels = [x.replace("Step", "").replace("Regional", "").replace("SeededInOut", " inside-out").replace("SeededOutIn", " outside-in") for x in iterations]
    legendLabels[1:] = ["+"+x for x in legendLabels[1:]]

    putext = ""
    if pileup is not None:
        putext = " (%s)" % pileup

    xmin = 0.33
    xmax = 0.87
    legendDw = 0
    effbox = PlotTextBox(xmin, None, xmax, 0.31, transparent=True)
    effbox.addText("t#bar{t} event tracks%s"%putext)
    effbox.addText("p_{T} > 0.9 GeV")

    # pt
    effbox_pt = effbox.clone()
    effbox_pt.replaceText(1, "")#|#eta| < 2.5, ^{}d_{0} < 3.5 cm")
    effbox_pt.move(dx=0.06, dy=-0.02)
#    effbox_pt.move(dx=-0.13, dy=0.6)
    plot = PlotStack()
    for it, leg in zip(iterations, legendLabels):
        hname = folder_track%it + "efficPt"
        h = phase1file.Get(hname)
        if not h:
            raise Exception("Did not find %s from %s" % (hname, phase1file.GetName()))
        h.SetFillColor(iter_colors[it])
        h.SetLineColor(ROOT.kBlack)
        plot.add(h, leg)
    _common = {
        "xtitle": "Simulated track p_{T} (GeV)",
        "xmin": 1e-1, "xmax": 2e2, "ymin": 0, "ymax": 1,
        "xlog": True,
        "legendDx": -0.13, "legendDy": -0.24, "legendDw": legendDw, "legendDh": 0.23,
        "legendTransparent": True,
        "customise": lambda: effbox_pt.Draw(),
        "drawOpt": "HIST",
    }
    drawPlot(prefix+"_efficiency_pt_cum", plot, ytitle="Tracking efficiency", **_common)
    

    # eta
    effbox_eta = effbox.clone()
    effbox_eta.replaceText(1, "p_{T} > 0.9 GeV, ^{}d_{0} < 2.5 cm")
    effbox_eta.move(dx=0.06, dy=-0.02)
#    effbox_pt.move(dx=-0.13, dy=0.6)
    plot = PlotStack()
    for it, leg in zip(iterations, legendLabels):
        hname = folder_track%it + "effic"
        h = phase1file.Get(hname)
        if not h:
            raise Exception("Did not find %s from %s" % (hname, phase1file.GetName()))
        h.SetFillColor(iter_colors[it])
        h.SetLineColor(ROOT.kBlack)
        plot.add(h, leg)
    _common = {
        "xtitle": "Simulated track #eta",
        "xmin": -4.5, "xmax": 4.5, "ymin": 0, "ymax": 1, #3-->4.5
        "legendDx": -0.15, "legendDy": -0.24, "legendDw": legendDw, "legendDh": 0.23,
        "legendTransparent": True,
        "customise": lambda: effbox_eta.Draw(),
        "drawOpt": "HIST",
    }
    drawPlot(prefix+"_efficiency_eta_cum", plot, ytitle="Tracking efficiency", **_common)


    # phi
    effbox_phi = effbox.clone()
    effbox_phi.replaceText(1, "p_{T} > 0.9 GeV, ^{}d_{0} < 2.5 cm")
    effbox_phi.move(dx=0.06, dy=-0.02)
#    effbox_pt.move(dx=-0.13, dy=0.6)
    plot = PlotStack()
    for it, leg in zip(iterations, legendLabels):
        hname = folder_track%it + "effic_vs_phi"
        h = phase1file.Get(hname)
        if not h:
            raise Exception("Did not find %s from %s" % (hname, phase1file.GetName()))
        h.SetFillColor(iter_colors[it])
        h.SetLineColor(ROOT.kBlack)
        plot.add(h, leg)
    _common = {
        "xtitle": "Simulated track #phi",
        "xmin": -3.5, "xmax": 3.5, "ymin": 0, "ymax": 1, 
        "legendDx": -0.15, "legendDy": -0.24, "legendDw": legendDw, "legendDh": 0.23,
        "legendTransparent": True,
        "customise": lambda: effbox_phi.Draw(),
        "drawOpt": "HIST",
    }
    drawPlot(prefix+"_efficiency_phi_cum", plot, ytitle="Tracking efficiency", **_common)
    
    # r
    effbox_r = effbox.clone()
    #effbox_r.replaceText(1, "p_{T} > 0.9 GeV,")
    effbox_r.removeText(1)
    effbox_r.addText("p_{T} > 0.9 GeV,", yspace=0.01)
    #effbox_r.addText("|#eta| < 2.5", yspace=0.01)
    effbox_r.transparent = False
    effbox_r.move(dx=-0.1, dy=0.6)
    _common = {
        "xtitle": "Sim. track prod. vertex radius (cm)",
        "xmin": 0, "xmax": 60, "ymin": 0, "ymax": 1.2,
        "legendDx": 0.02, "legendDy": -0.07, "legendDw": legendDw, "legendDh": 0.23,
#        "legendDx": -0.3, "legendDy": -0.12, "legendDw": legendDw+0.33, "legendDh": 0.05,
#        "legendColumns": 2,
#        "legendTransparent": True,
        "customiseBeforeLegend": lambda: effbox_r.Draw(),
        "drawOpt": "HIST",
    }
    plot = PlotStack()
    for it, leg in zip(iterations, legendLabels):
        #hname = folder_track%it + "effic_vs_vertpos"
        #h = phase1file.Get(hname)
        #if not h:
        #    raise Exception("Did not find %s from %s" % (hname, phase1file.GetName()))
        num_name = folder_track%it + "num_assoc(simToReco)_vertpos"
        denom_name = folder_track%it + "num_simul_vertpos"
        eff = calculateEfficiency(phase1file, num_name, denom_name, rebin=2)
        eff.SetFillColor(iter_colors[it])
        eff.SetLineColor(ROOT.kBlack)
        plot.add(eff, leg)

    drawPlot(prefix+"_efficiency_r_cum", plot, ytitle="Tracking efficiency", **_common)
    #"""
    ########### impact parameters
    # d0
    effbox_d0 = effbox.clone()
    effbox_d0.removeText(1)
    effbox_d0.addText("dxy", yspace=0.01)
    effbox_d0.transparent = True
    effbox_d0.move(dx=-0.1, dy=0.6)
    _common = {
        "xtitle": "impact parameter dxy",
        "xmin": -1.2, "xmax": 1.2, "ymin": 0, "ymax": 1,
        "legendDx": 0.02, "legendDy": -0.07, "legendDw": legendDw, "legendDh": 0.23,
#        "legendDx": -0.3, "legendDy": -0.12, "legendDw": legendDw+0.33, "legendDh": 0.05,
#        "legendColumns": 2,
        "legendTransparent": True,
        "customiseBeforeLegend": lambda: effbox_d0.Draw(),
        "drawOpt": "HIST",
    }
    plot = PlotStack()
    for it, leg in zip(iterations, legendLabels):
        #hname = folder_track%it + "effic_vs_vertpos"
        #h = phase1file.Get(hname)
        #if not h:
        #    raise Exception("Did not find %s from %s" % (hname, phase1file.GetName()))
        num_name = folder_track%it + "num_assoc(simToReco)_dxypv"
        denom_name = folder_track%it + "num_simul_dxypv"
        eff = calculateEfficiency(phase1file, num_name, denom_name, rebin=2)
        eff.SetFillColor(iter_colors[it])
        eff.SetLineColor(ROOT.kBlack)
        plot.add(eff, leg)

    drawPlot(prefix+"_efficiency_dxy_cum", plot, ytitle="Tracking efficiency", **_common)
    #############################

    # dz
    effbox_dz = effbox.clone()
    effbox_dz.removeText(1)
    effbox_dz.addText("dz", yspace=0.01)
    effbox_dz.transparent = True
    effbox_dz.move(dx=-0.1, dy=0.6)
    _common = {
        "xtitle": "impact parameter dz",
        "xmin": -20, "xmax": 20, "ymin": 0, "ymax": 1,
        "legendDx": 0.02, "legendDy": -0.07, "legendDw": legendDw, "legendDh": 0.23,
#        "legendDx": -0.3, "legendDy": -0.12, "legendDw": legendDw+0.33, "legendDh": 0.05,
#        "legendColumns": 2,
        "legendTransparent": True,
        "customiseBeforeLegend": lambda: effbox_dz.Draw(),
        "drawOpt": "HIST",
    }
    plot = PlotStack()
    for it, leg in zip(iterations, legendLabels):
        #hname = folder_track%it + "effic_vs_vertpos"
        #h = phase1file.Get(hname)
        #if not h:
        #    raise Exception("Did not find %s from %s" % (hname, phase1file.GetName()))
        num_name = folder_track%it + "num_assoc(simToReco)_dzpv"
        denom_name = folder_track%it + "num_simul_dzpv"
        eff = calculateEfficiency(phase1file, num_name, denom_name, rebin=2)
        eff.SetFillColor(iter_colors[it])
        eff.SetLineColor(ROOT.kBlack)
        plot.add(eff, leg)

    drawPlot(prefix+"_efficiency_dz_cum", plot, ytitle="Tracking efficiency", **_common)
    #############################
    #"""


    plot = PlotStack()
    for it, leg in zip(iterations, legendLabels):
        hname = folder_track%it + "effic_vs_simpvz"
        h = phase1file.Get(hname)
        if not h:
            raise Exception("Did not find %s from %s" % (hname, phase1file.GetName()))
        h.SetFillColor(iter_colors[it])
        h.SetLineColor(ROOT.kBlack)
        plot.add(h, leg)
    _common = {
        "xtitle": "Simulated vertex z (cm)",
        "xmin": -30, "xmax": 30., "ymin": 0, "ymax": 1,
        "xlog": False,
        "legendDx": -0.13, "legendDy": -0.24, "legendDw": legendDw, "legendDh": 0.23,
        "legendTransparent": True,
        "customise": lambda: effbox_pt.Draw(),
        "drawOpt": "HIST",
    }
    drawPlot(prefix+"_efficiency_simpvz_cum", plot, ytitle="Tracking efficiency", **_common)

################################################################################
################################################################################
################################################################################
def plotFake(files, prefix, pileup, isPhase2 = False):
    folder_track = "Tracking/Run summary/Track/"
    folder_vertex = "Vertexing/Run summary/PrimaryVertexV/"

    iterations = [
        "InitialStep",
        "HighPtTripletStep"
    ]
    if isPhase2 :
        iterations = [
            "InitialStep",
            "HighPtTripletStep"
            ]

    binLabels = ["All tracks (p_{T} > 0.9 GeV)"] + [x.replace("Step", "").replace("Regional", "").replace("SeededInOut", " inside-out").replace("SeededOutIn", " outside-in") for x in iterations]
    colls = ["hltPhase2CutsRecoTracksPt09Hp"] + ["hltPhase2CutsRecoTracks%sPt09Hp" % x for x in iterations]
    
    plot = Plot(files.getHistos(folder_track+"num_reco_coll"), files.getLegends(), files.getStyles())
    plot_assoc = Plot(files.getHistos(folder_track+"num_assoc(recoToSim)_coll"), files.getLegends(), files.getStyles())
    plot_norm = Plot(files.getHistos(folder_vertex+"offlinePrimaryVertices/TruePVLocationIndexCumulative"), files.getLegends(), files.getStyles())
    newhistos = []
    for (h, hassoc, hnorm) in zip(plot._histos, plot_assoc._histos, plot_norm._histos):
        d = plotting._th1ToOrderedDict(h)
        dassoc = plotting._th1ToOrderedDict(hassoc)
        norm = hnorm.GetEntries()
        hnew = ROOT.TH1F(h.GetName()+"_new", "", len(colls), 0, len(colls))
        for i, coll in enumerate(colls):
            if coll in d:
                vreco = d[coll]
                vassoc = dassoc[coll]
                vfake = vreco[0]-vassoc[0]
                print(vfake, norm)
                hnew.SetBinContent(i+1, vfake)
                hnew.SetBinError(i+1, math.sqrt(vfake))
        newhistos.append(hnew)
    plot._histos = newhistos

    _common = {
        "xtitle": "",
        #"xmin": 0, "xmax": 60, "ymin": 0, "ymax": 1.2,
        "legendDx": 0.02, "legendDy": -0.07,
#        "legendDx": -0.3, "legendDy": -0.12, "legendDw": legendDw+0.33, "legendDh": 0.05,
#        "legendColumns": 2,
#        "legendTransparent": True,
#        "customiseBeforeLegend": lambda: effbox_r.Draw(),
#        "drawOpt": "HIST",
        "xbinlabels": binLabels,
        "xbinlabelsize": 0.03,
        "xbinlabeloption": "d",
    }
    drawPlot(prefix+"_fakes_vs_coll", plot, ytitle="Number of fake tracks / event", **_common)


################################################################################
################################################################################
################################################################################
def plotResol(files, prefix, pileup, hasPU70=True):
    folder_track = "Tracking/Run summary/Track/hltPhase2CutsRecoHp_hltPhase2ingParticleRecoTrackAsssociation/"
    #folder_vertex = "Vertexing/Run summary/PrimaryVertexV/offlinePrimaryVertices/"
    folder_vertex = "Vertexing/Run summary/PrimaryVertexV/hltPhase2SelectedOfflinePrimaryVertices/"

    isrun2 = ("run2" in prefix)
    isrun2real = isrun2 and (len(files.getFiles()) == 3)

    xmin = 0.33
    xmax = 0.87
    legendDw = -0.1
    if isrun2:
        legendDw = 0
    if isrun2real:
        legendDw = 0.25
    hasNoPU = ("no PU" in files.getLegends()[0])

    putext = ""
    if pileup is not None:
        putext = " (%s)" % pileup

    effbox = PlotTextBox(xmin, None, xmax, 0.85, transparent=False)
    effbox.addText("t#bar{t} event tracks%s"%putext)
#    effbox.addText("p_{T} > 0.9 GeV, ^{}d_{0} < 3.5 cm")

    vertbox = PlotTextBox(xmin, None, xmax-0.15, 0.85, transparent=False)
    vertbox.addText("t#bar{t} events%s"%putext)

    # dxy
    plot = Plot(files.getHistos(folder_track+"dxyres_vs_pt_Sigma"), files.getLegends(), files.getStyles())
    _common = {
        "xtitle": "Simulated track p_{T} (GeV)",
        "xmin": 1e-1,
        #"xmax": 2e2,
        "xmax": 1e2,
        "ymin": 0, "ymax": 0.05,
        "xlog": True,
        "legendDx": -0.1, "legendDy": -0.15, "legendDw": legendDw,
        "customise": lambda: effbox.Draw(),
        "ratio": True
    }
    if isrun2real:
        _common["legendTextSize"] = 0.035
        _common["legendDx"] -= 0.17
        _common["legendDy"] += 0.15
        effbox.move(dy=-0.15, dx=0.05)

    _common_ip = copy.copy(_common)
    _common_ip["ymax"] = _common_ip["ymax"]*10000

    plot.scale(10000)
    drawPlot(prefix+"_resolution_dxy_pt", plot, ytitle="d_{0} resolution (#mum)", **_common_ip)

    # dz
    plot = Plot(files.getHistos(folder_track+"dzres_vs_pt_Sigma"), files.getLegends(), files.getStyles())
    plot.scale(10000)
    drawPlot(prefix+"_resolution_dz_pt", plot, ytitle="d_{z} resolution (#mum)", **_common_ip)

    # pt
    plot = Plot(files.getHistos(folder_track+"ptres_vs_pt_Sigma"), files.getLegends(), files.getStyles())
    drawPlot(prefix+"_resolution_pt_pt", plot, ytitle="p_{T} resolution / p_{T}", **_common)

    # pt^2 for Marco
    plot = Plot(files.getHistos(folder_track+"ptres_vs_pt_Sigma"), files.getLegends(), files.getStyles())
    new = []
    for h in plot.histos():
        x = []
        y = []
        axis = h.GetXaxis()
        for i in xrange(1, h.GetNbinsX()+1):
            x.append(axis.GetBinCenter(i)**2)
            y.append(h.GetBinContent(i))

        gr = ROOT.TGraph(len(x), array.array("d", x), array.array("d", y))
        new.append(gr)
    plot.setHistos(new)
    _common_pt2 = copy.copy(_common)
    _common_pt2["xtitle"] = "Simulated track p_{T}^{2} (GeV^{2})"
    _common_pt2["xmin"] = 1e-2
    _common_pt2["xmax"] = 1e4
    #drawPlot(prefix+"_resolution_pt_pt2", plot, ytitle="p_{T} resolution / p_{T}", **_common_pt2)

    # vs. eta
    _common["xtitle"] = "Simulated track #eta"
    _common["xmin"] = -4.5 #3-->4.5
    _common["xmax"] = 4.5
    _common["xlog"] = False
    _common_ip = copy.copy(_common)
    _common_ip["ymax"] = 0.1*10000
    plot = Plot(files.getHistos(folder_track+"dxyres_vs_eta_Sigma"), files.getLegends(), files.getStyles())
    plot.scale(10000)
    drawPlot(prefix+"_resolution_dxy_eta", plot, ytitle="d_{0} resolution (#mum)", **_common_ip)

    plot = Plot(files.getHistos(folder_track+"dzres_vs_eta_Sigma"), files.getLegends(), files.getStyles())
    plot.scale(10000)
    drawPlot(prefix+"_resolution_dz_eta", plot, ytitle="d_{z} resolution (#mum)", **_common_ip)

    plot = Plot(files.getHistos(folder_track+"ptres_vs_eta_Sigma"), files.getLegends(), files.getStyles())
    drawPlot(prefix+"_resolution_pt_eta", plot, ytitle="p_{T} resolution / p_{T}", **_common)


    # vertex x
    vertbox.move(dx=0.15,dy=0.05)
    plot = Plot(files.getHistos(folder_vertex+"RecoAllAssoc2GenMatched_ResolX_vs_NumTracks_Sigma"), files.getLegends(), files.getStyles())
    if hasNoPU:
        plot.remove(0)
    plot.scale(1e4)
    _common = {
        "xtitle": "Number of tracks",
        "xmin": 0, "xmax": 100, "ymin": 0, "ymax": 100,
        "legendDx": 0.03, "legendDy": -0.12, "legendDw": legendDw,
        "customise": lambda: vertbox.Draw(),
        "ratio": True
    }
    if isrun2real:
        _common["legendTextSize"] = 0.035
        _common["legendDx"] -= 0.3
        _common["legendDy"] += 0.13
        vertbox.move(dy=-0.15, dx=0.05)
    drawPlot(prefix+"_vertex_resolution_x_ntrk", plot, ytitle="Vertex x resolution (#mum)", **_common)

    plot = Plot(files.getHistos(folder_vertex+"RecoAllAssoc2GenMatched_ResolX_vs_NumTracks_Sigma"), files.getLegends(), files.getStyles())
    if hasNoPU:
        plot.remove(0)
    plot.scale(1e4)
    drawPlot(prefix+"_vertex_resolution_xy_ntrk", plot, ytitle="Vertex x/y resolution (#mum)", **_common)

    # vertex y
    plot = Plot(files.getHistos(folder_vertex+"RecoAllAssoc2GenMatched_ResolY_vs_NumTracks_Sigma"), files.getLegends(), files.getStyles())
    if hasNoPU:
        plot.remove(0)
    plot.scale(1e4)
    drawPlot(prefix+"_vertex_resolution_y_ntrk", plot, ytitle="Vertex y resolution (#mum)", **_common)

    # vertex z
    plot = Plot(files.getHistos(folder_vertex+"RecoAllAssoc2GenMatched_ResolZ_vs_NumTracks_Sigma"), files.getLegends(), files.getStyles())
    if hasNoPU:
        plot.remove(0)
    plot.scale(1e4)
    drawPlot(prefix+"_vertex_resolution_z_ntrk", plot, ytitle="Vertex z resolution (#mum)", **_common)


################################################################################
################################################################################
################################################################################
def plotVertex(files, prefix, pileup, hasPU70=True):
    #folder_vertex = "Vertexing/Run summary/PrimaryVertexV/offlinePrimaryVertices/"
    folder_vertex = "Vertexing/Run summary/PrimaryVertexV/hltPhase2SelectedOfflinePrimaryVertices/"

    xmin = 0.33
    xmax = 0.87
    legendDw = -0.1

    hasNoPU = ("no PU" in files.getLegends()[0])

    putext = ""
    if pileup is not None:
        putext = "(%s)" % pileup

    vertbox = PlotTextBox(xmin, None, xmax-0.15, 0.35, transparent=False)
    vertbox.addText("t#bar{t} events%s"%putext)

    # efficiency
    plot = Plot(files.getHistos(folder_vertex+"effic_vs_NumTracks"), files.getLegends(), files.getStyles())
    _common = dict(
        xtitle="NumTracks",
        xmin=10, xmax=70, ymin=0, ymax=1,
        legendDx=-0.2, legendDy=-0.3, legendDw=legendDw,
        customise=lambda: vertbox.Draw()
    )
    if hasPU70:
        _common["xmax"] = 200
    if hasNoPU:
        plot.remove(0)
    drawPlot(prefix+"_vertex_efficiency_vs_NumTracks", plot, ytitle="Vertex efficiency", **_common)

    # fake rate
    _common["ymax"] = 0.2
    _common["xmax"] = 120
    _common["legendDy"] += 0.15
    vertbox.move(dy=0.55)
    plot = Plot(files.getHistos(folder_vertex+"fakerate_vs_NumTracks"), files.getLegends(), files.getStyles())
    if hasNoPU:
        plot.remove(0)
    drawPlot(prefix+"_vertex_fakerate_vs_NumTracks", plot, ytitle="Vertex fake rate", **_common)

    # efficiency
    plot = Plot(files.getHistos(folder_vertex+"effic_vs_NumVertices"), files.getLegends(), files.getStyles())
    _common = dict(
        xtitle="NumVertices",
        xmin=120, xmax=70, ymin=0, ymax=0.55,
        legendDx=-0.2, legendDy=-0.3, legendDw=legendDw,
        customise=lambda: vertbox.Draw()
    )
    if hasPU70:
        _common["xmax"] = 220
    if hasNoPU:
        plot.remove(0)
    drawPlot(prefix+"_vertex_efficiency_vs_NumVertices", plot, ytitle="Vertex efficiency", **_common)
    
    # fake rate
    _common["ymax"] = 0.2
    _common["xmin"] = 40
    _common["xmax"] = 120
    _common["legendDy"] += 0.15
    vertbox.move(dy=0.55)
    plot = Plot(files.getHistos(folder_vertex+"fakerate_vs_NumVertices"), files.getLegends(), files.getStyles())
    if hasNoPU:
        plot.remove(0)
    drawPlot(prefix+"_vertex_fakerate_vs_NumVertices", plot, ytitle="Vertex fake rate", **_common)

    """
    # nvtx vs. PU
    _common_nvtx = copy.copy(_common)
    _common_nvtx["ymin"] = _common_nvtx["ymax"]
    _common_nvtx["ymax"] = _common_nvtx["xmax"]
    _common_nvtx["legendDy"] += 0.05
    plot = Plot(files.getHistos(folder_vertex+"RecoVtx_vs_GenVtx"), files.getLegends(), files.getStyles())
    if hasNoPU:
        plot.remove(0)
    drawPlot(prefix+"_vertex_nvtx_vs_pu", plot, ytitle="Vertices", **_common_nvtx)
    
    # merge rate
    plot = Plot(files.getHistos(folder_vertex+"merged_vs_PU"), files.getLegends(), files.getStyles())
    if hasNoPU:
        plot.remove(0)
    drawPlot(prefix+"_vertex_mergerate_pu", plot, ytitle="Vertex merge rate", **_common)

    vertbox.move(dx=0.1)
    del _common["xtitle"]
    del _common["xmin"]
    del _common["xmax"]
    _common["ymax"] = 1
    _common["legendDx"] += 0.3
    plot = Plot(files.getHistos(folder_vertex+"merged_vs_ClosestVertexInZ"), files.getLegends(), files.getStyles())
    drawPlot(prefix+"_vertex_mergerate_closestz", plot, xtitle="Distance to closest vertex in z (cm)", ytitle="Vertex merge rate", xlog=True, **_common)

    # purity
    vertbox.move(dx=-0.2)
    _common["ymin"] = 5e-4
    _common["ymax"] = 1
    _common["legendDx"] -= 0.3
    plot = Plot(files.getHistos(folder_vertex+"RecoPVAssoc2GenPVMatched_Purity"), files.getLegends(), files.getStyles())
    if hasNoPU:
        plot.remove(0)
    plot.normalizeToUnitArea()
    #drawPlot(prefix+"_vertex_purity", plot, xtitle="Primary vertex purity", ytitle="Fraction of events", ylog=True, **_common)

    """;
################################################################################
################################################################################

def plotPixelVertex(files, prefix, pileup, hasPU70=True):
    #folder_vertex = "Vertexing/Run summary/PrimaryVertexV/offlinePrimaryVertices/"
    #folder_vertex = "Vertexing/Run summary/PrimaryVertexV/hltPhase2SelectedOfflinePrimaryVertices/"
    folder_vertex = "Vertexing/Run summary/PrimaryVertexV/hltPhase2PixelVertices/"

    xmin = 0.33
    xmax = 0.87
    legendDw = -0.1

    hasNoPU = ("no PU" in files.getLegends()[0])

    putext = ""
    if pileup is not None:
        putext = "(%s)" % pileup

    vertbox = PlotTextBox(xmin, None, xmax-0.15, 0.35, transparent=False)
    vertbox.addText("t#bar{t} events%s"%putext)

    # efficiency
    plot = Plot(files.getHistos(folder_vertex+"effic_vs_NumTracks"), files.getLegends(), files.getStyles())
    _common = dict(
        xtitle="NumTracks",
        xmin=10, xmax=70, ymin=0, ymax=1,
        legendDx=-0.2, legendDy=-0.7, legendDw=legendDw,
        customise=lambda: vertbox.Draw()
    )
    if hasPU70:
        _common["xmax"] = 200
    if hasNoPU:
        plot.remove(0)
    drawPlot(prefix+"_pixelvertex_efficiency_vs_NumTracks", plot, ytitle="Vertex efficiency", **_common)

    # fake rate
    _common["ymax"] = 0.4
    _common["legendDy"] += 0.15
    vertbox.move(dy=0.55)
    plot = Plot(files.getHistos(folder_vertex+"fakerate_vs_NumTracks"), files.getLegends(), files.getStyles())
    if hasNoPU:
        plot.remove(0)
    drawPlot(prefix+"_pixelvertex_fakerate_vs_NumTracks", plot, ytitle="Vertex fake rate", **_common)

    # efficiency
    plot = Plot(files.getHistos(folder_vertex+"effic_vs_NumVertices"), files.getLegends(), files.getStyles())
    _common = dict(
        xtitle="NumVertices",
        xmin=120, xmax=70, ymin=0, ymax=0.55,
        legendDx=-0.2, legendDy=-0.3, legendDw=legendDw,
        customise=lambda: vertbox.Draw()
    )
    if hasPU70:
        _common["xmax"] = 220
    if hasNoPU:
        plot.remove(0)
    drawPlot(prefix+"_pixelvertex_efficiency_vs_NumVertices", plot, ytitle="Vertex efficiency", **_common)
    
    # fake rate
    _common["ymax"] = 0.5
    _common["xmin"] = 20
    _common["xmax"] = 100
    _common["legendDy"] += 0.15
    vertbox.move(dy=0.55)
    plot = Plot(files.getHistos(folder_vertex+"fakerate_vs_NumVertices"), files.getLegends(), files.getStyles())
    if hasNoPU:
        plot.remove(0)
    drawPlot(prefix+"_pixelvertex_fakerate_vs_NumVertices", plot, ytitle="Vertex fake rate", **_common)
    """

    # nvtx vs. PU
    _common_nvtx = copy.copy(_common)
    _common_nvtx["ymin"] = _common_nvtx["ymax"]
    _common_nvtx["ymax"] = _common_nvtx["xmax"]
    _common_nvtx["legendDy"] += 0.05
    plot = Plot(files.getHistos(folder_vertex+"RecoVtx_vs_GenVtx"), files.getLegends(), files.getStyles())
    if hasNoPU:
        plot.remove(0)
    drawPlot(prefix+"_pixelvertex_nvtx_vs_pu", plot, ytitle="Vertices", **_common_nvtx)
    
    # merge rate
    plot = Plot(files.getHistos(folder_vertex+"merged_vs_PU"), files.getLegends(), files.getStyles())
    if hasNoPU:
        plot.remove(0)
    drawPlot(prefix+"_pixelvertex_mergerate_pu", plot, ytitle="Vertex merge rate", **_common)

    vertbox.move(dx=0.1)
    del _common["xtitle"]
    del _common["xmin"]
    del _common["xmax"]
    _common["ymax"] = 1
    _common["legendDx"] += 0.3
    plot = Plot(files.getHistos(folder_vertex+"merged_vs_ClosestVertexInZ"), files.getLegends(), files.getStyles())
    drawPlot(prefix+"_pixelvertex_mergerate_closestz", plot, xtitle="Distance to closest vertex in z (cm)", ytitle="Vertex merge rate", xlog=True, **_common)

    # purity
    vertbox.move(dx=-0.2)
    _common["ymin"] = 5e-4
    _common["ymax"] = 1
    _common["legendDx"] -= 0.3
    plot = Plot(files.getHistos(folder_vertex+"RecoPVAssoc2GenPVMatched_Purity"), files.getLegends(), files.getStyles())
    if hasNoPU:
        plot.remove(0)
    plot.normalizeToUnitArea()
    #drawPlot(prefix+"_pixelvertex_purity", plot, xtitle="Primary vertex purity", ytitle="Fraction of events", ylog=True, **_common)
    """

################################################################################
################################################################################
def plotTime(fileCollections, prefix, pileups, legends, styles):
    folderTime = "DQMData/Run 1/DQM/Run summary/TimerService/process RECO/Paths"

    xmin = 0.33-0.07
    xmax = 0.87
    legendDw = -0.1
    vertbox = PlotTextBox(xmin, None, xmax-0.3, 0.7, transparent=False)
    vertbox.addText("t#bar{t} events")

    relbox = vertbox.clone()
    #relbox.addText("2016 no PU tracking time = 1")
    relbox.addText("tracking time of", yspace=0.01)
    relbox.addText("2016 no PU = 1")

    creator = plotting.AggregateBins("iteration", "reconstruction_step_module_average", trackingPlots._iterModuleMap(includeConvStep=False), ignoreMissingBins=True)

    normfactor = None

    maxAbs = 20
    maxRel = 80

    graphs = []
    graphs_abs = []
    for files in fileCollections:
        times = []
        for f in files.getFiles():
            tdir = f.Get(folderTime)
            h = creator.create(tdir)
            if not h:
                raise Exception("Did not find time from file %s" % f.GetPath())
            times.append(h.Integral()/1000.)

        # rely 2016 being the first being passed, and [0] being noPU
        if normfactor is None:
            normfactor = 1/times[0]

        gr = ROOT.TGraph(len(pileups), array.array("d", pileups), array.array("d", times))
        graphs_abs.append(gr)
        gr = ROOT.TGraph(len(pileups), array.array("d", pileups), array.array("d", [t*normfactor for t in times]))
        graphs.append(gr)

    print("Time normalization factor", normfactor)


    plot = Plot(graphs, legends, styles)
    drawPlot(prefix+"_time_vs_pu", plot, xtitle="Average pileup", ytitle="Tracking time (a.u.)",
             drawOpt="PL", ymax=maxRel,
             legendDx=-0.2, legendDw=legendDw,
             customise=lambda: relbox.Draw()
    )
    plot = Plot(graphs_abs, legends, styles)
    drawPlot(prefix+"_time_vs_pu_abs", plot, xtitle="Average pileup", ytitle="Tracking time (s)",
             drawOpt="PL", ymax=maxAbs,
             legendDx=-0.2, legendDw=legendDw,
             customise=lambda: vertbox.Draw()
    )

    ##########

    creator = plotting.AggregateBins("iteration", "reconstruction_step_module_average", trackingPlots._stepModuleMap(), ignoreMissingBins=True)

    graphs_seed = []
    graphs_seed_abs = []
    graphs_build = []
    graphs_build_abs = []
    for files in fileCollections:
        times_seed = []
        times_build = []
        for f in files.getFiles():
            tdir = f.Get(folderTime)
            h = creator.create(tdir)
            if not h:
                raise Exception("Did not find time from file %s" % f.GetPath())

            d = plotting._th1ToOrderedDict(h)

            times_seed.append(d["Seeding"][0]/1000.)
            times_build.append(d["Building"][0]/1000.)
            
        gr = ROOT.TGraph(len(pileups), array.array("d", pileups), array.array("d", times_seed))
        graphs_seed_abs.append(gr)
        gr = ROOT.TGraph(len(pileups), array.array("d", pileups), array.array("d", [t*normfactor for t in times_seed]))
        graphs_seed.append(gr)

        gr = ROOT.TGraph(len(pileups), array.array("d", pileups), array.array("d", times_build))
        graphs_build_abs.append(gr)
        gr = ROOT.TGraph(len(pileups), array.array("d", pileups), array.array("d", [t*normfactor for t in times_build]))
        graphs_build.append(gr)

    plot = Plot(graphs_seed, legends, styles)
    drawPlot(prefix+"_seedtime_vs_pu", plot, xtitle="Average pileup", ytitle="Seeding time (a.u.)",
             drawOpt="PL", ymax=maxRel,
             legendDx=-0.2, legendDw=legendDw,
             customise=lambda: relbox.Draw()
    )
    plot = Plot(graphs_seed_abs, legends, styles)
    drawPlot(prefix+"_seedtime_vs_pu_abs", plot, xtitle="Average pileup", ytitle="Seeding time (s)",
             drawOpt="PL", ymax=maxAbs,
             legendDx=-0.2, legendDw=legendDw,
             customise=lambda: vertbox.Draw()
    )

    plot = Plot(graphs_build, legends, styles)
    drawPlot(prefix+"_buildtime_vs_pu", plot, xtitle="Average pileup", ytitle="Pattern recognition time (a.u.)",
             drawOpt="PL", ymax=maxRel,
             legendDx=-0.2, legendDw=legendDw,
             customise=lambda: relbox.Draw()
    )
    plot = Plot(graphs_build_abs, legends, styles)
    drawPlot(prefix+"_buildtime_vs_pu_abs", plot, xtitle="Average pileup", ytitle="Pattern recognition time (s)",
             drawOpt="PL", ymax=maxAbs,
             legendDx=-0.2, legendDw=legendDw,
             customise=lambda: vertbox.Draw()
    )

    #######

    creator = plotting.AggregateBins("initialStepPreSplitting", "reconstruction_step_module_average", collections.OrderedDict(trackingPlots._iterations[0].modules()), ignoreMissingBins=True)

    graphs = []
    graphs_abs = []
    for files in fileCollections:
        times = []
        for f in files.getFiles():
            tdir = f.Get(folderTime)
            h = creator.create(tdir)
            if not h:
                raise Exception("Did not find time from file %s" % f.GetPath())

            d = plotting._th1ToOrderedDict(h)

            times.append(d["Seeding"][0]/1000.)

        gr = ROOT.TGraph(len(pileups), array.array("d", pileups), array.array("d", times))
        graphs_abs.append(gr)
        gr = ROOT.TGraph(len(pileups), array.array("d", pileups), array.array("d", [t*normfactor for t in times]))
        graphs.append(gr)

    ymaxfac = 0.025

    plot = Plot(graphs, legends, styles)
    drawPlot(prefix+"_pixeltracks_vs_pu", plot, xtitle="Average pileup", ytitle="Pixel tracking time (a.u.)",
             drawOpt="PL", ymax=maxRel*ymaxfac,
             legendDx=-0.2, legendDw=legendDw,
             customise=lambda: relbox.Draw()
    )
    plot = Plot(graphs_abs, legends, styles)
    drawPlot(prefix+"_pixeltracks_vs_pu_abs", plot, xtitle="Average pileup", ytitle="Pixel tracking time (s)",
             drawOpt="PL", ymax=maxAbs*ymaxfac,
             legendDx=-0.2, legendDw=legendDw,
             customise=lambda: vertbox.Draw()
    )

################################################################################
################################################################################
################################################################################
def plotMemory(prefix, data, legends, styles):
    xmin = 0.33
    xmax = 0.87
    legendDw = -0.1
    vertbox = PlotTextBox(xmin, None, xmax-0.3, 0.73, transparent=False)
    vertbox.addText("t#bar{t} events")

    graphs = []
    for l in legends:
        d = data[l]
        x = d.keys()
        x.sort()
        y = [d[i]/1000. for i in x]
        gr = ROOT.TGraph(len(x), array.array("d", x), array.array("d", y))
        graphs.append(gr)

    plot = Plot(graphs, legends, styles)
    drawPlot(prefix+"_trkonly_peakrss_vs_pu", plot, xtitle="Average pileup", ytitle="Peak memory (GB)",
             drawOpt="PL",
             ymin=1, ymax=3.2,
             legendDx=-0.2, legendDw=legendDw,
             customise=lambda: vertbox.Draw()
    )


################################################################################
################################################################################
################################################################################
def printEffFake(files, pileup):
    print("For pileup", pileup)
    for f, l in zip(files.getFiles(), files.getLegends()):
        eff_h = f.Get("DQMData/Run 1/Tracking/Run summary/Track/effic_vs_coll")
        fake_h = f.Get("DQMData/Run 1/Tracking/Run summary/Track/fakerate_vs_coll")

        eff_d = plotting._th1ToOrderedDict(eff_h)
        fake_d = plotting._th1ToOrderedDict(fake_h)

        print(l)

        #coll = "generalTracks"
        #collPt = coll
        coll = "hltPhase2CutsRecoTracksHp"
        collPt = "hltPhase2CutsRecoTracksPt09Hp"
        print("Efficiency", eff_d[coll])
        print("Fake rate ", fake_d[coll])
        print("Efficiency (track pt>0.9)", eff_d[collPt])
        print("Fake rate  (track pt>0.9)", fake_d[collPt])




def drawPlot(name, plot, xmin=None, ymin=0, xmax=None, ymax=None, xlog=False, ylog=False,
             xtitle=None, ytitle=None,
             drawOpt="PE",
             addLegend=True, legendDx=0, legendDy=0, legendDw=0, legendDh=0, legendTransparent=False, legendColumns=1, legendTextSize=0.04,
             rebin=None,
             ratio=False, ratioYmin=0.5, ratioYmax=1.2,
             customiseBeforeLegend=None, customise=None,
             period=14,
             #pos=11):
             pos=0,
             xbinlabels=None, xbinlabelsize=None, xbinlabeloption=None):
#    W = 800
#    H = 600
#    H_ref = 600
#    W_ref = 800

    ratioFactor = 1.25

    W = 600
    H = 600
    H_ref = 600
    W_ref = 600

    T = 0.08*H_ref
    B = 0.16*H_ref 
    L = 0.18*W_ref
    R = 0.04*W_ref

    H_canv = H
    if ratio:
        H_canv = int(H*ratioFactor)

    canv = ROOT.TCanvas(name,name,10,10,W,H_canv);
    canv.SetFillColor(0);
    canv.SetBorderMode(0);
    canv.SetFrameFillStyle(0);
    canv.SetFrameBorderMode(0);
    canv.SetLeftMargin( L/W );
    canv.SetRightMargin( R/W );
    canv.SetTopMargin( T/H );
    canv.SetBottomMargin( B/H );
    canv.SetTickx(0);
    canv.SetTicky(0);

    if ratio:
        plotting._modifyPadForRatio(canv, ratioFactor)

    if xmin is None:
        xmin = plot.getXmin()
    if xmax is None:
        xmax = plot.getXmax()
    if ymax is None:
        ymax = 1.1*plot.getYmax()

    bounds = (xmin, ymin, xmax, ymax)
    args = {"nrows": 1,
	    "zmax": None}
    args_ratio = {"nrows": 1,
	    "xbinlabels": None,
	    "xbinlabelsize": None,
	    "xbinlabeloption": None,
            "zmax": None}
    if xbinlabels is not None:
        args["xbinlabels"] = xbinlabels
        args["xbinlabelsize"] = xbinlabelsize
        args["xbinlabeloption"] = xbinlabeloption
    if xbinlabels is not None:
        args_ratio["xbinlabels"] = xbinlabels
        args_ratio["xbinlabelsize"] = xbinlabelsize
        args_ratio["xbinlabeloption"] = xbinlabeloption


    if ratio:
        ratioBounds = (xmin, ratioYmin, xmax, ratioYmax)
	#__init__(self, pad, bounds, zmax, ratioBounds, ratioFactor, nrows, xbinlabels=None, xbinlabelsize=None, xbinlabeloption=None, ratioYTitle=_ratioYTitle)
        frame = plotting.FrameRatio(canv, bounds = bounds, ratioBounds = ratioBounds, ratioFactor = ratioFactor,**args_ratio)  
        frame._frameRatio.GetYaxis().SetLabelSize(0.12)
    else:
        frame = plotting.Frame(canv, bounds, **args)

    if xtitle is not None:
        frame.setXTitle(xtitle)
    if ytitle is not None:
        frame.setYTitle(ytitle)

    frame.setXTitleOffset(1.15)
    frame.setYTitleOffset(1.55)

    frame.setLogx(xlog)
    frame.setLogy(ylog)

    if rebin is not None:
        plot.rebin(rebin)

    if ratio:
        frame._pad.cd()

    plot.draw(drawOpt)

    ratios = None
    if ratio:
        frame._padRatio.cd()
        ratios = plotting._calculateRatios(plot._histos)
        for r in ratios[1:]:
            r.draw()
        frame._pad.cd()

    if customiseBeforeLegend is not None:
        customiseBeforeLegend()

    if addLegend:
        lx1 = 0.6
        lx2 = 0.95
#        ly1 = 0.8
        ly1 = 0.75
        ly2 = 0.9
        #ly1 = 0.73
        #ly2 = 0.83
        
        #legendDx -= 0.21
        
        lx1 += legendDx
        lx2 += legendDx
        ly1 += legendDy
        ly2 += legendDy
        
        lx2 += legendDw
        ly1 -= legendDh
            
        legend = ROOT.TLegend(lx1, ly1, lx2, ly2)
        if legendColumns != 1:
            legend.SetNColumns(legendColumns)
        legend.SetTextSize(legendTextSize)
        legend.SetLineColor(1)
        legend.SetLineWidth(1)
        legend.SetLineStyle(1)
        legend.SetFillColor(0)
        legend.SetMargin(0.07)
        legend.SetBorderSize(0)
        if legendTransparent:
            legend.SetFillStyle(0)
        plot.addToLegend(legend, legendColumns)
        legend.Draw()

    frame._pad.cd()
    ROOT.CMS_lumi_v2(frame._pad, period, pos)

    canv.Update()
    canv.RedrawAxis();
    canv.GetFrame().Draw()

    if customise is not None:
        customise()

    canv.SaveAs(name+".png")
    canv.SaveAs(name+".pdf")

if __name__ == "__main__":
    main()
