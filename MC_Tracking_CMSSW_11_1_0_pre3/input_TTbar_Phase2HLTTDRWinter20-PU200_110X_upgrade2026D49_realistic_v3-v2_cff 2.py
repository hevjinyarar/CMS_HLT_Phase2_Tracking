import FWCore.ParameterSet.Config as cms

# Input source
source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
"root://xrootd-cms.infn.it//store/mc/Phase2HLTTDRWinter20DIGI/TT_TuneCP5_14TeV-powheg-pythia8/GEN-SIM-DIGI-RAW/PU200_110X_mcRun4_realistic_v3-v2/240000/55499734-1DDE-A94B-89FE-59897268BB29.root",
"root://xrootd-cms.infn.it//store/mc/Phase2HLTTDRWinter20DIGI/TT_TuneCP5_14TeV-powheg-pythia8/GEN-SIM-DIGI-RAW/PU200_110X_mcRun4_realistic_v3-v2/240000/54AA18A6-0B6A-284B-B15E-9074463466AF.root",
"root://xrootd-cms.infn.it//store/mc/Phase2HLTTDRWinter20DIGI/TT_TuneCP5_14TeV-powheg-pythia8/GEN-SIM-DIGI-RAW/PU200_110X_mcRun4_realistic_v3-v2/240000/5B81599F-1BA2-0F48-9065-25906E5292DF.root",
"root://xrootd-cms.infn.it//store/mc/Phase2HLTTDRWinter20DIGI/TT_TuneCP5_14TeV-powheg-pythia8/GEN-SIM-DIGI-RAW/PU200_110X_mcRun4_realistic_v3-v2/240000/EF280CE1-BB1A-3049-BB69-95A9F96E66A6.root",
"root://xrootd-cms.infn.it//store/mc/Phase2HLTTDRWinter20DIGI/TT_TuneCP5_14TeV-powheg-pythia8/GEN-SIM-DIGI-RAW/PU200_110X_mcRun4_realistic_v3-v2/240000/6F8C060D-4E3C-FE44-A51A-6A6A2E41A520.root",
"root://xrootd-cms.infn.it//store/mc/Phase2HLTTDRWinter20DIGI/TT_TuneCP5_14TeV-powheg-pythia8/GEN-SIM-DIGI-RAW/PU200_110X_mcRun4_realistic_v3-v2/240000/CA40A687-0EA8-DA44-B529-B020D0C3ED4B.root",
"root://xrootd-cms.infn.it//store/mc/Phase2HLTTDRWinter20DIGI/TT_TuneCP5_14TeV-powheg-pythia8/GEN-SIM-DIGI-RAW/PU200_110X_mcRun4_realistic_v3-v2/240000/88168EEB-B667-374A-AD70-8FED5ADE5727.root",
"root://xrootd-cms.infn.it//store/mc/Phase2HLTTDRWinter20DIGI/TT_TuneCP5_14TeV-powheg-pythia8/GEN-SIM-DIGI-RAW/PU200_110X_mcRun4_realistic_v3-v2/240000/EEC48AE9-F4A9-9F44-B47E-2C38EBB2339D.root",
"root://xrootd-cms.infn.it//store/mc/Phase2HLTTDRWinter20DIGI/TT_TuneCP5_14TeV-powheg-pythia8/GEN-SIM-DIGI-RAW/PU200_110X_mcRun4_realistic_v3-v2/240000/722C0158-1994-EE41-A0E7-BA8AA6410E65.root",
"root://xrootd-cms.infn.it//store/mc/Phase2HLTTDRWinter20DIGI/TT_TuneCP5_14TeV-powheg-pythia8/GEN-SIM-DIGI-RAW/PU200_110X_mcRun4_realistic_v3-v2/240000/16F67D15-FA53-5C43-A24D-0AE8B8AC1EC8.root",
"root://xrootd-cms.infn.it//store/mc/Phase2HLTTDRWinter20DIGI/TT_TuneCP5_14TeV-powheg-pythia8/GEN-SIM-DIGI-RAW/PU200_110X_mcRun4_realistic_v3-v2/240000/5523D1EA-4B7E-1341-9A64-F1F74F2242E9.root",
"root://xrootd-cms.infn.it//store/mc/Phase2HLTTDRWinter20DIGI/TT_TuneCP5_14TeV-powheg-pythia8/GEN-SIM-DIGI-RAW/PU200_110X_mcRun4_realistic_v3-v2/240000/0F348E06-6F14-5645-921D-7E9FE51EC642.root",
"root://xrootd-cms.infn.it//store/mc/Phase2HLTTDRWinter20DIGI/TT_TuneCP5_14TeV-powheg-pythia8/GEN-SIM-DIGI-RAW/PU200_110X_mcRun4_realistic_v3-v2/240000/987D0C87-DD3E-F947-93FF-5B0EDC2A2F96.root",
"root://xrootd-cms.infn.it//store/mc/Phase2HLTTDRWinter20DIGI/TT_TuneCP5_14TeV-powheg-pythia8/GEN-SIM-DIGI-RAW/PU200_110X_mcRun4_realistic_v3-v2/240000/5F12BF73-60EA-A74E-AD2E-36F78AE70B96.root",
"root://xrootd-cms.infn.it//store/mc/Phase2HLTTDRWinter20DIGI/TT_TuneCP5_14TeV-powheg-pythia8/GEN-SIM-DIGI-RAW/PU200_110X_mcRun4_realistic_v3-v2/240000/89FDB3B4-FAB9-D04E-A92D-1A6BDA7BD886.root",
"root://xrootd-cms.infn.it//store/mc/Phase2HLTTDRWinter20DIGI/TT_TuneCP5_14TeV-powheg-pythia8/GEN-SIM-DIGI-RAW/PU200_110X_mcRun4_realistic_v3-v2/240000/870D7E80-71CC-A44A-87E0-CD52EF0A781C.root",
"root://xrootd-cms.infn.it//store/mc/Phase2HLTTDRWinter20DIGI/TT_TuneCP5_14TeV-powheg-pythia8/GEN-SIM-DIGI-RAW/PU200_110X_mcRun4_realistic_v3-v2/240000/9E9D03D7-451E-AE46-A797-D5F86BE27D0F.root",
"root://xrootd-cms.infn.it//store/mc/Phase2HLTTDRWinter20DIGI/TT_TuneCP5_14TeV-powheg-pythia8/GEN-SIM-DIGI-RAW/PU200_110X_mcRun4_realistic_v3-v2/240000/73B23F9A-38F1-3F40-9C29-EDC7536DD22A.root",
"root://xrootd-cms.infn.it//store/mc/Phase2HLTTDRWinter20DIGI/TT_TuneCP5_14TeV-powheg-pythia8/GEN-SIM-DIGI-RAW/PU200_110X_mcRun4_realistic_v3-v2/240000/76C6CAE9-5F7F-A247-BF4B-5F9A0748CBF0.root",
"root://xrootd-cms.infn.it//store/mc/Phase2HLTTDRWinter20DIGI/TT_TuneCP5_14TeV-powheg-pythia8/GEN-SIM-DIGI-RAW/PU200_110X_mcRun4_realistic_v3-v2/240000/1923486B-B37C-0A42-A472-1EA6293C2099.root",
"root://xrootd-cms.infn.it//store/mc/Phase2HLTTDRWinter20DIGI/TT_TuneCP5_14TeV-powheg-pythia8/GEN-SIM-DIGI-RAW/PU200_110X_mcRun4_realistic_v3-v2/240000/A1E62D5F-1093-A54F-974D-5BF6145EC89E.root",
"root://xrootd-cms.infn.it//store/mc/Phase2HLTTDRWinter20DIGI/TT_TuneCP5_14TeV-powheg-pythia8/GEN-SIM-DIGI-RAW/PU200_110X_mcRun4_realistic_v3-v2/240000/5C5BF4E7-1444-4743-8C93-54D702682EE9.root",
"root://xrootd-cms.infn.it//store/mc/Phase2HLTTDRWinter20DIGI/TT_TuneCP5_14TeV-powheg-pythia8/GEN-SIM-DIGI-RAW/PU200_110X_mcRun4_realistic_v3-v2/240000/109FCB0A-4DE7-5441-B12F-DA26DAE6DDB8.root",
"root://xrootd-cms.infn.it//store/mc/Phase2HLTTDRWinter20DIGI/TT_TuneCP5_14TeV-powheg-pythia8/GEN-SIM-DIGI-RAW/PU200_110X_mcRun4_realistic_v3-v2/240000/EA3F03D4-1F35-1D48-B533-3B391AF3B756.root",
"root://xrootd-cms.infn.it//store/mc/Phase2HLTTDRWinter20DIGI/TT_TuneCP5_14TeV-powheg-pythia8/GEN-SIM-DIGI-RAW/PU200_110X_mcRun4_realistic_v3-v2/240000/4B26B962-6F19-1142-96A3-FED1FF616F0F.root",
"root://xrootd-cms.infn.it//store/mc/Phase2HLTTDRWinter20DIGI/TT_TuneCP5_14TeV-powheg-pythia8/GEN-SIM-DIGI-RAW/PU200_110X_mcRun4_realistic_v3-v2/240000/5CD5F672-1905-E946-9752-8E87213BE5AD.root"
    ),
    secondaryFileNames = cms.untracked.vstring()
)

