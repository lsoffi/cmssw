from PhysicsTools.SelectorUtils.centralIDRegistry import central_id_registry

import FWCore.ParameterSet.Config as cms

# Common functions and classes for ID definition are imported here:
from RecoEgamma.PhotonIdentification.Identification.cutBasedPhotonID_tools \
    import ( WorkingPoint_OOT_V1,
             IsolationCutInputsOOT,
             configureVIDCutBasedPhoID_OOT_V1,
             configureVIDCutBasedPhoID_OOT_V2,
             configureVIDCutBasedPhoID_OOT_V3,
             configureVIDCutBasedPhoID_OOT_V4)             

#
# This is the first version of Spring16 cuts for 80X samples
#
# The cut values are taken from the twiki:
#       https://twiki.cern.ch/twiki/bin/viewauth/CMS/CutBasedPhotonIdentificationRun2
#       (where they may not stay, if a newer version of cuts becomes available for these
#        conditions)
# See also the presentation explaining these working points :
#     https://indico.cern.ch/event/662751/contributions/2778043/attachments/1562017/2459674/EGamma_WorkShop_21.11.17_Debabrata.pdf

#
# First, define cut values
#

# Loose working point Barrel and Endcap
idName = "cutBasedPhotonID-Fall17-94X-OOT-V1-loose"
WP_Loose_EB = WorkingPoint_OOT_V1(
    idName    ,  # idName
    0.0185    ,  # hOverECut
    0.0125   ,  # full5x5_SigmaIEtaIEtaCut
    1.0,  #smaj
    1.0,  #smaj
    1.0,  #smaj
    1.0,  #smaj
    1.0,  #smaj
    8.5     ,  # trkIso_C1
    0.0009         ,  # trkIso_C2
    12.    ,  # HCalIso_C1
    0.0052    ,  # HCalIso_C2
    0.0052    ,  # HCalIso_C3
    8.     ,  # ECalIso_C1
    0.00092       # ECalIso_C2
    )
WP_Loose_EE = WorkingPoint_OOT_V1( #assuming now same cuts in EE since OOT are only in EB for 2017 
    idName    ,  # idName                                                                                                                                                                              
    0.0185    ,  # hOverECut                                                                                                                                                                           
    0.0125   ,  # full5x5_SigmaIEtaIEtaCut                                                                                                                                                               
    1.0, #smaj
    1.0, #smaj
    1.0, #smaj
    1.0, #smaj
    1.0, #smaj
    8.5     ,  # trkIso_C1                                                                                                                                                                               
    0.0009         ,  # trkIso_C2                                                                                                                                                            
    12.    ,  # HCalIso_C1                                            
    0.0052    ,  # HCalIso_C2                                                                                                                                                                           
    0.0052    ,  # HCalIso_C3                                                                                                                                                                           
    8.     ,  # ECalIso_C1                                                                                                                                                                              
    0.00092       # ECalIso_C2                                                                                                                                                                                                                                                
   )

# Tight working point Barrel and Endcap
idName = "cutBasedPhotonID-Fall17-94X-OOT-V1-tight"
WP_Tight_EB = WorkingPoint_OOT_V1(
    idName    ,  # idName                                                                                                                                                                               
    0.02148    ,  # hOverECut                                                                                                                                                                           
    0.00996   ,  # full5x5_SigmaIEtaIEtaCut                                                                                                                                                              
    # Isolation cuts are generally absIso < C1 + pt*C2, except for NeuHad is < C1 + pt*C2 + pt*pt*C3                                                                                                     
    #smaj<C1+(abs(eta)-0.8)*C2+C3*exp(C4*pt+C5)

    0.35,    #smaj_C1
    0.311,    #smaj_C2
    0.1465,    #smaj_C3
    -0.01775,    #smaj_C4
    1.948,    #smaj_C5
    4.0     ,  # trkIso_C1                                                                                                                                                                               
    0.0         ,  # trkIso_C2                                                                                                                                                                           
    4.    ,  # HCalIso_C1                                                                                                                                                                                
    -0.005802    ,  # HCalIso_C2                                                                                                                                                                         
    2.921e-5    ,  # HCalIso_C3                                                                                                                                                                          
    5.     ,  # ECalIso_C1                                                                                                                                                                               
    0.003008       # ECalIso_C2                                                                                                                                                                          
)

