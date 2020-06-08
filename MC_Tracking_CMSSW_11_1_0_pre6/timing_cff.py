import FWCore.ParameterSet.Config as cms

##################for timing 

FastTimerService = cms.Service("FastTimerService",
    dqmLumiSectionsRange = cms.untracked.uint32(2500),
    dqmMemoryRange = cms.untracked.double(1000000),
    dqmMemoryResolution = cms.untracked.double(5000),
    dqmModuleMemoryRange = cms.untracked.double(100000),
    dqmModuleMemoryResolution = cms.untracked.double(500),
    dqmModuleTimeRange = cms.untracked.double(100.0),
    dqmModuleTimeResolution = cms.untracked.double(0.5),
    dqmPath = cms.untracked.string('DQM/TimerService'),
    dqmPathMemoryRange = cms.untracked.double(1000000),
    dqmPathMemoryResolution = cms.untracked.double(5000),
    dqmPathTimeRange = cms.untracked.double(10000.0),
    dqmPathTimeResolution = cms.untracked.double(10.0),
    dqmTimeRange = cms.untracked.double(10000.0),
    dqmTimeResolution = cms.untracked.double(10.0),
    enableDQM = cms.untracked.bool(True),
    enableDQMTransitions = cms.untracked.bool(False),
    enableDQMbyLumiSection = cms.untracked.bool(True),
    enableDQMbyModule = cms.untracked.bool(False),
    enableDQMbyPath = cms.untracked.bool(False),
    enableDQMbyProcesses = cms.untracked.bool(False),
    highlightModules = cms.untracked.VPSet(),
    printEventSummary = cms.untracked.bool(False),
    printJobSummary = cms.untracked.bool(True),
    printRunSummary = cms.untracked.bool(False)
)


