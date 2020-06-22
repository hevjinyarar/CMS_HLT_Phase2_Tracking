
##############
import FWCore.ParameterSet.Config as cms

from Configuration.StandardSequences.Reconstruction_cff import *


######### 
# "online": has hltPhase2 prefix either because it is introduced or the module with the same name offline is of another kind,  
# e.g. generalTracks (online:TrackListMerger, offline: DuplicateListMerger)
##############

def customize_TRK_v6(process):
	
	#online
	process.hltPhase2PSetPvClusterComparerForIT = cms.PSet( 
	  track_chi2_max = cms.double( 20.0 ),
	  track_pt_max = cms.double( 20.0 ),
	  track_prob_min = cms.double( -1.0 ),
	  track_pt_min = cms.double( 1.0 )
	)

	process.pixelTrackFilterByKinematics.ptMin = cms.double( 0.9 ) #previous 0.1

	process.pixelTracksSeedLayers.FPix = cms.PSet( 
		HitProducer = cms.string('siPixelRecHits'), #PreSplitting'),
		TTRHBuilder = cms.string('WithTrackAngle')
	#      hitErrorRPhi = cms.double( 0.0051 ),
	#      TTRHBuilder = cms.string( "hltESPTTRHBuilderPixelOnly" ),
	#      useErrorsFromParam = cms.bool( True ),
	#      hitErrorRZ = cms.double( 0.0036 ),
	#      HitProducer = cms.string( "hltSiPixelRecHits" )
	    )
	process.pixelTracksSeedLayers.BPix = cms.PSet( 
		HitProducer = cms.string('siPixelRecHits'), #PreSplitting'),
		TTRHBuilder = cms.string('WithTrackAngle')
	#      hitErrorRPhi = cms.double( 0.0027 ),
	#      TTRHBuilder = cms.string( "hltESPTTRHBuilderPixelOnly" ),
	#      useErrorsFromParam = cms.bool( True ),
	#      hitErrorRZ = cms.double( 0.006 ),
	#      HitProducer = cms.string( "hltSiPixelRecHits" )
	    )

	process.pixelTracksSeedLayers.layerList = cms.vstring( 
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
		'FPix5_neg+FPix6_neg+FPix7_neg+FPix8_neg'
	#      'BPix1+BPix2+BPix3+BPix4',
	#      'BPix1+BPix2+BPix3+FPix1_pos',
	#      'BPix1+BPix2+BPix3+FPix1_neg',
	#      'BPix1+BPix2+FPix1_pos+FPix2_pos',
	#      'BPix1+BPix2+FPix1_neg+FPix2_neg',
	#      'BPix1+FPix1_pos+FPix2_pos+FPix3_pos',
	#      'BPix1+FPix1_neg+FPix2_neg+FPix3_neg' 
	    )
	

	process.pixelTracksTrackingRegions.RegionPSet.ptMin = cms.double( 0.9 ) # previous 0.8

	process.pixelTracks.mightGet = cms.untracked.vstring("")

	# this has to be re-defined, offline is PrimaryVertexProducer
	process.hltPhase2PixelVertices = cms.EDProducer( "PixelVertexProducer",
	    WtAverage = cms.bool( True ),
	    Method2 = cms.bool( True ),
	    beamSpot = cms.InputTag( "offlineBeamSpot" ),
	    PVcomparer = cms.PSet(  refToPSet_ = cms.string( "hltPhase2PSetPvClusterComparerForIT" ) ),
	    Verbosity = cms.int32( 0 ),
	    UseError = cms.bool( True ),
	    TrackCollection = cms.InputTag( "pixelTracks" ),
	    PtMin = cms.double( 1.0 ),
	    NTrkMin = cms.int32( 2 ),
	    ZOffset = cms.double( 5.0 ),
	    Finder = cms.string( "DivisiveVertexFinder" ),
	    ZSeparation = cms.double( 0.05 )
	)

	process.hltPhase2TrimmedPixelVertices = cms.EDProducer( "PixelVertexCollectionTrimmer",
	    src = cms.InputTag( "hltPhase2PixelVertices" ),
	    fractionSumPt2 = cms.double( 0.3 ),
	    minSumPt2 = cms.double( 0.0 ),
	    PVcomparer = cms.PSet(  refToPSet_ = cms.string( "hltPhase2PSetPvClusterComparerForIT" ) ),
	    maxVtx = cms.uint32( 100 ) # > 200 # previous 100
	)


	########################## vertex modules

	process.inclusiveVertexFinder.minPt = cms.double(0.9) # ptcut previous 0.8

	process.trackVertexArbitrator.trackMinPt = cms.double(0.9) # ptcut previous 0.4

	process.trackWithVertexRefSelectorBeforeSorting.ptMin = cms.double(0.9) # ptcut previous 0.3

	process.unsortedOfflinePrimaryVertices.minPt = cms.double(0.9) # ptcut previous 0.0

	process.firstStepPrimaryVerticesUnsorted.minPt = cms.double(0.9) # ptcut previous 0.0


	##################### tracking modules

	trackAlgoPriorityOrder.algoOrder = cms.vstring(
		'initialStep', 
		'highPtTripletStep'### v2
	    )
	
	# online beacuse offline it is a DuplicateListMerger
	process.hltPhase2GeneralTracks = cms.EDProducer("TrackListMerger",  
	    Epsilon = cms.double(-0.001),
	    FoundHitBonus = cms.double(5.0),
	    LostHitPenalty = cms.double(5.0),
	    MaxNormalizedChisq = cms.double(1000.0),
	    MinFound = cms.int32(3),
	    MinPT = cms.double(0.9), # ptcut previous 0.05
	    ShareFrac = cms.double(0.19),
	    TrackProducers = cms.VInputTag(
		#"initialStepTracks", "highPtTripletStepTracks" ### v2
		"hltPhase2InitialStepTrackselectionHighPurity", "hltPhase2HighPtTripletStepTrackselectionHighPurity" ### v2 # trackcutclassifier
	    ),
	    allowFirstHitShare = cms.bool(True),
	    copyExtras = cms.untracked.bool(True),
	    copyMVA = cms.bool(False), # trackcutclassifier before True
	    hasSelector = cms.vint32(
		0, 0#, 1#, 1, 1,  ### v2 # trackcutclassifier
		#1
	    ),
	    indivShareFrac = cms.vdouble(
		#1.0, 0.16#, 0.095, 0.09, 0.09, ### v2
		##0.09
		1.0, 1.0 # trackcutclassifier
	    ),
	    makeReKeyedSeeds = cms.untracked.bool(False),
	    newQuality = cms.string('confirmed'),
	    selectedTrackQuals = cms.VInputTag(
		#cms.InputTag("initialStepSelector","initialStep"), cms.InputTag("highPtTripletStepSelector","highPtTripletStep")### v2
		cms.InputTag("hltPhase2InitialStepTrackselectionHighPurity"), cms.InputTag("hltPhase2HighPtTripletStepTrackselectionHighPurity") # trackcutclassifier
		
	    ),
	    setsToMerge = cms.VPSet(cms.PSet(
		pQual = cms.bool(True),
		tLists = cms.vint32(
		    0, 1#, 2#, 3, 4, ### v2
		    #5
		)
	    )),
	    trackAlgoPriorityOrder = cms.string('trackAlgoPriorityOrder'),
	    writeOnlyTrkQuals = cms.bool(False)
	)

	########## highpttriplet

	process.highPtTripletStepClusters.overrideTrkQuals = cms.InputTag("") # trackcutclassifier

	#online
	process.hltPhase2HighPtTripletStepTrackCutClassifier = cms.EDProducer( "TrackCutClassifier",
	    src = cms.InputTag( "highPtTripletStepTracks" ),
	    beamspot = cms.InputTag( "offlineBeamSpot" ),
	    vertices = cms.InputTag( "hltPhase2PixelVertices" ), # pixelVertices previous firstStepPrimaryVertices" ),
	    qualityCuts = cms.vdouble( -0.7, 0.1, 0.7 ),
	    mva = cms.PSet( 
	      minPixelHits = cms.vint32( 0, 0, 3 ), ##
	      maxDzWrtBS = cms.vdouble( 3.40282346639E38, 24.0, 15.0 ),
	      dr_par = cms.PSet( 
		d0err = cms.vdouble( 0.003, 0.003, 0.003 ),
		dr_par2 = cms.vdouble( 0.6, 0.5, 0.45 ), ##
		dr_par1 = cms.vdouble( 0.7, 0.6, 0.6 ), 
		dr_exp = cms.vint32( 4, 4, 4 ), 
		d0err_par = cms.vdouble( 0.002, 0.002, 0.001 )
	      ),
	      maxLostLayers = cms.vint32( 3, 3, 2 ),
	      min3DLayers = cms.vint32( 3, 3, 4 ),
	      dz_par = cms.PSet( 
		dz_par1 = cms.vdouble( 0.8, 0.7, 0.7 ),
		dz_par2 = cms.vdouble( 0.6, 0.6, 0.55 ),
		dz_exp = cms.vint32( 4, 4, 4 )
	      ),
	      minNVtxTrk = cms.int32( 3 ), ## offline 2, online 3 switching to 3
	      maxDz = cms.vdouble( 0.5, 0.2, 3.40282346639E38 ), ##
	      minNdof = cms.vdouble( 1.0E-5, 1.0E-5, 1.0E-5 ), ##
	      maxChi2 = cms.vdouble( 9999.0, 9999.0, 9999.0 ), 
	      maxChi2n = cms.vdouble( 2.0, 1.0, 0.8 ),
	      maxDr = cms.vdouble( 0.5, 0.03, 3.40282346639E38 ), ##
	      minLayers = cms.vint32( 3, 3, 4 )
	    ),
	    ignoreVertices = cms.bool( False )
	)

	#online
	process.hltPhase2HighPtTripletStepTrackselectionHighPurity = cms.EDProducer( "TrackCollectionFilterCloner",
	    minQuality = cms.string( "highPurity" ),
	    copyExtras = cms.untracked.bool( True ),
	    copyTrajectories = cms.untracked.bool( False ),
	    originalSource = cms.InputTag( "highPtTripletStepTracks" ),
	    originalQualVals = cms.InputTag( 'hltPhase2HighPtTripletStepTrackCutClassifier','QualityMasks' ),
	    originalMVAVals = cms.InputTag( 'hltPhase2HighPtTripletStepTrackCutClassifier','MVAValues' )
	)

	process.highPtTripletStepTrajectoryFilterBase.constantValueForLostHitsFractionFilter = cms.double(1.0) # previous 2.0
	process.highPtTripletStepTrajectoryFilterBase.maxCCCLostHits = cms.int32(0) # previous 9999
	process.highPtTripletStepTrajectoryFilterBase.maxLostHits = cms.int32(1) # previous 999
	process.highPtTripletStepTrajectoryFilterBase.maxLostHitsFraction = cms.double(999.0) # previous 0.1
	process.highPtTripletStepTrajectoryFilterBase.minPt = cms.double(0.9) # ptcut previous 0.2
	process.highPtTripletStepTrajectoryFilterBase.seedExtension = cms.int32(1) # previous 0 


	process.highPtTripletStepTrajectoryFilterInOut.minPt = cms.double(0.9) # ptcut previous 0.4

	process.highPtTripletStepChi2Est.MaxChi2 = cms.double(16.0) # previous 20.0
	process.highPtTripletStepChi2Est.MinPtForHitRecoveryInGluedDet = cms.double(1000000.0) # previous 1000000000000
	process.highPtTripletStepChi2Est.clusterChargeCut = cms.PSet(
		refToPSet_ = cms.string('SiStripClusterChargeCutLoose') # previous SiStripClusterChargeCutNone
	    )
	process.highPtTripletStepChi2Est.pTChargeCutThreshold = cms.double(-1) # previous 15.0

	process.highPtTripletStepTrajectoryBuilder.alwaysUseInvalidHits = cms.bool(False) # previous True
	process.highPtTripletStepTrajectoryBuilder.propagatorAlong = cms.string('PropagatorWithMaterialParabolicMf') # previous PropagatorWithMaterial
	process.highPtTripletStepTrajectoryBuilder.propagatorOpposite = cms.string('PropagatorWithMaterialParabolicMfOpposite') # previous PropagatorWithMaterialOpposite

	process.highPtTripletStepTrackCandidates.SimpleMagneticField = cms.string('ParabolicMf') # previous ''
	process.highPtTripletStepTrackCandidates.TransientInitialStateEstimatorParameters = cms.PSet(
		numberMeasurementsForFit = cms.int32(4),
		propagatorAlongTISE = cms.string('PropagatorWithMaterialParabolicMf'), # previous PropagatorWithMaterial
		propagatorOppositeTISE = cms.string('PropagatorWithMaterialParabolicMfOpposite') # previous PropagatorWithMaterialOpposite
	    )
	process.highPtTripletStepTrackCandidates.maxNSeeds = cms.uint32(100000) # previous 500000
	process.highPtTripletStepTrackCandidates.maxSeedsBeforeCleaning = cms.uint32(1000) # previous 5000
	process.highPtTripletStepTrackCandidates.useHitsSplitting = cms.bool(False) # previous True

	process.highPtTripletStepTrackingRegions.RegionPSet.ptMin = cms.double(0.9)  # ptcut previous 0.7) 

	########################  initial step

	process.initialStepSeeds.mightGet = cms.untracked.vstring('')

	#online
	process.hltPhase2InitialStepTrackCutClassifier = cms.EDProducer( "TrackCutClassifier",
	    src = cms.InputTag( "initialStepTracks" ),
	    beamspot = cms.InputTag( "offlineBeamSpot" ),
	    vertices = cms.InputTag( "hltPhase2PixelVertices" ), # pixelVertices previous firstStepPrimaryVertices" ),
	    qualityCuts = cms.vdouble( -0.7, 0.1, 0.7 ),
	    mva = cms.PSet( 
		minPixelHits = cms.vint32(0,0,3), ######
		maxDzWrtBS = cms.vdouble( 3.40282346639E38, 24.0, 15.0 ), 
		dr_par = cms.PSet( 
		  d0err = cms.vdouble( 0.003, 0.003, 0.003 ),
		  dr_par1 = cms.vdouble( 0.8, 0.7, 0.6 ),  
		  dr_par2 = cms.vdouble( 0.6, 0.5, 0.45 ), 
		  dr_exp = cms.vint32( 4, 4, 4 ),
		  d0err_par = cms.vdouble( 0.001, 0.001, 0.001 )
		),
		maxLostLayers = cms.vint32( 3, 2, 2 ),
		min3DLayers = cms.vint32( 3, 3, 3),
		dz_par = cms.PSet( 
		  dz_par1 = cms.vdouble( 0.9, 0.8, 0.7 ), 
		  dz_par2 = cms.vdouble( 0.8, 0.7, 0.55 ), 
		  dz_exp = cms.vint32( 4, 4, 4 )
		),
		minNVtxTrk = cms.int32( 3 ), # offline 2, online 3 switching to 3
		maxDz = cms.vdouble( 0.5, 0.2, 3.40282346639E38 ), ##
		minNdof = cms.vdouble( 1.0E-5, 1.0E-5, 1.0E-5 ), ##
		maxChi2 = cms.vdouble( 9999.0, 25.0, 16.0 ), 
		maxChi2n = cms.vdouble( 2.0, 1.4, 1.2), 
		maxDr = cms.vdouble( 0.5, 0.03, 3.40282346639E38 ), ##
		minLayers = cms.vint32( 3, 3, 3 ) ##
	    ),
	    ignoreVertices = cms.bool( False ) 
	)
	#online
	process.hltPhase2InitialStepTrackselectionHighPurity = cms.EDProducer( "TrackCollectionFilterCloner",
	    minQuality = cms.string( "highPurity" ),
	    copyExtras = cms.untracked.bool( True ),
	    copyTrajectories = cms.untracked.bool( False ),
	    originalSource = cms.InputTag( "initialStepTracks" ),
	    originalQualVals = cms.InputTag('hltPhase2InitialStepTrackCutClassifier','QualityMasks' ),
	    originalMVAVals = cms.InputTag('hltPhase2InitialStepTrackCutClassifier','MVAValues' )
	)

	process.initialStepChi2Est.MaxChi2 = cms.double(9.0) # previous 30.0
	process.initialStepChi2Est.MinPtForHitRecoveryInGluedDet = cms.double(1000000.0) # previous 1000000000000


	process.initialStepTrajectoryBuilder.alwaysUseInvalidHits = cms.bool(False) # previous True
	process.initialStepTrajectoryBuilder.inOutTrajectoryFilter = cms.PSet(
		refToPSet_ = cms.string('initialStepTrajectoryFilter') # previous CkfBaseTrajectoryFilter_block
	    )
	process.initialStepTrajectoryBuilder.maxCand = cms.int32(2) # previous 3
	process.initialStepTrajectoryBuilder.propagatorAlong = cms.string('PropagatorWithMaterialParabolicMf') # previous PropagatorWithMaterial
	process.initialStepTrajectoryBuilder.propagatorOpposite = cms.string('PropagatorWithMaterialParabolicMfOpposite') # previous PropagatorWithMaterialOpposite

	process.initialStepTrajectoryFilter.constantValueForLostHitsFractionFilter = cms.double(1.0) # previous 2
	process.initialStepTrajectoryFilter.maxCCCLostHits = cms.int32(0) # previous 9999
	process.initialStepTrajectoryFilter.maxLostHits = cms.int32(1) # previous 999
	process.initialStepTrajectoryFilter.maxLostHitsFraction = cms.double(999) # previous 0.1
	process.initialStepTrajectoryFilter.minPt = cms.double(0.9) # previous 0.2 # ptcut previous 0.3
	process.initialStepTrajectoryFilter.minPt = cms.double(0.9) # previous 0.2 # ptcut previous 0.3


	process.initialStepTrackCandidates.SimpleMagneticField = cms.string('ParabolicMf') # previous ''
	process.initialStepTrackCandidates.TransientInitialStateEstimatorParameters = cms.PSet(
		numberMeasurementsForFit = cms.int32(4),
		propagatorAlongTISE = cms.string('PropagatorWithMaterialParabolicMf'), # previous PropagatorWithMaterial
		propagatorOppositeTISE = cms.string('PropagatorWithMaterialParabolicMfOpposite') # previous PropagatorWithMaterialOpposite
	    )
	process.initialStepTrackCandidates.maxNSeeds = cms.uint32(100000) # previous 500000
	process.initialStepTrackCandidates.maxSeedsBeforeCleaning = cms.uint32(1000) # previous 5000
	process.initialStepTrackCandidates.useHitsSplitting = cms.bool(False) # previous True



	process.initialStepTrackingRegions.RegionPSet.ptMin = cms.double(0.9) # ptcut previous 0.6


	############# ordered setup

	process.itLocalReco = cms.Sequence(
	    process.siPhase2Clusters + 
	    process.siPixelClusters + 
	    process.siPixelClusterShapeCache + 
	    process.siPixelRecHits 
	)
	process.otLocalReco = cms.Sequence(
	    process.MeasurementTrackerEvent 
	)

	process.pixelTracksSequence = cms.Sequence(
	    process.pixelTrackFilterByKinematics + 
	    process.pixelFitterByHelixProjections +  
	    process.pixelTracksTrackingRegions +  # = hlt
	    process.pixelTracksSeedLayers +  
	    process.pixelTracksHitDoublets + 
	    process.pixelTracksHitQuadruplets + 
	    process.pixelTracks
	)

	process.hltPhase2PixelVerticesSequence = cms.Sequence( # pixelVertices
	    process.hltPhase2PixelVertices + 
	    process.hltPhase2TrimmedPixelVertices 
	)


	process.hltPhase2InitialStepPVSequence = cms.Sequence(
	    process.firstStepPrimaryVerticesUnsorted + 
	    process.initialStepTrackRefsForJets +
	    process.caloTowerForTrk + # uses hbhereco, hfreco, horeco, ecalRecHit
	    process.ak4CaloJetsForTrk +  # uses caloTowerForTrk
	    process.firstStepPrimaryVertices
	)


	process.hltPhase2InitialStepSequence = cms.Sequence(
	    process.initialStepSeedLayers + 
	    process.initialStepTrackingRegions + 
	    process.initialStepHitDoublets + 
	    process.initialStepHitQuadruplets + 
	    process.initialStepSeeds + 
	    process.initialStepTrackCandidates + 
	    process.initialStepTracks +
	    #hltPhase2InitialStepPVSequence + # use pixelVertices
	    process.hltPhase2InitialStepTrackCutClassifier + 
	    process.hltPhase2InitialStepTrackselectionHighPurity
	)

	process.hltPhase2HighPtTripletStepSequence = cms.Sequence(
	    process.highPtTripletStepClusters +
	    process.highPtTripletStepSeedLayers +
	    process.highPtTripletStepTrackingRegions +
	    process.highPtTripletStepHitDoublets +
	    process.highPtTripletStepHitTriplets +
	    process.highPtTripletStepSeeds +
	    process.highPtTripletStepTrackCandidates +
	    process.highPtTripletStepTracks +
	    process.hltPhase2HighPtTripletStepTrackCutClassifier +
	    process.hltPhase2HighPtTripletStepTrackselectionHighPurity
	)

	process.ecalUncalibRecHitSequence = cms.Sequence(
	    process.bunchSpacingProducer +
	    process.ecalMultiFitUncalibRecHit +
	    process.ecalDetIdToBeRecovered
	)

	process.caloLocalReco = cms.Sequence(
	    process.hbhereco +
	    process.hfprereco + 
	    process.hfreco + #uses hfprereco
	    process.horeco +
	    process.ecalUncalibRecHitSequence +
	    process.ecalRecHit
	)

	process.vertexReco = cms.Sequence(
	    process.hltPhase2InitialStepPVSequence + # pixelVertices moved to here, for now still keeping it
	    process.ak4CaloJetsForTrk + # uses caloTowerForTrk
	    process.unsortedOfflinePrimaryVertices +
	    process.trackWithVertexRefSelectorBeforeSorting +
	    process.trackRefsForJetsBeforeSorting +
	    process.offlinePrimaryVertices + 
	    process.offlinePrimaryVerticesWithBS +
	    process.inclusiveVertexFinder +
	    process.vertexMerger +
	    process.trackVertexArbitrator +
	    process.inclusiveSecondaryVertices
	)

	process.MC_Tracking_v6 = cms.Path(
	    process.itLocalReco +
	    process.offlineBeamSpot + #cmssw_10_6
	    process.otLocalReco +
	    #caloLocalReco +
	    process.trackerClusterCheck + 
	    process.pixelTracksSequence + # pixeltracks
	    process.hltPhase2PixelVerticesSequence + # pixelvertices
	##############################################
	    process.hltPhase2InitialStepSequence +
	    process.hltPhase2HighPtTripletStepSequence +
	##############################################
	    process.hltPhase2GeneralTracks 
	)

	process.MC_Vertexing_v6 = cms.Path(
	    process.caloLocalReco +
	    process.vertexReco
	)

	return process