WP_Tight_EE = WorkingPoint_OOT_V1(
      
    idName    ,  # idName                                                                                                                                                                               
    0.02148    ,  # hOverECut                                                                                                                                                                           
    0.00996   ,  # full5x5_SigmaIEtaIEtaCut                                                                                                                                                              
    # Isolation cuts are generally absIso < C1 + pt*C2, except for NeuHad is < C1 + pt*C2 + pt*pt*C3                                                                                                     
    #smaj<C1+(abs(eta)-0.8)*C2+C3*exp(C4*pt+C5)

    0.35,    #smaj_C1
    0.311,    #smaj_C2
    0.1465,    #smaj_C3
    -0.01775,    #smaj_C4
    1.948,    #smaj_C5
    4.0     ,  # trkIso_C1                                                                                                                                                                               
    0.0         ,  # trkIso_C2                                                                                                                                                                           
    4.    ,  # HCalIso_C1                                                                                                                                                                                
    -0.005802    ,  # HCalIso_C2                                                                                                                                                                         
    2.921e-5    ,  # HCalIso_C3                                                                                                                                                                          
    5.     ,  # ECalIso_C1                                                                                                                                                                               
    0.003008       # ECalIso_C2                                                                                                                                                                          
)



# Tight working point Barrel and Endcap Only Isos
idName = "cutBasedPhotonID-Fall17-94X-OOT-V1-tight-OnlyIsos"
WP_Tight_OnlyIsos_EB = WorkingPoint_OOT_V1(
    idName    ,  # idName                                                                                                                                                                               
    0.02148    ,  # hOverECut                                                                                                                                                                           
    0.00996   ,  # full5x5_SigmaIEtaIEtaCut                                                                                                                                                              
    # Isolation cuts are generally absIso < C1 + pt*C2, except for NeuHad is < C1 + pt*C2 + pt*pt*C3                                                                                                     
    #smaj<C1+(abs(eta)-0.8)*C2+C3*exp(C4*pt+C5)

    0.35,    #smaj_C1
    0.311,    #smaj_C2
    0.1465,    #smaj_C3
    -0.01775,    #smaj_C4
    1.948,    #smaj_C5
    4.0     ,  # trkIso_C1                                                                                                                                                                               
    0.0         ,  # trkIso_C2                                                                                                                                                                           
    4.    ,  # HCalIso_C1                                                                                                                                                                                
    -0.005802    ,  # HCalIso_C2                                                                                                                                                                         
    2.921e-5    ,  # HCalIso_C3                                                                                                                                                                          
    5.     ,  # ECalIso_C1                                                                                                                                                                               
    0.003008       # ECalIso_C2                                                                                                                                                                          
)

WP_Tight_OnlyIsos_EE = WorkingPoint_OOT_V1(
      
    idName    ,  # idName                                                                                                                                                                               
    0.02148    ,  # hOverECut                                                                                                                                                                           
    0.00996   ,  # full5x5_SigmaIEtaIEtaCut                                                                                                                                                              
    # Isolation cuts are generally absIso < C1 + pt*C2, except for NeuHad is < C1 + pt*C2 + pt*pt*C3                                                                                                     
    #smaj<C1+(abs(eta)-0.8)*C2+C3*exp(C4*pt+C5)

    0.35,    #smaj_C1
    0.311,    #smaj_C2
    0.1465,    #smaj_C3
    -0.01775,    #smaj_C4
    1.948,    #smaj_C5
    4.0     ,  # trkIso_C1                                                                                                                                                                               
    0.0         ,  # trkIso_C2                                                                                                                                                                           
    4.    ,  # HCalIso_C1                                                                                                                                                                                
    -0.005802    ,  # HCalIso_C2                                                                                                                                                                         
    2.921e-5    ,  # HCalIso_C3                                                                                                                                                                          
    5.     ,  # ECalIso_C1                                                                                                                                                                               
    0.003008       # ECalIso_C2                                                                                                                                                                          
)