## message log for timing
MessageLogger = cms.Service( "MessageLogger",
    suppressInfo = cms.untracked.vstring(  ),
    debugs = cms.untracked.PSet( 
      threshold = cms.untracked.string( "INFO" ),
      placeholder = cms.untracked.bool( True ),
      suppressInfo = cms.untracked.vstring(  ),
      suppressWarning = cms.untracked.vstring(  ),
      suppressDebug = cms.untracked.vstring(  ),
      suppressError = cms.untracked.vstring(  )
    ),
    suppressDebug = cms.untracked.vstring(  ),
    cout = cms.untracked.PSet(  placeholder = cms.untracked.bool( True ) ),
    cerr_stats = cms.untracked.PSet( 
      threshold = cms.untracked.string( "WARNING" ),
      output = cms.untracked.string( "cerr" ),
      optionalPSet = cms.untracked.bool( True )
    ),
    warnings = cms.untracked.PSet( 
      threshold = cms.untracked.string( "INFO" ),
      placeholder = cms.untracked.bool( True ),
      suppressInfo = cms.untracked.vstring(  ),
      suppressWarning = cms.untracked.vstring(  ),
      suppressDebug = cms.untracked.vstring(  ),
      suppressError = cms.untracked.vstring(  )
    ),
    statistics = cms.untracked.vstring( 'cerr' ),
    cerr = cms.untracked.PSet( 
      INFO = cms.untracked.PSet(  limit = cms.untracked.int32( 0 ) ),
      noTimeStamps = cms.untracked.bool( False ),
      FwkReport = cms.untracked.PSet( 
        reportEvery = cms.untracked.int32( 1 ),
        limit = cms.untracked.int32( 0 )
      ),
      default = cms.untracked.PSet(  limit = cms.untracked.int32( 10000000 ) ),
      Root_NoDictionary = cms.untracked.PSet(  limit = cms.untracked.int32( 0 ) ),
      FwkJob = cms.untracked.PSet(  limit = cms.untracked.int32( 0 ) ),
      FwkSummary = cms.untracked.PSet( 
        reportEvery = cms.untracked.int32( 1 ),
        limit = cms.untracked.int32( 10000000 )
      ),
      threshold = cms.untracked.string( "INFO" ),
      suppressInfo = cms.untracked.vstring(  ),
      suppressWarning = cms.untracked.vstring(  ),
      suppressDebug = cms.untracked.vstring(  ),
      suppressError = cms.untracked.vstring(  )
    ),
    FrameworkJobReport = cms.untracked.PSet( 
      default = cms.untracked.PSet(  limit = cms.untracked.int32( 0 ) ),
      FwkJob = cms.untracked.PSet(  limit = cms.untracked.int32( 10000000 ) )
    ),
    suppressWarning = cms.untracked.vstring( 'hltOnlineBeamSpot',
      'hltCtf3HitL1SeededWithMaterialTracks',
      'hltL3MuonsOIState',
      'hltPixelTracksForHighMult',
      'hltHITPixelTracksHE',
      'hltHITPixelTracksHB',
      'hltCtfL1SeededWithMaterialTracks',
      'hltRegionalTracksForL3MuonIsolation',
      'hltSiPixelClusters',
      'hltActivityStartUpElectronPixelSeeds',
      'hltLightPFTracks',
      'hltPixelVertices3DbbPhi',
      'hltL3MuonsIOHit',
      'hltPixelTracks',
      'hltSiPixelDigis',
      'hltL3MuonsOIHit',
      'hltL1SeededElectronGsfTracks',
      'hltL1SeededStartUpElectronPixelSeeds',
      'hltBLifetimeRegionalCtfWithMaterialTracksbbPhiL1FastJetFastPV',
      'hltCtfActivityWithMaterialTracks' ),
    errors = cms.untracked.PSet( 
      threshold = cms.untracked.string( "INFO" ),
      placeholder = cms.untracked.bool( True ),
      suppressInfo = cms.untracked.vstring(  ),
      suppressWarning = cms.untracked.vstring(  ),
      suppressDebug = cms.untracked.vstring(  ),
      suppressError = cms.untracked.vstring(  )
    ),
    fwkJobReports = cms.untracked.vstring( 'FrameworkJobReport' ),
    debugModules = cms.untracked.vstring(  ),
    infos = cms.untracked.PSet( 
      threshold = cms.untracked.string( "INFO" ),
      Root_NoDictionary = cms.untracked.PSet(  limit = cms.untracked.int32( 0 ) ),
      placeholder = cms.untracked.bool( True ),
      suppressInfo = cms.untracked.vstring(  ),
      suppressWarning = cms.untracked.vstring(  ),
      suppressDebug = cms.untracked.vstring(  ),
      suppressError = cms.untracked.vstring(  )
    ),
    categories = cms.untracked.vstring( 'FwkJob',
      'FwkReport',
      'FwkSummary',
      'Root_NoDictionary' ),
    destinations = cms.untracked.vstring( 'warnings',
      'errors',
      'infos',
      'debugs',
      'cout',
      'cerr' ),
    threshold = cms.untracked.string( "INFO" ),
    suppressError = cms.untracked.vstring( 'hltOnlineBeamSpot',
      'hltL3MuonCandidates',
      'hltL3TkTracksFromL2OIState',
      'hltPFJetCtfWithMaterialTracks',
      'hltL3TkTracksFromL2IOHit',
      'hltL3TkTracksFromL2OIHit' )
)


##################################### for timing
# enable the TrigReport and TimeReport
options = cms.untracked.PSet(
    wantSummary = cms.untracked.bool( True )
)
options.numberOfStreams = cms.untracked.uint32(4)
options.numberOfThreads = cms.untracked.uint32(4)



##################for timing 

# Path and EndPath definitions
hltGetConditions = cms.EDAnalyzer( "EventSetupRecordDataGetter",
    toGet = cms.VPSet( 
    ),
    verbose = cms.untracked.bool( False )
)
hltGetRaw = cms.EDAnalyzer( "HLTGetRaw",
    RawDataCollection = cms.InputTag( "rawDataCollector" )
)
hltBoolFalse = cms.EDFilter( "HLTBool",
    result = cms.bool( False )
)

