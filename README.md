# CMS_HLT_Phase2_Tracking

### CMSSW_11_1_0_pre6

Release generated script with new paths plugged in
############
step3_RAW2DIGI_RECO_VALIDATION_DQM.py 

needs:
- raw2digi_step_cff.py
- MC_Tracking_v2_cff.py / v4 / v6 / v6_1 / v7_1
- MC_prevalidation_cff.py / MC_prevalidation_v6_cff.py
- MC_Dqmoffline_cff.py

### CMSSW_11_1_0_pre3

Release generated script with new paths plugged in
############
step3_RAW2DIGI_RECO_VALIDATION_DQM.py 

needs:
- raw2digi_step_cff.py
- MC_Tracking_v2_cff.py / MC_Tracking_v4_cff.py / MC_Tracking_v6_cff.py
- MC_prevalidation_cff.py / MC_prevalidation_v6_cff.py
- MC_Dqmoffline_cff.py


### CMSSW_11_0_0_pre6

Release generated script with new paths plugged in
############

step3_RAW2DIGI_RECO_VALIDATION_DQM.py 

needs:
- extras_cmssw_11_0_cff.py (extra modules needed)
- raw2digi_step_cff.py
- MC_Tracking_v0_cmssw_11_0_cff.py / MC_Tracking_v1_cmssw_11_0_cff.py / MC_Tracking_v2_cmssw_11_0_cff.py
- MC_prevalidation_v0_cff.py / MC_prevalidation_v1_cff.py / MC_prevalidation_v2_cff.py
- MC_Dqmoffline_step_v0_cff.py / MC_Dqmoffline_step_v1_cff.py / MC_Dqmoffline_step_v2_cff.py



### CMSSW_10_6_0_patch2

Version 2) Release generated script with new paths plugged in
############

step3_RAW2DIGI_RECO_VALIDATION_DQM_MC.py 

needs:
- input_TTbar_PhaseIITDRSpring19DR-NoPU_106X_upgrade2023_realistic_v3_cff.py
- input_TTbar_PhaseIITDRSpring19DR-PU200_106X_upgrade2023_realistic_v3_cff.py
- extras.py (extra modules needed)
- raw2digi_step_cff.py
- MC_Tracking_v0_cmssw_10_6_cff.py / MC_Tracking_v1_cmssw_10_6_cff.py / MC_Tracking_v2_cmssw_10_6_cff.py
- MC_prevalidation_v0_cmssw_10_6_cff.py / MC_prevalidation_v1_cmssw_10_6_cff.py / MC_prevalidation_v2_cmssw_10_6_cff.py (all cleaned)
- MC_Dqmoffline_step_v0_cff.py / MC_Dqmoffline_step_v1_cff.py / MC_Dqmoffline_step_v2_cff.py






### CMSSW_10_4_0_mtd5

Cleaned up from the release generated script
###########

step3_performance_modular.py 			#performance studies
needs:

- input_TTbar_PhaseIIMTDTDRAutumn18DR-noPU_103X_upgrade2023_realistic_v2-v1_cff.py
- input_TTbar_PhaseIIMTDTDRAutumn18DR-PU200_103X_upgrade2023_realistic_v2-v1_cff.py
- raw2digi_step_cff.py
- MC_Tracking_v0_cff.py / MC_Tracking_v1_cff.py / MC_Tracking_v2_cff.py
- MC_prevalidation_v0_cff.py / MC_prevalidation_v1_cff.py / MC_prevalidation_v2_cff.py (all cleaned)
- MC_Dqmoffline_step_v0_cff.py / MC_Dqmoffline_step_v1_cff.py / MC_Dqmoffline_step_v2_cff.py

############

step3_timing_modular.py 			#timing studies

needs:
- input_TTbar_PhaseIIMTDTDRAutumn18DR-noPU_103X_upgrade2023_realistic_v2-v1_cff.py (input sample list)
- input_TTbar_PhaseIIMTDTDRAutumn18DR-PU200_103X_upgrade2023_realistic_v2-v1_cff.py
- raw2digi_step_cff.py
- MC_Tracking_v0_cff.py / MC_Tracking_v1_cff.py / MC_Tracking_v2_cff.py





Version 2) Release generated script with new paths plugged in
############

step3_RAW2DIGI_RECO_VALIDATION_DQM.py

needs:
- input_TTbar_PhaseIIMTDTDRAutumn18DR-noPU_103X_upgrade2023_realistic_v2-v1_cff.py (input sample list) or step2.root
- input_TTbar_PhaseIIMTDTDRAutumn18DR-PU200_103X_upgrade2023_realistic_v2-v1_cff.py
- extras.py (extra modules from step3_performance_modular.py)
- raw2digi_step_cff.py
- MC_Tracking_v0_cff.py / MC_Tracking_v1_cff.py / MC_Tracking_v2_cff.py
- MC_prevalidation_v0_cff.py / MC_prevalidation_v1_cff.py / MC_prevalidation_v2_cff.py (all cleaned)
- MC_Dqmoffline_step_v0_cff.py / MC_Dqmoffline_step_v1_cff.py / MC_Dqmoffline_step_v2_cff.py