# Tight working point Barrel and Endcap NoSmaj
idName = "cutBasedPhotonID-Fall17-94X-OOT-V1-tight-NoSmaj"
WP_Tight_NoSmaj_EB = WorkingPoint_OOT_V1(
    idName    ,  # idName                                                                                                                                                                               
    0.02148    ,  # hOverECut                                                                                                                                                                           
    0.00996   ,  # full5x5_SigmaIEtaIEtaCut                                                                                                                                                              
    # Isolation cuts are generally absIso < C1 + pt*C2, except for NeuHad is < C1 + pt*C2 + pt*pt*C3                                                                                                     
    #smaj<C1+(abs(eta)-0.8)*C2+C3*exp(C4*pt+C5)

    0.35,    #smaj_C1
    0.311,    #smaj_C2
    0.1465,    #smaj_C3
    -0.01775,    #smaj_C4
    1.948,    #smaj_C5
    4.0     ,  # trkIso_C1                                                                                                                                                                               
    0.0         ,  # trkIso_C2                                                                                                                                                                           
    4.    ,  # HCalIso_C1                                                                                                                                                                                
    -0.005802    ,  # HCalIso_C2                                                                                                                                                                         
    2.921e-5    ,  # HCalIso_C3                                                                                                                                                                          
    5.     ,  # ECalIso_C1                                                                                                                                                                               
    0.003008       # ECalIso_C2                                                                                                                                                                          
)

WP_Tight_NoSmaj_EE = WorkingPoint_OOT_V1(
      
    idName    ,  # idName                                                                                                                                                                               
    0.02148    ,  # hOverECut                                                                                                                                                                           
    0.00996   ,  # full5x5_SigmaIEtaIEtaCut                                                                                                                                                              
    # Isolation cuts are generally absIso < C1 + pt*C2, except for NeuHad is < C1 + pt*C2 + pt*pt*C3                                                                                                     
    #smaj<C1+(abs(eta)-0.8)*C2+C3*exp(C4*pt+C5)

    0.35,    #smaj_C1
    0.311,    #smaj_C2
    0.1465,    #smaj_C3
    -0.01775,    #smaj_C4
    1.948,    #smaj_C5
    4.0     ,  # trkIso_C1                                                                                                                                                                               
    0.0         ,  # trkIso_C2                                                                                                                                                                           
    4.    ,  # HCalIso_C1                                                                                                                                                                                
    -0.005802    ,  # HCalIso_C2                                                                                                                                                                         
    2.921e-5    ,  # HCalIso_C3                                                                                                                                                                          
    5.     ,  # ECalIso_C1                                                                                                                                                                               
    0.003008       # ECalIso_C2                                                                                                                                                                          
)

# Tight working point Barrel and Endcap OnlySmaj
idName = "cutBasedPhotonID-Fall17-94X-OOT-V1-tight-OnlySmaj"
WP_Tight_OnlySmaj_EB = WorkingPoint_OOT_V1(
    idName    ,  # idName                                                                                                                                                                               
    0.02148    ,  # hOverECut                                                                                                                                                                           
    0.00996   ,  # full5x5_SigmaIEtaIEtaCut                                                                                                                                                              
    # Isolation cuts are generally absIso < C1 + pt*C2, except for NeuHad is < C1 + pt*C2 + pt*pt*C3                                                                                                     
    #smaj<C1+(abs(eta)-0.8)*C2+C3*exp(C4*pt+C5)

    0.35,    #smaj_C1
    0.311,    #smaj_C2
    0.1465,    #smaj_C3
    -0.01775,    #smaj_C4
    1.948,    #smaj_C5
    4.0     ,  # trkIso_C1                                                                                                                                                                               
    0.0         ,  # trkIso_C2                                                                                                                                                                           
    4.    ,  # HCalIso_C1                                                                                                                                                                                
    -0.005802    ,  # HCalIso_C2                                                                                                                                                                         
    2.921e-5    ,  # HCalIso_C3                                                                                                                                                                          
    5.     ,  # ECalIso_C1                                                                                                                                                                               
    0.003008       # ECalIso_C2                                                                                                                                                                          
)

