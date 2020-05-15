import FWCore.ParameterSet.Config as cms

# input_TTbar_PhaseIIMTDTDRAutumn18DR-noPU_103X_upgrade2023_realistic_v2-v1_cff
# Input source
source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(

"root://xrootd-cms.infn.it//store/mc/PhaseIIMTDTDRAutumn18DR/TTbar_TuneCP5_14TeV_pythia8/FEVT/NoPU_103X_upgrade2023_realistic_v2-v1/120000/52367B7C-7FD2-EB42-B8E6-8B2220342B71.root",
"root://xrootd-cms.infn.it//store/mc/PhaseIIMTDTDRAutumn18DR/TTbar_TuneCP5_14TeV_pythia8/FEVT/NoPU_103X_upgrade2023_realistic_v2-v1/120000/52ED4F85-BC99-9448-9BEE-62A70F73E2D6.root",
"root://xrootd-cms.infn.it//store/mc/PhaseIIMTDTDRAutumn18DR/TTbar_TuneCP5_14TeV_pythia8/FEVT/NoPU_103X_upgrade2023_realistic_v2-v1/120000/61462B79-42F7-C444-BD36-D10CEA0D8058.root",
"root://xrootd-cms.infn.it//store/mc/PhaseIIMTDTDRAutumn18DR/TTbar_TuneCP5_14TeV_pythia8/FEVT/NoPU_103X_upgrade2023_realistic_v2-v1/120000/7EEA54C7-B5C6-7A4B-A1F4-33DD7AE52C2E.root",
"root://xrootd-cms.infn.it//store/mc/PhaseIIMTDTDRAutumn18DR/TTbar_TuneCP5_14TeV_pythia8/FEVT/NoPU_103X_upgrade2023_realistic_v2-v1/120000/C55F46DA-B87F-5A4E-9FBD-3F4E7546DF46.root",
"root://xrootd-cms.infn.it//store/mc/PhaseIIMTDTDRAutumn18DR/TTbar_TuneCP5_14TeV_pythia8/FEVT/NoPU_103X_upgrade2023_realistic_v2-v1/120000/0E397618-9C4E-9546-825C-9667395E7C45.root",
"root://xrootd-cms.infn.it//store/mc/PhaseIIMTDTDRAutumn18DR/TTbar_TuneCP5_14TeV_pythia8/FEVT/NoPU_103X_upgrade2023_realistic_v2-v1/120000/1F011FCC-E09F-524C-BD85-EBB29F05EDB2.root",
"root://xrootd-cms.infn.it//store/mc/PhaseIIMTDTDRAutumn18DR/TTbar_TuneCP5_14TeV_pythia8/FEVT/NoPU_103X_upgrade2023_realistic_v2-v1/120000/CEC20166-4652-334E-B649-09E066A01745.root",
"root://xrootd-cms.infn.it//store/mc/PhaseIIMTDTDRAutumn18DR/TTbar_TuneCP5_14TeV_pythia8/FEVT/NoPU_103X_upgrade2023_realistic_v2-v1/120000/F8B0DF1F-BB5F-A146-9BE7-0D721D4ED581.root",
"root://xrootd-cms.infn.it//store/mc/PhaseIIMTDTDRAutumn18DR/TTbar_TuneCP5_14TeV_pythia8/FEVT/NoPU_103X_upgrade2023_realistic_v2-v1/120000/CB45034D-5036-C64D-BB24-9EC0F123F23A.root",
"root://xrootd-cms.infn.it//store/mc/PhaseIIMTDTDRAutumn18DR/TTbar_TuneCP5_14TeV_pythia8/FEVT/NoPU_103X_upgrade2023_realistic_v2-v1/120000/4191FDB2-BB16-3844-BD37-8AC447F1B0BC.root",
"root://xrootd-cms.infn.it//store/mc/PhaseIIMTDTDRAutumn18DR/TTbar_TuneCP5_14TeV_pythia8/FEVT/NoPU_103X_upgrade2023_realistic_v2-v1/120000/DF287B9D-A806-B041-BE70-C7B0C137C112.root",
"root://xrootd-cms.infn.it//store/mc/PhaseIIMTDTDRAutumn18DR/TTbar_TuneCP5_14TeV_pythia8/FEVT/NoPU_103X_upgrade2023_realistic_v2-v1/120000/1D2C0551-D284-E74D-975F-894ABE553B3C.root",
"root://xrootd-cms.infn.it//store/mc/PhaseIIMTDTDRAutumn18DR/TTbar_TuneCP5_14TeV_pythia8/FEVT/NoPU_103X_upgrade2023_realistic_v2-v1/120000/5D4F95D6-1F3C-EA44-99C4-0D78910296F1.root",
"root://xrootd-cms.infn.it//store/mc/PhaseIIMTDTDRAutumn18DR/TTbar_TuneCP5_14TeV_pythia8/FEVT/NoPU_103X_upgrade2023_realistic_v2-v1/120000/0A491CB9-451E-1244-9B4C-084BAC1AAB2A.root",
"/root://xrootd-cms.infn.it/store/mc/PhaseIIMTDTDRAutumn18DR/TTbar_TuneCP5_14TeV_pythia8/FEVT/NoPU_103X_upgrade2023_realistic_v2-v1/120000/4383469C-3221-4840-A9C7-5BEAF8A14DA8.root",
"root://xrootd-cms.infn.it//store/mc/PhaseIIMTDTDRAutumn18DR/TTbar_TuneCP5_14TeV_pythia8/FEVT/NoPU_103X_upgrade2023_realistic_v2-v1/120000/287F2B1B-A0F2-9246-816A-7A6DFA81C1D9.root",
"root://xrootd-cms.infn.it//store/mc/PhaseIIMTDTDRAutumn18DR/TTbar_TuneCP5_14TeV_pythia8/FEVT/NoPU_103X_upgrade2023_realistic_v2-v1/120000/C1D0991E-73A8-834E-A75C-772AD518EC92.root",
"root://xrootd-cms.infn.it//store/mc/PhaseIIMTDTDRAutumn18DR/TTbar_TuneCP5_14TeV_pythia8/FEVT/NoPU_103X_upgrade2023_realistic_v2-v1/120000/2E3A5B4B-B133-EA49-8868-A253D7DD4252.root",
"root://xrootd-cms.infn.it//store/mc/PhaseIIMTDTDRAutumn18DR/TTbar_TuneCP5_14TeV_pythia8/FEVT/NoPU_103X_upgrade2023_realistic_v2-v1/120000/C35175A9-E2B7-9C4B-BE1D-F6AD194BA88A.root",
"root://xrootd-cms.infn.it//store/mc/PhaseIIMTDTDRAutumn18DR/TTbar_TuneCP5_14TeV_pythia8/FEVT/NoPU_103X_upgrade2023_realistic_v2-v1/120000/95A036AE-8749-AA4A-9A66-317E93BDE806.root",
"root://xrootd-cms.infn.it//store/mc/PhaseIIMTDTDRAutumn18DR/TTbar_TuneCP5_14TeV_pythia8/FEVT/NoPU_103X_upgrade2023_realistic_v2-v1/60000/27AA3609-07DD-E24E-86C0-EC318CFCC09C.root",
"root://xrootd-cms.infn.it//store/mc/PhaseIIMTDTDRAutumn18DR/TTbar_TuneCP5_14TeV_pythia8/FEVT/NoPU_103X_upgrade2023_realistic_v2-v1/60000/267EBC21-3BEF-FB4F-B1C9-79614E6FB9E2.root",
"root://xrootd-cms.infn.it//store/mc/PhaseIIMTDTDRAutumn18DR/TTbar_TuneCP5_14TeV_pythia8/FEVT/NoPU_103X_upgrade2023_realistic_v2-v1/120000/74B7077A-63E9-A54D-A522-19703FFABA85.root"

    ),
    secondaryFileNames = cms.untracked.vstring()
)