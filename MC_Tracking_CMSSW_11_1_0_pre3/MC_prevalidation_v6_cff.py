import FWCore.ParameterSet.Config as cms

###################### prevalidation_step
"""
################################# list of actually needed modules that are in a cms.Path (here for bookkeeping)
from Configuration.StandardSequences.Validation_cff import quickTrackAssociatorByHits, tpClusterProducer, trackingParticleNumberOfLayersProducer, trackingParticlesBHadron, trackingParticlesConversion, simHitTPAssocProducer
"""

from  Configuration.StandardSequences.Validation_cff import *

###added for pixelVertices

hltPhase2PixelVertexAssociatorByPositionAndTracks = cms.EDProducer("VertexAssociatorByPositionAndTracksProducer",
    absT = cms.double(-1),
    absZ = cms.double(0.1),
    maxRecoT = cms.double(-1),
    maxRecoZ = cms.double(1000),
    sharedTrackFraction = cms.double(-1),
    sigmaT = cms.double(-1),
    sigmaZ = cms.double(3),
    trackAssociation = cms.InputTag("hltPhase2TrackingParticlePixelTrackAsssociation")
)

hltPhase2TrackingParticlePixelTrackAsssociation = cms.EDProducer("TrackAssociatorEDProducer",
    associator = cms.InputTag("quickTrackAssociatorByHits"),#PreSplitting"),
    ignoremissingtrackcollection = cms.untracked.bool(False),
    label_tp = cms.InputTag("mix","MergedTrackTruth"),
    label_tr = cms.InputTag("hltPhase2PixelTracks")
)

hltPhase2TrackValidatorPixelTrackingOnly = cms.EDProducer("MultiTrackValidator", #cmssw_11_1 previous cms.EDAnalyzer
    cores = cms.InputTag(""), #cmssw_10_6
    UseAssociators = cms.bool(False),
    associators = cms.untracked.VInputTag("hltPhase2TrackingParticlePixelTrackAsssociation"),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    calculateDrSingleCollection = cms.untracked.bool(True),
    chargedOnlyTP = cms.bool(True),
    dEdx1Tag = cms.InputTag("dedxHarmonic2"),
    dEdx2Tag = cms.InputTag("dedxTruncated40"),
    dirName = cms.string('Tracking/PixelTrack/'),
    doMVAPlots = cms.untracked.bool(False),
    doPVAssociationPlots = cms.untracked.bool(True),
    doPlotsOnlyForTruePV = cms.untracked.bool(False),
    doRecoTrackPlots = cms.untracked.bool(True),
    doResolutionPlotsForLabels = cms.VInputTag(),
    doSeedPlots = cms.untracked.bool(False),
    doSimPlots = cms.untracked.bool(True),
    doSimTrackPlots = cms.untracked.bool(True),
    doSummaryPlots = cms.untracked.bool(True),
    dodEdxPlots = cms.untracked.bool(False),
    histoProducerAlgoBlock = cms.PSet(
	mindrj = cms.double(0.001),#cmssw_10_6 
        maxdrj = cms.double(0.1),#cmssw_10_6
        nintdrj = cms.int32(100), #cmssw_10_6
        GpSelectorForEfficiencyVsEta = cms.PSet(
            chargedOnly = cms.bool(True),
	    invertRapidityCut = cms.bool(False), # cmssw_11_1
            lip = cms.double(30.0),
            maxPhi = cms.double(3.2), # cmssw_11_1
            minPhi = cms.double(-3.2), # cmssw_11_1
            maxRapidity = cms.double(4.5), #previous 2.5
            minRapidity = cms.double(-4.5), #previous -2.5
            pdgId = cms.vint32(),
            ptMin = cms.double(0.9),
            status = cms.int32(1),
            tip = cms.double(2.5) #previous 3.5
        ),
        GpSelectorForEfficiencyVsPhi = cms.PSet(
            chargedOnly = cms.bool(True),
	    invertRapidityCut = cms.bool(False), # cmssw_11_1
            lip = cms.double(30.0),
            maxPhi = cms.double(3.2), # cmssw_11_1
            minPhi = cms.double(-3.2), # cmssw_11_1
            maxRapidity = cms.double(4.5), #previous 2.5
            minRapidity = cms.double(-4.5), #previous -2.5
            pdgId = cms.vint32(),
            ptMin = cms.double(0.9),
            status = cms.int32(1),
            tip = cms.double(2.5) #previous 3.5
        ),
        GpSelectorForEfficiencyVsPt = cms.PSet(
            chargedOnly = cms.bool(True),
	    invertRapidityCut = cms.bool(False), # cmssw_11_1
            lip = cms.double(30.0),
            maxPhi = cms.double(3.2), # cmssw_11_1
            minPhi = cms.double(-3.2), # cmssw_11_1
            maxRapidity = cms.double(4.5), #previous 2.5
            minRapidity = cms.double(-4.5), #previous -2.5
            pdgId = cms.vint32(),
            ptMin = cms.double(0.05),
            status = cms.int32(1),
            tip = cms.double(2.5) #previous 3.5
        ),
        GpSelectorForEfficiencyVsVTXR = cms.PSet(
            chargedOnly = cms.bool(True),
	    invertRapidityCut = cms.bool(False), # cmssw_11_1
            lip = cms.double(30.0),
            maxPhi = cms.double(3.2), # cmssw_11_1
            minPhi = cms.double(-3.2), # cmssw_11_1
            maxRapidity = cms.double(2.5),
            minRapidity = cms.double(-2.5),
            pdgId = cms.vint32(),
            ptMin = cms.double(0.9),
            status = cms.int32(1),
            tip = cms.double(2.5) #previous 30
        ),
        GpSelectorForEfficiencyVsVTXZ = cms.PSet(
            chargedOnly = cms.bool(True),
	    invertRapidityCut = cms.bool(False), # cmssw_11_1
            lip = cms.double(35.0),
            maxPhi = cms.double(3.2), # cmssw_11_1
            minPhi = cms.double(-3.2), # cmssw_11_1
            maxRapidity = cms.double(4.5), #previous 2.5
            minRapidity = cms.double(-4.5), #previous -2.5
            pdgId = cms.vint32(),
            ptMin = cms.double(0.9),
            status = cms.int32(1),
            tip = cms.double(2.5) #previous 3.5
        ),
        TpSelectorForEfficiencyVsEta = cms.PSet(
            chargedOnly = cms.bool(True),
	    invertRapidityCut = cms.bool(False), # cmssw_11_1
            intimeOnly = cms.bool(False),
            lip = cms.double(30.0),
            maxPhi = cms.double(3.2),
            maxRapidity = cms.double(4.5),
            minHit = cms.int32(0),
            minPhi = cms.double(-3.2),
            minRapidity = cms.double(-4.5),
            pdgId = cms.vint32(),
            ptMax = cms.double(1e+100),
            ptMin = cms.double(0.9),
            signalOnly = cms.bool(True),
            stableOnly = cms.bool(False),
            tip = cms.double(2.5) #previous 3.5
        ),
        TpSelectorForEfficiencyVsPhi = cms.PSet(
            chargedOnly = cms.bool(True),
	    invertRapidityCut = cms.bool(False), # cmssw_11_1
            intimeOnly = cms.bool(False),
            lip = cms.double(30.0),
            maxPhi = cms.double(3.2),
            maxRapidity = cms.double(4.5), #previous 2.5
            minHit = cms.int32(0),
            minPhi = cms.double(-3.2),
            minRapidity = cms.double(-4.5), #previous -2.5
            pdgId = cms.vint32(),
            ptMax = cms.double(1e+100),
            ptMin = cms.double(0.9),
            signalOnly = cms.bool(True),
            stableOnly = cms.bool(False),
            tip = cms.double(2.5) #previous 3.5
        ),
        TpSelectorForEfficiencyVsPt = cms.PSet(
            chargedOnly = cms.bool(True),
	    invertRapidityCut = cms.bool(False), # cmssw_11_1
            intimeOnly = cms.bool(False),
            lip = cms.double(30.0),
            maxPhi = cms.double(3.2),
            maxRapidity = cms.double(4.5),
            minHit = cms.int32(0),
            minPhi = cms.double(-3.2),
            minRapidity = cms.double(-4.5),
            pdgId = cms.vint32(),
            ptMax = cms.double(1e+100),
            ptMin = cms.double(0.05),
            signalOnly = cms.bool(True),
            stableOnly = cms.bool(False),
            tip = cms.double(2.5) #previous 3.5
        ),
        TpSelectorForEfficiencyVsVTXR = cms.PSet(
            chargedOnly = cms.bool(True),
	    invertRapidityCut = cms.bool(False), # cmssw_11_1
            intimeOnly = cms.bool(False),
            lip = cms.double(30.0),
            maxPhi = cms.double(3.2),
            maxRapidity = cms.double(4.5),
            minHit = cms.int32(0),
            minPhi = cms.double(-3.2),
            minRapidity = cms.double(-4.5),
            pdgId = cms.vint32(),
            ptMax = cms.double(1e+100),
            ptMin = cms.double(0.9),
            signalOnly = cms.bool(True),
            stableOnly = cms.bool(False),
            tip = cms.double(60.0) 
        ),
        TpSelectorForEfficiencyVsVTXZ = cms.PSet(
            chargedOnly = cms.bool(True),
	    invertRapidityCut = cms.bool(False), # cmssw_11_1
            intimeOnly = cms.bool(False),
            lip = cms.double(30.0),
            maxPhi = cms.double(3.2),
            maxRapidity = cms.double(4.5),
            minHit = cms.int32(0),
            minPhi = cms.double(-3.2),
            minRapidity = cms.double(-4.5),
            pdgId = cms.vint32(),
            ptMax = cms.double(1e+100),
            ptMin = cms.double(0.9),
            signalOnly = cms.bool(True),
            stableOnly = cms.bool(False),
            tip = cms.double(2.5) #previous 3.5
        ),
        cotThetaRes_nbin = cms.int32(300),
        cotThetaRes_rangeMax = cms.double(0.02),
        cotThetaRes_rangeMin = cms.double(-0.02),
	doMTDPlots = cms.untracked.bool(True), # cmssw_11_1
        dxyDzZoom = cms.double(25),
        dxyRes_nbin = cms.int32(500),
        dxyRes_rangeMax = cms.double(0.1),
        dxyRes_rangeMin = cms.double(-0.1),
        dzRes_nbin = cms.int32(150),
        dzRes_rangeMax = cms.double(0.05),
        dzRes_rangeMin = cms.double(-0.05),
        generalGpSelector = cms.PSet(
            chargedOnly = cms.bool(True),
            lip = cms.double(30.0),
	    invertRapidityCut = cms.bool(False), # cmssw_11_1
            maxPhi = cms.double(3.2), # cmssw_11_1
            minPhi = cms.double(-3.2), # cmssw_11_1
            maxRapidity = cms.double(4.5), #previous 2.5
            minRapidity = cms.double(-4.5), #previous -2.5
            pdgId = cms.vint32(),
            ptMin = cms.double(0.9),
            status = cms.int32(1),
            tip = cms.double(2.5) #previous 3.5
        ),
        generalTpSelector = cms.PSet(
            chargedOnly = cms.bool(True),
            intimeOnly = cms.bool(False),
	    invertRapidityCut = cms.bool(False), # cmssw_11_1
            lip = cms.double(30.0),
            maxPhi = cms.double(3.2),
            maxRapidity = cms.double(4.5),
            minHit = cms.int32(0),
            minPhi = cms.double(-3.2),
            minRapidity = cms.double(-4.5),
            pdgId = cms.vint32(),
            ptMax = cms.double(1e+100),
            ptMin = cms.double(0.9),
            signalOnly = cms.bool(True),
            stableOnly = cms.bool(False),
            tip = cms.double(30.0)
        ),
        maxChi2 = cms.double(20),
        maxDeDx = cms.double(10.0),
        maxDxy = cms.double(25),
        maxDz = cms.double(30),
        maxDzpvCumulative = cms.double(0.6),
        maxDzpvsigCumulative = cms.double(10),
        maxEta = cms.double(4.5),
        maxHit = cms.double(80.5),
        maxLayers = cms.double(25.5),
        maxMVA = cms.double(1),
        maxPVz = cms.double(60),
        maxPhi = cms.double(3.1416),
        maxPt = cms.double(1000),
        maxPu = cms.double(259.5),
        maxTracks = cms.double(2000),
        maxVertcount = cms.double(160.5),
        maxVertpos = cms.double(100),
        maxZpos = cms.double(30),
        maxdr = cms.double(1),
        minChi2 = cms.double(0),
        minDeDx = cms.double(0.0),
        minDxy = cms.double(-25),
        minDz = cms.double(-30),
        minEta = cms.double(-4.5),
        minHit = cms.double(-0.5),
        minLayers = cms.double(-0.5),
        minMVA = cms.double(-1),
        minPVz = cms.double(-60),
        minPhi = cms.double(-3.1416),
        minPt = cms.double(0.1),
        minPu = cms.double(-0.5),
        minTracks = cms.double(0),
        minVertcount = cms.double(-0.5),
        minVertpos = cms.double(0.01),
        minZpos = cms.double(-30),
        mindr = cms.double(0.001),
        nintChi2 = cms.int32(40),
        nintDeDx = cms.int32(40),
        nintDxy = cms.int32(100),
        nintDz = cms.int32(60),
        nintDzpvCumulative = cms.int32(240),
        nintDzpvsigCumulative = cms.int32(200),
        nintEta = cms.int32(90),
        nintHit = cms.int32(81),
        nintLayers = cms.int32(26),
        nintMVA = cms.int32(100),
        nintPVz = cms.int32(120),
        nintPhi = cms.int32(36),
        nintPt = cms.int32(40),
        nintPu = cms.int32(130),
        nintTracks = cms.int32(200),
        nintVertcount = cms.int32(161),
        nintVertpos = cms.int32(40),
        nintZpos = cms.int32(60),
        nintdr = cms.int32(100),
        phiRes_nbin = cms.int32(300),
        phiRes_rangeMax = cms.double(0.01),
        phiRes_rangeMin = cms.double(-0.01),
        ptRes_nbin = cms.int32(100),
        ptRes_rangeMax = cms.double(0.1),
        ptRes_rangeMin = cms.double(-0.1),
        seedingLayerSets = cms.vstring(
            'BPix1+BPix2+BPix3+BPix4', 
            'BPix1+BPix2+BPix3+FPix1_pos', 
            'BPix1+BPix2+BPix3+FPix1_neg', 
            'BPix1+BPix2+FPix1_pos+FPix2_pos', 
            'BPix1+BPix2+FPix1_neg+FPix2_neg', 
            'BPix1+FPix1_pos+FPix2_pos+FPix3_pos', 
            'BPix1+FPix1_neg+FPix2_neg+FPix3_neg', 
            'FPix1_pos+FPix2_pos+FPix3_pos+FPix4_pos', 
            'FPix1_neg+FPix2_neg+FPix3_neg+FPix4_neg', 
            'FPix2_pos+FPix3_pos+FPix4_pos+FPix5_pos', 
            'FPix2_neg+FPix3_neg+FPix4_neg+FPix5_neg', 
            'FPix3_pos+FPix4_pos+FPix5_pos+FPix6_pos', 
            'FPix3_neg+FPix4_neg+FPix5_neg+FPix6_neg', 
            'FPix4_pos+FPix5_pos+FPix6_pos+FPix7_pos', 
            'FPix4_neg+FPix5_neg+FPix6_neg+FPix7_neg', 
            'FPix5_pos+FPix6_pos+FPix7_pos+FPix8_pos', 
            'FPix5_neg+FPix6_neg+FPix7_neg+FPix8_neg', 
            #'BPix1+BPix2+BPix3', 
            #'BPix2+BPix3+BPix4', 
            #'BPix1+BPix3+BPix4', 
            #'BPix1+BPix2+BPix4', 
            #'BPix2+BPix3+FPix1_pos', 
            #'BPix2+BPix3+FPix1_neg', 
            #'BPix1+BPix2+FPix1_pos', 
            #'BPix1+BPix2+FPix1_neg', 
            #'BPix2+FPix1_pos+FPix2_pos', 
            #'BPix2+FPix1_neg+FPix2_neg', 
            #'BPix1+FPix1_pos+FPix2_pos', 
            #'BPix1+FPix1_neg+FPix2_neg', 
            #'FPix1_pos+FPix2_pos+FPix3_pos', 
            #'FPix1_neg+FPix2_neg+FPix3_neg', 
            #'BPix1+FPix2_pos+FPix3_pos', 
            #'BPix1+FPix2_neg+FPix3_neg', 
            #'FPix2_pos+FPix3_pos+FPix4_pos', 
            #'FPix2_neg+FPix3_neg+FPix4_neg', 
            #'FPix3_pos+FPix4_pos+FPix5_pos', 
            #'FPix3_neg+FPix4_neg+FPix5_neg', 
            #'FPix4_pos+FPix5_pos+FPix6_pos', 
            #'FPix4_neg+FPix5_neg+FPix6_neg', 
            #'FPix5_pos+FPix6_pos+FPix7_pos', 
            #'FPix5_neg+FPix6_neg+FPix7_neg', 
            #'FPix6_pos+FPix7_pos+FPix8_pos', 
            #'FPix6_neg+FPix7_neg+FPix8_neg', 
            #'BPix1+BPix2', 
            #'BPix1+BPix3', 
            #'BPix2+BPix3', 
            #'BPix1+FPix1_pos', 
            #'BPix1+FPix1_neg', 
            #'BPix2+FPix1_pos', 
            #'BPix2+FPix1_neg'
        ),
        useFabsEta = cms.bool(False),
        useInvPt = cms.bool(False),
        useLogPt = cms.untracked.bool(True),
        useLogVertpos = cms.untracked.bool(True)
    ),
    ignoremissingtrackcollection = cms.untracked.bool(False),
    intimeOnlyTP = cms.bool(True),
    invertRapidityCutTP = cms.bool(False), # cmssw_11_1
    label = cms.VInputTag("hltPhase2PixelTracks"),
    label_pileupinfo = cms.InputTag("addPileupInfo"),
    label_tp_effic = cms.InputTag("mix","MergedTrackTruth"),
    label_tp_effic_refvector = cms.bool(False),
    label_tp_fake = cms.InputTag("mix","MergedTrackTruth"),
    label_tp_fake_refvector = cms.bool(False),
    label_tp_nlayers = cms.InputTag("trackingParticleNumberOfLayersProducer","trackerLayers"),
    label_tp_npixellayers = cms.InputTag("trackingParticleNumberOfLayersProducer","pixelLayers"),
    label_tp_nstripstereolayers = cms.InputTag("trackingParticleNumberOfLayersProducer","stripStereoLayers"),
    label_tv = cms.InputTag("mix","MergedTrackTruth"),
    label_vertex = cms.untracked.InputTag("hltPhase2PixelVertices"),
    lipTP = cms.double(30.0),
    maxRapidityTP = cms.double(4.5),
    minHitTP = cms.int32(0),
    minRapidityTP = cms.double(-4.5),
    mvaLabels = cms.untracked.PSet(

    ),
    parametersDefiner = cms.string('LhcParametersDefinerForTP'),
    pdgIdTP = cms.vint32(),
    ptMaxTP = cms.double(1e+100),
    ptMinTP = cms.double(0.005),
    signalOnlyTP = cms.bool(False),
    sim = cms.VInputTag(
        cms.InputTag("g4SimHits","TrackerHitsPixelBarrelLowTof"), cms.InputTag("g4SimHits","TrackerHitsPixelBarrelHighTof"), cms.InputTag("g4SimHits","TrackerHitsPixelEndcapLowTof"), cms.InputTag("g4SimHits","TrackerHitsPixelEndcapHighTof"), cms.InputTag("g4SimHits","TrackerHitsTIBLowTof"), 
        cms.InputTag("g4SimHits","TrackerHitsTIBHighTof"), cms.InputTag("g4SimHits","TrackerHitsTIDLowTof"), cms.InputTag("g4SimHits","TrackerHitsTIDHighTof"), cms.InputTag("g4SimHits","TrackerHitsTOBLowTof"), cms.InputTag("g4SimHits","TrackerHitsTOBHighTof"), 
        cms.InputTag("g4SimHits","TrackerHitsTECLowTof"), cms.InputTag("g4SimHits","TrackerHitsTECHighTof")
    ),
    simHitTpMapTag = cms.InputTag("simHitTPAssocProducer"),
    simPVMaxZ = cms.untracked.double(-1),
    stableOnlyTP = cms.bool(False),
    tipTP = cms.double(60.0), 
    trackCollectionForDrCalculation = cms.InputTag("hltPhase2PixelTracks"),
    useGsf = cms.bool(False),
    useLogPt = cms.untracked.bool(True),
    vertexAssociator = cms.untracked.InputTag("hltPhase2PixelVertexAssociatorByPositionAndTracks")
)

################################################################


