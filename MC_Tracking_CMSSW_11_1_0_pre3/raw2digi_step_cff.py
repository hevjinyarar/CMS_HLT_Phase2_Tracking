import FWCore.ParameterSet.Config as cms

################# process.raw2digi_step
"""
################################# list of actually needed modules that are in a cms.Path (here for bookkeeping)
from Configuration.StandardSequences.RawToDigi_cff import ecalDigis, hcalDigis, muonCSCDigis, muonDTDigis, muonGEMDigis, muonRPCDigis,  scalersRawToDigi
"""

from Configuration.StandardSequences.RawToDigi_cff import *

""" #is not in cmssw_11_1
muonRPCNewDigis = cms.EDProducer("RPCDigiMerger",
    inputTagCPPFDigis = cms.InputTag("rpcCPPFRawToDigi"),
    inputTagOMTFDigis = cms.InputTag("omtfStage2Digis"),
    inputTagTwinMuxDigis = cms.InputTag("rpcTwinMuxRawToDigi")
)
"""

raw2digi_step = cms.Path(cms.Task(ecalDigis, hcalDigis, muonCSCDigis, muonDTDigis, muonGEMDigis, muonRPCDigis,  scalersRawToDigi)) #muonRPCNewDigis 