WP_Tight_OnlySmaj_EE = WorkingPoint_OOT_V1(
      
    idName    ,  # idName                                                                                                                                                                               
    0.02148    ,  # hOverECut                                                                                                                                                                           
    0.00996   ,  # full5x5_SigmaIEtaIEtaCut                                                                                                                                                              
    # Isolation cuts are generally absIso < C1 + pt*C2, except for NeuHad is < C1 + pt*C2 + pt*pt*C3                                                                                                     
    #smaj<C1+(abs(eta)-0.8)*C2+C3*exp(C4*pt+C5)

    0.35,    #smaj_C1
    0.311,    #smaj_C2
    0.1465,    #smaj_C3
    -0.01775,    #smaj_C4
    1.948,    #smaj_C5
    4.0     ,  # trkIso_C1                                                                                                                                                                               
    0.0         ,  # trkIso_C2                                                                                                                                                                           
    4.    ,  # HCalIso_C1                                                                                                                                                                                
    -0.005802    ,  # HCalIso_C2                                                                                                                                                                         
    2.921e-5    ,  # HCalIso_C3                                                                                                                                                                          
    5.     ,  # ECalIso_C1                                                                                                                                                                               
    0.003008       # ECalIso_C2                                                                                                                                                                          
)




# Second, define where to find the precomputed isolations and what effective
# areas to use for pile-up correction
isoInputs = IsolationCutInputsOOT(
    # chHadIsolationMapName  
    'photonIDValueMapProducer:phoTrkIsolation' ,
    # chHadIsolationEffAreas 
    "RecoEgamma/PhotonIdentification/data/Fall17/effAreaPhotons_cone03_TrkIso_OOT_V1.txt",
    # neuHadIsolationMapName
    'photonIDValueMapProducer:phoHcalPFClIsolation' ,
    # neuHadIsolationEffAreas
    "RecoEgamma/PhotonIdentification/data/Fall17/effAreaPhotons_cone03_pfClusterHcalIso_OOT_V1.txt" ,
    # phoIsolationMapName  
    "photonIDValueMapProducer:phoEcalPFClIsolation" ,
    # phoIsolationEffAreas
    "RecoEgamma/PhotonIdentification/data/Fall17/effAreaPhotons_cone03_pfClusterEcalIso_OOT_V1.txt"

)

#
# Finally, set up VID configuration for all cuts
#
cutBasedPhotonID_Fall17_94X_OOT_V1_loose  = configureVIDCutBasedPhoID_OOT_V1 ( WP_Loose_EB, WP_Loose_EE, isoInputs)
cutBasedPhotonID_Fall17_94X_OOT_V1_tight  = configureVIDCutBasedPhoID_OOT_V1 ( WP_Tight_EB, WP_Tight_EE, isoInputs)
cutBasedPhotonID_Fall17_94X_OOT_V1_tight_OnlyIsos  = configureVIDCutBasedPhoID_OOT_V2 ( WP_Tight_OnlyIsos_EB, WP_Tight_OnlyIsos_EE, isoInputs)
cutBasedPhotonID_Fall17_94X_OOT_V1_tight_NoSmaj  = configureVIDCutBasedPhoID_OOT_V3 ( WP_Tight_NoSmaj_EB, WP_Tight_NoSmaj_EE, isoInputs)
cutBasedPhotonID_Fall17_94X_OOT_V1_tight_OnlySmaj  = configureVIDCutBasedPhoID_OOT_V4 ( WP_Tight_OnlySmaj_EB, WP_Tight_OnlySmaj_EE, isoInputs)

## The MD5 sum numbers below reflect the exact set of cut variables
# and values above. If anything changes, one has to 
# 1) comment out the lines below about the registry, 
# 2) run "calculateMD5 <this file name> <one of the VID config names just above>
# 3) update the MD5 sum strings below and uncomment the lines again.
#

#central_id_registry.register(cutBasedPhotonID_Fall17_94X_V1_loose.idName,
#                             '45515ee95e01fa36972ff7ba69186c97')
#central_id_registry.register(cutBasedPhotonID_Fall17_94X_V1_medium.idName,
#                             '772f7921fa146b630e4dbe79e475a421')
#central_id_registry.register(cutBasedPhotonID_Fall17_94X_V1_tight.idName,
#                             'e260fee6f9011fb13ff56d45cccd21c5')

#cutBasedPhotonID_Fall17_94X_V1_loose.isPOGApproved = cms.untracked.bool(True)
#cutBasedPhotonID_Fall17_94X_V1_medium.isPOGApproved = cms.untracked.bool(True)
#cutBasedPhotonID_Fall17_94X_V1_tight.isPOGApproved = cms.untracked.bool(True)