hltPhase2TrackValidatorTrackingOnly = cms.EDProducer("MultiTrackValidator", #cmssw_11_1 previous cms.EDAnalyzer
    cores = cms.InputTag("highPtJetsForTrk"), #cmssw_10_6    # cmssw_11_1 
    UseAssociators = cms.bool(False),
    associators = cms.untracked.VInputTag("hltPhase2TrackingParticleRecoTrackAsssociation"),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    calculateDrSingleCollection = cms.untracked.bool(True),
    chargedOnlyTP = cms.bool(True),
    dEdx1Tag = cms.InputTag("dedxHarmonic2"),
    dEdx2Tag = cms.InputTag("dedxTruncated40"),
    dirName = cms.string('Tracking/Track/'),
    doMVAPlots = cms.untracked.bool(False),
    doPVAssociationPlots = cms.untracked.bool(True),
    doPlotsOnlyForTruePV = cms.untracked.bool(False),
    doRecoTrackPlots = cms.untracked.bool(True),
    doResolutionPlotsForLabels = cms.VInputTag("hltPhase2GeneralTracks", "hltPhase2CutsRecoTracksHp", "hltPhase2GeneralTracksPt09", "hltPhase2CutsRecoTracksBtvLike"),
    doSeedPlots = cms.untracked.bool(False),
    doSimPlots = cms.untracked.bool(True),
    doSimTrackPlots = cms.untracked.bool(True),
    doSummaryPlots = cms.untracked.bool(True),
    dodEdxPlots = cms.untracked.bool(False),
    histoProducerAlgoBlock = cms.PSet(
	mindrj = cms.double(0.001),#cmssw_10_6 
        maxdrj = cms.double(0.1),#cmssw_10_6
        nintdrj = cms.int32(100), #cmssw_10_6
        GpSelectorForEfficiencyVsEta = cms.PSet(
            chargedOnly = cms.bool(True),
            invertRapidityCut = cms.bool(False), # cmssw_11_1
            lip = cms.double(30.0),
            maxPhi = cms.double(3.2), # cmssw_11_1
            minPhi = cms.double(-3.2), # cmssw_11_1
            maxRapidity = cms.double(4.5), #previous 2.5 
            minRapidity = cms.double(-4.5), #previous -2.5
            pdgId = cms.vint32(),
            ptMin = cms.double(0.9),
            status = cms.int32(1),
            tip = cms.double(2.5) #previous 3.5
        ),
        GpSelectorForEfficiencyVsPhi = cms.PSet(
            chargedOnly = cms.bool(True),
            invertRapidityCut = cms.bool(False), # cmssw_11_1
            lip = cms.double(30.0),
            maxPhi = cms.double(3.2), # cmssw_11_1
            minPhi = cms.double(-3.2), # cmssw_11_1
            maxRapidity = cms.double(4.5), #previous 2.5
            minRapidity = cms.double(-4.5), #previous -2.5
            pdgId = cms.vint32(),
            ptMin = cms.double(0.9),
            status = cms.int32(1),
            tip = cms.double(2.5) #previous 3.5
        ),
        GpSelectorForEfficiencyVsPt = cms.PSet(
            chargedOnly = cms.bool(True),
            invertRapidityCut = cms.bool(False), # cmssw_11_1
            lip = cms.double(30.0),
            maxPhi = cms.double(3.2), # cmssw_11_1
            minPhi = cms.double(-3.2), # cmssw_11_1
            maxRapidity = cms.double(4.5), #previous 2.5
            minRapidity = cms.double(-4.5), #previous -2.5
            pdgId = cms.vint32(),
            ptMin = cms.double(0.9), # previous 0.05
            status = cms.int32(1),
            tip = cms.double(2.5) #previous 3.5
        ),
        GpSelectorForEfficiencyVsVTXR = cms.PSet(
            chargedOnly = cms.bool(True),
            invertRapidityCut = cms.bool(False), # cmssw_11_1
            lip = cms.double(30.0),
            maxPhi = cms.double(3.2), # cmssw_11_1
            minPhi = cms.double(-3.2), # cmssw_11_1
            maxRapidity = cms.double(4.5), #previous 2.5
            minRapidity = cms.double(-4.5), #previous -2.5
            pdgId = cms.vint32(),
            ptMin = cms.double(0.9),
            status = cms.int32(1),
            tip = cms.double(30.0) 
        ),
        GpSelectorForEfficiencyVsVTXZ = cms.PSet(
            chargedOnly = cms.bool(True),
            invertRapidityCut = cms.bool(False), # cmssw_11_1
            lip = cms.double(35.0),
            maxPhi = cms.double(3.2), # cmssw_11_1
            minPhi = cms.double(-3.2), # cmssw_11_1
            maxRapidity = cms.double(4.5), #previous 2.5
            minRapidity = cms.double(-4.5), #previous -2.5
            pdgId = cms.vint32(),
            ptMin = cms.double(0.9),
            status = cms.int32(1),
            tip = cms.double(2.5) #previous 3.5
        ),
        TpSelectorForEfficiencyVsEta = cms.PSet(
            chargedOnly = cms.bool(True),
            invertRapidityCut = cms.bool(False), # cmssw_11_1
            intimeOnly = cms.bool(False),
            lip = cms.double(30.0),
            maxPhi = cms.double(3.2),
            maxRapidity = cms.double(4.5),
            minHit = cms.int32(0),
            minPhi = cms.double(-3.2),
            minRapidity = cms.double(-4.5),
            pdgId = cms.vint32(),
            ptMax = cms.double(1e+100),
            ptMin = cms.double(0.9),
            signalOnly = cms.bool(True),
            stableOnly = cms.bool(False),
            tip = cms.double(2.5) #previous 3.5
        ),
        TpSelectorForEfficiencyVsPhi = cms.PSet(
            chargedOnly = cms.bool(True),
            invertRapidityCut = cms.bool(False), # cmssw_11_1
            intimeOnly = cms.bool(False),
            lip = cms.double(30.0),
            maxPhi = cms.double(3.2),
            maxRapidity = cms.double(4.5),
            minHit = cms.int32(0),
            minPhi = cms.double(-3.2),
            minRapidity = cms.double(-4.5),
            pdgId = cms.vint32(),
            ptMax = cms.double(1e+100),
            ptMin = cms.double(0.9),
            signalOnly = cms.bool(True),
            stableOnly = cms.bool(False),
            tip = cms.double(2.5) #previous 3.5
        ),
        TpSelectorForEfficiencyVsPt = cms.PSet(
            chargedOnly = cms.bool(True),
            invertRapidityCut = cms.bool(False), # cmssw_11_1
            intimeOnly = cms.bool(False),
            lip = cms.double(30.0),
            maxPhi = cms.double(3.2),
            maxRapidity = cms.double(4.5),
            minHit = cms.int32(0),
            minPhi = cms.double(-3.2),
            minRapidity = cms.double(-4.5),
            pdgId = cms.vint32(),
            ptMax = cms.double(1e+100),
            ptMin = cms.double(0.9), # previous 0.05
            signalOnly = cms.bool(True),
            stableOnly = cms.bool(False),
            tip = cms.double(2.5) #previous 3.5
        ),
        TpSelectorForEfficiencyVsVTXR = cms.PSet(
            chargedOnly = cms.bool(True),
            invertRapidityCut = cms.bool(False), # cmssw_11_1
            intimeOnly = cms.bool(False),
            lip = cms.double(30.0),
            maxPhi = cms.double(3.2),
            maxRapidity = cms.double(4.5),
            minHit = cms.int32(0),
            minPhi = cms.double(-3.2),
            minRapidity = cms.double(-4.5),
            pdgId = cms.vint32(),
            ptMax = cms.double(1e+100),
            ptMin = cms.double(0.9),
            signalOnly = cms.bool(True),
            stableOnly = cms.bool(False),
            tip = cms.double(60.0) 
        ),
        TpSelectorForEfficiencyVsVTXZ = cms.PSet(
            chargedOnly = cms.bool(True),
            invertRapidityCut = cms.bool(False), # cmssw_11_1
            intimeOnly = cms.bool(False),
            lip = cms.double(30.0),
            maxPhi = cms.double(3.2),
            maxRapidity = cms.double(4.5),
            minHit = cms.int32(0),
            minPhi = cms.double(-3.2),
            minRapidity = cms.double(-4.5),
            pdgId = cms.vint32(),
            ptMax = cms.double(1e+100),
            ptMin = cms.double(0.9),
            signalOnly = cms.bool(True),
            stableOnly = cms.bool(False),
            tip = cms.double(2.5) #previous 3.5
        ),
        cotThetaRes_nbin = cms.int32(300),
        cotThetaRes_rangeMax = cms.double(0.02),
        cotThetaRes_rangeMin = cms.double(-0.02),
        doMTDPlots = cms.untracked.bool(True), # cmssw_11_1
        dxyDzZoom = cms.double(25),
        dxyRes_nbin = cms.int32(500),
        dxyRes_rangeMax = cms.double(0.1),
        dxyRes_rangeMin = cms.double(-0.1),
        dzRes_nbin = cms.int32(150),
        dzRes_rangeMax = cms.double(0.05),
        dzRes_rangeMin = cms.double(-0.05),
        generalGpSelector = cms.PSet(
            chargedOnly = cms.bool(True),
            invertRapidityCut = cms.bool(False), # cmssw_11_1
            lip = cms.double(30.0),
            maxPhi = cms.double(3.2), # cmssw_11_1
            minPhi = cms.double(-3.2), # cmssw_11_1
            maxRapidity = cms.double(4.5), #previous 2.5
            minRapidity = cms.double(-4.5), #previous -2.5
            pdgId = cms.vint32(),
            ptMin = cms.double(0.9),
            status = cms.int32(1),
            tip = cms.double(2.5) #previous 3.5
        ),
        generalTpSelector = cms.PSet(
            chargedOnly = cms.bool(True),
            invertRapidityCut = cms.bool(False), # cmssw_11_1
            intimeOnly = cms.bool(False),
            lip = cms.double(30.0),
            maxPhi = cms.double(3.2),
            maxRapidity = cms.double(4.5),
            minHit = cms.int32(0),
            minPhi = cms.double(-3.2),
            minRapidity = cms.double(-4.5),
            pdgId = cms.vint32(),
            ptMax = cms.double(1e+100),
            ptMin = cms.double(0.9),
            signalOnly = cms.bool(True),
            stableOnly = cms.bool(False),
            tip = cms.double(2.5) #previous 3.5
        ),
        maxChi2 = cms.double(20),
        maxDeDx = cms.double(10.0),
        maxDxy = cms.double(25),
        maxDz = cms.double(30),
        maxDzpvCumulative = cms.double(0.6),
        maxDzpvsigCumulative = cms.double(10),
        maxEta = cms.double(4.5),
        maxHit = cms.double(80.5),
        maxLayers = cms.double(25.5),
        maxMVA = cms.double(1),
        maxPVz = cms.double(60),
        maxPhi = cms.double(3.1416),
        maxPt = cms.double(1000),
        maxPu = cms.double(259.5),
        maxTracks = cms.double(2000),
        maxVertcount = cms.double(160.5),
        maxVertpos = cms.double(100),
        maxZpos = cms.double(30),
        maxdr = cms.double(1),
        minChi2 = cms.double(0),
        minDeDx = cms.double(0.0),
        minDxy = cms.double(-25),
        minDz = cms.double(-30),
        minEta = cms.double(-4.5),
        minHit = cms.double(-0.5),
        minLayers = cms.double(-0.5),
        minMVA = cms.double(-1),
        minPVz = cms.double(-60),
        minPhi = cms.double(-3.1416),
        minPt = cms.double(0.1), # logscale
        minPu = cms.double(-0.5),
        minTracks = cms.double(0),
        minVertcount = cms.double(-0.5),
        minVertpos = cms.double(0.01),
        minZpos = cms.double(-30),
        mindr = cms.double(0.001),
        nintChi2 = cms.int32(40),
        nintDeDx = cms.int32(40),
        nintDxy = cms.int32(100),
        nintDz = cms.int32(60),
        nintDzpvCumulative = cms.int32(240),
        nintDzpvsigCumulative = cms.int32(200),
        nintEta = cms.int32(90),
        nintHit = cms.int32(81),
        nintLayers = cms.int32(26),
        nintMVA = cms.int32(100),
        nintPVz = cms.int32(120),
        nintPhi = cms.int32(36),
        nintPt = cms.int32(40),
        nintPu = cms.int32(130),
        nintTracks = cms.int32(200),
        nintVertcount = cms.int32(161),
        nintVertpos = cms.int32(40),
        nintZpos = cms.int32(60),
        nintdr = cms.int32(100),
        phiRes_nbin = cms.int32(300),
        phiRes_rangeMax = cms.double(0.01),
        phiRes_rangeMin = cms.double(-0.01),
        ptRes_nbin = cms.int32(100),
        ptRes_rangeMax = cms.double(0.1),
        ptRes_rangeMin = cms.double(-0.1),
        seedingLayerSets = cms.vstring(
            'BPix1+BPix2+BPix3+BPix4', 
            'BPix1+BPix2+BPix3+FPix1_pos', 
            'BPix1+BPix2+BPix3+FPix1_neg', 
            'BPix1+BPix2+FPix1_pos+FPix2_pos', 
            'BPix1+BPix2+FPix1_neg+FPix2_neg', 
            'BPix1+FPix1_pos+FPix2_pos+FPix3_pos', 
            'BPix1+FPix1_neg+FPix2_neg+FPix3_neg', 
            'FPix1_pos+FPix2_pos+FPix3_pos+FPix4_pos', 
            'FPix1_neg+FPix2_neg+FPix3_neg+FPix4_neg', 
            'FPix2_pos+FPix3_pos+FPix4_pos+FPix5_pos', 
            'FPix2_neg+FPix3_neg+FPix4_neg+FPix5_neg', 
            'FPix3_pos+FPix4_pos+FPix5_pos+FPix6_pos', 
            'FPix3_neg+FPix4_neg+FPix5_neg+FPix6_neg', 
            'FPix4_pos+FPix5_pos+FPix6_pos+FPix7_pos', 
            'FPix4_neg+FPix5_neg+FPix6_neg+FPix7_neg', 
            'FPix5_pos+FPix6_pos+FPix7_pos+FPix8_pos', 
            'FPix5_neg+FPix6_neg+FPix7_neg+FPix8_neg', 
            'BPix1+BPix2+BPix3', 
            'BPix2+BPix3+BPix4', 
            'BPix1+BPix3+BPix4', 
            'BPix1+BPix2+BPix4', 
            'BPix2+BPix3+FPix1_pos', 
            'BPix2+BPix3+FPix1_neg', 
            'BPix1+BPix2+FPix1_pos', 
            'BPix1+BPix2+FPix1_neg', 
            'BPix2+FPix1_pos+FPix2_pos', 
            'BPix2+FPix1_neg+FPix2_neg', 
            'BPix1+FPix1_pos+FPix2_pos', 
            'BPix1+FPix1_neg+FPix2_neg', 
            'FPix1_pos+FPix2_pos+FPix3_pos', 
            'FPix1_neg+FPix2_neg+FPix3_neg', 
            'BPix1+FPix2_pos+FPix3_pos', 
            'BPix1+FPix2_neg+FPix3_neg', 
            'FPix2_pos+FPix3_pos+FPix4_pos', 
            'FPix2_neg+FPix3_neg+FPix4_neg', 
            'FPix3_pos+FPix4_pos+FPix5_pos', 
            'FPix3_neg+FPix4_neg+FPix5_neg', 
            'FPix4_pos+FPix5_pos+FPix6_pos', 
            'FPix4_neg+FPix5_neg+FPix6_neg', 
            'FPix5_pos+FPix6_pos+FPix7_pos', 
            'FPix5_neg+FPix6_neg+FPix7_neg', 
            'FPix6_pos+FPix7_pos+FPix8_pos', 
            'FPix6_neg+FPix7_neg+FPix8_neg', 
            'BPix1+BPix2', 
            'BPix1+BPix3', 
            'BPix2+BPix3', 
            'BPix1+FPix1_pos', 
            'BPix1+FPix1_neg', 
            'BPix2+FPix1_pos', 
            'BPix2+FPix1_neg'
        ),
        useFabsEta = cms.bool(False),
        useInvPt = cms.bool(False),
        useLogPt = cms.untracked.bool(True),
        useLogVertpos = cms.untracked.bool(True)
    ),
    ignoremissingtrackcollection = cms.untracked.bool(False),
    intimeOnlyTP = cms.bool(True),
    invertRapidityCutTP = cms.bool(False), # cmssw_11_1
    label = cms.VInputTag(
        "hltPhase2GeneralTracks", "hltPhase2CutsRecoTracksHp", "hltPhase2CutsRecoTracksInitialStep", "hltPhase2CutsRecoTracksHighPtTripletStep",   		"hltPhase2CutsRecoTracksInitialStepHp", "hltPhase2CutsRecoTracksHighPtTripletStepHp",   
        "hltPhase2CutsRecoTracksInitialStepByOriginalAlgo", "hltPhase2CutsRecoTracksHighPtTripletStepByOriginalAlgo",   	"hltPhase2CutsRecoTracksInitialStepByOriginalAlgoHp","hltPhase2CutsRecoTracksHighPtTripletStepByOriginalAlgoHp", 
        "hltPhase2GeneralTracksPt09", "hltPhase2CutsRecoTracksPt09Hp", "hltPhase2CutsRecoTracksBtvLike", "hltPhase2CutsRecoTracksInitialStepByAlgoMask", 
        "hltPhase2CutsRecoTracksHighPtTripletStepByAlgoMask",  "hltPhase2CutsRecoTracksInitialStepByAlgoMaskHp", "hltPhase2CutsRecoTracksHighPtTripletStepByAlgoMaskHp", 
        "hltPhase2CutsRecoTracksPt09InitialStep", "hltPhase2CutsRecoTracksPt09HighPtTripletStep", "hltPhase2CutsRecoTracksPt09InitialStepHp", "hltPhase2CutsRecoTracksPt09HighPtTripletStepHp"
    ),
    label_pileupinfo = cms.InputTag("addPileupInfo"),
    label_tp_effic = cms.InputTag("mix","MergedTrackTruth"),
    label_tp_effic_refvector = cms.bool(False),
    label_tp_fake = cms.InputTag("mix","MergedTrackTruth"),
    label_tp_fake_refvector = cms.bool(False),
    label_tp_nlayers = cms.InputTag("trackingParticleNumberOfLayersProducer","trackerLayers"),
    label_tp_npixellayers = cms.InputTag("trackingParticleNumberOfLayersProducer","pixelLayers"),
    label_tp_nstripstereolayers = cms.InputTag("trackingParticleNumberOfLayersProducer","stripStereoLayers"),
    label_tv = cms.InputTag("mix","MergedTrackTruth"),
    label_vertex = cms.untracked.InputTag("hltPhase2OfflinePrimaryVertices"),
    lipTP = cms.double(30.0),
    maxRapidityTP = cms.double(4.5),
    minHitTP = cms.int32(0),
    minRapidityTP = cms.double(-4.5),
    mvaLabels = cms.untracked.PSet(

    ),
    parametersDefiner = cms.string('LhcParametersDefinerForTP'),
    pdgIdTP = cms.vint32(),
    ptMaxTP = cms.double(1e+100),
    ptMinTP = cms.double(0.9), # previous 0.005
    signalOnlyTP = cms.bool(False),
    sim = cms.VInputTag(
        cms.InputTag("g4SimHits","TrackerHitsPixelBarrelLowTof"), cms.InputTag("g4SimHits","TrackerHitsPixelBarrelHighTof"), cms.InputTag("g4SimHits","TrackerHitsPixelEndcapLowTof"), cms.InputTag("g4SimHits","TrackerHitsPixelEndcapHighTof"), cms.InputTag("g4SimHits","TrackerHitsTIBLowTof"), 
        cms.InputTag("g4SimHits","TrackerHitsTIBHighTof"), cms.InputTag("g4SimHits","TrackerHitsTIDLowTof"), cms.InputTag("g4SimHits","TrackerHitsTIDHighTof"), cms.InputTag("g4SimHits","TrackerHitsTOBLowTof"), cms.InputTag("g4SimHits","TrackerHitsTOBHighTof"), 
        cms.InputTag("g4SimHits","TrackerHitsTECLowTof"), cms.InputTag("g4SimHits","TrackerHitsTECHighTof")
    ),
    simHitTpMapTag = cms.InputTag("simHitTPAssocProducer"),
    simPVMaxZ = cms.untracked.double(-1),
    stableOnlyTP = cms.bool(False),
    tipTP = cms.double(60.0), 
    trackCollectionForDrCalculation = cms.InputTag("hltPhase2GeneralTracks"),
    useGsf = cms.bool(False),
    useLogPt = cms.untracked.bool(True),
    vertexAssociator = cms.untracked.InputTag("hltPhase2VertexAssociatorByPositionAndTracks")
)