#HLTriggerFirstPath = cms.Path( hltGetConditions + hltGetRaw + hltBoolFalse )
#HLTriggerFirstPath = cms.Path( hltGetRaw + hltBoolFalse )


hltTrigReport = cms.EDAnalyzer( "HLTrigReport",
    ReferencePath = cms.untracked.string( "HLTriggerFinalPath" ),
    ReferenceRate = cms.untracked.double( 100.0 ),
    serviceBy = cms.untracked.string( "never" ),
    resetBy = cms.untracked.string( "never" ),
    reportBy = cms.untracked.string( "job" ),
    HLTriggerResults = cms.InputTag( 'TriggerResults','','TIMING' )
)
hltTriggerSummaryAOD = cms.EDProducer( "TriggerSummaryProducerAOD",
    processName = cms.string( "@" )
)
hltTriggerSummaryRAW = cms.EDProducer( "TriggerSummaryProducerRAW",
    processName = cms.string( "@" )
)
hltBoolFalse = cms.EDFilter( "HLTBool",
    result = cms.bool( False )
)
#HLTriggerFinalPath = cms.Path( hltTriggerSummaryAOD + hltTriggerSummaryRAW + hltBoolFalse )
#HLTAnalyzerEndpath = cms.EndPath( hltTrigReport )

FastMonitoringService = cms.Service( "FastMonitoringService",
  fastMonIntervals = cms.untracked.uint32( 2 ),
  sleepTime = cms.untracked.int32( 1 )
)


# instrument the menu with the modules and EndPath needed for timing studies

# configure the FastTimerService
#load( "HLTrigger.Timer.FastTimerService_cfi" )
# print a text summary at the end of the job
FastTimerService.printEventSummary         = False
FastTimerService.printRunSummary           = False
FastTimerService.printJobSummary           = True

# enable DQM plots
FastTimerService.enableDQM                 = True

# enable per-path DQM plots (starting with CMSSW 9.2.3-patch2)
FastTimerService.enableDQMbyPath           = True

# enable per-module DQM plots
FastTimerService.enableDQMbyModule         = True

# enable per-event DQM plots vs lumisection
FastTimerService.enableDQMbyLumiSection    = True
FastTimerService.dqmLumiSectionsRange      = 2500

# set the time resolution of the DQM plots
FastTimerService.dqmTimeRange              = 80000.
FastTimerService.dqmTimeResolution         =    10.
FastTimerService.dqmPathTimeRange          = 80000.
FastTimerService.dqmPathTimeResolution     =    10.
FastTimerService.dqmModuleTimeRange        =  8000.
FastTimerService.dqmModuleTimeResolution   =     1.

FastTimerService.dqmMemoryRange            = 1000000
FastTimerService.dqmMemoryResolution       =    5000
FastTimerService.dqmPathMemoryRange        = 1000000
FastTimerService.dqmPathMemoryResolution   =    5000
FastTimerService.dqmModuleMemoryRange      =  100000
FastTimerService.dqmModuleMemoryResolution =     500


# set the base DQM folder for the plots
FastTimerService.dqmPath                   = 'HLT/TimerService'
FastTimerService.enableDQMbyProcesses      = False

#load("hlt_timing_setup_cff")
EvFDaqDirector = cms.Service( "EvFDaqDirector",
  buBaseDir = cms.untracked.string( "." ),
  baseDir = cms.untracked.string( "." ),
  fuLockPollInterval = cms.untracked.uint32( 2000 ),
  runNumber = cms.untracked.uint32( 0 ),
  #microMergeDisabled = cms.untracked.bool( False ), # cmssw_11_1
  outputAdler32Recheck = cms.untracked.bool( False ),
  selectedTransferMode = cms.untracked.string( "" ),
  requireTransfersPSet = cms.untracked.bool( False )#,
  #emptyLumisectionMode = cms.untracked.bool( False ) # cmssw_11_1
)

#TimingOutput = cms.EndPath( fastTimerServiceClient + dqmFileSaver )