hltPhase2TrackValidatorTPPtLess09Standalone = cms.EDProducer("MultiTrackValidator", #cmssw_11_1 previous cms.EDAnalyzer 
    cores = cms.InputTag("highPtJets"), #cmssw_10_6  #cmssw_11_1
    UseAssociators = cms.bool(False),
    associators = cms.untracked.VInputTag("hltPhase2TrackingParticleRecoTrackAsssociation"),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    calculateDrSingleCollection = cms.untracked.bool(True),
    chargedOnlyTP = cms.bool(True),
    dEdx1Tag = cms.InputTag("dedxHarmonic2"),
    dEdx2Tag = cms.InputTag("dedxTruncated40"),
    dirName = cms.string('Tracking/TrackTPPtLess09/'),
    doMVAPlots = cms.untracked.bool(False),
    doPVAssociationPlots = cms.untracked.bool(True),
    doPlotsOnlyForTruePV = cms.untracked.bool(False),
    doRecoTrackPlots = cms.untracked.bool(False),
    doResolutionPlotsForLabels = cms.VInputTag("disabled"),
    doSeedPlots = cms.untracked.bool(False),
    doSimPlots = cms.untracked.bool(False),
    doSimTrackPlots = cms.untracked.bool(True),
    doSummaryPlots = cms.untracked.bool(True),
    dodEdxPlots = cms.untracked.bool(False),
    histoProducerAlgoBlock = cms.PSet(
	mindrj = cms.double(0.001), #cmssw_10_6
        maxdrj = cms.double(0.1), #cmssw_10_6
        nintdrj = cms.int32(100), #cmssw_10_6
        GpSelectorForEfficiencyVsEta = cms.PSet(
            chargedOnly = cms.bool(True),
            invertRapidityCut = cms.bool(False), # cmssw_11_1
            lip = cms.double(30.0),
            maxPhi = cms.double(3.2), # cmssw_11_1
            minPhi = cms.double(-3.2), # cmssw_11_1
            maxRapidity = cms.double(4.5), #previous 2.5 
            minRapidity = cms.double(-4.5), #previous -2.5
            pdgId = cms.vint32(),
            ptMin = cms.double(0.9),
            status = cms.int32(1),
            tip = cms.double(2.5) #previous 3.5
        ),
        GpSelectorForEfficiencyVsPhi = cms.PSet(
            chargedOnly = cms.bool(True),
            invertRapidityCut = cms.bool(False), # cmssw_11_1
            lip = cms.double(30.0),
            maxPhi = cms.double(3.2), # cmssw_11_1
            minPhi = cms.double(-3.2), # cmssw_11_1
            maxRapidity = cms.double(4.5), #previous 2.5
            minRapidity = cms.double(-4.5), #previous -2.5
            pdgId = cms.vint32(),
            ptMin = cms.double(0.9),
            status = cms.int32(1),
            tip = cms.double(2.5) #previous 3.5
        ),
        GpSelectorForEfficiencyVsPt = cms.PSet(
            chargedOnly = cms.bool(True),
            invertRapidityCut = cms.bool(False), # cmssw_11_1
            lip = cms.double(30.0),
            maxPhi = cms.double(3.2), # cmssw_11_1
            minPhi = cms.double(-3.2), # cmssw_11_1
            maxRapidity = cms.double(4.5), #previous 2.5
            minRapidity = cms.double(-4.5), #previous -2.5
            pdgId = cms.vint32(),
            ptMin = cms.double(0.9), # previous 0.05
            status = cms.int32(1),
            tip = cms.double(2.5) #previous 3.5
        ),
        GpSelectorForEfficiencyVsVTXR = cms.PSet(
            chargedOnly = cms.bool(True),
            invertRapidityCut = cms.bool(False), # cmssw_11_1
            lip = cms.double(30.0),
            maxPhi = cms.double(3.2), # cmssw_11_1
            minPhi = cms.double(-3.2), # cmssw_11_1
            maxRapidity = cms.double(4.5), #previous 2.5
            minRapidity = cms.double(-4.5), #previous -2.5
            pdgId = cms.vint32(),
            ptMin = cms.double(0.9),
            status = cms.int32(1),
            tip = cms.double(30.0) 
        ),
        GpSelectorForEfficiencyVsVTXZ = cms.PSet(
            chargedOnly = cms.bool(True),
            invertRapidityCut = cms.bool(False), # cmssw_11_1
            lip = cms.double(35.0),
            maxPhi = cms.double(3.2), # cmssw_11_1
            minPhi = cms.double(-3.2), # cmssw_11_1
            maxRapidity = cms.double(4.5), #previous 2.5
            minRapidity = cms.double(-4.5), #previous -2.5
            pdgId = cms.vint32(),
            ptMin = cms.double(0.9),
            status = cms.int32(1),
            tip = cms.double(2.5) #previous 3.5
        ),
        TpSelectorForEfficiencyVsEta = cms.PSet(
            chargedOnly = cms.bool(True),
            invertRapidityCut = cms.bool(False), # cmssw_11_1
            intimeOnly = cms.bool(False),
            lip = cms.double(30.0),
            maxPhi = cms.double(3.2),
            maxRapidity = cms.double(4.5),
            minHit = cms.int32(0),
            minPhi = cms.double(-3.2),
            minRapidity = cms.double(-4.5),
            pdgId = cms.vint32(),
            ptMax = cms.double(1e+100),
            ptMin = cms.double(0.9), # previous 0.05
            signalOnly = cms.bool(True),
            stableOnly = cms.bool(False),
            tip = cms.double(2.5) #previous 3.5
        ),
        TpSelectorForEfficiencyVsPhi = cms.PSet(
            chargedOnly = cms.bool(True),
            invertRapidityCut = cms.bool(False), # cmssw_11_1
            intimeOnly = cms.bool(False),
            lip = cms.double(30.0),
            maxPhi = cms.double(3.2),
            maxRapidity = cms.double(4.5),
            minHit = cms.int32(0),
            minPhi = cms.double(-3.2),
            minRapidity = cms.double(-4.5),
            pdgId = cms.vint32(),
            ptMax = cms.double(1e+100),
            ptMin = cms.double(0.9), # previous 0.05
            signalOnly = cms.bool(True),
            stableOnly = cms.bool(False),
            tip = cms.double(2.5) #previous 3.5
        ),
        TpSelectorForEfficiencyVsPt = cms.PSet(
            chargedOnly = cms.bool(True),
            invertRapidityCut = cms.bool(False), # cmssw_11_1
            intimeOnly = cms.bool(False),
            lip = cms.double(30.0),
            maxPhi = cms.double(3.2),
            maxRapidity = cms.double(4.5),
            minHit = cms.int32(0),
            minPhi = cms.double(-3.2),
            minRapidity = cms.double(-4.5),
            pdgId = cms.vint32(),
            ptMax = cms.double(1e+100),
            ptMin = cms.double(0.9), # previous 0.05
            signalOnly = cms.bool(True),
            stableOnly = cms.bool(False),
            tip = cms.double(2.5) #previous 3.5
        ),
        TpSelectorForEfficiencyVsVTXR = cms.PSet(
            chargedOnly = cms.bool(True),
            invertRapidityCut = cms.bool(False), # cmssw_11_1
            intimeOnly = cms.bool(False),
            lip = cms.double(30.0),
            maxPhi = cms.double(3.2),
            maxRapidity = cms.double(4.5),
            minHit = cms.int32(0),
            minPhi = cms.double(-3.2),
            minRapidity = cms.double(-4.5),
            pdgId = cms.vint32(),
            ptMax = cms.double(1e+100),
            ptMin = cms.double(0.9), # previous 0.05
            signalOnly = cms.bool(True),
            stableOnly = cms.bool(False),
            tip = cms.double(60.0) 
        ),
        TpSelectorForEfficiencyVsVTXZ = cms.PSet(
            chargedOnly = cms.bool(True),
            invertRapidityCut = cms.bool(False), # cmssw_11_1
            intimeOnly = cms.bool(False),
            lip = cms.double(30.0),
            maxPhi = cms.double(3.2),
            maxRapidity = cms.double(4.5),
            minHit = cms.int32(0),
            minPhi = cms.double(-3.2),
            minRapidity = cms.double(-4.5),
            pdgId = cms.vint32(),
            ptMax = cms.double(1e+100),
            ptMin = cms.double(0.9), # previous 0.05
            signalOnly = cms.bool(True),
            stableOnly = cms.bool(False),
            tip = cms.double(2.5) #previous 3.5
        ),
        cotThetaRes_nbin = cms.int32(300),
        cotThetaRes_rangeMax = cms.double(0.02),
        cotThetaRes_rangeMin = cms.double(-0.02),
        doMTDPlots = cms.untracked.bool(True), # cmssw_11_1
        dxyDzZoom = cms.double(25),
        dxyRes_nbin = cms.int32(500),
        dxyRes_rangeMax = cms.double(0.1),
        dxyRes_rangeMin = cms.double(-0.1),
        dzRes_nbin = cms.int32(150),
        dzRes_rangeMax = cms.double(0.05),
        dzRes_rangeMin = cms.double(-0.05),
        generalGpSelector = cms.PSet(
            chargedOnly = cms.bool(True),
            invertRapidityCut = cms.bool(False), # cmssw_11_1
            lip = cms.double(30.0),
            maxPhi = cms.double(3.2), # cmssw_11_1
            minPhi = cms.double(-3.2), # cmssw_11_1
            maxRapidity = cms.double(4.5), #previous 2.5
            minRapidity = cms.double(-4.5), #previous -2.5
            pdgId = cms.vint32(),
            ptMin = cms.double(0.9),
            status = cms.int32(1),
            tip = cms.double(2.5) #previous 3.5
        ),
        generalTpSelector = cms.PSet(
            chargedOnly = cms.bool(True),
            invertRapidityCut = cms.bool(False), # cmssw_11_1
            intimeOnly = cms.bool(False),
            lip = cms.double(30.0),
            maxPhi = cms.double(3.2),
            maxRapidity = cms.double(4.5),
            minHit = cms.int32(0),
            minPhi = cms.double(-3.2),
            minRapidity = cms.double(-4.5),
            pdgId = cms.vint32(),
            ptMax = cms.double(1e+100),
            ptMin = cms.double(0.9),
            signalOnly = cms.bool(True),
            stableOnly = cms.bool(False),
            tip = cms.double(2.5) #previous 3.5
        ),
        maxChi2 = cms.double(20),
        maxDeDx = cms.double(10.0),
        maxDxy = cms.double(25),
        maxDz = cms.double(30),
        maxDzpvCumulative = cms.double(0.6),
        maxDzpvsigCumulative = cms.double(10),
        maxEta = cms.double(4.5),
        maxHit = cms.double(80.5),
        maxLayers = cms.double(25.5),
        maxMVA = cms.double(1),
        maxPVz = cms.double(60),
        maxPhi = cms.double(3.1416),
        maxPt = cms.double(1000),
        maxPu = cms.double(259.5),
        maxTracks = cms.double(2000),
        maxVertcount = cms.double(160.5),
        maxVertpos = cms.double(100),
        maxZpos = cms.double(30),
        maxdr = cms.double(1),
        minChi2 = cms.double(0),
        minDeDx = cms.double(0.0),
        minDxy = cms.double(-25),
        minDz = cms.double(-30),
        minEta = cms.double(-4.5),
        minHit = cms.double(-0.5),
        minLayers = cms.double(-0.5),
        minMVA = cms.double(-1),
        minPVz = cms.double(-60),
        minPhi = cms.double(-3.1416),
        minPt = cms.double(0.1), # logscale
        minPu = cms.double(-0.5),
        minTracks = cms.double(0),
        minVertcount = cms.double(-0.5),
        minVertpos = cms.double(0.01),
        minZpos = cms.double(-30),
        mindr = cms.double(0.001),
        nintChi2 = cms.int32(40),
        nintDeDx = cms.int32(40),
        nintDxy = cms.int32(100),
        nintDz = cms.int32(60),
        nintDzpvCumulative = cms.int32(240),
        nintDzpvsigCumulative = cms.int32(200),
        nintEta = cms.int32(90),
        nintHit = cms.int32(81),
        nintLayers = cms.int32(26),
        nintMVA = cms.int32(100),
        nintPVz = cms.int32(120),
        nintPhi = cms.int32(36),
        nintPt = cms.int32(40),
        nintPu = cms.int32(130),
        nintTracks = cms.int32(200),
        nintVertcount = cms.int32(161),
        nintVertpos = cms.int32(40),
        nintZpos = cms.int32(60),
        nintdr = cms.int32(100),
        phiRes_nbin = cms.int32(300),
        phiRes_rangeMax = cms.double(0.01),
        phiRes_rangeMin = cms.double(-0.01),
        ptRes_nbin = cms.int32(100),
        ptRes_rangeMax = cms.double(0.1),
        ptRes_rangeMin = cms.double(-0.1),
        seedingLayerSets = cms.vstring(
            'BPix1+BPix2+BPix3+BPix4', 
            'BPix1+BPix2+BPix3+FPix1_pos', 
            'BPix1+BPix2+BPix3+FPix1_neg', 
            'BPix1+BPix2+FPix1_pos+FPix2_pos', 
            'BPix1+BPix2+FPix1_neg+FPix2_neg', 
            'BPix1+FPix1_pos+FPix2_pos+FPix3_pos', 
            'BPix1+FPix1_neg+FPix2_neg+FPix3_neg', 
            'FPix1_pos+FPix2_pos+FPix3_pos+FPix4_pos', 
            'FPix1_neg+FPix2_neg+FPix3_neg+FPix4_neg', 
            'FPix2_pos+FPix3_pos+FPix4_pos+FPix5_pos', 
            'FPix2_neg+FPix3_neg+FPix4_neg+FPix5_neg', 
            'FPix3_pos+FPix4_pos+FPix5_pos+FPix6_pos', 
            'FPix3_neg+FPix4_neg+FPix5_neg+FPix6_neg', 
            'FPix4_pos+FPix5_pos+FPix6_pos+FPix7_pos', 
            'FPix4_neg+FPix5_neg+FPix6_neg+FPix7_neg', 
            'FPix5_pos+FPix6_pos+FPix7_pos+FPix8_pos', 
            'FPix5_neg+FPix6_neg+FPix7_neg+FPix8_neg', 
            'BPix1+BPix2+BPix3', 
            'BPix2+BPix3+BPix4', 
            'BPix1+BPix3+BPix4', 
            'BPix1+BPix2+BPix4', 
            'BPix2+BPix3+FPix1_pos', 
            'BPix2+BPix3+FPix1_neg', 
            'BPix1+BPix2+FPix1_pos', 
            'BPix1+BPix2+FPix1_neg', 
            'BPix2+FPix1_pos+FPix2_pos', 
            'BPix2+FPix1_neg+FPix2_neg', 
            'BPix1+FPix1_pos+FPix2_pos', 
            'BPix1+FPix1_neg+FPix2_neg', 
            'FPix1_pos+FPix2_pos+FPix3_pos', 
            'FPix1_neg+FPix2_neg+FPix3_neg', 
            'BPix1+FPix2_pos+FPix3_pos', 
            'BPix1+FPix2_neg+FPix3_neg', 
            'FPix2_pos+FPix3_pos+FPix4_pos', 
            'FPix2_neg+FPix3_neg+FPix4_neg', 
            'FPix3_pos+FPix4_pos+FPix5_pos', 
            'FPix3_neg+FPix4_neg+FPix5_neg', 
            'FPix4_pos+FPix5_pos+FPix6_pos', 
            'FPix4_neg+FPix5_neg+FPix6_neg', 
            'FPix5_pos+FPix6_pos+FPix7_pos', 
            'FPix5_neg+FPix6_neg+FPix7_neg', 
            'FPix6_pos+FPix7_pos+FPix8_pos', 
            'FPix6_neg+FPix7_neg+FPix8_neg', 
            'BPix1+BPix2', 
            'BPix1+BPix3', 
            'BPix2+BPix3', 
            'BPix1+FPix1_pos', 
            'BPix1+FPix1_neg', 
            'BPix2+FPix1_pos', 
            'BPix2+FPix1_neg'
        ),
        useFabsEta = cms.bool(False),
        useInvPt = cms.bool(False),
        useLogPt = cms.untracked.bool(True),
        useLogVertpos = cms.untracked.bool(True)
    ),
    ignoremissingtrackcollection = cms.untracked.bool(False),
    intimeOnlyTP = cms.bool(True),
    invertRapidityCutTP = cms.bool(False), # cmssw_11_1
    label = cms.VInputTag(
        "hltPhase2GeneralTracks", "hltPhase2CutsRecoTracksHp", "hltPhase2CutsRecoTracksInitialStep", "hltPhase2CutsRecoTracksHighPtTripletStep",  
        "hltPhase2CutsRecoTracksInitialStepHp", "hltPhase2CutsRecoTracksHighPtTripletStepHp",   
        "hltPhase2CutsRecoTracksInitialStepByOriginalAlgo", "hltPhase2CutsRecoTracksHighPtTripletStepByOriginalAlgo",   	"hltPhase2CutsRecoTracksInitialStepByOriginalAlgoHp", "hltPhase2CutsRecoTracksHighPtTripletStepByOriginalAlgoHp", 
        "hltPhase2CutsRecoTracksInitialStepByAlgoMask", "hltPhase2CutsRecoTracksHighPtTripletStepByAlgoMask",   
        "hltPhase2CutsRecoTracksInitialStepByAlgoMaskHp", "hltPhase2CutsRecoTracksHighPtTripletStepByAlgoMaskHp",   
        "hltPhase2CutsRecoTracksPt09InitialStep", 
        "hltPhase2CutsRecoTracksPt09HighPtTripletStep", "hltPhase2CutsRecoTracksPt09InitialStepHp", "hltPhase2CutsRecoTracksPt09HighPtTripletStepHp"
    ),
    label_pileupinfo = cms.InputTag("addPileupInfo"),
    label_tp_effic = cms.InputTag("mix","MergedTrackTruth"),
    label_tp_effic_refvector = cms.bool(False),
    label_tp_fake = cms.InputTag("mix","MergedTrackTruth"),
    label_tp_fake_refvector = cms.bool(False),
    label_tp_nlayers = cms.InputTag("trackingParticleNumberOfLayersProducer","trackerLayers"),
    label_tp_npixellayers = cms.InputTag("trackingParticleNumberOfLayersProducer","pixelLayers"),
    label_tp_nstripstereolayers = cms.InputTag("trackingParticleNumberOfLayersProducer","stripStereoLayers"),
    label_tv = cms.InputTag("mix","MergedTrackTruth"),
    label_vertex = cms.untracked.InputTag("hltPhase2OfflinePrimaryVertices"),
    lipTP = cms.double(30.0),
    maxRapidityTP = cms.double(4.5),
    minHitTP = cms.int32(0),
    minRapidityTP = cms.double(-4.5),
    mvaLabels = cms.untracked.PSet(

    ),
    parametersDefiner = cms.string('LhcParametersDefinerForTP'),
    pdgIdTP = cms.vint32(),
    ptMaxTP = cms.double(0.9),
    ptMinTP = cms.double(0.9), # previous 0.005
    signalOnlyTP = cms.bool(False),
    sim = cms.VInputTag(
        cms.InputTag("g4SimHits","TrackerHitsPixelBarrelLowTof"), cms.InputTag("g4SimHits","TrackerHitsPixelBarrelHighTof"), cms.InputTag("g4SimHits","TrackerHitsPixelEndcapLowTof"), cms.InputTag("g4SimHits","TrackerHitsPixelEndcapHighTof"), cms.InputTag("g4SimHits","TrackerHitsTIBLowTof"), 
        cms.InputTag("g4SimHits","TrackerHitsTIBHighTof"), cms.InputTag("g4SimHits","TrackerHitsTIDLowTof"), cms.InputTag("g4SimHits","TrackerHitsTIDHighTof"), cms.InputTag("g4SimHits","TrackerHitsTOBLowTof"), cms.InputTag("g4SimHits","TrackerHitsTOBHighTof"), 
        cms.InputTag("g4SimHits","TrackerHitsTECLowTof"), cms.InputTag("g4SimHits","TrackerHitsTECHighTof")
    ),
    simHitTpMapTag = cms.InputTag("simHitTPAssocProducer"),
    simPVMaxZ = cms.untracked.double(-1),
    stableOnlyTP = cms.bool(False),
    tipTP = cms.double(60.0), 
    trackCollectionForDrCalculation = cms.InputTag("hltPhase2GeneralTracks"),
    useGsf = cms.bool(False),
    useLogPt = cms.untracked.bool(True),
    vertexAssociator = cms.untracked.InputTag("hltPhase2VertexAssociatorByPositionAndTracks")
)


hltPhase2TrackValidatorFromPVStandalone = cms.EDProducer("MultiTrackValidator", #cmssw_11_1 previous cms.EDAnalyzer
    cores = cms.InputTag("highPtJets"), #cmssw_10_6  #cmssw_11_1
    UseAssociators = cms.bool(False),
    associators = cms.untracked.VInputTag("hltPhase2TrackingParticleRecoTrackAsssociation"),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    calculateDrSingleCollection = cms.untracked.bool(True),
    chargedOnlyTP = cms.bool(True),
    dEdx1Tag = cms.InputTag("dedxHarmonic2"),
    dEdx2Tag = cms.InputTag("dedxTruncated40"),
    dirName = cms.string('Tracking/TrackFromPV/'),
    doMVAPlots = cms.untracked.bool(False),
    doPVAssociationPlots = cms.untracked.bool(False),
    doPlotsOnlyForTruePV = cms.untracked.bool(True),
    doRecoTrackPlots = cms.untracked.bool(True),
    doResolutionPlotsForLabels = cms.VInputTag(),
    doSeedPlots = cms.untracked.bool(False),
    doSimPlots = cms.untracked.bool(True),
    doSimTrackPlots = cms.untracked.bool(True),
    doSummaryPlots = cms.untracked.bool(True),
    dodEdxPlots = cms.untracked.bool(False),
    histoProducerAlgoBlock = cms.PSet(
	mindrj = cms.double(0.001), #cmssw_10_6
        maxdrj = cms.double(0.1), #cmssw_10_6
        nintdrj = cms.int32(100), #cmssw_10_6
        GpSelectorForEfficiencyVsEta = cms.PSet(
            chargedOnly = cms.bool(True),
            invertRapidityCut = cms.bool(False), # cmssw_11_1
            lip = cms.double(30.0),
            maxPhi = cms.double(3.2), # cmssw_11_1
            minPhi = cms.double(-3.2), # cmssw_11_1
            maxRapidity = cms.double(4.5), #previous 2.5 
            minRapidity = cms.double(-4.5), #previous -2.5
            pdgId = cms.vint32(),
            ptMin = cms.double(0.9),
            status = cms.int32(1),
            tip = cms.double(2.5) #previous 3.5
        ),
        GpSelectorForEfficiencyVsPhi = cms.PSet(
            chargedOnly = cms.bool(True),
            invertRapidityCut = cms.bool(False), # cmssw_11_1
            lip = cms.double(30.0),
            maxPhi = cms.double(3.2), # cmssw_11_1
            minPhi = cms.double(-3.2), # cmssw_11_1
            maxRapidity = cms.double(4.5), #previous 2.5
            minRapidity = cms.double(-4.5), #previous -2.5
            pdgId = cms.vint32(),
            ptMin = cms.double(0.9),
            status = cms.int32(1),
            tip = cms.double(2.5) #previous 3.5
        ),
        GpSelectorForEfficiencyVsPt = cms.PSet(
            chargedOnly = cms.bool(True),
            invertRapidityCut = cms.bool(False), # cmssw_11_1
            lip = cms.double(30.0),
            maxPhi = cms.double(3.2), # cmssw_11_1
            minPhi = cms.double(-3.2), # cmssw_11_1
            maxRapidity = cms.double(4.5), #previous 2.5
            minRapidity = cms.double(-4.5), #previous -2.5
            pdgId = cms.vint32(),
            ptMin = cms.double(0.9), # previous 0.05
            status = cms.int32(1),
            tip = cms.double(2.5) #previous 3.5
        ),
        GpSelectorForEfficiencyVsVTXR = cms.PSet(
            chargedOnly = cms.bool(True),
            invertRapidityCut = cms.bool(False), # cmssw_11_1
            lip = cms.double(30.0),
            maxPhi = cms.double(3.2), # cmssw_11_1
            minPhi = cms.double(-3.2), # cmssw_11_1
            maxRapidity = cms.double(4.5), #previous 2.5
            minRapidity = cms.double(-4.5), #previous -2.5
            pdgId = cms.vint32(),
            ptMin = cms.double(0.9),
            status = cms.int32(1),
            tip = cms.double(30.0) 
        ),
        GpSelectorForEfficiencyVsVTXZ = cms.PSet(
            chargedOnly = cms.bool(True),
            invertRapidityCut = cms.bool(False), # cmssw_11_1
            lip = cms.double(35.0),
            maxPhi = cms.double(3.2), # cmssw_11_1
            minPhi = cms.double(-3.2), # cmssw_11_1
            maxRapidity = cms.double(4.5), #previous 2.5
            minRapidity = cms.double(-4.5), #previous -2.5
            pdgId = cms.vint32(),
            ptMin = cms.double(0.9),
            status = cms.int32(1),
            tip = cms.double(2.5) #previous 3.5
        ),
        TpSelectorForEfficiencyVsEta = cms.PSet(
            chargedOnly = cms.bool(True),
            invertRapidityCut = cms.bool(False), # cmssw_11_1
            intimeOnly = cms.bool(False),
            lip = cms.double(30.0),
            maxPhi = cms.double(3.2),
            maxRapidity = cms.double(4.5),
            minHit = cms.int32(0),
            minPhi = cms.double(-3.2),
            minRapidity = cms.double(-4.5),
            pdgId = cms.vint32(),
            ptMax = cms.double(1e+100),
            ptMin = cms.double(0.9),
            signalOnly = cms.bool(True),
            stableOnly = cms.bool(False),
            tip = cms.double(2.5) #previous 3.5
        ),
        TpSelectorForEfficiencyVsPhi = cms.PSet(
            chargedOnly = cms.bool(True),
            invertRapidityCut = cms.bool(False), # cmssw_11_1
            intimeOnly = cms.bool(False),
            lip = cms.double(30.0),
            maxPhi = cms.double(3.2),
            maxRapidity = cms.double(4.5),
            minHit = cms.int32(0),
            minPhi = cms.double(-3.2),
            minRapidity = cms.double(-4.5),
            pdgId = cms.vint32(),
            ptMax = cms.double(1e+100),
            ptMin = cms.double(0.9),
            signalOnly = cms.bool(True),
            stableOnly = cms.bool(False),
            tip = cms.double(2.5) #previous 3.5
        ),
        TpSelectorForEfficiencyVsPt = cms.PSet(
            chargedOnly = cms.bool(True),
            invertRapidityCut = cms.bool(False), # cmssw_11_1
            intimeOnly = cms.bool(False),
            lip = cms.double(30.0),
            maxPhi = cms.double(3.2),
            maxRapidity = cms.double(4.5),
            minHit = cms.int32(0),
            minPhi = cms.double(-3.2),
            minRapidity = cms.double(-4.5),
            pdgId = cms.vint32(),
            ptMax = cms.double(1e+100),
            ptMin = cms.double(0.9), # previous 0.05
            signalOnly = cms.bool(True),
            stableOnly = cms.bool(False),
            tip = cms.double(2.5) #previous 3.5
        ),
        TpSelectorForEfficiencyVsVTXR = cms.PSet(
            chargedOnly = cms.bool(True),
            invertRapidityCut = cms.bool(False), # cmssw_11_1
            intimeOnly = cms.bool(False),
            lip = cms.double(30.0),
            maxPhi = cms.double(3.2),
            maxRapidity = cms.double(4.5),
            minHit = cms.int32(0),
            minPhi = cms.double(-3.2),
            minRapidity = cms.double(-4.5),
            pdgId = cms.vint32(),
            ptMax = cms.double(1e+100),
            ptMin = cms.double(0.9),
            signalOnly = cms.bool(True),
            stableOnly = cms.bool(False),
            tip = cms.double(60.0)
        ),
        TpSelectorForEfficiencyVsVTXZ = cms.PSet(
            chargedOnly = cms.bool(True),
            invertRapidityCut = cms.bool(False), # cmssw_11_1
            intimeOnly = cms.bool(False),
            lip = cms.double(30.0),
            maxPhi = cms.double(3.2),
            maxRapidity = cms.double(4.5),
            minHit = cms.int32(0),
            minPhi = cms.double(-3.2),
            minRapidity = cms.double(-4.5),
            pdgId = cms.vint32(),
            ptMax = cms.double(1e+100),
            ptMin = cms.double(0.9),
            signalOnly = cms.bool(True),
            stableOnly = cms.bool(False),
            tip = cms.double(2.5) #previous 3.5
        ),
        cotThetaRes_nbin = cms.int32(300),
        cotThetaRes_rangeMax = cms.double(0.02),
        cotThetaRes_rangeMin = cms.double(-0.02),
        doMTDPlots = cms.untracked.bool(True), # cmssw_11_1
        dxyDzZoom = cms.double(25),
        dxyRes_nbin = cms.int32(500),
        dxyRes_rangeMax = cms.double(0.1),
        dxyRes_rangeMin = cms.double(-0.1),
        dzRes_nbin = cms.int32(150),
        dzRes_rangeMax = cms.double(0.05),
        dzRes_rangeMin = cms.double(-0.05),
        generalGpSelector = cms.PSet(
            chargedOnly = cms.bool(True),
            invertRapidityCut = cms.bool(False), # cmssw_11_1
            lip = cms.double(30.0),
            maxPhi = cms.double(3.2), # cmssw_11_1
            minPhi = cms.double(-3.2), # cmssw_11_1
            maxRapidity = cms.double(4.5), #previous 2.5
            minRapidity = cms.double(-4.5), #previous -2.5
            pdgId = cms.vint32(),
            ptMin = cms.double(0.9),
            status = cms.int32(1),
            tip = cms.double(2.5) #previous 3.5
        ),
        generalTpSelector = cms.PSet(
            chargedOnly = cms.bool(True),
            invertRapidityCut = cms.bool(False), # cmssw_11_1
            intimeOnly = cms.bool(False),
            lip = cms.double(30.0),
            maxPhi = cms.double(3.2),
            maxRapidity = cms.double(4.5),
            minHit = cms.int32(0),
            minPhi = cms.double(-3.2),
            minRapidity = cms.double(-4.5),
            pdgId = cms.vint32(),
            ptMax = cms.double(1e+100),
            ptMin = cms.double(0.9),
            signalOnly = cms.bool(True),
            stableOnly = cms.bool(False),
            tip = cms.double(2.5) #previous 3.5
        ),
        maxChi2 = cms.double(20),
        maxDeDx = cms.double(10.0),
        maxDxy = cms.double(25),
        maxDz = cms.double(30),
        maxDzpvCumulative = cms.double(0.6),
        maxDzpvsigCumulative = cms.double(10),
        maxEta = cms.double(4.5),
        maxHit = cms.double(80.5),
        maxLayers = cms.double(25.5),
        maxMVA = cms.double(1),
        maxPVz = cms.double(60),
        maxPhi = cms.double(3.1416),
        maxPt = cms.double(1000),
        maxPu = cms.double(259.5),
        maxTracks = cms.double(2000),
        maxVertcount = cms.double(160.5),
        maxVertpos = cms.double(100),
        maxZpos = cms.double(30),
        maxdr = cms.double(1),
        minChi2 = cms.double(0),
        minDeDx = cms.double(0.0),
        minDxy = cms.double(-25),
        minDz = cms.double(-30),
        minEta = cms.double(-4.5),
        minHit = cms.double(-0.5),
        minLayers = cms.double(-0.5),
        minMVA = cms.double(-1),
        minPVz = cms.double(-60),
        minPhi = cms.double(-3.1416),
        minPt = cms.double(0.1), # logscale
        minPu = cms.double(-0.5),
        minTracks = cms.double(0),
        minVertcount = cms.double(-0.5),
        minVertpos = cms.double(0.01),
        minZpos = cms.double(-30),
        mindr = cms.double(0.001),
        nintChi2 = cms.int32(40),
        nintDeDx = cms.int32(40),
        nintDxy = cms.int32(100),
        nintDz = cms.int32(60),
        nintDzpvCumulative = cms.int32(240),
        nintDzpvsigCumulative = cms.int32(200),
        nintEta = cms.int32(90),
        nintHit = cms.int32(81),
        nintLayers = cms.int32(26),
        nintMVA = cms.int32(100),
        nintPVz = cms.int32(120),
        nintPhi = cms.int32(36),
        nintPt = cms.int32(40),
        nintPu = cms.int32(130),
        nintTracks = cms.int32(200),
        nintVertcount = cms.int32(161),
        nintVertpos = cms.int32(40),
        nintZpos = cms.int32(60),
        nintdr = cms.int32(100),
        phiRes_nbin = cms.int32(300),
        phiRes_rangeMax = cms.double(0.01),
        phiRes_rangeMin = cms.double(-0.01),
        ptRes_nbin = cms.int32(100),
        ptRes_rangeMax = cms.double(0.1),
        ptRes_rangeMin = cms.double(-0.1),
        seedingLayerSets = cms.vstring(
            'BPix1+BPix2+BPix3+BPix4', 
            'BPix1+BPix2+BPix3+FPix1_pos', 
            'BPix1+BPix2+BPix3+FPix1_neg', 
            'BPix1+BPix2+FPix1_pos+FPix2_pos', 
            'BPix1+BPix2+FPix1_neg+FPix2_neg', 
            'BPix1+FPix1_pos+FPix2_pos+FPix3_pos', 
            'BPix1+FPix1_neg+FPix2_neg+FPix3_neg', 
            'FPix1_pos+FPix2_pos+FPix3_pos+FPix4_pos', 
            'FPix1_neg+FPix2_neg+FPix3_neg+FPix4_neg', 
            'FPix2_pos+FPix3_pos+FPix4_pos+FPix5_pos', 
            'FPix2_neg+FPix3_neg+FPix4_neg+FPix5_neg', 
            'FPix3_pos+FPix4_pos+FPix5_pos+FPix6_pos', 
            'FPix3_neg+FPix4_neg+FPix5_neg+FPix6_neg', 
            'FPix4_pos+FPix5_pos+FPix6_pos+FPix7_pos', 
            'FPix4_neg+FPix5_neg+FPix6_neg+FPix7_neg', 
            'FPix5_pos+FPix6_pos+FPix7_pos+FPix8_pos', 
            'FPix5_neg+FPix6_neg+FPix7_neg+FPix8_neg', 
            'BPix1+BPix2+BPix3', 
            'BPix2+BPix3+BPix4', 
            'BPix1+BPix3+BPix4', 
            'BPix1+BPix2+BPix4', 
            'BPix2+BPix3+FPix1_pos', 
            'BPix2+BPix3+FPix1_neg', 
            'BPix1+BPix2+FPix1_pos', 
            'BPix1+BPix2+FPix1_neg', 
            'BPix2+FPix1_pos+FPix2_pos', 
            'BPix2+FPix1_neg+FPix2_neg', 
            'BPix1+FPix1_pos+FPix2_pos', 
            'BPix1+FPix1_neg+FPix2_neg', 
            'FPix1_pos+FPix2_pos+FPix3_pos', 
            'FPix1_neg+FPix2_neg+FPix3_neg', 
            'BPix1+FPix2_pos+FPix3_pos', 
            'BPix1+FPix2_neg+FPix3_neg', 
            'FPix2_pos+FPix3_pos+FPix4_pos', 
            'FPix2_neg+FPix3_neg+FPix4_neg', 
            'FPix3_pos+FPix4_pos+FPix5_pos', 
            'FPix3_neg+FPix4_neg+FPix5_neg', 
            'FPix4_pos+FPix5_pos+FPix6_pos', 
            'FPix4_neg+FPix5_neg+FPix6_neg', 
            'FPix5_pos+FPix6_pos+FPix7_pos', 
            'FPix5_neg+FPix6_neg+FPix7_neg', 
            'FPix6_pos+FPix7_pos+FPix8_pos', 
            'FPix6_neg+FPix7_neg+FPix8_neg', 
            'BPix1+BPix2', 
            'BPix1+BPix3', 
            'BPix2+BPix3', 
            'BPix1+FPix1_pos', 
            'BPix1+FPix1_neg', 
            'BPix2+FPix1_pos', 
            'BPix2+FPix1_neg'
        ),
        useFabsEta = cms.bool(False),
        useInvPt = cms.bool(False),
        useLogPt = cms.untracked.bool(True),
        useLogVertpos = cms.untracked.bool(True)
    ),
    ignoremissingtrackcollection = cms.untracked.bool(False),
    intimeOnlyTP = cms.bool(True),
    invertRapidityCutTP = cms.bool(False), # cmssw_11_1
    label = cms.VInputTag(
        "hltPhase2GeneralTracksFromPV", "hltPhase2CutsRecoTracksFromPVHp", "hltPhase2GeneralTracksFromPVPt09", "hltPhase2CutsRecoTracksFromPVPt09Hp", "hltPhase2CutsRecoTracksFromPVInitialStep", 
        "hltPhase2CutsRecoTracksFromPVHighPtTripletStep", "hltPhase2CutsRecoTracksFromPVInitialStepHp", "hltPhase2CutsRecoTracksFromPVHighPtTripletStepHp", 
        "hltPhase2CutsRecoTracksFromPVPt09InitialStep", "hltPhase2CutsRecoTracksFromPVPt09HighPtTripletStep", 
        "hltPhase2CutsRecoTracksFromPVPt09InitialStepHp", "hltPhase2CutsRecoTracksFromPVPt09HighPtTripletStepHp",
    ),
    label_pileupinfo = cms.InputTag("addPileupInfo"),
    label_tp_effic = cms.InputTag("hltPhase2TrackingParticlesSignal"),
    label_tp_effic_refvector = cms.bool(True),
    label_tp_fake = cms.InputTag("hltPhase2TrackingParticlesSignal"),
    label_tp_fake_refvector = cms.bool(True),
    label_tp_nlayers = cms.InputTag("trackingParticleNumberOfLayersProducer","trackerLayers"),
    label_tp_npixellayers = cms.InputTag("trackingParticleNumberOfLayersProducer","pixelLayers"),
    label_tp_nstripstereolayers = cms.InputTag("trackingParticleNumberOfLayersProducer","stripStereoLayers"),
    label_tv = cms.InputTag("mix","MergedTrackTruth"),
    label_vertex = cms.untracked.InputTag("hltPhase2OfflinePrimaryVertices"),
    lipTP = cms.double(30.0),
    maxRapidityTP = cms.double(4.5),
    minHitTP = cms.int32(0),
    minRapidityTP = cms.double(-4.5),
    mvaLabels = cms.untracked.PSet(

    ),
    parametersDefiner = cms.string('LhcParametersDefinerForTP'),
    pdgIdTP = cms.vint32(),
    ptMaxTP = cms.double(1e+100),
    ptMinTP = cms.double(0.9), # previous 0.005
    signalOnlyTP = cms.bool(False),
    sim = cms.VInputTag(
        cms.InputTag("g4SimHits","TrackerHitsPixelBarrelLowTof"), cms.InputTag("g4SimHits","TrackerHitsPixelBarrelHighTof"), cms.InputTag("g4SimHits","TrackerHitsPixelEndcapLowTof"), cms.InputTag("g4SimHits","TrackerHitsPixelEndcapHighTof"), cms.InputTag("g4SimHits","TrackerHitsTIBLowTof"), 
        cms.InputTag("g4SimHits","TrackerHitsTIBHighTof"), cms.InputTag("g4SimHits","TrackerHitsTIDLowTof"), cms.InputTag("g4SimHits","TrackerHitsTIDHighTof"), cms.InputTag("g4SimHits","TrackerHitsTOBLowTof"), cms.InputTag("g4SimHits","TrackerHitsTOBHighTof"), 
        cms.InputTag("g4SimHits","TrackerHitsTECLowTof"), cms.InputTag("g4SimHits","TrackerHitsTECHighTof")
    ),
    simHitTpMapTag = cms.InputTag("simHitTPAssocProducer"),
    simPVMaxZ = cms.untracked.double(-1),
    stableOnlyTP = cms.bool(False),
    tipTP = cms.double(60.0), 
    trackCollectionForDrCalculation = cms.InputTag("hltPhase2GeneralTracksFromPV"),
    useGsf = cms.bool(False),
    useLogPt = cms.untracked.bool(True),
    vertexAssociator = cms.untracked.InputTag("hltPhase2VertexAssociatorByPositionAndTracks")
)


hltPhase2TrackValidatorFromPVAllTPStandalone = cms.EDProducer("MultiTrackValidator", #cmssw_11_1 previous cms.EDAnalyzer
    cores = cms.InputTag("highPtJets"), #cmssw_10_6 #cmssw_11_1
    UseAssociators = cms.bool(False),
    associators = cms.untracked.VInputTag("hltPhase2TrackingParticleRecoTrackAsssociation"),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    calculateDrSingleCollection = cms.untracked.bool(True),
    chargedOnlyTP = cms.bool(True),
    dEdx1Tag = cms.InputTag("dedxHarmonic2"),
    dEdx2Tag = cms.InputTag("dedxTruncated40"),
    dirName = cms.string('Tracking/TrackFromPVAllTP/'),
    doMVAPlots = cms.untracked.bool(False),
    doPVAssociationPlots = cms.untracked.bool(False),
    doPlotsOnlyForTruePV = cms.untracked.bool(True),
    doRecoTrackPlots = cms.untracked.bool(True),
    doResolutionPlotsForLabels = cms.VInputTag("disabled"),
    doSeedPlots = cms.untracked.bool(False),
    doSimPlots = cms.untracked.bool(False),
    doSimTrackPlots = cms.untracked.bool(False),
    doSummaryPlots = cms.untracked.bool(True),
    dodEdxPlots = cms.untracked.bool(False),
    histoProducerAlgoBlock = cms.PSet(
	mindrj = cms.double(0.001),
        maxdrj = cms.double(0.1),
        nintdrj = cms.int32(100),
        GpSelectorForEfficiencyVsEta = cms.PSet(
            chargedOnly = cms.bool(True),
            invertRapidityCut = cms.bool(False), # cmssw_11_1
            lip = cms.double(30.0),
            maxPhi = cms.double(3.2), # cmssw_11_1
            minPhi = cms.double(-3.2), # cmssw_11_1
            maxRapidity = cms.double(4.5), #previous 2.5 
            minRapidity = cms.double(-4.5), #previous -2.5
            pdgId = cms.vint32(),
            ptMin = cms.double(0.9),
            status = cms.int32(1),
            tip = cms.double(2.5) #previous 3.5
        ),
        GpSelectorForEfficiencyVsPhi = cms.PSet(
            chargedOnly = cms.bool(True),
            invertRapidityCut = cms.bool(False), # cmssw_11_1
            lip = cms.double(30.0),
            maxPhi = cms.double(3.2), # cmssw_11_1
            minPhi = cms.double(-3.2), # cmssw_11_1
            maxRapidity = cms.double(4.5), #previous 2.5
            minRapidity = cms.double(-4.5), #previous -2.5
            pdgId = cms.vint32(),
            ptMin = cms.double(0.9),
            status = cms.int32(1),
            tip = cms.double(2.5) #previous 3.5
        ),
        GpSelectorForEfficiencyVsPt = cms.PSet(
            chargedOnly = cms.bool(True),
            invertRapidityCut = cms.bool(False), # cmssw_11_1
            lip = cms.double(30.0),
            maxPhi = cms.double(3.2), # cmssw_11_1
            minPhi = cms.double(-3.2), # cmssw_11_1
            maxRapidity = cms.double(4.5), #previous 2.5
            minRapidity = cms.double(-4.5), #previous -2.5
            pdgId = cms.vint32(),
            ptMin = cms.double(0.9), # previous 0.05
            status = cms.int32(1),
            tip = cms.double(2.5) #previous 3.5
        ),
        GpSelectorForEfficiencyVsVTXR = cms.PSet(
            chargedOnly = cms.bool(True),
            invertRapidityCut = cms.bool(False), # cmssw_11_1
            lip = cms.double(30.0),
            maxPhi = cms.double(3.2), # cmssw_11_1
            minPhi = cms.double(-3.2), # cmssw_11_1
            maxRapidity = cms.double(4.5), #previous 2.5
            minRapidity = cms.double(-4.5), #previous -2.5
            pdgId = cms.vint32(),
            ptMin = cms.double(0.9),
            status = cms.int32(1),
            tip = cms.double(30.0) 
        ),
        GpSelectorForEfficiencyVsVTXZ = cms.PSet(
            chargedOnly = cms.bool(True),
            invertRapidityCut = cms.bool(False), # cmssw_11_1
            lip = cms.double(35.0),
            maxPhi = cms.double(3.2), # cmssw_11_1
            minPhi = cms.double(-3.2), # cmssw_11_1
            maxRapidity = cms.double(4.5), #previous 2.5
            minRapidity = cms.double(-4.5), #previous -2.5
            pdgId = cms.vint32(),
            ptMin = cms.double(0.9),
            status = cms.int32(1),
            tip = cms.double(2.5) #previous 3.5
        ),
        TpSelectorForEfficiencyVsEta = cms.PSet(
            chargedOnly = cms.bool(True),
            invertRapidityCut = cms.bool(False), # cmssw_11_1
            intimeOnly = cms.bool(False),
            lip = cms.double(30.0),
            maxPhi = cms.double(3.2),
            maxRapidity = cms.double(4.5),
            minHit = cms.int32(0),
            minPhi = cms.double(-3.2),
            minRapidity = cms.double(-4.5),
            pdgId = cms.vint32(),
            ptMax = cms.double(1e+100),
            ptMin = cms.double(0.9),
            signalOnly = cms.bool(True),
            stableOnly = cms.bool(False),
            tip = cms.double(2.5) #previous 3.5
        ),
        TpSelectorForEfficiencyVsPhi = cms.PSet(
            chargedOnly = cms.bool(True),
            invertRapidityCut = cms.bool(False), # cmssw_11_1
            intimeOnly = cms.bool(False),
            lip = cms.double(30.0),
            maxPhi = cms.double(3.2),
            maxRapidity = cms.double(4.5),
            minHit = cms.int32(0),
            minPhi = cms.double(-3.2),
            minRapidity = cms.double(-4.5),
            pdgId = cms.vint32(),
            ptMax = cms.double(1e+100),
            ptMin = cms.double(0.9),
            signalOnly = cms.bool(True),
            stableOnly = cms.bool(False),
            tip = cms.double(2.5) #previous 3.5
        ),
        TpSelectorForEfficiencyVsPt = cms.PSet(
            chargedOnly = cms.bool(True),
            invertRapidityCut = cms.bool(False), # cmssw_11_1
            intimeOnly = cms.bool(False),
            lip = cms.double(30.0),
            maxPhi = cms.double(3.2),
            maxRapidity = cms.double(4.5),
            minHit = cms.int32(0),
            minPhi = cms.double(-3.2),
            minRapidity = cms.double(-4.5),
            pdgId = cms.vint32(),
            ptMax = cms.double(1e+100),
            ptMin = cms.double(0.9), # previous 0.05
            signalOnly = cms.bool(True),
            stableOnly = cms.bool(False),
            tip = cms.double(2.5) #previous 3.5
        ),
        TpSelectorForEfficiencyVsVTXR = cms.PSet(
            chargedOnly = cms.bool(True),
            invertRapidityCut = cms.bool(False), # cmssw_11_1
            intimeOnly = cms.bool(False),
            lip = cms.double(30.0),
            maxPhi = cms.double(3.2),
            maxRapidity = cms.double(4.5),
            minHit = cms.int32(0),
            minPhi = cms.double(-3.2),
            minRapidity = cms.double(-4.5),
            pdgId = cms.vint32(),
            ptMax = cms.double(1e+100),
            ptMin = cms.double(0.9),
            signalOnly = cms.bool(True),
            stableOnly = cms.bool(False),
            tip = cms.double(60.0)
        ),
        TpSelectorForEfficiencyVsVTXZ = cms.PSet(
            chargedOnly = cms.bool(True),
            invertRapidityCut = cms.bool(False), # cmssw_11_1
            intimeOnly = cms.bool(False),
            lip = cms.double(30.0),
            maxPhi = cms.double(3.2),
            maxRapidity = cms.double(4.5),
            minHit = cms.int32(0),
            minPhi = cms.double(-3.2),
            minRapidity = cms.double(-4.5),
            pdgId = cms.vint32(),
            ptMax = cms.double(1e+100),
            ptMin = cms.double(0.9),
            signalOnly = cms.bool(True),
            stableOnly = cms.bool(False),
            tip = cms.double(2.5) #previous 3.5
        ),
        cotThetaRes_nbin = cms.int32(300),
        cotThetaRes_rangeMax = cms.double(0.02),
        cotThetaRes_rangeMin = cms.double(-0.02),
        doMTDPlots = cms.untracked.bool(True), # cmssw_11_1
        dxyDzZoom = cms.double(25),
        dxyRes_nbin = cms.int32(500),
        dxyRes_rangeMax = cms.double(0.1),
        dxyRes_rangeMin = cms.double(-0.1),
        dzRes_nbin = cms.int32(150),
        dzRes_rangeMax = cms.double(0.05),
        dzRes_rangeMin = cms.double(-0.05),
        generalGpSelector = cms.PSet(
            chargedOnly = cms.bool(True),
            invertRapidityCut = cms.bool(False), # cmssw_11_1
            lip = cms.double(30.0),
            maxPhi = cms.double(3.2), # cmssw_11_1
            minPhi = cms.double(-3.2), # cmssw_11_1
            maxRapidity = cms.double(4.5), #previous 2.5
            minRapidity = cms.double(-4.5), #previous -2.5
            pdgId = cms.vint32(),
            ptMin = cms.double(0.9),
            status = cms.int32(1),
            tip = cms.double(2.5) #previous 3.5
        ),
        generalTpSelector = cms.PSet(
            chargedOnly = cms.bool(True),
            invertRapidityCut = cms.bool(False), # cmssw_11_1
            intimeOnly = cms.bool(False),
            lip = cms.double(30.0),
            maxPhi = cms.double(3.2),
            maxRapidity = cms.double(4.5),
            minHit = cms.int32(0),
            minPhi = cms.double(-3.2),
            minRapidity = cms.double(-4.5),
            pdgId = cms.vint32(),
            ptMax = cms.double(1e+100),
            ptMin = cms.double(0.9),
            signalOnly = cms.bool(True),
            stableOnly = cms.bool(False),
            tip = cms.double(2.5) #previous 3.5
        ),
        maxChi2 = cms.double(20),
        maxDeDx = cms.double(10.0),
        maxDxy = cms.double(25),
        maxDz = cms.double(30),
        maxDzpvCumulative = cms.double(0.6),
        maxDzpvsigCumulative = cms.double(10),
        maxEta = cms.double(4.5),
        maxHit = cms.double(80.5),
        maxLayers = cms.double(25.5),
        maxMVA = cms.double(1),
        maxPVz = cms.double(60),
        maxPhi = cms.double(3.1416),
        maxPt = cms.double(1000),
        maxPu = cms.double(259.5),
        maxTracks = cms.double(2000),
        maxVertcount = cms.double(160.5),
        maxVertpos = cms.double(100),
        maxZpos = cms.double(30),
        maxdr = cms.double(1),
        minChi2 = cms.double(0),
        minDeDx = cms.double(0.0),
        minDxy = cms.double(-25),
        minDz = cms.double(-30),
        minEta = cms.double(-4.5),
        minHit = cms.double(-0.5),
        minLayers = cms.double(-0.5),
        minMVA = cms.double(-1),
        minPVz = cms.double(-60),
        minPhi = cms.double(-3.1416),
        minPt = cms.double(0.1),
        minPu = cms.double(-0.5),
        minTracks = cms.double(0),
        minVertcount = cms.double(-0.5),
        minVertpos = cms.double(0.01),
        minZpos = cms.double(-30),
        mindr = cms.double(0.001),
        nintChi2 = cms.int32(40),
        nintDeDx = cms.int32(40),
        nintDxy = cms.int32(100),
        nintDz = cms.int32(60),
        nintDzpvCumulative = cms.int32(240),
        nintDzpvsigCumulative = cms.int32(200),
        nintEta = cms.int32(90),
        nintHit = cms.int32(81),
        nintLayers = cms.int32(26),
        nintMVA = cms.int32(100),
        nintPVz = cms.int32(120),
        nintPhi = cms.int32(36),
        nintPt = cms.int32(40),
        nintPu = cms.int32(130),
        nintTracks = cms.int32(200),
        nintVertcount = cms.int32(161),
        nintVertpos = cms.int32(40),
        nintZpos = cms.int32(60),
        nintdr = cms.int32(100),
        phiRes_nbin = cms.int32(300),
        phiRes_rangeMax = cms.double(0.01),
        phiRes_rangeMin = cms.double(-0.01),
        ptRes_nbin = cms.int32(100),
        ptRes_rangeMax = cms.double(0.1),
        ptRes_rangeMin = cms.double(-0.1),
        seedingLayerSets = cms.vstring(
            'BPix1+BPix2+BPix3+BPix4', 
            'BPix1+BPix2+BPix3+FPix1_pos', 
            'BPix1+BPix2+BPix3+FPix1_neg', 
            'BPix1+BPix2+FPix1_pos+FPix2_pos', 
            'BPix1+BPix2+FPix1_neg+FPix2_neg', 
            'BPix1+FPix1_pos+FPix2_pos+FPix3_pos', 
            'BPix1+FPix1_neg+FPix2_neg+FPix3_neg', 
            'FPix1_pos+FPix2_pos+FPix3_pos+FPix4_pos', 
            'FPix1_neg+FPix2_neg+FPix3_neg+FPix4_neg', 
            'FPix2_pos+FPix3_pos+FPix4_pos+FPix5_pos', 
            'FPix2_neg+FPix3_neg+FPix4_neg+FPix5_neg', 
            'FPix3_pos+FPix4_pos+FPix5_pos+FPix6_pos', 
            'FPix3_neg+FPix4_neg+FPix5_neg+FPix6_neg', 
            'FPix4_pos+FPix5_pos+FPix6_pos+FPix7_pos', 
            'FPix4_neg+FPix5_neg+FPix6_neg+FPix7_neg', 
            'FPix5_pos+FPix6_pos+FPix7_pos+FPix8_pos', 
            'FPix5_neg+FPix6_neg+FPix7_neg+FPix8_neg', 
            'BPix1+BPix2+BPix3', 
            'BPix2+BPix3+BPix4', 
            'BPix1+BPix3+BPix4', 
            'BPix1+BPix2+BPix4', 
            'BPix2+BPix3+FPix1_pos', 
            'BPix2+BPix3+FPix1_neg', 
            'BPix1+BPix2+FPix1_pos', 
            'BPix1+BPix2+FPix1_neg', 
            'BPix2+FPix1_pos+FPix2_pos', 
            'BPix2+FPix1_neg+FPix2_neg', 
            'BPix1+FPix1_pos+FPix2_pos', 
            'BPix1+FPix1_neg+FPix2_neg', 
            'FPix1_pos+FPix2_pos+FPix3_pos', 
            'FPix1_neg+FPix2_neg+FPix3_neg', 
            'BPix1+FPix2_pos+FPix3_pos', 
            'BPix1+FPix2_neg+FPix3_neg', 
            'FPix2_pos+FPix3_pos+FPix4_pos', 
            'FPix2_neg+FPix3_neg+FPix4_neg', 
            'FPix3_pos+FPix4_pos+FPix5_pos', 
            'FPix3_neg+FPix4_neg+FPix5_neg', 
            'FPix4_pos+FPix5_pos+FPix6_pos', 
            'FPix4_neg+FPix5_neg+FPix6_neg', 
            'FPix5_pos+FPix6_pos+FPix7_pos', 
            'FPix5_neg+FPix6_neg+FPix7_neg', 
            'FPix6_pos+FPix7_pos+FPix8_pos', 
            'FPix6_neg+FPix7_neg+FPix8_neg', 
            'BPix1+BPix2', 
            'BPix1+BPix3', 
            'BPix2+BPix3', 
            'BPix1+FPix1_pos', 
            'BPix1+FPix1_neg', 
            'BPix2+FPix1_pos', 
            'BPix2+FPix1_neg'
        ),
        useFabsEta = cms.bool(False),
        useInvPt = cms.bool(False),
        useLogPt = cms.untracked.bool(True),
        useLogVertpos = cms.untracked.bool(True)
    ),
    ignoremissingtrackcollection = cms.untracked.bool(False),
    intimeOnlyTP = cms.bool(True),
    invertRapidityCutTP = cms.bool(False), # cmssw_11_1
    label = cms.VInputTag(
        "hltPhase2GeneralTracksFromPV", "hltPhase2CutsRecoTracksFromPVHp", "hltPhase2GeneralTracksFromPVPt09", "hltPhase2CutsRecoTracksFromPVPt09Hp", "hltPhase2CutsRecoTracksFromPVInitialStep", 
        "hltPhase2CutsRecoTracksFromPVHighPtTripletStep", "hltPhase2CutsRecoTracksFromPVInitialStepHp", "hltPhase2CutsRecoTracksFromPVHighPtTripletStepHp", 
        "hltPhase2CutsRecoTracksFromPVPt09InitialStep", "hltPhase2CutsRecoTracksFromPVPt09HighPtTripletStep",  
        "hltPhase2CutsRecoTracksFromPVPt09InitialStepHp", "hltPhase2CutsRecoTracksFromPVPt09HighPtTripletStepHp"
    ),
    label_pileupinfo = cms.InputTag("addPileupInfo"),
    label_tp_effic = cms.InputTag("mix","MergedTrackTruth"),
    label_tp_effic_refvector = cms.bool(False),
    label_tp_fake = cms.InputTag("mix","MergedTrackTruth"),
    label_tp_fake_refvector = cms.bool(False),
    label_tp_nlayers = cms.InputTag("trackingParticleNumberOfLayersProducer","trackerLayers"),
    label_tp_npixellayers = cms.InputTag("trackingParticleNumberOfLayersProducer","pixelLayers"),
    label_tp_nstripstereolayers = cms.InputTag("trackingParticleNumberOfLayersProducer","stripStereoLayers"),
    label_tv = cms.InputTag("mix","MergedTrackTruth"),
    label_vertex = cms.untracked.InputTag("hltPhase2OfflinePrimaryVertices"),
    lipTP = cms.double(30.0),
    maxRapidityTP = cms.double(4.5),
    minHitTP = cms.int32(0),
    minRapidityTP = cms.double(-4.5),
    mvaLabels = cms.untracked.PSet(

    ),
    parametersDefiner = cms.string('LhcParametersDefinerForTP'),
    pdgIdTP = cms.vint32(),
    ptMaxTP = cms.double(1e+100),
    ptMinTP = cms.double(0.9), # previous 0.005
    signalOnlyTP = cms.bool(False),
    sim = cms.VInputTag(
        cms.InputTag("g4SimHits","TrackerHitsPixelBarrelLowTof"), cms.InputTag("g4SimHits","TrackerHitsPixelBarrelHighTof"), cms.InputTag("g4SimHits","TrackerHitsPixelEndcapLowTof"), cms.InputTag("g4SimHits","TrackerHitsPixelEndcapHighTof"), cms.InputTag("g4SimHits","TrackerHitsTIBLowTof"), 
        cms.InputTag("g4SimHits","TrackerHitsTIBHighTof"), cms.InputTag("g4SimHits","TrackerHitsTIDLowTof"), cms.InputTag("g4SimHits","TrackerHitsTIDHighTof"), cms.InputTag("g4SimHits","TrackerHitsTOBLowTof"), cms.InputTag("g4SimHits","TrackerHitsTOBHighTof"), 
        cms.InputTag("g4SimHits","TrackerHitsTECLowTof"), cms.InputTag("g4SimHits","TrackerHitsTECHighTof")
    ),
    simHitTpMapTag = cms.InputTag("simHitTPAssocProducer"),
    simPVMaxZ = cms.untracked.double(-1),
    stableOnlyTP = cms.bool(False),
    tipTP = cms.double(60.0), 
    trackCollectionForDrCalculation = cms.InputTag("hltPhase2GeneralTracksFromPV"),
    useGsf = cms.bool(False),
    useLogPt = cms.untracked.bool(True),
    vertexAssociator = cms.untracked.InputTag("hltPhase2VertexAssociatorByPositionAndTracks")
)


hltPhase2TrackValidatorAllTPEfficStandalone = cms.EDProducer("MultiTrackValidator", #cmssw_11_1 previous cms.EDAnalyzer
    cores = cms.InputTag("highPtJets"), #cmssw_10_6  #cmssw_11_1
    UseAssociators = cms.bool(False),
    associators = cms.untracked.VInputTag("hltPhase2TrackingParticleRecoTrackAsssociation"),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    calculateDrSingleCollection = cms.untracked.bool(True),
    chargedOnlyTP = cms.bool(True),
    dEdx1Tag = cms.InputTag("dedxHarmonic2"),
    dEdx2Tag = cms.InputTag("dedxTruncated40"),
    dirName = cms.string('Tracking/TrackAllTPEffic/'),
    doMVAPlots = cms.untracked.bool(False),
    doPVAssociationPlots = cms.untracked.bool(False),
    doPlotsOnlyForTruePV = cms.untracked.bool(False),
    doRecoTrackPlots = cms.untracked.bool(True),
    doResolutionPlotsForLabels = cms.VInputTag("disabled"),
    doSeedPlots = cms.untracked.bool(False),
    doSimPlots = cms.untracked.bool(False),
    doSimTrackPlots = cms.untracked.bool(True),
    doSummaryPlots = cms.untracked.bool(True),
    dodEdxPlots = cms.untracked.bool(False),
    histoProducerAlgoBlock = cms.PSet(
	mindrj = cms.double(0.001),
        maxdrj = cms.double(0.1),
        nintdrj = cms.int32(100),
        GpSelectorForEfficiencyVsEta = cms.PSet(
            chargedOnly = cms.bool(True),
            invertRapidityCut = cms.bool(False), # cmssw_11_1
            lip = cms.double(30.0),
            maxPhi = cms.double(3.2), # cmssw_11_1
            minPhi = cms.double(-3.2), # cmssw_11_1
            maxRapidity = cms.double(4.5), #previous 2.5 
            minRapidity = cms.double(-4.5), #previous -2.5
            pdgId = cms.vint32(),
            ptMin = cms.double(0.9),
            status = cms.int32(1),
            tip = cms.double(2.5) #previous 3.5
        ),
        GpSelectorForEfficiencyVsPhi = cms.PSet(
            chargedOnly = cms.bool(True),
            invertRapidityCut = cms.bool(False), # cmssw_11_1
            lip = cms.double(30.0),
            maxPhi = cms.double(3.2), # cmssw_11_1
            minPhi = cms.double(-3.2), # cmssw_11_1
            maxRapidity = cms.double(4.5), #previous 2.5
            minRapidity = cms.double(-4.5), #previous -2.5
            pdgId = cms.vint32(),
            ptMin = cms.double(0.9),
            status = cms.int32(1),
            tip = cms.double(2.5) #previous 3.5
        ),
        GpSelectorForEfficiencyVsPt = cms.PSet(
            chargedOnly = cms.bool(True),
            invertRapidityCut = cms.bool(False), # cmssw_11_1
            lip = cms.double(30.0),
            maxPhi = cms.double(3.2), # cmssw_11_1
            minPhi = cms.double(-3.2), # cmssw_11_1
            maxRapidity = cms.double(4.5), #previous 2.5
            minRapidity = cms.double(-4.5), #previous -2.5
            pdgId = cms.vint32(),
            ptMin = cms.double(0.9), # previous 0.05
            status = cms.int32(1),
            tip = cms.double(2.5) #previous 3.5
        ),
        GpSelectorForEfficiencyVsVTXR = cms.PSet(
            chargedOnly = cms.bool(True),
            invertRapidityCut = cms.bool(False), # cmssw_11_1
            lip = cms.double(30.0),
            maxPhi = cms.double(3.2), # cmssw_11_1
            minPhi = cms.double(-3.2), # cmssw_11_1
            maxRapidity = cms.double(4.5), #previous 2.5
            minRapidity = cms.double(-4.5), #previous -2.5
            pdgId = cms.vint32(),
            ptMin = cms.double(0.9),
            status = cms.int32(1),
            tip = cms.double(30.0) 
        ),
        GpSelectorForEfficiencyVsVTXZ = cms.PSet(
            chargedOnly = cms.bool(True),
            invertRapidityCut = cms.bool(False), # cmssw_11_1
            lip = cms.double(35.0),
            maxPhi = cms.double(3.2), # cmssw_11_1
            minPhi = cms.double(-3.2), # cmssw_11_1
            maxRapidity = cms.double(4.5), #previous 2.5
            minRapidity = cms.double(-4.5), #previous -2.5
            pdgId = cms.vint32(),
            ptMin = cms.double(0.9),
            status = cms.int32(1),
            tip = cms.double(2.5) #previous 3.5
        ),
        TpSelectorForEfficiencyVsEta = cms.PSet(
            chargedOnly = cms.bool(True),
            invertRapidityCut = cms.bool(False), # cmssw_11_1
            intimeOnly = cms.bool(False),
            lip = cms.double(30.0),
            maxPhi = cms.double(3.2),
            maxRapidity = cms.double(4.5),
            minHit = cms.int32(0),
            minPhi = cms.double(-3.2),
            minRapidity = cms.double(-4.5),
            pdgId = cms.vint32(),
            ptMax = cms.double(1e+100),
            ptMin = cms.double(0.9),
            signalOnly = cms.bool(False),
            stableOnly = cms.bool(False),
            tip = cms.double(2.5) #previous 3.5
        ),
        TpSelectorForEfficiencyVsPhi = cms.PSet(
            chargedOnly = cms.bool(True),
            invertRapidityCut = cms.bool(False), # cmssw_11_1
            intimeOnly = cms.bool(False),
            lip = cms.double(30.0),
            maxPhi = cms.double(3.2),
            maxRapidity = cms.double(4.5),
            minHit = cms.int32(0),
            minPhi = cms.double(-3.2),
            minRapidity = cms.double(-4.5),
            pdgId = cms.vint32(),
            ptMax = cms.double(1e+100),
            ptMin = cms.double(0.9),
            signalOnly = cms.bool(False),
            stableOnly = cms.bool(False),
            tip = cms.double(2.5) #previous 3.5
        ),
        TpSelectorForEfficiencyVsPt = cms.PSet(
            chargedOnly = cms.bool(True),
            invertRapidityCut = cms.bool(False), # cmssw_11_1
            intimeOnly = cms.bool(False),
            lip = cms.double(30.0),
            maxPhi = cms.double(3.2),
            maxRapidity = cms.double(4.5),
            minHit = cms.int32(0),
            minPhi = cms.double(-3.2),
            minRapidity = cms.double(-4.5),
            pdgId = cms.vint32(),
            ptMax = cms.double(1e+100),
            ptMin = cms.double(0.9), # previous 0.05
            signalOnly = cms.bool(False),
            stableOnly = cms.bool(False),
            tip = cms.double(2.5) #previous 3.5
        ),
        TpSelectorForEfficiencyVsVTXR = cms.PSet(
            chargedOnly = cms.bool(True),
            invertRapidityCut = cms.bool(False), # cmssw_11_1
            intimeOnly = cms.bool(False),
            lip = cms.double(30.0),
            maxPhi = cms.double(3.2),
            maxRapidity = cms.double(4.5),
            minHit = cms.int32(0),
            minPhi = cms.double(-3.2),
            minRapidity = cms.double(-4.5),
            pdgId = cms.vint32(),
            ptMax = cms.double(1e+100),
            ptMin = cms.double(0.9),
            signalOnly = cms.bool(False),
            stableOnly = cms.bool(False),
            tip = cms.double(60.0) 
        ),
        TpSelectorForEfficiencyVsVTXZ = cms.PSet(
            chargedOnly = cms.bool(True),
            invertRapidityCut = cms.bool(False), # cmssw_11_1
            intimeOnly = cms.bool(False),
            lip = cms.double(30.0),
            maxPhi = cms.double(3.2),
            maxRapidity = cms.double(4.5),
            minHit = cms.int32(0),
            minPhi = cms.double(-3.2),
            minRapidity = cms.double(-4.5),
            pdgId = cms.vint32(),
            ptMax = cms.double(1e+100),
            ptMin = cms.double(0.9),
            signalOnly = cms.bool(False),
            stableOnly = cms.bool(False),
            tip = cms.double(2.5) #previous 3.5
        ),
        cotThetaRes_nbin = cms.int32(300),
        cotThetaRes_rangeMax = cms.double(0.02),
        cotThetaRes_rangeMin = cms.double(-0.02),
        doMTDPlots = cms.untracked.bool(True), # cmssw_11_1
        dxyDzZoom = cms.double(25),
        dxyRes_nbin = cms.int32(500),
        dxyRes_rangeMax = cms.double(0.1),
        dxyRes_rangeMin = cms.double(-0.1),
        dzRes_nbin = cms.int32(150),
        dzRes_rangeMax = cms.double(0.05),
        dzRes_rangeMin = cms.double(-0.05),
        generalGpSelector = cms.PSet(
            chargedOnly = cms.bool(True),
            invertRapidityCut = cms.bool(False), # cmssw_11_1
            lip = cms.double(30.0),
            maxPhi = cms.double(3.2), # cmssw_11_1
            minPhi = cms.double(-3.2), # cmssw_11_1
            maxRapidity = cms.double(4.5), #previous 2.5
            minRapidity = cms.double(-4.5), #previous -2.5
            pdgId = cms.vint32(),
            ptMin = cms.double(0.9),
            status = cms.int32(1),
            tip = cms.double(2.5) #previous 3.5
        ),
        generalTpSelector = cms.PSet(
            chargedOnly = cms.bool(True),
            invertRapidityCut = cms.bool(False), # cmssw_11_1
            intimeOnly = cms.bool(False),
            lip = cms.double(30.0),
            maxPhi = cms.double(3.2),
            maxRapidity = cms.double(4.5),
            minHit = cms.int32(0),
            minPhi = cms.double(-3.2),
            minRapidity = cms.double(-4.5),
            pdgId = cms.vint32(),
            ptMax = cms.double(1e+100),
            ptMin = cms.double(0.9),
            signalOnly = cms.bool(False),
            stableOnly = cms.bool(False),
            tip = cms.double(2.5) #previous 3.5
        ),
        maxChi2 = cms.double(20),
        maxDeDx = cms.double(10.0),
        maxDxy = cms.double(25),
        maxDz = cms.double(30),
        maxDzpvCumulative = cms.double(0.6),
        maxDzpvsigCumulative = cms.double(10),
        maxEta = cms.double(4.5),
        maxHit = cms.double(80.5),
        maxLayers = cms.double(25.5),
        maxMVA = cms.double(1),
        maxPVz = cms.double(60),
        maxPhi = cms.double(3.1416),
        maxPt = cms.double(1000),
        maxPu = cms.double(259.5),
        maxTracks = cms.double(2000),
        maxVertcount = cms.double(160.5),
        maxVertpos = cms.double(100),
        maxZpos = cms.double(30),
        maxdr = cms.double(1),
        minChi2 = cms.double(0),
        minDeDx = cms.double(0.0),
        minDxy = cms.double(-25),
        minDz = cms.double(-30),
        minEta = cms.double(-4.5),
        minHit = cms.double(-0.5),
        minLayers = cms.double(-0.5),
        minMVA = cms.double(-1),
        minPVz = cms.double(-60),
        minPhi = cms.double(-3.1416),
        minPt = cms.double(0.1),
        minPu = cms.double(-0.5),
        minTracks = cms.double(0),
        minVertcount = cms.double(-0.5),
        minVertpos = cms.double(0.01),
        minZpos = cms.double(-30),
        mindr = cms.double(0.001),
        nintChi2 = cms.int32(40),
        nintDeDx = cms.int32(40),
        nintDxy = cms.int32(100),
        nintDz = cms.int32(60),
        nintDzpvCumulative = cms.int32(240),
        nintDzpvsigCumulative = cms.int32(200),
        nintEta = cms.int32(90),
        nintHit = cms.int32(81),
        nintLayers = cms.int32(26),
        nintMVA = cms.int32(100),
        nintPVz = cms.int32(120),
        nintPhi = cms.int32(36),
        nintPt = cms.int32(40),
        nintPu = cms.int32(130),
        nintTracks = cms.int32(200),
        nintVertcount = cms.int32(161),
        nintVertpos = cms.int32(40),
        nintZpos = cms.int32(60),
        nintdr = cms.int32(100),
        phiRes_nbin = cms.int32(300),
        phiRes_rangeMax = cms.double(0.01),
        phiRes_rangeMin = cms.double(-0.01),
        ptRes_nbin = cms.int32(100),
        ptRes_rangeMax = cms.double(0.1),
        ptRes_rangeMin = cms.double(-0.1),
        seedingLayerSets = cms.vstring(
            'BPix1+BPix2+BPix3+BPix4', 
            'BPix1+BPix2+BPix3+FPix1_pos', 
            'BPix1+BPix2+BPix3+FPix1_neg', 
            'BPix1+BPix2+FPix1_pos+FPix2_pos', 
            'BPix1+BPix2+FPix1_neg+FPix2_neg', 
            'BPix1+FPix1_pos+FPix2_pos+FPix3_pos', 
            'BPix1+FPix1_neg+FPix2_neg+FPix3_neg', 
            'FPix1_pos+FPix2_pos+FPix3_pos+FPix4_pos', 
            'FPix1_neg+FPix2_neg+FPix3_neg+FPix4_neg', 
            'FPix2_pos+FPix3_pos+FPix4_pos+FPix5_pos', 
            'FPix2_neg+FPix3_neg+FPix4_neg+FPix5_neg', 
            'FPix3_pos+FPix4_pos+FPix5_pos+FPix6_pos', 
            'FPix3_neg+FPix4_neg+FPix5_neg+FPix6_neg', 
            'FPix4_pos+FPix5_pos+FPix6_pos+FPix7_pos', 
            'FPix4_neg+FPix5_neg+FPix6_neg+FPix7_neg', 
            'FPix5_pos+FPix6_pos+FPix7_pos+FPix8_pos', 
            'FPix5_neg+FPix6_neg+FPix7_neg+FPix8_neg', 
            'BPix1+BPix2+BPix3', 
            'BPix2+BPix3+BPix4', 
            'BPix1+BPix3+BPix4', 
            'BPix1+BPix2+BPix4', 
            'BPix2+BPix3+FPix1_pos', 
            'BPix2+BPix3+FPix1_neg', 
            'BPix1+BPix2+FPix1_pos', 
            'BPix1+BPix2+FPix1_neg', 
            'BPix2+FPix1_pos+FPix2_pos', 
            'BPix2+FPix1_neg+FPix2_neg', 
            'BPix1+FPix1_pos+FPix2_pos', 
            'BPix1+FPix1_neg+FPix2_neg', 
            'FPix1_pos+FPix2_pos+FPix3_pos', 
            'FPix1_neg+FPix2_neg+FPix3_neg', 
            'BPix1+FPix2_pos+FPix3_pos', 
            'BPix1+FPix2_neg+FPix3_neg', 
            'FPix2_pos+FPix3_pos+FPix4_pos', 
            'FPix2_neg+FPix3_neg+FPix4_neg', 
            'FPix3_pos+FPix4_pos+FPix5_pos', 
            'FPix3_neg+FPix4_neg+FPix5_neg', 
            'FPix4_pos+FPix5_pos+FPix6_pos', 
            'FPix4_neg+FPix5_neg+FPix6_neg', 
            'FPix5_pos+FPix6_pos+FPix7_pos', 
            'FPix5_neg+FPix6_neg+FPix7_neg', 
            'FPix6_pos+FPix7_pos+FPix8_pos', 
            'FPix6_neg+FPix7_neg+FPix8_neg', 
            'BPix1+BPix2', 
            'BPix1+BPix3', 
            'BPix2+BPix3', 
            'BPix1+FPix1_pos', 
            'BPix1+FPix1_neg', 
            'BPix2+FPix1_pos', 
            'BPix2+FPix1_neg'
        ),
        useFabsEta = cms.bool(False),
        useInvPt = cms.bool(False),
        useLogPt = cms.untracked.bool(True),
        useLogVertpos = cms.untracked.bool(True)
    ),
    ignoremissingtrackcollection = cms.untracked.bool(False),
    intimeOnlyTP = cms.bool(True),
    invertRapidityCutTP = cms.bool(False), # cmssw_11_1
    label = cms.VInputTag(
        "hltPhase2GeneralTracks", "hltPhase2CutsRecoTracksHp", "hltPhase2CutsRecoTracksInitialStep", "hltPhase2CutsRecoTracksHighPtTripletStep", 
        "hltPhase2CutsRecoTracksInitialStepHp", "hltPhase2CutsRecoTracksHighPtTripletStepHp", 
        "hltPhase2CutsRecoTracksInitialStepByOriginalAlgo", "hltPhase2CutsRecoTracksHighPtTripletStepByOriginalAlgo",  "hltPhase2CutsRecoTracksInitialStepByOriginalAlgoHp", "hltPhase2CutsRecoTracksHighPtTripletStepByOriginalAlgoHp"
    ),
    label_pileupinfo = cms.InputTag("addPileupInfo"),
    label_tp_effic = cms.InputTag("mix","MergedTrackTruth"),
    label_tp_effic_refvector = cms.bool(False),
    label_tp_fake = cms.InputTag("mix","MergedTrackTruth"),
    label_tp_fake_refvector = cms.bool(False),
    label_tp_nlayers = cms.InputTag("trackingParticleNumberOfLayersProducer","trackerLayers"),
    label_tp_npixellayers = cms.InputTag("trackingParticleNumberOfLayersProducer","pixelLayers"),
    label_tp_nstripstereolayers = cms.InputTag("trackingParticleNumberOfLayersProducer","stripStereoLayers"),
    label_tv = cms.InputTag("mix","MergedTrackTruth"),
    label_vertex = cms.untracked.InputTag("hltPhase2OfflinePrimaryVertices"),
    lipTP = cms.double(30.0),
    maxRapidityTP = cms.double(4.5),
    minHitTP = cms.int32(0),
    minRapidityTP = cms.double(-4.5),
    mvaLabels = cms.untracked.PSet(

    ),
    parametersDefiner = cms.string('LhcParametersDefinerForTP'),
    pdgIdTP = cms.vint32(),
    ptMaxTP = cms.double(1e+100),
    ptMinTP = cms.double(0.9), # previous 0.005
    signalOnlyTP = cms.bool(False),
    sim = cms.VInputTag(
        cms.InputTag("g4SimHits","TrackerHitsPixelBarrelLowTof"), cms.InputTag("g4SimHits","TrackerHitsPixelBarrelHighTof"), cms.InputTag("g4SimHits","TrackerHitsPixelEndcapLowTof"), cms.InputTag("g4SimHits","TrackerHitsPixelEndcapHighTof"), cms.InputTag("g4SimHits","TrackerHitsTIBLowTof"), 
        cms.InputTag("g4SimHits","TrackerHitsTIBHighTof"), cms.InputTag("g4SimHits","TrackerHitsTIDLowTof"), cms.InputTag("g4SimHits","TrackerHitsTIDHighTof"), cms.InputTag("g4SimHits","TrackerHitsTOBLowTof"), cms.InputTag("g4SimHits","TrackerHitsTOBHighTof"), 
        cms.InputTag("g4SimHits","TrackerHitsTECLowTof"), cms.InputTag("g4SimHits","TrackerHitsTECHighTof")
    ),
    simHitTpMapTag = cms.InputTag("simHitTPAssocProducer"),
    simPVMaxZ = cms.untracked.double(-1),
    stableOnlyTP = cms.bool(False),
    tipTP = cms.double(60.0),
    trackCollectionForDrCalculation = cms.InputTag("hltPhase2GeneralTracks"),
    useGsf = cms.bool(False),
    useLogPt = cms.untracked.bool(True),
    vertexAssociator = cms.untracked.InputTag("hltPhase2VertexAssociatorByPositionAndTracks")
)

hltPhase2TrackValidatorBHadronTrackingOnly = cms.EDProducer("MultiTrackValidator", #cmssw_11_1 previous cms.EDAnalyzer
    cores = cms.InputTag("highPtJetsForTrk"), #cmssw_10_6 #cmssw_11_1
    UseAssociators = cms.bool(False),
    associators = cms.untracked.VInputTag("hltPhase2TrackingParticleRecoTrackAsssociation"),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    calculateDrSingleCollection = cms.untracked.bool(True),
    chargedOnlyTP = cms.bool(True),
    dEdx1Tag = cms.InputTag("dedxHarmonic2"),
    dEdx2Tag = cms.InputTag("dedxTruncated40"),
    dirName = cms.string('Tracking/TrackBHadron/'),
    doMVAPlots = cms.untracked.bool(False),
    doPVAssociationPlots = cms.untracked.bool(True),
    doPlotsOnlyForTruePV = cms.untracked.bool(False),
    doRecoTrackPlots = cms.untracked.bool(False),
    doResolutionPlotsForLabels = cms.VInputTag("hltPhase2GeneralTracks", "hltPhase2CutsRecoTracksHp", "hltPhase2GeneralTracksPt09", "hltPhase2CutsRecoTracksBtvLike"),
    doSeedPlots = cms.untracked.bool(False),
    doSimPlots = cms.untracked.bool(True),
    doSimTrackPlots = cms.untracked.bool(True),
    doSummaryPlots = cms.untracked.bool(True),
    dodEdxPlots = cms.untracked.bool(False),
    histoProducerAlgoBlock = cms.PSet(
	mindrj = cms.double(0.001),
        maxdrj = cms.double(0.1),
        nintdrj = cms.int32(100),
        
        GpSelectorForEfficiencyVsEta = cms.PSet(
            chargedOnly = cms.bool(True),
            invertRapidityCut = cms.bool(False), # cmssw_11_1
            lip = cms.double(30.0),
            maxPhi = cms.double(3.2), # cmssw_11_1
            minPhi = cms.double(-3.2), # cmssw_11_1
            maxRapidity = cms.double(4.5), #previous 2.5 
            minRapidity = cms.double(-4.5), #previous -2.5
            pdgId = cms.vint32(),
            ptMin = cms.double(0.9),
            status = cms.int32(1),
            tip = cms.double(2.5) #previous 3.5
        ),
        GpSelectorForEfficiencyVsPhi = cms.PSet(
            chargedOnly = cms.bool(True),
            invertRapidityCut = cms.bool(False), # cmssw_11_1
            lip = cms.double(30.0),
            maxPhi = cms.double(3.2), # cmssw_11_1
            minPhi = cms.double(-3.2), # cmssw_11_1
            maxRapidity = cms.double(4.5), #previous 2.5
            minRapidity = cms.double(-4.5), #previous -2.5
            pdgId = cms.vint32(),
            ptMin = cms.double(0.9),
            status = cms.int32(1),
            tip = cms.double(2.5) #previous 3.5
        ),
        GpSelectorForEfficiencyVsPt = cms.PSet(
            chargedOnly = cms.bool(True),
            invertRapidityCut = cms.bool(False), # cmssw_11_1
            lip = cms.double(30.0),
            maxPhi = cms.double(3.2), # cmssw_11_1
            minPhi = cms.double(-3.2), # cmssw_11_1
            maxRapidity = cms.double(4.5), #previous 2.5
            minRapidity = cms.double(-4.5), #previous -2.5
            pdgId = cms.vint32(),
            ptMin = cms.double(0.9), # previous 0.05
            status = cms.int32(1),
            tip = cms.double(2.5) #previous 3.5
        ),
        GpSelectorForEfficiencyVsVTXR = cms.PSet(
            chargedOnly = cms.bool(True),
            invertRapidityCut = cms.bool(False), # cmssw_11_1
            lip = cms.double(30.0),
            maxPhi = cms.double(3.2), # cmssw_11_1
            minPhi = cms.double(-3.2), # cmssw_11_1
            maxRapidity = cms.double(4.5), #previous 2.5
            minRapidity = cms.double(-4.5), #previous -2.5
            pdgId = cms.vint32(),
            ptMin = cms.double(0.9),
            status = cms.int32(1),
            tip = cms.double(30.0) 
        ),
        GpSelectorForEfficiencyVsVTXZ = cms.PSet(
            chargedOnly = cms.bool(True),
            invertRapidityCut = cms.bool(False), # cmssw_11_1
            lip = cms.double(35.0),
            maxPhi = cms.double(3.2), # cmssw_11_1
            minPhi = cms.double(-3.2), # cmssw_11_1
            maxRapidity = cms.double(4.5), #previous 2.5
            minRapidity = cms.double(-4.5), #previous -2.5
            pdgId = cms.vint32(),
            ptMin = cms.double(0.9),
            status = cms.int32(1),
            tip = cms.double(2.5) #previous 3.5
        ),
        TpSelectorForEfficiencyVsEta = cms.PSet(
            chargedOnly = cms.bool(True),
            invertRapidityCut = cms.bool(False), # cmssw_11_1
            intimeOnly = cms.bool(False),
            lip = cms.double(30.0),
            maxPhi = cms.double(3.2),
            maxRapidity = cms.double(4.5),
            minHit = cms.int32(0),
            minPhi = cms.double(-3.2),
            minRapidity = cms.double(-4.5),
            pdgId = cms.vint32(),
            ptMax = cms.double(1e+100),
            ptMin = cms.double(0.9),
            signalOnly = cms.bool(True),
            stableOnly = cms.bool(False),
            tip = cms.double(2.5) #previous 3.5
        ),
        TpSelectorForEfficiencyVsPhi = cms.PSet(
            chargedOnly = cms.bool(True),
            invertRapidityCut = cms.bool(False), # cmssw_11_1
            intimeOnly = cms.bool(False),
            lip = cms.double(30.0),
            maxPhi = cms.double(3.2),
            maxRapidity = cms.double(4.5),
            minHit = cms.int32(0),
            minPhi = cms.double(-3.2),
            minRapidity = cms.double(-4.5),
            pdgId = cms.vint32(),
            ptMax = cms.double(1e+100),
            ptMin = cms.double(0.9),
            signalOnly = cms.bool(True),
            stableOnly = cms.bool(False),
            tip = cms.double(2.5) #previous 3.5
        ),
        TpSelectorForEfficiencyVsPt = cms.PSet(
            chargedOnly = cms.bool(True),
            invertRapidityCut = cms.bool(False), # cmssw_11_1
            intimeOnly = cms.bool(False),
            lip = cms.double(30.0),
            maxPhi = cms.double(3.2),
            maxRapidity = cms.double(4.5),
            minHit = cms.int32(0),
            minPhi = cms.double(-3.2),
            minRapidity = cms.double(-4.5),
            pdgId = cms.vint32(),
            ptMax = cms.double(1e+100),
            ptMin = cms.double(0.9), # previous 0.05
            signalOnly = cms.bool(True),
            stableOnly = cms.bool(False),
            tip = cms.double(2.5) #previous 3.5
        ),
        TpSelectorForEfficiencyVsVTXR = cms.PSet(
            chargedOnly = cms.bool(True),
            invertRapidityCut = cms.bool(False), # cmssw_11_1
            intimeOnly = cms.bool(False),
            lip = cms.double(30.0),
            maxPhi = cms.double(3.2),
            maxRapidity = cms.double(4.5),
            minHit = cms.int32(0),
            minPhi = cms.double(-3.2),
            minRapidity = cms.double(-4.5),
            pdgId = cms.vint32(),
            ptMax = cms.double(1e+100),
            ptMin = cms.double(0.9),
            signalOnly = cms.bool(True),
            stableOnly = cms.bool(False),
            tip = cms.double(60.0) 
        ),
        TpSelectorForEfficiencyVsVTXZ = cms.PSet(
            chargedOnly = cms.bool(True),
            invertRapidityCut = cms.bool(False), # cmssw_11_1
            intimeOnly = cms.bool(False),
            lip = cms.double(30.0),
            maxPhi = cms.double(3.2),
            maxRapidity = cms.double(4.5),
            minHit = cms.int32(0),
            minPhi = cms.double(-3.2),
            minRapidity = cms.double(-4.5),
            pdgId = cms.vint32(),
            ptMax = cms.double(1e+100),
            ptMin = cms.double(0.9),
            signalOnly = cms.bool(True),
            stableOnly = cms.bool(False),
            tip = cms.double(2.5) #previous 3.5
        ),
        cotThetaRes_nbin = cms.int32(300),
        cotThetaRes_rangeMax = cms.double(0.02),
        cotThetaRes_rangeMin = cms.double(-0.02),
        doMTDPlots = cms.untracked.bool(True), # cmssw_11_1
        dxyDzZoom = cms.double(25),
        dxyRes_nbin = cms.int32(500),
        dxyRes_rangeMax = cms.double(0.1),
        dxyRes_rangeMin = cms.double(-0.1),
        dzRes_nbin = cms.int32(150),
        dzRes_rangeMax = cms.double(0.05),
        dzRes_rangeMin = cms.double(-0.05),
        generalGpSelector = cms.PSet(
            chargedOnly = cms.bool(True),
            invertRapidityCut = cms.bool(False), # cmssw_11_1
            lip = cms.double(30.0),
            maxPhi = cms.double(3.2), # cmssw_11_1
            minPhi = cms.double(-3.2), # cmssw_11_1
            maxRapidity = cms.double(4.5), #previous 2.5
            minRapidity = cms.double(-4.5), #previous -2.5
            pdgId = cms.vint32(),
            ptMin = cms.double(0.9),
            status = cms.int32(1),
            tip = cms.double(2.5) #previous 3.5
        ),
        generalTpSelector = cms.PSet(
            chargedOnly = cms.bool(True),
            invertRapidityCut = cms.bool(False), # cmssw_11_1
            intimeOnly = cms.bool(False),
            lip = cms.double(30.0),
            maxPhi = cms.double(3.2),
            maxRapidity = cms.double(4.5),
            minHit = cms.int32(0),
            minPhi = cms.double(-3.2),
            minRapidity = cms.double(-4.5),
            pdgId = cms.vint32(),
            ptMax = cms.double(1e+100),
            ptMin = cms.double(0.9),
            signalOnly = cms.bool(True),
            stableOnly = cms.bool(False),
            tip = cms.double(2.5) #previous 3.5
        ),
        maxChi2 = cms.double(20),
        maxDeDx = cms.double(10.0),
        maxDxy = cms.double(25),
        maxDz = cms.double(30),
        maxDzpvCumulative = cms.double(0.6),
        maxDzpvsigCumulative = cms.double(10),
        maxEta = cms.double(4.5),
        maxHit = cms.double(80.5),
        maxLayers = cms.double(25.5),
        maxMVA = cms.double(1),
        maxPVz = cms.double(60),
        maxPhi = cms.double(3.1416),
        maxPt = cms.double(1000),
        maxPu = cms.double(259.5),
        maxTracks = cms.double(2000),
        maxVertcount = cms.double(160.5),
        maxVertpos = cms.double(100),
        maxZpos = cms.double(30),
        maxdr = cms.double(1),
        minChi2 = cms.double(0),
        minDeDx = cms.double(0.0),
        minDxy = cms.double(-25),
        minDz = cms.double(-30),
        minEta = cms.double(-4.5),
        minHit = cms.double(-0.5),
        minLayers = cms.double(-0.5),
        minMVA = cms.double(-1),
        minPVz = cms.double(-60),
        minPhi = cms.double(-3.1416),
        minPt = cms.double(0.1),
        minPu = cms.double(-0.5),
        minTracks = cms.double(0),
        minVertcount = cms.double(-0.5),
        minVertpos = cms.double(0.01),
        minZpos = cms.double(-30),
        mindr = cms.double(0.001),
        nintChi2 = cms.int32(40),
        nintDeDx = cms.int32(40),
        nintDxy = cms.int32(100),
        nintDz = cms.int32(60),
        nintDzpvCumulative = cms.int32(240),
        nintDzpvsigCumulative = cms.int32(200),
        nintEta = cms.int32(90),
        nintHit = cms.int32(81),
        nintLayers = cms.int32(26),
        nintMVA = cms.int32(100),
        nintPVz = cms.int32(120),
        nintPhi = cms.int32(36),
        nintPt = cms.int32(40),
        nintPu = cms.int32(130),
        nintTracks = cms.int32(200),
        nintVertcount = cms.int32(161),
        nintVertpos = cms.int32(40),
        nintZpos = cms.int32(60),
        nintdr = cms.int32(100),
        phiRes_nbin = cms.int32(300),
        phiRes_rangeMax = cms.double(0.01),
        phiRes_rangeMin = cms.double(-0.01),
        ptRes_nbin = cms.int32(100),
        ptRes_rangeMax = cms.double(0.1),
        ptRes_rangeMin = cms.double(-0.1),
        seedingLayerSets = cms.vstring(
            'BPix1+BPix2+BPix3+BPix4', 
            'BPix1+BPix2+BPix3+FPix1_pos', 
            'BPix1+BPix2+BPix3+FPix1_neg', 
            'BPix1+BPix2+FPix1_pos+FPix2_pos', 
            'BPix1+BPix2+FPix1_neg+FPix2_neg', 
            'BPix1+FPix1_pos+FPix2_pos+FPix3_pos', 
            'BPix1+FPix1_neg+FPix2_neg+FPix3_neg', 
            'FPix1_pos+FPix2_pos+FPix3_pos+FPix4_pos', 
            'FPix1_neg+FPix2_neg+FPix3_neg+FPix4_neg', 
            'FPix2_pos+FPix3_pos+FPix4_pos+FPix5_pos', 
            'FPix2_neg+FPix3_neg+FPix4_neg+FPix5_neg', 
            'FPix3_pos+FPix4_pos+FPix5_pos+FPix6_pos', 
            'FPix3_neg+FPix4_neg+FPix5_neg+FPix6_neg', 
            'FPix4_pos+FPix5_pos+FPix6_pos+FPix7_pos', 
            'FPix4_neg+FPix5_neg+FPix6_neg+FPix7_neg', 
            'FPix5_pos+FPix6_pos+FPix7_pos+FPix8_pos', 
            'FPix5_neg+FPix6_neg+FPix7_neg+FPix8_neg', 
            'BPix1+BPix2+BPix3', 
            'BPix2+BPix3+BPix4', 
            'BPix1+BPix3+BPix4', 
            'BPix1+BPix2+BPix4', 
            'BPix2+BPix3+FPix1_pos', 
            'BPix2+BPix3+FPix1_neg', 
            'BPix1+BPix2+FPix1_pos', 
            'BPix1+BPix2+FPix1_neg', 
            'BPix2+FPix1_pos+FPix2_pos', 
            'BPix2+FPix1_neg+FPix2_neg', 
            'BPix1+FPix1_pos+FPix2_pos', 
            'BPix1+FPix1_neg+FPix2_neg', 
            'FPix1_pos+FPix2_pos+FPix3_pos', 
            'FPix1_neg+FPix2_neg+FPix3_neg', 
            'BPix1+FPix2_pos+FPix3_pos', 
            'BPix1+FPix2_neg+FPix3_neg', 
            'FPix2_pos+FPix3_pos+FPix4_pos', 
            'FPix2_neg+FPix3_neg+FPix4_neg', 
            'FPix3_pos+FPix4_pos+FPix5_pos', 
            'FPix3_neg+FPix4_neg+FPix5_neg', 
            'FPix4_pos+FPix5_pos+FPix6_pos', 
            'FPix4_neg+FPix5_neg+FPix6_neg', 
            'FPix5_pos+FPix6_pos+FPix7_pos', 
            'FPix5_neg+FPix6_neg+FPix7_neg', 
            'FPix6_pos+FPix7_pos+FPix8_pos', 
            'FPix6_neg+FPix7_neg+FPix8_neg', 
            'BPix1+BPix2', 
            'BPix1+BPix3', 
            'BPix2+BPix3', 
            'BPix1+FPix1_pos', 
            'BPix1+FPix1_neg', 
            'BPix2+FPix1_pos', 
            'BPix2+FPix1_neg'
        ),
        useFabsEta = cms.bool(False),
        useInvPt = cms.bool(False),
        useLogPt = cms.untracked.bool(True),
        useLogVertpos = cms.untracked.bool(True)
    ),
    ignoremissingtrackcollection = cms.untracked.bool(False),
    intimeOnlyTP = cms.bool(True),
    invertRapidityCutTP = cms.bool(False), # cmssw_11_1
    label = cms.VInputTag(
        "hltPhase2GeneralTracks", "hltPhase2CutsRecoTracksHp", "hltPhase2CutsRecoTracksInitialStep", "hltPhase2CutsRecoTracksHighPtTripletStep", 
        "hltPhase2CutsRecoTracksInitialStepHp", "hltPhase2CutsRecoTracksHighPtTripletStepHp",
        "hltPhase2CutsRecoTracksInitialStepByOriginalAlgo", "hltPhase2CutsRecoTracksHighPtTripletStepByOriginalAlgo",  "hltPhase2CutsRecoTracksInitialStepByOriginalAlgoHp", "hltPhase2CutsRecoTracksHighPtTripletStepByOriginalAlgoHp", 
        "hltPhase2CutsRecoTracksBtvLike", "hltPhase2CutsRecoTracksInitialStepByAlgoMask", "hltPhase2CutsRecoTracksHighPtTripletStepByAlgoMask", 
        "hltPhase2CutsRecoTracksInitialStepByAlgoMaskHp", "hltPhase2CutsRecoTracksHighPtTripletStepByAlgoMaskHp"
    ),
    label_pileupinfo = cms.InputTag("addPileupInfo"),
    label_tp_effic = cms.InputTag("trackingParticlesBHadron"),
    label_tp_effic_refvector = cms.bool(True),
    label_tp_fake = cms.InputTag("mix","MergedTrackTruth"),
    label_tp_fake_refvector = cms.bool(False),
    label_tp_nlayers = cms.InputTag("trackingParticleNumberOfLayersProducer","trackerLayers"),
    label_tp_npixellayers = cms.InputTag("trackingParticleNumberOfLayersProducer","pixelLayers"),
    label_tp_nstripstereolayers = cms.InputTag("trackingParticleNumberOfLayersProducer","stripStereoLayers"),
    label_tv = cms.InputTag("mix","MergedTrackTruth"),
    label_vertex = cms.untracked.InputTag("hltPhase2OfflinePrimaryVertices"),
    lipTP = cms.double(30.0),
    maxRapidityTP = cms.double(4.5),
    minHitTP = cms.int32(0),
    minRapidityTP = cms.double(-4.5),
    mvaLabels = cms.untracked.PSet(

    ),
    parametersDefiner = cms.string('LhcParametersDefinerForTP'),
    pdgIdTP = cms.vint32(),
    ptMaxTP = cms.double(1e+100),
    ptMinTP = cms.double(0.9), # previous 0.005
    signalOnlyTP = cms.bool(False),
    sim = cms.VInputTag(
        cms.InputTag("g4SimHits","TrackerHitsPixelBarrelLowTof"), cms.InputTag("g4SimHits","TrackerHitsPixelBarrelHighTof"), cms.InputTag("g4SimHits","TrackerHitsPixelEndcapLowTof"), cms.InputTag("g4SimHits","TrackerHitsPixelEndcapHighTof"), cms.InputTag("g4SimHits","TrackerHitsTIBLowTof"), 
        cms.InputTag("g4SimHits","TrackerHitsTIBHighTof"), cms.InputTag("g4SimHits","TrackerHitsTIDLowTof"), cms.InputTag("g4SimHits","TrackerHitsTIDHighTof"), cms.InputTag("g4SimHits","TrackerHitsTOBLowTof"), cms.InputTag("g4SimHits","TrackerHitsTOBHighTof"), 
        cms.InputTag("g4SimHits","TrackerHitsTECLowTof"), cms.InputTag("g4SimHits","TrackerHitsTECHighTof")
    ),
    simHitTpMapTag = cms.InputTag("simHitTPAssocProducer"),
    simPVMaxZ = cms.untracked.double(-1),
    stableOnlyTP = cms.bool(False),
    tipTP = cms.double(60.0), 
    trackCollectionForDrCalculation = cms.InputTag("hltPhase2GeneralTracks"),
    useGsf = cms.bool(False),
    useLogPt = cms.untracked.bool(True),
    vertexAssociator = cms.untracked.InputTag("hltPhase2VertexAssociatorByPositionAndTracks")
)


hltPhase2TrackValidatorSeedingTrackingOnly = cms.EDProducer("MultiTrackValidator", #cmssw_11_1 previous cms.EDAnalyzer
    cores = cms.InputTag("highPtJetsForTrk"), #cmssw_10_6 #cmssw_11_1
    UseAssociators = cms.bool(True),
    associators = cms.untracked.VInputTag("quickTrackAssociatorByHits"),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    calculateDrSingleCollection = cms.untracked.bool(True),
    chargedOnlyTP = cms.bool(True),
    dEdx1Tag = cms.InputTag("dedxHarmonic2"),
    dEdx2Tag = cms.InputTag("dedxTruncated40"),
    dirName = cms.string('Tracking/TrackSeeding/'),
    doMVAPlots = cms.untracked.bool(False),
    doPVAssociationPlots = cms.untracked.bool(False),
    doPlotsOnlyForTruePV = cms.untracked.bool(False),
    doRecoTrackPlots = cms.untracked.bool(True),
    doResolutionPlotsForLabels = cms.VInputTag("disabled"),
    doSeedPlots = cms.untracked.bool(True),
    doSimPlots = cms.untracked.bool(False),
    doSimTrackPlots = cms.untracked.bool(True),
    doSummaryPlots = cms.untracked.bool(True),
    dodEdxPlots = cms.untracked.bool(False),
    histoProducerAlgoBlock = cms.PSet(
	mindrj = cms.double(0.001),
        maxdrj = cms.double(0.1),
        nintdrj = cms.int32(100),
        
        GpSelectorForEfficiencyVsEta = cms.PSet(
            chargedOnly = cms.bool(True),
            invertRapidityCut = cms.bool(False), # cmssw_11_1
            lip = cms.double(30.0),
            maxPhi = cms.double(3.2), # cmssw_11_1
            minPhi = cms.double(-3.2), # cmssw_11_1
            maxRapidity = cms.double(4.5), #previous 2.5 
            minRapidity = cms.double(-4.5), #previous -2.5
            pdgId = cms.vint32(),
            ptMin = cms.double(0.9),
            status = cms.int32(1),
            tip = cms.double(2.5) #previous 3.5
        ),
        GpSelectorForEfficiencyVsPhi = cms.PSet(
            chargedOnly = cms.bool(True),
            invertRapidityCut = cms.bool(False), # cmssw_11_1
            lip = cms.double(30.0),
            maxPhi = cms.double(3.2), # cmssw_11_1
            minPhi = cms.double(-3.2), # cmssw_11_1
            maxRapidity = cms.double(4.5), #previous 2.5
            minRapidity = cms.double(-4.5), #previous -2.5
            pdgId = cms.vint32(),
            ptMin = cms.double(0.9),
            status = cms.int32(1),
            tip = cms.double(2.5) #previous 3.5
        ),
        GpSelectorForEfficiencyVsPt = cms.PSet(
            chargedOnly = cms.bool(True),
            invertRapidityCut = cms.bool(False), # cmssw_11_1
            lip = cms.double(30.0),
            maxPhi = cms.double(3.2), # cmssw_11_1
            minPhi = cms.double(-3.2), # cmssw_11_1
            maxRapidity = cms.double(4.5), #previous 2.5
            minRapidity = cms.double(-4.5), #previous -2.5
            pdgId = cms.vint32(),
            ptMin = cms.double(0.9), # previous 0.05
            status = cms.int32(1),
            tip = cms.double(2.5) #previous 3.5
        ),
        GpSelectorForEfficiencyVsVTXR = cms.PSet(
            chargedOnly = cms.bool(True),
            invertRapidityCut = cms.bool(False), # cmssw_11_1
            lip = cms.double(30.0),
            maxPhi = cms.double(3.2), # cmssw_11_1
            minPhi = cms.double(-3.2), # cmssw_11_1
            maxRapidity = cms.double(4.5), #previous 2.5
            minRapidity = cms.double(-4.5), #previous -2.5
            pdgId = cms.vint32(),
            ptMin = cms.double(0.9),
            status = cms.int32(1),
            tip = cms.double(30.0) 
        ),
        GpSelectorForEfficiencyVsVTXZ = cms.PSet(
            chargedOnly = cms.bool(True),
            invertRapidityCut = cms.bool(False), # cmssw_11_1
            lip = cms.double(35.0),
            maxPhi = cms.double(3.2), # cmssw_11_1
            minPhi = cms.double(-3.2), # cmssw_11_1
            maxRapidity = cms.double(4.5), #previous 2.5
            minRapidity = cms.double(-4.5), #previous -2.5
            pdgId = cms.vint32(),
            ptMin = cms.double(0.9),
            status = cms.int32(1),
            tip = cms.double(2.5) #previous 3.5
        ),
        TpSelectorForEfficiencyVsEta = cms.PSet(
            chargedOnly = cms.bool(True),
            invertRapidityCut = cms.bool(False), # cmssw_11_1
            intimeOnly = cms.bool(False),
            lip = cms.double(30.0),
            maxPhi = cms.double(3.2),
            maxRapidity = cms.double(4.5),
            minHit = cms.int32(0),
            minPhi = cms.double(-3.2),
            minRapidity = cms.double(-4.5),
            pdgId = cms.vint32(),
            ptMax = cms.double(1e+100),
            ptMin = cms.double(0.9),
            signalOnly = cms.bool(True),
            stableOnly = cms.bool(False),
            tip = cms.double(2.5) #previous 3.5
        ),
        TpSelectorForEfficiencyVsPhi = cms.PSet(
            chargedOnly = cms.bool(True),
            invertRapidityCut = cms.bool(False), # cmssw_11_1
            intimeOnly = cms.bool(False),
            lip = cms.double(30.0),
            maxPhi = cms.double(3.2),
            maxRapidity = cms.double(4.5),
            minHit = cms.int32(0),
            minPhi = cms.double(-3.2),
            minRapidity = cms.double(-4.5),
            pdgId = cms.vint32(),
            ptMax = cms.double(1e+100),
            ptMin = cms.double(0.9),
            signalOnly = cms.bool(True),
            stableOnly = cms.bool(False),
            tip = cms.double(2.5) #previous 3.5
        ),
        TpSelectorForEfficiencyVsPt = cms.PSet(
            chargedOnly = cms.bool(True),
            invertRapidityCut = cms.bool(False), # cmssw_11_1
            intimeOnly = cms.bool(False),
            lip = cms.double(30.0),
            maxPhi = cms.double(3.2),
            maxRapidity = cms.double(4.5),
            minHit = cms.int32(0),
            minPhi = cms.double(-3.2),
            minRapidity = cms.double(-4.5),
            pdgId = cms.vint32(),
            ptMax = cms.double(1e+100),
            ptMin = cms.double(0.9), # previous 0.05
            signalOnly = cms.bool(True),
            stableOnly = cms.bool(False),
            tip = cms.double(2.5) #previous 3.5
        ),
        TpSelectorForEfficiencyVsVTXR = cms.PSet(
            chargedOnly = cms.bool(True),
            invertRapidityCut = cms.bool(False), # cmssw_11_1
            intimeOnly = cms.bool(False),
            lip = cms.double(30.0),
            maxPhi = cms.double(3.2),
            maxRapidity = cms.double(4.5),
            minHit = cms.int32(0),
            minPhi = cms.double(-3.2),
            minRapidity = cms.double(-4.5),
            pdgId = cms.vint32(),
            ptMax = cms.double(1e+100),
            ptMin = cms.double(0.9),
            signalOnly = cms.bool(True),
            stableOnly = cms.bool(False),
            tip = cms.double(60.0) 
        ),
        TpSelectorForEfficiencyVsVTXZ = cms.PSet(
            chargedOnly = cms.bool(True),
            invertRapidityCut = cms.bool(False), # cmssw_11_1
            intimeOnly = cms.bool(False),
            lip = cms.double(30.0),
            maxPhi = cms.double(3.2),
            maxRapidity = cms.double(4.5),
            minHit = cms.int32(0),
            minPhi = cms.double(-3.2),
            minRapidity = cms.double(-4.5),
            pdgId = cms.vint32(),
            ptMax = cms.double(1e+100),
            ptMin = cms.double(0.9),
            signalOnly = cms.bool(True),
            stableOnly = cms.bool(False),
            tip = cms.double(2.5) #previous 3.5
        ),
        cotThetaRes_nbin = cms.int32(300),
        cotThetaRes_rangeMax = cms.double(0.02),
        cotThetaRes_rangeMin = cms.double(-0.02),
        doMTDPlots = cms.untracked.bool(True), # cmssw_11_1
        dxyDzZoom = cms.double(25),
        dxyRes_nbin = cms.int32(500),
        dxyRes_rangeMax = cms.double(0.1),
        dxyRes_rangeMin = cms.double(-0.1),
        dzRes_nbin = cms.int32(150),
        dzRes_rangeMax = cms.double(0.05),
        dzRes_rangeMin = cms.double(-0.05),
        generalGpSelector = cms.PSet(
            chargedOnly = cms.bool(True),
            invertRapidityCut = cms.bool(False), # cmssw_11_1
            lip = cms.double(30.0),
            maxPhi = cms.double(3.2), # cmssw_11_1
            minPhi = cms.double(-3.2), # cmssw_11_1
            maxRapidity = cms.double(4.5), #previous 2.5
            minRapidity = cms.double(-4.5), #previous -2.5
            pdgId = cms.vint32(),
            ptMin = cms.double(0.9),
            status = cms.int32(1),
            tip = cms.double(2.5) #previous 3.5
        ),
        generalTpSelector = cms.PSet(
            chargedOnly = cms.bool(True),
            invertRapidityCut = cms.bool(False), # cmssw_11_1
            intimeOnly = cms.bool(False),
            lip = cms.double(30.0),
            maxPhi = cms.double(3.2),
            maxRapidity = cms.double(4.5),
            minHit = cms.int32(0),
            minPhi = cms.double(-3.2),
            minRapidity = cms.double(-4.5),
            pdgId = cms.vint32(),
            ptMax = cms.double(1e+100),
            ptMin = cms.double(0.9),
            signalOnly = cms.bool(True),
            stableOnly = cms.bool(False),
            tip = cms.double(2.5) #previous 3.5
        ),
        maxChi2 = cms.double(20),
        maxDeDx = cms.double(10.0),
        maxDxy = cms.double(25),
        maxDz = cms.double(30),
        maxDzpvCumulative = cms.double(0.6),
        maxDzpvsigCumulative = cms.double(10),
        maxEta = cms.double(4.5),
        maxHit = cms.double(80.5),
        maxLayers = cms.double(25.5),
        maxMVA = cms.double(1),
        maxPVz = cms.double(60),
        maxPhi = cms.double(3.1416),
        maxPt = cms.double(1000),
        maxPu = cms.double(259.5),
        maxTracks = cms.double(2000),
        maxVertcount = cms.double(160.5),
        maxVertpos = cms.double(100),
        maxZpos = cms.double(30),
        maxdr = cms.double(1),
        minChi2 = cms.double(0),
        minDeDx = cms.double(0.0),
        minDxy = cms.double(-25),
        minDz = cms.double(-30),
        minEta = cms.double(-4.5),
        minHit = cms.double(-0.5),
        minLayers = cms.double(-0.5),
        minMVA = cms.double(-1),
        minPVz = cms.double(-60),
        minPhi = cms.double(-3.1416),
        minPt = cms.double(0.1),
        minPu = cms.double(-0.5),
        minTracks = cms.double(0),
        minVertcount = cms.double(-0.5),
        minVertpos = cms.double(0.01),
        minZpos = cms.double(-30),
        mindr = cms.double(0.001),
        nintChi2 = cms.int32(40),
        nintDeDx = cms.int32(40),
        nintDxy = cms.int32(100),
        nintDz = cms.int32(60),
        nintDzpvCumulative = cms.int32(240),
        nintDzpvsigCumulative = cms.int32(200),
        nintEta = cms.int32(90),
        nintHit = cms.int32(81),
        nintLayers = cms.int32(26),
        nintMVA = cms.int32(100),
        nintPVz = cms.int32(120),
        nintPhi = cms.int32(36),
        nintPt = cms.int32(40),
        nintPu = cms.int32(130),
        nintTracks = cms.int32(200),
        nintVertcount = cms.int32(161),
        nintVertpos = cms.int32(40),
        nintZpos = cms.int32(60),
        nintdr = cms.int32(100),
        phiRes_nbin = cms.int32(300),
        phiRes_rangeMax = cms.double(0.01),
        phiRes_rangeMin = cms.double(-0.01),
        ptRes_nbin = cms.int32(100),
        ptRes_rangeMax = cms.double(0.1),
        ptRes_rangeMin = cms.double(-0.1),
        seedingLayerSets = cms.vstring(
            'BPix1+BPix2+BPix3+BPix4', 
            'BPix1+BPix2+BPix3+FPix1_pos', 
            'BPix1+BPix2+BPix3+FPix1_neg', 
            'BPix1+BPix2+FPix1_pos+FPix2_pos', 
            'BPix1+BPix2+FPix1_neg+FPix2_neg', 
            'BPix1+FPix1_pos+FPix2_pos+FPix3_pos', 
            'BPix1+FPix1_neg+FPix2_neg+FPix3_neg', 
            'FPix1_pos+FPix2_pos+FPix3_pos+FPix4_pos', 
            'FPix1_neg+FPix2_neg+FPix3_neg+FPix4_neg', 
            'FPix2_pos+FPix3_pos+FPix4_pos+FPix5_pos', 
            'FPix2_neg+FPix3_neg+FPix4_neg+FPix5_neg', 
            'FPix3_pos+FPix4_pos+FPix5_pos+FPix6_pos', 
            'FPix3_neg+FPix4_neg+FPix5_neg+FPix6_neg', 
            'FPix4_pos+FPix5_pos+FPix6_pos+FPix7_pos', 
            'FPix4_neg+FPix5_neg+FPix6_neg+FPix7_neg', 
            'FPix5_pos+FPix6_pos+FPix7_pos+FPix8_pos', 
            'FPix5_neg+FPix6_neg+FPix7_neg+FPix8_neg', 
            'BPix1+BPix2+BPix3', 
            'BPix2+BPix3+BPix4', 
            'BPix1+BPix3+BPix4', 
            'BPix1+BPix2+BPix4', 
            'BPix2+BPix3+FPix1_pos', 
            'BPix2+BPix3+FPix1_neg', 
            'BPix1+BPix2+FPix1_pos', 
            'BPix1+BPix2+FPix1_neg', 
            'BPix2+FPix1_pos+FPix2_pos', 
            'BPix2+FPix1_neg+FPix2_neg', 
            'BPix1+FPix1_pos+FPix2_pos', 
            'BPix1+FPix1_neg+FPix2_neg', 
            'FPix1_pos+FPix2_pos+FPix3_pos', 
            'FPix1_neg+FPix2_neg+FPix3_neg', 
            'BPix1+FPix2_pos+FPix3_pos', 
            'BPix1+FPix2_neg+FPix3_neg', 
            'FPix2_pos+FPix3_pos+FPix4_pos', 
            'FPix2_neg+FPix3_neg+FPix4_neg', 
            'FPix3_pos+FPix4_pos+FPix5_pos', 
            'FPix3_neg+FPix4_neg+FPix5_neg', 
            'FPix4_pos+FPix5_pos+FPix6_pos', 
            'FPix4_neg+FPix5_neg+FPix6_neg', 
            'FPix5_pos+FPix6_pos+FPix7_pos', 
            'FPix5_neg+FPix6_neg+FPix7_neg', 
            'FPix6_pos+FPix7_pos+FPix8_pos', 
            'FPix6_neg+FPix7_neg+FPix8_neg', 
            'BPix1+BPix2', 
            'BPix1+BPix3', 
            'BPix2+BPix3', 
            'BPix1+FPix1_pos', 
            'BPix1+FPix1_neg', 
            'BPix2+FPix1_pos', 
            'BPix2+FPix1_neg'
        ),
        useFabsEta = cms.bool(False),
        useInvPt = cms.bool(False),
        useLogPt = cms.untracked.bool(True),
        useLogVertpos = cms.untracked.bool(True)
    ),
    ignoremissingtrackcollection = cms.untracked.bool(False),
    intimeOnlyTP = cms.bool(True),
    invertRapidityCutTP = cms.bool(False), # cmssw_11_1
    label = cms.VInputTag(
        "hltPhase2SeedTracksinitialStepSeeds", "hltPhase2SeedTrackshighPtTripletStepSeeds" ### v2
    ),
    label_pileupinfo = cms.InputTag("addPileupInfo"),
    label_tp_effic = cms.InputTag("mix","MergedTrackTruth"),
    label_tp_effic_refvector = cms.bool(False),
    label_tp_fake = cms.InputTag("mix","MergedTrackTruth"),
    label_tp_fake_refvector = cms.bool(False),
    label_tp_nlayers = cms.InputTag("trackingParticleNumberOfLayersProducer","trackerLayers"),
    label_tp_npixellayers = cms.InputTag("trackingParticleNumberOfLayersProducer","pixelLayers"),
    label_tp_nstripstereolayers = cms.InputTag("trackingParticleNumberOfLayersProducer","stripStereoLayers"),
    label_tv = cms.InputTag("mix","MergedTrackTruth"),
    label_vertex = cms.untracked.InputTag("hltPhase2OfflinePrimaryVertices"),
    lipTP = cms.double(30.0),
    maxRapidityTP = cms.double(4.5),
    minHitTP = cms.int32(0),
    minRapidityTP = cms.double(-4.5),
    mvaLabels = cms.untracked.PSet(

    ),
    parametersDefiner = cms.string('LhcParametersDefinerForTP'),
    pdgIdTP = cms.vint32(),
    ptMaxTP = cms.double(1e+100),
    ptMinTP = cms.double(0.9), # previous 0.005
    signalOnlyTP = cms.bool(False),
    sim = cms.VInputTag(
        cms.InputTag("g4SimHits","TrackerHitsPixelBarrelLowTof"), cms.InputTag("g4SimHits","TrackerHitsPixelBarrelHighTof"), cms.InputTag("g4SimHits","TrackerHitsPixelEndcapLowTof"), cms.InputTag("g4SimHits","TrackerHitsPixelEndcapHighTof"), cms.InputTag("g4SimHits","TrackerHitsTIBLowTof"), 
        cms.InputTag("g4SimHits","TrackerHitsTIBHighTof"), cms.InputTag("g4SimHits","TrackerHitsTIDLowTof"), cms.InputTag("g4SimHits","TrackerHitsTIDHighTof"), cms.InputTag("g4SimHits","TrackerHitsTOBLowTof"), cms.InputTag("g4SimHits","TrackerHitsTOBHighTof"), 
        cms.InputTag("g4SimHits","TrackerHitsTECLowTof"), cms.InputTag("g4SimHits","TrackerHitsTECHighTof")
    ),
    simHitTpMapTag = cms.InputTag("simHitTPAssocProducer"),
    simPVMaxZ = cms.untracked.double(-1),
    stableOnlyTP = cms.bool(False),
    tipTP = cms.double(60.0), 
    trackCollectionForDrCalculation = cms.InputTag("hltPhase2GeneralTracks"),
    useGsf = cms.bool(False),
    useLogPt = cms.untracked.bool(True),
    vertexAssociator = cms.untracked.InputTag("hltPhase2VertexAssociatorByPositionAndTracks")
)

hltPhase2VertexAssociatorByPositionAndTracks = cms.EDProducer("VertexAssociatorByPositionAndTracksProducer",
    absT = cms.double(-1),
    absZ = cms.double(0.1),
    maxRecoT = cms.double(-1),
    maxRecoZ = cms.double(1000),
    sharedTrackFraction = cms.double(-1),
    sigmaT = cms.double(-1),
    sigmaZ = cms.double(3),
    trackAssociation = cms.InputTag("hltPhase2TrackingParticleRecoTrackAsssociation")
)


hltPhase2CutsRecoTracksBtvLike = cms.EDProducer("RecoTrackViewRefSelector",
    algorithm = cms.vstring(),
    algorithmMaskContains = cms.vstring(),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    invertRapidityCut = cms.bool(False), # cmssw_11_1
    lip = cms.double(17.0),
    maxChi2 = cms.double(5.0),
    maxPhi = cms.double(3.2),
    maxRapidity = cms.double(9),
    min3DLayer = cms.int32(0),
    minHit = cms.int32(0),
    minLayer = cms.int32(0),
    minPhi = cms.double(-3.2),
    minPixelHit = cms.int32(1),
    minRapidity = cms.double(-9), 
    originalAlgorithm = cms.vstring(),
    ptMin = cms.double(1.0),
    quality = cms.vstring(),
    src = cms.InputTag("hltPhase2GeneralTracks"),
    tip = cms.double(0.2), 
    usePV = cms.bool(True),
    vertexTag = cms.InputTag("hltPhase2OfflinePrimaryVertices")
)


hltPhase2CutsRecoTracksFromPVHighPtTripletStep = cms.EDProducer("RecoTrackViewRefSelector",
    algorithm = cms.vstring('highPtTripletStep'),
    algorithmMaskContains = cms.vstring(),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    invertRapidityCut = cms.bool(False), # cmssw_11_1
    lip = cms.double(300.0),
    maxChi2 = cms.double(10000.0),
    maxPhi = cms.double(3.2),
    maxRapidity = cms.double(4.5),
    min3DLayer = cms.int32(0),
    minHit = cms.int32(0),
    minLayer = cms.int32(3),
    minPhi = cms.double(-3.2),
    minPixelHit = cms.int32(0),
    minRapidity = cms.double(-4.5),
    originalAlgorithm = cms.vstring(),
    ptMin = cms.double(0.9), # previous 0.1
    quality = cms.vstring('loose'),
    src = cms.InputTag("hltPhase2GeneralTracksFromPV"),
    tip = cms.double(120),
    usePV = cms.bool(False),
    vertexTag = cms.InputTag("hltPhase2OfflinePrimaryVertices")
)


hltPhase2CutsRecoTracksFromPVHighPtTripletStepHp = cms.EDProducer("RecoTrackViewRefSelector",
    algorithm = cms.vstring('highPtTripletStep'),
    algorithmMaskContains = cms.vstring(),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    invertRapidityCut = cms.bool(False), # cmssw_11_1
    lip = cms.double(300.0),
    maxChi2 = cms.double(10000.0),
    maxPhi = cms.double(3.2),
    maxRapidity = cms.double(4.5),
    min3DLayer = cms.int32(0),
    minHit = cms.int32(0),
    minLayer = cms.int32(3),
    minPhi = cms.double(-3.2),
    minPixelHit = cms.int32(0),
    minRapidity = cms.double(-4.5),
    originalAlgorithm = cms.vstring(),
    ptMin = cms.double(0.9), # previous 0.1
    quality = cms.vstring('highPurity'),
    src = cms.InputTag("hltPhase2GeneralTracksFromPV"),
    tip = cms.double(120), 
    usePV = cms.bool(False),
    vertexTag = cms.InputTag("hltPhase2OfflinePrimaryVertices")
)

hltPhase2CutsRecoTracksFromPVHp = cms.EDProducer("RecoTrackViewRefSelector",
    algorithm = cms.vstring(),
    algorithmMaskContains = cms.vstring(),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    invertRapidityCut = cms.bool(False), # cmssw_11_1
    lip = cms.double(300.0),
    maxChi2 = cms.double(10000.0),
    maxPhi = cms.double(3.2),
    maxRapidity = cms.double(4.5),
    min3DLayer = cms.int32(0),
    minHit = cms.int32(0),
    minLayer = cms.int32(3),
    minPhi = cms.double(-3.2),
    minPixelHit = cms.int32(0),
    minRapidity = cms.double(-4.5),
    originalAlgorithm = cms.vstring(),
    ptMin = cms.double(0.9), # previous 0.1
    quality = cms.vstring('highPurity'),
    src = cms.InputTag("hltPhase2GeneralTracksFromPV"),
    tip = cms.double(120),
    usePV = cms.bool(False),
    vertexTag = cms.InputTag("hltPhase2OfflinePrimaryVertices")
)


hltPhase2CutsRecoTracksFromPVInitialStep = cms.EDProducer("RecoTrackViewRefSelector",
    algorithm = cms.vstring('initialStep'),
    algorithmMaskContains = cms.vstring(),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    invertRapidityCut = cms.bool(False), # cmssw_11_1
    lip = cms.double(300.0),
    maxChi2 = cms.double(10000.0),
    maxPhi = cms.double(3.2),
    maxRapidity = cms.double(4.5),
    min3DLayer = cms.int32(0),
    minHit = cms.int32(0),
    minLayer = cms.int32(3),
    minPhi = cms.double(-3.2),
    minPixelHit = cms.int32(0),
    minRapidity = cms.double(-4.5),
    originalAlgorithm = cms.vstring(),
    ptMin = cms.double(0.9), # previous 0.1
    quality = cms.vstring('loose'),
    src = cms.InputTag("hltPhase2GeneralTracksFromPV"),
    tip = cms.double(120), 
    usePV = cms.bool(False),
    vertexTag = cms.InputTag("hltPhase2OfflinePrimaryVertices")
)


hltPhase2CutsRecoTracksFromPVInitialStepHp = cms.EDProducer("RecoTrackViewRefSelector",
    algorithm = cms.vstring('initialStep'),
    algorithmMaskContains = cms.vstring(),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    invertRapidityCut = cms.bool(False), # cmssw_11_1
    lip = cms.double(300.0),
    maxChi2 = cms.double(10000.0),
    maxPhi = cms.double(3.2),
    maxRapidity = cms.double(4.5),
    min3DLayer = cms.int32(0),
    minHit = cms.int32(0),
    minLayer = cms.int32(3),
    minPhi = cms.double(-3.2),
    minPixelHit = cms.int32(0),
    minRapidity = cms.double(-4.5),
    originalAlgorithm = cms.vstring(),
    ptMin = cms.double(0.9), # previous 0.1
    quality = cms.vstring('highPurity'),
    src = cms.InputTag("hltPhase2GeneralTracksFromPV"),
    tip = cms.double(120), 
    usePV = cms.bool(False),
    vertexTag = cms.InputTag("hltPhase2OfflinePrimaryVertices")
)

hltPhase2CutsRecoTracksFromPVPt09HighPtTripletStep = cms.EDProducer("RecoTrackViewRefSelector",
    algorithm = cms.vstring('highPtTripletStep'),
    algorithmMaskContains = cms.vstring(),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    invertRapidityCut = cms.bool(False), # cmssw_11_1
    lip = cms.double(300.0),
    maxChi2 = cms.double(10000.0),
    maxPhi = cms.double(3.2),
    maxRapidity = cms.double(4.5),
    min3DLayer = cms.int32(0),
    minHit = cms.int32(0),
    minLayer = cms.int32(3),
    minPhi = cms.double(-3.2),
    minPixelHit = cms.int32(0),
    minRapidity = cms.double(-4.5),
    originalAlgorithm = cms.vstring(),
    ptMin = cms.double(0.9), # previous 0.1
    quality = cms.vstring('loose'),
    src = cms.InputTag("hltPhase2GeneralTracksFromPVPt09"),
    tip = cms.double(120.0), 
    usePV = cms.bool(False),
    vertexTag = cms.InputTag("hltPhase2OfflinePrimaryVertices")
)


hltPhase2CutsRecoTracksFromPVPt09HighPtTripletStepHp = cms.EDProducer("RecoTrackViewRefSelector",
    algorithm = cms.vstring('highPtTripletStep'),
    algorithmMaskContains = cms.vstring(),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    invertRapidityCut = cms.bool(False), # cmssw_11_1
    lip = cms.double(300.0),
    maxChi2 = cms.double(10000.0),
    maxPhi = cms.double(3.2),
    maxRapidity = cms.double(4.5),
    min3DLayer = cms.int32(0),
    minHit = cms.int32(0),
    minLayer = cms.int32(3),
    minPhi = cms.double(-3.2),
    minPixelHit = cms.int32(0),
    minRapidity = cms.double(-4.5),
    originalAlgorithm = cms.vstring(),
    ptMin = cms.double(0.9), # previous 0.1
    quality = cms.vstring('highPurity'),
    src = cms.InputTag("hltPhase2GeneralTracksFromPVPt09"),
    tip = cms.double(120), 
    usePV = cms.bool(False),
    vertexTag = cms.InputTag("hltPhase2OfflinePrimaryVertices")
)

hltPhase2CutsRecoTracksFromPVPt09Hp = cms.EDProducer("RecoTrackViewRefSelector",
    algorithm = cms.vstring(),
    algorithmMaskContains = cms.vstring(),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    invertRapidityCut = cms.bool(False), # cmssw_11_1
    lip = cms.double(300.0),
    maxChi2 = cms.double(10000.0),
    maxPhi = cms.double(3.2),
    maxRapidity = cms.double(4.5),
    min3DLayer = cms.int32(0),
    minHit = cms.int32(0),
    minLayer = cms.int32(3),
    minPhi = cms.double(-3.2),
    minPixelHit = cms.int32(0),
    minRapidity = cms.double(-4.5),
    originalAlgorithm = cms.vstring(),
    ptMin = cms.double(0.9), # previous 0.1
    quality = cms.vstring('highPurity'),
    src = cms.InputTag("hltPhase2GeneralTracksFromPVPt09"),
    tip = cms.double(120), 
    usePV = cms.bool(False),
    vertexTag = cms.InputTag("hltPhase2OfflinePrimaryVertices")
)

hltPhase2CutsRecoTracksFromPVPt09InitialStep = cms.EDProducer("RecoTrackViewRefSelector",
    algorithm = cms.vstring('initialStep'),
    algorithmMaskContains = cms.vstring(),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    invertRapidityCut = cms.bool(False), # cmssw_11_1
    lip = cms.double(300.0),
    maxChi2 = cms.double(10000.0),
    maxPhi = cms.double(3.2),
    maxRapidity = cms.double(4.5),
    min3DLayer = cms.int32(0),
    minHit = cms.int32(0),
    minLayer = cms.int32(3),
    minPhi = cms.double(-3.2),
    minPixelHit = cms.int32(0),
    minRapidity = cms.double(-4.5),
    originalAlgorithm = cms.vstring(),
    ptMin = cms.double(0.9), # previous 0.1
    quality = cms.vstring('loose'),
    src = cms.InputTag("hltPhase2GeneralTracksFromPVPt09"),
    tip = cms.double(120), 
    usePV = cms.bool(False),
    vertexTag = cms.InputTag("hltPhase2OfflinePrimaryVertices")
)


hltPhase2CutsRecoTracksFromPVPt09InitialStepHp = cms.EDProducer("RecoTrackViewRefSelector",
    algorithm = cms.vstring('initialStep'),
    algorithmMaskContains = cms.vstring(),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    invertRapidityCut = cms.bool(False), # cmssw_11_1
    lip = cms.double(300.0),
    maxChi2 = cms.double(10000.0),
    maxPhi = cms.double(3.2),
    maxRapidity = cms.double(4.5),
    min3DLayer = cms.int32(0),
    minHit = cms.int32(0),
    minLayer = cms.int32(3),
    minPhi = cms.double(-3.2),
    minPixelHit = cms.int32(0),
    minRapidity = cms.double(-4.5),
    originalAlgorithm = cms.vstring(),
    ptMin = cms.double(0.9), #previous 0.1
    quality = cms.vstring('highPurity'),
    src = cms.InputTag("hltPhase2GeneralTracksFromPVPt09"),
    tip = cms.double(120),
    usePV = cms.bool(False),
    vertexTag = cms.InputTag("hltPhase2OfflinePrimaryVertices")
)


hltPhase2CutsRecoTracksHighPtTripletStep = cms.EDProducer("RecoTrackViewRefSelector",
    algorithm = cms.vstring('highPtTripletStep'),
    algorithmMaskContains = cms.vstring(),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    invertRapidityCut = cms.bool(False), # cmssw_11_1
    lip = cms.double(300.0),
    maxChi2 = cms.double(10000), 
    maxPhi = cms.double(3.2),
    maxRapidity = cms.double(4.5),
    min3DLayer = cms.int32(0),
    minHit = cms.int32(0),
    minLayer = cms.int32(3),
    minPhi = cms.double(-3.2),
    minPixelHit = cms.int32(0),
    minRapidity = cms.double(-4.5),
    originalAlgorithm = cms.vstring(),
    ptMin = cms.double(0.9), # previous 0.1
    quality = cms.vstring('loose'),
    src = cms.InputTag("hltPhase2GeneralTracks"),
    tip = cms.double(120), 
    usePV = cms.bool(False),
    vertexTag = cms.InputTag("hltPhase2OfflinePrimaryVertices")
)


hltPhase2CutsRecoTracksHighPtTripletStepByAlgoMask = cms.EDProducer("RecoTrackViewRefSelector",
    algorithm = cms.vstring(),
    algorithmMaskContains = cms.vstring('highPtTripletStep'),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    invertRapidityCut = cms.bool(False), # cmssw_11_1
    lip = cms.double(300.0),
    maxChi2 = cms.double(10000.0),
    maxPhi = cms.double(3.2),
    maxRapidity = cms.double(4.5),
    min3DLayer = cms.int32(0),
    minHit = cms.int32(0),
    minLayer = cms.int32(3),
    minPhi = cms.double(-3.2),
    minPixelHit = cms.int32(0),
    minRapidity = cms.double(-4.5),
    originalAlgorithm = cms.vstring(),
    ptMin = cms.double(0.9), # previous 0.1
    quality = cms.vstring('loose'),
    src = cms.InputTag("hltPhase2GeneralTracks"),
    tip = cms.double(120), 
    usePV = cms.bool(False),
    vertexTag = cms.InputTag("hltPhase2OfflinePrimaryVertices")
)


hltPhase2CutsRecoTracksHighPtTripletStepByAlgoMaskHp = cms.EDProducer("RecoTrackViewRefSelector",
    algorithm = cms.vstring(),
    algorithmMaskContains = cms.vstring('highPtTripletStep'),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    invertRapidityCut = cms.bool(False), # cmssw_11_1
    lip = cms.double(300.0),
    maxChi2 = cms.double(10000.0),
    maxPhi = cms.double(3.2),
    maxRapidity = cms.double(4.5),
    min3DLayer = cms.int32(0),
    minHit = cms.int32(0),
    minLayer = cms.int32(3),
    minPhi = cms.double(-3.2),
    minPixelHit = cms.int32(0),
    minRapidity = cms.double(-4.5),
    originalAlgorithm = cms.vstring(),
    ptMin = cms.double(0.9), # previous 0.1
    quality = cms.vstring('highPurity'),
    src = cms.InputTag("hltPhase2GeneralTracks"),
    tip = cms.double(120),
    usePV = cms.bool(False),
    vertexTag = cms.InputTag("hltPhase2OfflinePrimaryVertices")
)


hltPhase2CutsRecoTracksHighPtTripletStepByOriginalAlgo = cms.EDProducer("RecoTrackViewRefSelector",
    algorithm = cms.vstring(),
    algorithmMaskContains = cms.vstring(),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    invertRapidityCut = cms.bool(False), # cmssw_11_1
    lip = cms.double(300.0),
    maxChi2 = cms.double(10000.0),
    maxPhi = cms.double(3.2),
    maxRapidity = cms.double(4.5),
    min3DLayer = cms.int32(0),
    minHit = cms.int32(0),
    minLayer = cms.int32(3),
    minPhi = cms.double(-3.2),
    minPixelHit = cms.int32(0),
    minRapidity = cms.double(-4.5),
    originalAlgorithm = cms.vstring('highPtTripletStep'),
    ptMin = cms.double(0.9), # previous 0.1
    quality = cms.vstring('loose'),
    src = cms.InputTag("hltPhase2GeneralTracks"),
    tip = cms.double(120), 
    usePV = cms.bool(False),
    vertexTag = cms.InputTag("hltPhase2OfflinePrimaryVertices")
)


hltPhase2CutsRecoTracksHighPtTripletStepByOriginalAlgoHp = cms.EDProducer("RecoTrackViewRefSelector",
    algorithm = cms.vstring(),
    algorithmMaskContains = cms.vstring(),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    invertRapidityCut = cms.bool(False), # cmssw_11_1
    lip = cms.double(300.0),
    maxChi2 = cms.double(10000.0),
    maxPhi = cms.double(3.2),
    maxRapidity = cms.double(4.5),
    min3DLayer = cms.int32(0),
    minHit = cms.int32(0),
    minLayer = cms.int32(3),
    minPhi = cms.double(-3.2),
    minPixelHit = cms.int32(0),
    minRapidity = cms.double(-4.5),
    originalAlgorithm = cms.vstring('highPtTripletStep'),
    ptMin = cms.double(0.9), # previous 0.1 
    quality = cms.vstring('highPurity'),
    src = cms.InputTag("hltPhase2GeneralTracks"),
    tip = cms.double(120), 
    usePV = cms.bool(False),
    vertexTag = cms.InputTag("hltPhase2OfflinePrimaryVertices")
)


hltPhase2CutsRecoTracksHighPtTripletStepHp = cms.EDProducer("RecoTrackViewRefSelector",
    algorithm = cms.vstring('highPtTripletStep'),
    algorithmMaskContains = cms.vstring(),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    invertRapidityCut = cms.bool(False), # cmssw_11_1
    lip = cms.double(300.0),
    maxChi2 = cms.double(10000.0),
    maxPhi = cms.double(3.2),
    maxRapidity = cms.double(4.5),
    min3DLayer = cms.int32(0),
    minHit = cms.int32(0),
    minLayer = cms.int32(3),
    minPhi = cms.double(-3.2),
    minPixelHit = cms.int32(0),
    minRapidity = cms.double(-4.5),
    originalAlgorithm = cms.vstring(),
    ptMin = cms.double(0.9), # previous 0.1
    quality = cms.vstring('highPurity'),
    src = cms.InputTag("hltPhase2GeneralTracks"),
    tip = cms.double(120), 
    usePV = cms.bool(False),
    vertexTag = cms.InputTag("hltPhase2OfflinePrimaryVertices")
)

hltPhase2CutsRecoTracksHp = cms.EDProducer("RecoTrackViewRefSelector",
    algorithm = cms.vstring(),
    algorithmMaskContains = cms.vstring(),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    invertRapidityCut = cms.bool(False), # cmssw_11_1
    lip = cms.double(300.0),
    maxChi2 = cms.double(10000.0),
    maxPhi = cms.double(3.2),
    maxRapidity = cms.double(4.5),
    min3DLayer = cms.int32(0),
    minHit = cms.int32(0),
    minLayer = cms.int32(3),
    minPhi = cms.double(-3.2),
    minPixelHit = cms.int32(0),
    minRapidity = cms.double(-4.5),
    originalAlgorithm = cms.vstring(),
    ptMin = cms.double(0.9), # previous 0.1
    quality = cms.vstring('highPurity'),
    src = cms.InputTag("hltPhase2GeneralTracks"),
    tip = cms.double(120), 
    usePV = cms.bool(False),
    vertexTag = cms.InputTag("hltPhase2OfflinePrimaryVertices")
)


hltPhase2CutsRecoTracksInitialStep = cms.EDProducer("RecoTrackViewRefSelector",
    algorithm = cms.vstring('initialStep'),
    algorithmMaskContains = cms.vstring(),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    invertRapidityCut = cms.bool(False), # cmssw_11_1
    lip = cms.double(300.0),
    maxChi2 = cms.double(10000.0),
    maxPhi = cms.double(3.2),
    maxRapidity = cms.double(4.5),
    min3DLayer = cms.int32(0),
    minHit = cms.int32(0),
    minLayer = cms.int32(3),
    minPhi = cms.double(-3.2),
    minPixelHit = cms.int32(0),
    minRapidity = cms.double(-4.5),
    originalAlgorithm = cms.vstring(),
    ptMin = cms.double(0.9), # previous 0.1
    quality = cms.vstring('loose'),
    src = cms.InputTag("hltPhase2GeneralTracks"),
    tip = cms.double(120), 
    usePV = cms.bool(False),
    vertexTag = cms.InputTag("hltPhase2OfflinePrimaryVertices")
)


hltPhase2CutsRecoTracksInitialStepByAlgoMask = cms.EDProducer("RecoTrackViewRefSelector",
    algorithm = cms.vstring(),
    algorithmMaskContains = cms.vstring('initialStep'),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    invertRapidityCut = cms.bool(False), # cmssw_11_1
    lip = cms.double(300.0),
    maxChi2 = cms.double(10000.0),
    maxPhi = cms.double(3.2),
    maxRapidity = cms.double(4.5),
    min3DLayer = cms.int32(0),
    minHit = cms.int32(0),
    minLayer = cms.int32(3),
    minPhi = cms.double(-3.2),
    minPixelHit = cms.int32(0),
    minRapidity = cms.double(-4.5),
    originalAlgorithm = cms.vstring(),
    ptMin = cms.double(0.9), # previous 0.1
    quality = cms.vstring('loose'),
    src = cms.InputTag("hltPhase2GeneralTracks"),
    tip = cms.double(120), 
    usePV = cms.bool(False),
    vertexTag = cms.InputTag("hltPhase2OfflinePrimaryVertices")
)


hltPhase2CutsRecoTracksInitialStepByAlgoMaskHp = cms.EDProducer("RecoTrackViewRefSelector",
    algorithm = cms.vstring(),
    algorithmMaskContains = cms.vstring('initialStep'),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    invertRapidityCut = cms.bool(False), # cmssw_11_1
    lip = cms.double(300.0),
    maxChi2 = cms.double(10000.0),
    maxPhi = cms.double(3.2),
    maxRapidity = cms.double(4.5),
    min3DLayer = cms.int32(0),
    minHit = cms.int32(0),
    minLayer = cms.int32(3),
    minPhi = cms.double(-3.2),
    minPixelHit = cms.int32(0),
    minRapidity = cms.double(-4.5),
    originalAlgorithm = cms.vstring(),
    ptMin = cms.double(0.9), # previous 0.1
    quality = cms.vstring('highPurity'),
    src = cms.InputTag("hltPhase2GeneralTracks"),
    tip = cms.double(120.0), 
    usePV = cms.bool(False),
    vertexTag = cms.InputTag("hltPhase2OfflinePrimaryVertices")
)


hltPhase2CutsRecoTracksInitialStepByOriginalAlgo = cms.EDProducer("RecoTrackViewRefSelector",
    algorithm = cms.vstring(),
    algorithmMaskContains = cms.vstring(),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    invertRapidityCut = cms.bool(False), # cmssw_11_1
    lip = cms.double(300.0),
    maxChi2 = cms.double(10000.0),
    maxPhi = cms.double(3.2),
    maxRapidity = cms.double(4.5),
    min3DLayer = cms.int32(0),
    minHit = cms.int32(0),
    minLayer = cms.int32(3),
    minPhi = cms.double(-3.2),
    minPixelHit = cms.int32(0),
    minRapidity = cms.double(-4.5),
    originalAlgorithm = cms.vstring('initialStep'),
    ptMin = cms.double(0.9), # previous 0.1
    quality = cms.vstring('loose'),
    src = cms.InputTag("hltPhase2GeneralTracks"),
    tip = cms.double(120.0), 
    usePV = cms.bool(False),
    vertexTag = cms.InputTag("hltPhase2OfflinePrimaryVertices")
)


hltPhase2CutsRecoTracksInitialStepByOriginalAlgoHp = cms.EDProducer("RecoTrackViewRefSelector",
    algorithm = cms.vstring(),
    algorithmMaskContains = cms.vstring(),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    invertRapidityCut = cms.bool(False), # cmssw_11_1
    lip = cms.double(300.0),
    maxChi2 = cms.double(10000.0),
    maxPhi = cms.double(3.2),
    maxRapidity = cms.double(4.5),
    min3DLayer = cms.int32(0),
    minHit = cms.int32(0),
    minLayer = cms.int32(3),
    minPhi = cms.double(-3.2),
    minPixelHit = cms.int32(0),
    minRapidity = cms.double(-4.5),
    originalAlgorithm = cms.vstring('initialStep'),
    ptMin = cms.double(0.9), # previous 0.1 
    quality = cms.vstring('highPurity'),
    src = cms.InputTag("hltPhase2GeneralTracks"),
    tip = cms.double(120.0), 
    usePV = cms.bool(False),
    vertexTag = cms.InputTag("hltPhase2OfflinePrimaryVertices")
)


hltPhase2CutsRecoTracksInitialStepHp = cms.EDProducer("RecoTrackViewRefSelector",
    algorithm = cms.vstring('initialStep'),
    algorithmMaskContains = cms.vstring(),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    invertRapidityCut = cms.bool(False), # cmssw_11_1
    lip = cms.double(300.0),
    maxChi2 = cms.double(10000.0),
    maxPhi = cms.double(3.2),
    maxRapidity = cms.double(4.5),
    min3DLayer = cms.int32(0),
    minHit = cms.int32(0),
    minLayer = cms.int32(3),
    minPhi = cms.double(-3.2),
    minPixelHit = cms.int32(0),
    minRapidity = cms.double(-4.5),
    originalAlgorithm = cms.vstring(),
    ptMin = cms.double(0.9), # previous 0.1
    quality = cms.vstring('highPurity'),
    src = cms.InputTag("hltPhase2GeneralTracks"),
    tip = cms.double(120.0), 
    usePV = cms.bool(False),
    vertexTag = cms.InputTag("hltPhase2OfflinePrimaryVertices")
)


hltPhase2CutsRecoTracksPt09HighPtTripletStep = cms.EDProducer("RecoTrackViewRefSelector",
    algorithm = cms.vstring('highPtTripletStep'),
    algorithmMaskContains = cms.vstring(),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    invertRapidityCut = cms.bool(False), # cmssw_11_1
    lip = cms.double(300.0),
    maxChi2 = cms.double(10000.0),
    maxPhi = cms.double(3.2),
    maxRapidity = cms.double(4.5),
    min3DLayer = cms.int32(0),
    minHit = cms.int32(0),
    minLayer = cms.int32(3),
    minPhi = cms.double(-3.2),
    minPixelHit = cms.int32(0),
    minRapidity = cms.double(-4.5),
    originalAlgorithm = cms.vstring(),
    ptMin = cms.double(0.9), # previous 0.1
    quality = cms.vstring('loose'),
    src = cms.InputTag("hltPhase2GeneralTracksPt09"),
    tip = cms.double(120.0), 
    usePV = cms.bool(False),
    vertexTag = cms.InputTag("hltPhase2OfflinePrimaryVertices")
)


hltPhase2CutsRecoTracksPt09HighPtTripletStepHp = cms.EDProducer("RecoTrackViewRefSelector",
    algorithm = cms.vstring('highPtTripletStep'),
    algorithmMaskContains = cms.vstring(),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    invertRapidityCut = cms.bool(False), # cmssw_11_1
    lip = cms.double(300.0),
    maxChi2 = cms.double(10000.0),
    maxPhi = cms.double(3.2),
    maxRapidity = cms.double(4.5),
    min3DLayer = cms.int32(0),
    minHit = cms.int32(0),
    minLayer = cms.int32(3),
    minPhi = cms.double(-3.2),
    minPixelHit = cms.int32(0),
    minRapidity = cms.double(-4.5),
    originalAlgorithm = cms.vstring(),
    ptMin = cms.double(0.9), # previous 0.1
    quality = cms.vstring('highPurity'),
    src = cms.InputTag("hltPhase2GeneralTracksPt09"),
    tip = cms.double(120.0), 
    usePV = cms.bool(False),
    vertexTag = cms.InputTag("hltPhase2OfflinePrimaryVertices")
)

hltPhase2CutsRecoTracksPt09Hp = cms.EDProducer("RecoTrackViewRefSelector",
    algorithm = cms.vstring(),
    algorithmMaskContains = cms.vstring(),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    invertRapidityCut = cms.bool(False), # cmssw_11_1
    lip = cms.double(300.0),
    maxChi2 = cms.double(10000.0),
    maxPhi = cms.double(3.2),
    maxRapidity = cms.double(4.5),
    min3DLayer = cms.int32(0),
    minHit = cms.int32(0),
    minLayer = cms.int32(3),
    minPhi = cms.double(-3.2),
    minPixelHit = cms.int32(0),
    minRapidity = cms.double(-4.5),
    originalAlgorithm = cms.vstring(),
    ptMin = cms.double(0.9), # previous 0.1
    quality = cms.vstring('highPurity'),
    src = cms.InputTag("hltPhase2GeneralTracksPt09"),
    tip = cms.double(120.0), 
    usePV = cms.bool(False),
    vertexTag = cms.InputTag("hltPhase2OfflinePrimaryVertices")
)


hltPhase2CutsRecoTracksPt09InitialStep = cms.EDProducer("RecoTrackViewRefSelector",
    algorithm = cms.vstring('initialStep'),
    algorithmMaskContains = cms.vstring(),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    invertRapidityCut = cms.bool(False), # cmssw_11_1
    lip = cms.double(300.0),
    maxChi2 = cms.double(10000.0),
    maxPhi = cms.double(3.2),
    maxRapidity = cms.double(4.5),
    min3DLayer = cms.int32(0),
    minHit = cms.int32(0),
    minLayer = cms.int32(3),
    minPhi = cms.double(-3.2),
    minPixelHit = cms.int32(0),
    minRapidity = cms.double(-4.5),
    originalAlgorithm = cms.vstring(),
    ptMin = cms.double(0.9), # previous 0.1
    quality = cms.vstring('loose'),
    src = cms.InputTag("hltPhase2GeneralTracksPt09"),
    tip = cms.double(120.0), 
    usePV = cms.bool(False),
    vertexTag = cms.InputTag("hltPhase2OfflinePrimaryVertices")
)


hltPhase2CutsRecoTracksPt09InitialStepHp = cms.EDProducer("RecoTrackViewRefSelector",
    algorithm = cms.vstring('initialStep'),
    algorithmMaskContains = cms.vstring(),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    invertRapidityCut = cms.bool(False), # cmssw_11_1
    lip = cms.double(300.0),
    maxChi2 = cms.double(10000.0),
    maxPhi = cms.double(3.2),
    maxRapidity = cms.double(4.5),
    min3DLayer = cms.int32(0),
    minHit = cms.int32(0),
    minLayer = cms.int32(3),
    minPhi = cms.double(-3.2),
    minPixelHit = cms.int32(0),
    minRapidity = cms.double(-4.5),
    originalAlgorithm = cms.vstring(),
    ptMin = cms.double(0.9), #previous 0.1
    quality = cms.vstring('highPurity'),
    src = cms.InputTag("hltPhase2GeneralTracksPt09"),
    tip = cms.double(120.0), 
    usePV = cms.bool(False),
    vertexTag = cms.InputTag("hltPhase2OfflinePrimaryVertices")
)

hltPhase2GeneralTracksFromPV = cms.EDProducer("TrackWithVertexRefSelector",
    copyExtras = cms.untracked.bool(False),
    copyTrajectories = cms.untracked.bool(False),
    d0Max = cms.double(999.0),
    dzMax = cms.double(999.0),
    etaMax = cms.double(5), 
    etaMin = cms.double(-5),
    nSigmaDtVertex = cms.double(0),
    nVertices = cms.uint32(1),
    normalizedChi2 = cms.double(999999.0),
    numberOfLostHits = cms.uint32(999),
    numberOfValidHits = cms.uint32(0),
    numberOfValidPixelHits = cms.uint32(0),
    ptErrorCut = cms.double(10000000000.0),
    ptMax = cms.double(10000000000.0),
    ptMin = cms.double(0.9), # previous 0
    quality = cms.string('loose'),
    rhoVtx = cms.double(10000000000.0),
    src = cms.InputTag("hltPhase2GeneralTracks"),
    timeResosTag = cms.InputTag(""),
    timesTag = cms.InputTag(""),
    useVtx = cms.bool(True),
    vertexTag = cms.InputTag("hltPhase2OfflinePrimaryVertices"),
    vtxFallback = cms.bool(False),
    zetaVtx = cms.double(0.1)
)


hltPhase2GeneralTracksFromPVPt09 = cms.EDProducer("RecoTrackViewRefSelector",
    algorithm = cms.vstring(),
    algorithmMaskContains = cms.vstring(),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    invertRapidityCut = cms.bool(False), # cmssw_11_1
    lip = cms.double(300.0),
    maxChi2 = cms.double(10000.0),
    maxPhi = cms.double(3.2),
    maxRapidity = cms.double(4.5),
    min3DLayer = cms.int32(0),
    minHit = cms.int32(0),
    minLayer = cms.int32(3),
    minPhi = cms.double(-3.2),
    minPixelHit = cms.int32(0),
    minRapidity = cms.double(-4.5),
    originalAlgorithm = cms.vstring(),
    ptMin = cms.double(0.9),
    quality = cms.vstring('loose'),
    src = cms.InputTag("hltPhase2GeneralTracksFromPV"),
    tip = cms.double(120.0), 
    usePV = cms.bool(False),
    vertexTag = cms.InputTag("hltPhase2OfflinePrimaryVertices")
)


hltPhase2GeneralTracksPt09 = cms.EDProducer("RecoTrackViewRefSelector",
    algorithm = cms.vstring(),
    algorithmMaskContains = cms.vstring(),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    invertRapidityCut = cms.bool(False), # cmssw_11_1
    lip = cms.double(300.0),
    maxChi2 = cms.double(10000.0),
    maxPhi = cms.double(3.2),
    maxRapidity = cms.double(4.5),
    min3DLayer = cms.int32(0),
    minHit = cms.int32(0),
    minLayer = cms.int32(3),
    minPhi = cms.double(-3.2),
    minPixelHit = cms.int32(0),
    minRapidity = cms.double(-4.5),
    originalAlgorithm = cms.vstring(),
    ptMin = cms.double(0.9),
    quality = cms.vstring('loose'),
    src = cms.InputTag("hltPhase2GeneralTracks"),
    tip = cms.double(120.0), 
    usePV = cms.bool(False),
    vertexTag = cms.InputTag("hltPhase2OfflinePrimaryVertices")
)

hltPhase2SeedTrackshighPtTripletStepSeeds = cms.EDProducer("TrackFromSeedProducer",
    TTRHBuilder = cms.string('WithoutRefit'),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    src = cms.InputTag("hltPhase2HighPtTripletStepSeeds")
)


hltPhase2SeedTracksinitialStepSeeds = cms.EDProducer("TrackFromSeedProducer",
    TTRHBuilder = cms.string('WithoutRefit'),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    src = cms.InputTag("hltPhase2InitialStepSeeds")
)

hltPhase2TrackingParticleRecoTrackAsssociation = cms.EDProducer("TrackAssociatorEDProducer",
    associator = cms.InputTag("quickTrackAssociatorByHits"),
    ignoremissingtrackcollection = cms.untracked.bool(False),
    label_tp = cms.InputTag("mix","MergedTrackTruth"),
    label_tr = cms.InputTag("hltPhase2GeneralTracks")
)

hltPhase2TrackingParticlesElectron = cms.EDFilter("TrackingParticleRefSelector",
    chargedOnly = cms.bool(True),
    intimeOnly = cms.bool(False),
    invertRapidityCut = cms.bool(False), # cmssw_11_1
    lip = cms.double(100000.0),
    maxPhi = cms.double(3.2),
    maxRapidity = cms.double(4.5), #10
    minHit = cms.int32(0),
    minPhi = cms.double(-3.2),
    minRapidity = cms.double(-4.5), #-10
    pdgId = cms.vint32(-11, 11),
    ptMax = cms.double(1e+100),
    ptMin = cms.double(0),
    signalOnly = cms.bool(False),
    src = cms.InputTag("mix","MergedTrackTruth"),
    stableOnly = cms.bool(False),
    tip = cms.double(100000.0)
)

hltPhase2TrackingParticlesSignal = cms.EDFilter("TrackingParticleRefSelector",
    chargedOnly = cms.bool(False),
    intimeOnly = cms.bool(False),
    invertRapidityCut = cms.bool(False), #cmssw_11_1
    lip = cms.double(100000.0),
    maxPhi = cms.double(3.2),
    maxRapidity = cms.double(4.5), #10
    minHit = cms.int32(0),
    minPhi = cms.double(-3.2),
    minRapidity = cms.double(-4.5), #-10
    pdgId = cms.vint32(),
    ptMax = cms.double(1e+100),
    ptMin = cms.double(0),
    signalOnly = cms.bool(True),
    src = cms.InputTag("mix","MergedTrackTruth"),
    stableOnly = cms.bool(False),
    tip = cms.double(100000.0)
)

hltPhase2V0Validator = cms.EDProducer("V0Validator",
    DQMRootFileName = cms.untracked.string(''),
    dirName = cms.untracked.string('Vertexing/V0V'),
    kShortCollection = cms.untracked.InputTag("generalV0Candidates","Kshort"),
    lambdaCollection = cms.untracked.InputTag("generalV0Candidates","Lambda"),
    trackAssociatorMap = cms.untracked.InputTag("hltPhase2TrackingParticleRecoTrackAsssociation"),
    trackingVertexCollection = cms.untracked.InputTag("mix","MergedTrackTruth"),
    vertexCollection = cms.untracked.InputTag("hltPhase2OfflinePrimaryVertices")
)

hltPhase2SelectedOfflinePrimaryVertices = cms.EDFilter("VertexSelector",
    cut = cms.string('isValid & ndof > 4 & tracksSize > 0 & abs(z) <= 24 & abs(position.Rho) <= 2.'),
    filter = cms.bool(False),
    src = cms.InputTag("hltPhase2OfflinePrimaryVertices")
)

hltPhase2SelectedOfflinePrimaryVerticesWithBS = cms.EDFilter("VertexSelector",
    cut = cms.string('isValid & ndof > 4 & tracksSize > 0 & abs(z) <= 24 & abs(position.Rho) <= 2.'),
    filter = cms.bool(False),
    src = cms.InputTag("hltPhase2OfflinePrimaryVerticesWithBS")
)

hltPhase2SelectedPixelVertices = cms.EDFilter("VertexSelector",
    cut = cms.string('isValid & ndof > 4 & tracksSize > 0 & abs(z) <= 24 & abs(position.Rho) <= 2.'),
    filter = cms.bool(False),
    src = cms.InputTag("hltPhase2PixelVertices")
)

hltPhase2VertexAnalysisTrackingOnly = cms.EDProducer("PrimaryVertexAnalyzer4PUSlimmed",
    do_generic_sim_plots = cms.untracked.bool(True),
    root_folder = cms.untracked.string('Vertexing/PrimaryVertexV'),
    trackAssociatorMap = cms.untracked.InputTag("hltPhase2TrackingParticleRecoTrackAsssociation"),
    trackingParticleCollection = cms.untracked.InputTag("mix","MergedTrackTruth"),
    trackingVertexCollection = cms.untracked.InputTag("mix","MergedTrackTruth"),
    use_only_charged_tracks = cms.untracked.bool(True),
    verbose = cms.untracked.bool(False),
    vertexAssociator = cms.untracked.InputTag("hltPhase2VertexAssociatorByPositionAndTracks"),
    vertexRecoCollections = cms.VInputTag("hltPhase2OfflinePrimaryVertices", "hltPhase2OfflinePrimaryVerticesWithBS", "hltPhase2SelectedOfflinePrimaryVertices", "hltPhase2SelectedOfflinePrimaryVerticesWithBS", "hltPhase2FirstStepPrimaryVertices")
)

hltPhase2PixelVertexAnalysisTrackingOnly = cms.EDProducer("PrimaryVertexAnalyzer4PUSlimmed",
    do_generic_sim_plots = cms.untracked.bool(False),
    root_folder = cms.untracked.string('Vertexing/PrimaryVertexV'),
    trackAssociatorMap = cms.untracked.InputTag("hltPhase2TrackingParticlePixelTrackAsssociation"),
    trackingParticleCollection = cms.untracked.InputTag("mix","MergedTrackTruth"),
    trackingVertexCollection = cms.untracked.InputTag("mix","MergedTrackTruth"),
    use_only_charged_tracks = cms.untracked.bool(True),
    verbose = cms.untracked.bool(False),
    vertexAssociator = cms.untracked.InputTag("hltPhase2PixelVertexAssociatorByPositionAndTracks"),
    vertexRecoCollections = cms.VInputTag("hltPhase2PixelVertices", "hltPhase2SelectedPixelVertices")
)

#########################################################################

MC_prevalidation_v6 = cms.Path(cms.Task(hltPhase2VertexAssociatorByPositionAndTracks, hltPhase2CutsRecoTracksBtvLike, hltPhase2CutsRecoTracksFromPVHighPtTripletStep, hltPhase2CutsRecoTracksFromPVHighPtTripletStepHp, hltPhase2CutsRecoTracksFromPVHp, hltPhase2CutsRecoTracksFromPVInitialStep, hltPhase2CutsRecoTracksFromPVInitialStepHp, hltPhase2CutsRecoTracksFromPVPt09HighPtTripletStep, hltPhase2CutsRecoTracksFromPVPt09HighPtTripletStepHp, hltPhase2CutsRecoTracksFromPVPt09Hp, hltPhase2CutsRecoTracksFromPVPt09InitialStep, hltPhase2CutsRecoTracksFromPVPt09InitialStepHp, hltPhase2CutsRecoTracksHighPtTripletStep, hltPhase2CutsRecoTracksHighPtTripletStepByAlgoMask, hltPhase2CutsRecoTracksHighPtTripletStepByAlgoMaskHp, hltPhase2CutsRecoTracksHighPtTripletStepByOriginalAlgo, hltPhase2CutsRecoTracksHighPtTripletStepByOriginalAlgoHp, hltPhase2CutsRecoTracksHighPtTripletStepHp, hltPhase2CutsRecoTracksHp, hltPhase2CutsRecoTracksInitialStep, hltPhase2CutsRecoTracksInitialStepByAlgoMask, hltPhase2CutsRecoTracksInitialStepByAlgoMaskHp, hltPhase2CutsRecoTracksInitialStepByOriginalAlgo, hltPhase2CutsRecoTracksInitialStepByOriginalAlgoHp, hltPhase2CutsRecoTracksInitialStepHp, hltPhase2CutsRecoTracksPt09HighPtTripletStep, hltPhase2CutsRecoTracksPt09HighPtTripletStepHp, hltPhase2CutsRecoTracksPt09Hp, hltPhase2CutsRecoTracksPt09InitialStep, hltPhase2CutsRecoTracksPt09InitialStepHp, hltPhase2GeneralTracksFromPV, hltPhase2GeneralTracksFromPVPt09, hltPhase2GeneralTracksPt09, quickTrackAssociatorByHits, hltPhase2SeedTrackshighPtTripletStepSeeds, hltPhase2SeedTracksinitialStepSeeds, tpClusterProducer, trackingParticleNumberOfLayersProducer, hltPhase2TrackingParticleRecoTrackAsssociation, trackingParticlesBHadron, trackingParticlesConversion, hltPhase2TrackingParticlesElectron, hltPhase2TrackingParticlesSignal), cms.Task(hltPhase2SelectedOfflinePrimaryVertices, hltPhase2SelectedOfflinePrimaryVerticesWithBS, simHitTPAssocProducer, hltPhase2V0Validator, hltPhase2VertexAnalysisTrackingOnly), cms.Task(hltPhase2PixelVertexAssociatorByPositionAndTracks, hltPhase2TrackingParticlePixelTrackAsssociation, hltPhase2SelectedPixelVertices, hltPhase2PixelVertexAnalysisTrackingOnly)) ### pixelVertices last cms.Task

MC_validation_v6 = cms.Path( hltPhase2TrackValidatorPixelTrackingOnly + hltPhase2TrackValidatorTrackingOnly + hltPhase2TrackValidatorTPPtLess09Standalone+ hltPhase2TrackValidatorFromPVStandalone + hltPhase2TrackValidatorFromPVAllTPStandalone + hltPhase2TrackValidatorAllTPEfficStandalone + hltPhase2TrackValidatorBHadronTrackingOnly + hltPhase2TrackValidatorSeedingTrackingOnly)# + trackValidatorSeedingPreSplittingTrackingOnly+trackValidatorBuilding+trackValidatorBuildingPreSplitting) 


