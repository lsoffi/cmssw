 
import FWCore.ParameterSet.Config as cms

# Barrel/endcap division in eta
ebCutOff = 1.479

# ===============================================
# Define containers used by cut definitions
# ===============================================

class WorkingPoint_V1:
    """
    This is a container class to hold numerical cut values for either
    the barrel or endcap set of cuts
    """
    def __init__(self, 
                 idName,
                 hOverECut,
                 full5x5_sigmaIEtaIEtaCut,
                 # Isolation cuts are generally pt-dependent: cut = C1 + pt * C2
                 absPFChaHadIsoWithEACut_C1,
                 absPFChaHadIsoWithEACut_C2,
                 absPFNeuHadIsoWithEACut_C1,
                 absPFNeuHadIsoWithEACut_C2,
                 absPFPhoIsoWithEACut_C1,
                 absPFPhoIsoWithEACut_C2
                 ):
        self.idName    = idName
        self.hOverECut = hOverECut
        self.full5x5_sigmaIEtaIEtaCut = full5x5_sigmaIEtaIEtaCut
        self.absPFChaHadIsoWithEACut_C1  = absPFChaHadIsoWithEACut_C1 # charged hadron isolation C1
        self.absPFChaHadIsoWithEACut_C2  = absPFChaHadIsoWithEACut_C2 # ........ C2
        self.absPFNeuHadIsoWithEACut_C1  = absPFNeuHadIsoWithEACut_C1 # neutral hadron isolation C1
        self.absPFNeuHadIsoWithEACut_C2  = absPFNeuHadIsoWithEACut_C2 # ........ C2
        self.absPFPhoIsoWithEACut_C1     = absPFPhoIsoWithEACut_C1    # photon isolation C1
        self.absPFPhoIsoWithEACut_C2     = absPFPhoIsoWithEACut_C2    # ........ C2



class WorkingPoint_V2:
    """
    This is a container class to hold numerical cut values for either
    the barrel or endcap set of cuts
    This version of the container is different from the previous one
    by the fact that it contains three constants instead of two for
    the neutral hadron isolation cut, for exponantial parameterization
    """
    def __init__(self, 
                 idName,
                 hOverECut,
                 full5x5_sigmaIEtaIEtaCut,
                 # Isolation cuts are generally pt-dependent: cut = C1 + pt * C2
                 # except for the neutral hadron isolation where it is cut = C1+exp(pt*C2+C3)
                 absPFChaHadIsoWithEACut_C1,
                 absPFChaHadIsoWithEACut_C2,
                 absPFNeuHadIsoWithEACut_C1,
                 absPFNeuHadIsoWithEACut_C2,
                 absPFNeuHadIsoWithEACut_C3,
                 absPFPhoIsoWithEACut_C1,
                 absPFPhoIsoWithEACut_C2
                 ):
        self.idName    = idName
        self.hOverECut = hOverECut
        self.full5x5_sigmaIEtaIEtaCut = full5x5_sigmaIEtaIEtaCut
        self.absPFChaHadIsoWithEACut_C1  = absPFChaHadIsoWithEACut_C1 # charged hadron isolation C1
        self.absPFChaHadIsoWithEACut_C2  = absPFChaHadIsoWithEACut_C2 # ........ C2
        self.absPFNeuHadIsoWithEACut_C1  = absPFNeuHadIsoWithEACut_C1 # neutral hadron isolation C1
        self.absPFNeuHadIsoWithEACut_C2  = absPFNeuHadIsoWithEACut_C2 # ........ C2
        self.absPFNeuHadIsoWithEACut_C3  = absPFNeuHadIsoWithEACut_C3 # ........ C3
        self.absPFPhoIsoWithEACut_C1     = absPFPhoIsoWithEACut_C1    # photon isolation C1
        self.absPFPhoIsoWithEACut_C2     = absPFPhoIsoWithEACut_C2    # ........ C2

class WorkingPoint_HPT_V1:
    """
    This is a container class to hold numerical cut values for either
    the barrel or endcap set of cuts
    This version of the container is different from the previous one
    by the fact that it contains three constants instead of two for
    the neutral hadron isolation cut, for exponantial parameterization
    """
    def __init__(self, 
                 idName,
                 r9Cut,
                 hOverECut,
                 full5x5_sigmaIEtaIEtaCut,
                 # Isolation cuts are generally pt-dependent: cut = C1 + pt * C2
                 # except for the neutral hadron isolation where it is cut = C1+exp(pt*C2+C3)
                 absPFChaHadIsoWithEACut_C1,
                 absPFChaHadIsoWithEACut_C2,
                 absPFNeuHadIsoWithEACut_C1,
                 absPFNeuHadIsoWithEACut_C2,
                 absPFNeuHadIsoWithEACut_C3,
                 absPFPhoIsoWithEACut_C1,
                 absPFPhoIsoWithEACut_C2
                 ):
        self.idName    = idName
        self.r9Cut=r9Cut
        self.hOverECut = hOverECut
        self.full5x5_sigmaIEtaIEtaCut = full5x5_sigmaIEtaIEtaCut
        self.absPFChaHadIsoWithEACut_C1  = absPFChaHadIsoWithEACut_C1 # charged hadron isolation C1
        self.absPFChaHadIsoWithEACut_C2  = absPFChaHadIsoWithEACut_C2 # ........ C2
        self.absPFNeuHadIsoWithEACut_C1  = absPFNeuHadIsoWithEACut_C1 # neutral hadron isolation C1
        self.absPFNeuHadIsoWithEACut_C2  = absPFNeuHadIsoWithEACut_C2 # ........ C2
        self.absPFNeuHadIsoWithEACut_C3  = absPFNeuHadIsoWithEACut_C3 # ........ C3
        self.absPFPhoIsoWithEACut_C1     = absPFPhoIsoWithEACut_C1    # photon isolation C1
        self.absPFPhoIsoWithEACut_C2     = absPFPhoIsoWithEACut_C2    # ........ C2

class WorkingPoint_OOT_V1:
    """
    This is a container class to hold numerical cut values for either
    the barrel or endcap set of cuts
    This version of the container is different from the previous one
    by the fact that it contains three constants instead of two for
    the neutral hadron isolation cut, for exponantial parameterization
    """
    def __init__(self, 
                 idName,
                 hOverECut,
                 full5x5_sigmaIEtaIEtaCut,
                 smajCut_C1,
                 smajCut_C2,
                 smajCut_C3,
                 smajCut_C4,
                 smajCut_C5,
                 # Isolation cuts are generally pt-dependent: cut = C1 + pt * C2
                 # except for the neutral hadron isolation where it is cut = C1+exp(pt*C2+C3)
                 absTrkIsoWithEACut_C1,
                 absTrkIsoWithEACut_C2,
                 absPFClusterHCalIsoWithEACut_C1,
                 absPFClusterHCalIsoWithEACut_C2,
                 absPFClusterHCalIsoWithEACut_C3,
                 absPFClusterECalIsoWithEACut_C1,
                 absPFClusterECalIsoWithEACut_C2,
                 ):
        self.idName    = idName
        self.hOverECut = hOverECut
        self.full5x5_sigmaIEtaIEtaCut = full5x5_sigmaIEtaIEtaCut
        self.smajCut_C1 = smajCut_C1
        self.smajCut_C2 = smajCut_C2
        self.smajCut_C3 = smajCut_C3
        self.smajCut_C4 = smajCut_C4
        self.smajCut_C5 = smajCut_C5
        self.absTrkIsoWithEACut_C1  = absTrkIsoWithEACut_C1# trk isolation C1
        self.absTrkIsoWithEACut_C2  = absTrkIsoWithEACut_C2 # ........ C2
             
        self.absPFClusterHCalIsoWithEACut_C1  = absPFClusterHCalIsoWithEACut_C1 # pf cluster hcal isolation C1
        self.absPFClusterHCalIsoWithEACut_C2  = absPFClusterHCalIsoWithEACut_C2 # ........ C2
        self.absPFClusterHCalIsoWithEACut_C3  = absPFClusterHCalIsoWithEACut_C3 # ........ C3
        self.absPFClusterECalIsoWithEACut_C1  = absPFClusterECalIsoWithEACut_C1 # pf cluster ecal isolation C1
        self.absPFClusterECalIsoWithEACut_C2  = absPFClusterECalIsoWithEACut_C2 # ........ C2


class WorkingPoint_OOT_V2:
    """
    This is a container class to hold numerical cut values for either
    the barrel or endcap set of cuts
    This version of the container is different from the previous one
    by the fact that it contains three constants instead of two for
    the neutral hadron isolation cut, for exponantial parameterization
    """
    def __init__(self, 
                 idName,
                 hOverECut,
                 full5x5_sigmaIEtaIEtaCut,
                 smajCut_C1,
                 # Isolation cuts are generally pt-dependent: cut = C1 + pt * C2
                 # except for the neutral hadron isolation where it is cut = C1+exp(pt*C2+C3)
                 absTrkIsoWithEACut_C1,
                 absTrkIsoWithEACut_C2,
                 absPFClusterHCalIsoWithEACut_C1,
                 absPFClusterHCalIsoWithEACut_C2,
                 absPFClusterHCalIsoWithEACut_C3,
                 absPFClusterECalIsoWithEACut_C1,
                 absPFClusterECalIsoWithEACut_C2,
                 ):
        self.idName    = idName
        self.hOverECut = hOverECut
        self.full5x5_sigmaIEtaIEtaCut = full5x5_sigmaIEtaIEtaCut
        self.smajCut = smajCut_C1
        self.absTrkIsoWithEACut_C1  = absTrkIsoWithEACut_C1# trk isolation C1
        self.absTrkIsoWithEACut_C2  = absTrkIsoWithEACut_C2 # ........ C2
             
        self.absPFClusterHCalIsoWithEACut_C1  = absPFClusterHCalIsoWithEACut_C1 # pf cluster hcal isolation C1
        self.absPFClusterHCalIsoWithEACut_C2  = absPFClusterHCalIsoWithEACut_C2 # ........ C2
        self.absPFClusterHCalIsoWithEACut_C3  = absPFClusterHCalIsoWithEACut_C3 # ........ C3
        self.absPFClusterECalIsoWithEACut_C1  = absPFClusterECalIsoWithEACut_C1 # pf cluster ecal isolation C1
        self.absPFClusterECalIsoWithEACut_C2  = absPFClusterECalIsoWithEACut_C2 # ........ C2


class WorkingPoint_OOT_V3:
    """
    This is a container class to hold numerical cut values for either
    the barrel or endcap set of cuts
    This version of the container is different from the previous one
    by the fact that it contains three constants instead of two for
    the neutral hadron isolation cut, for exponantial parameterization
    """
    def __init__(self, 
                 idName,
                 hOverECut,
                 full5x5_sigmaIEtaIEtaCut,
                 smajCut_C1,
                 # Isolation cuts are generally pt-dependent: cut = C1 + pt * C2
                 # except for the neutral hadron isolation where it is cut = C1+exp(pt*C2+C3)
                 absPFChaHadIsoWithEACut_C1,
                 absPFChaHadIsoWithEACut_C2,
                 absPFNeuHadIsoWithEACut_C1,
                 absPFNeuHadIsoWithEACut_C2,
                 absPFNeuHadIsoWithEACut_C3,
                 absPFPhoIsoWithEACut_C1,
                 absPFPhoIsoWithEACut_C2
                 ):
        self.idName    = idName
        self.hOverECut = hOverECut
        self.full5x5_sigmaIEtaIEtaCut = full5x5_sigmaIEtaIEtaCut
        self.smajCut = smajCut_C1
        self.absPFChaHadIsoWithEACut_C1  = absPFChaHadIsoWithEACut_C1 # charged hadron isolation C1
        self.absPFChaHadIsoWithEACut_C2  = absPFChaHadIsoWithEACut_C2 # ........ C2
        self.absPFNeuHadIsoWithEACut_C1  = absPFNeuHadIsoWithEACut_C1 # neutral hadron isolation C1
        self.absPFNeuHadIsoWithEACut_C2  = absPFNeuHadIsoWithEACut_C2 # ........ C2
        self.absPFNeuHadIsoWithEACut_C3  = absPFNeuHadIsoWithEACut_C3 # ........ C3
        self.absPFPhoIsoWithEACut_C1     = absPFPhoIsoWithEACut_C1    # photon isolation C1
        self.absPFPhoIsoWithEACut_C2     = absPFPhoIsoWithEACut_C2    # ........ C2


class WorkingPoint_OOT_V4:
    """
    This is a container class to hold numerical cut values for either
    the barrel or endcap set of cuts
    This version of the container is different from the previous one
    by the fact that it contains three constants instead of two for
    the neutral hadron isolation cut, for exponantial parameterization
    """
    def __init__(self, 
                 idName,
                 hOverECut,
                 full5x5_sigmaIEtaIEtaCut,
                 smajCut_C1,
                 sminCut_C1,
                 # Isolation cuts are generally pt-dependent: cut = C1 + pt * C2
                 # except for the neutral hadron isolation where it is cut = C1+exp(pt*C2+C3)
                 absTrkIsoWithEACut_C1,
                 absTrkIsoWithEACut_C2,
                 absPFClusterHCalIsoWithEACut_C1,
                 absPFClusterHCalIsoWithEACut_C2,
                 absPFClusterHCalIsoWithEACut_C3,
                 absPFClusterECalIsoWithEACut_C1,
                 absPFClusterECalIsoWithEACut_C2,
                 ):
        self.idName    = idName
        self.hOverECut = hOverECut
        self.full5x5_sigmaIEtaIEtaCut = full5x5_sigmaIEtaIEtaCut
        self.smajCut = smajCut_C1
        self.sminCut = sminCut_C1
        self.absTrkIsoWithEACut_C1  = absTrkIsoWithEACut_C1# trk isolation C1
        self.absTrkIsoWithEACut_C2  = absTrkIsoWithEACut_C2 # ........ C2
             
        self.absPFClusterHCalIsoWithEACut_C1  = absPFClusterHCalIsoWithEACut_C1 # pf cluster hcal isolation C1
        self.absPFClusterHCalIsoWithEACut_C2  = absPFClusterHCalIsoWithEACut_C2 # ........ C2
        self.absPFClusterHCalIsoWithEACut_C3  = absPFClusterHCalIsoWithEACut_C3 # ........ C3
        self.absPFClusterECalIsoWithEACut_C1  = absPFClusterECalIsoWithEACut_C1 # pf cluster ecal isolation C1
        self.absPFClusterECalIsoWithEACut_C2  = absPFClusterECalIsoWithEACut_C2 # ........ C2


class WorkingPoint_OOT_V5:
    """
    This is a container class to hold numerical cut values for either
    the barrel or endcap set of cuts
    This version of the container is different from the previous one
    by the fact that it contains three constants instead of two for
    the neutral hadron isolation cut, for exponantial parameterization
    """
    def __init__(self, 
                 idName,
                 hOverECut,
                 full5x5_sigmaIEtaIEtaCut,
                 smajCut_C1,
                 sminCut_C1,
                 # Isolation cuts are generally pt-dependent: cut = C1 + pt * C2
                 # except for the neutral hadron isolation where it is cut = C1+exp(pt*C2+C3)
                 absPFChaHadIsoWithEACut_C1,
                 absPFChaHadIsoWithEACut_C2,
                 absPFNeuHadIsoWithEACut_C1,
                 absPFNeuHadIsoWithEACut_C2,
                 absPFNeuHadIsoWithEACut_C3,
                 absPFPhoIsoWithEACut_C1,
                 absPFPhoIsoWithEACut_C2
                 ):
        self.idName    = idName
        self.hOverECut = hOverECut
        self.full5x5_sigmaIEtaIEtaCut = full5x5_sigmaIEtaIEtaCut
        self.smajCut = smajCut_C1
        self.sminCut = sminCut_C1
        self.absPFChaHadIsoWithEACut_C1  = absPFChaHadIsoWithEACut_C1 # charged hadron isolation C1
        self.absPFChaHadIsoWithEACut_C2  = absPFChaHadIsoWithEACut_C2 # ........ C2
        self.absPFNeuHadIsoWithEACut_C1  = absPFNeuHadIsoWithEACut_C1 # neutral hadron isolation C1
        self.absPFNeuHadIsoWithEACut_C2  = absPFNeuHadIsoWithEACut_C2 # ........ C2
        self.absPFNeuHadIsoWithEACut_C3  = absPFNeuHadIsoWithEACut_C3 # ........ C3
        self.absPFPhoIsoWithEACut_C1     = absPFPhoIsoWithEACut_C1    # photon isolation C1
        self.absPFPhoIsoWithEACut_C2     = absPFPhoIsoWithEACut_C2    # ........ C2


class IsolationCutInputs:
    """
    A container class that holds the names of the isolation maps in the event record
    and the names of the files with the effective area constants for pile-up corrections
    """
    def __init__(self, 
                 chHadIsolationMapName,
                 chHadIsolationEffAreas,
                 neuHadIsolationMapName,
                 neuHadIsolationEffAreas,
                 phoIsolationMapName,
                 phoIsolationEffAreas
                 ):
                 self.chHadIsolationMapName   = chHadIsolationMapName    
                 self.chHadIsolationEffAreas  = chHadIsolationEffAreas  
                 self.neuHadIsolationMapName  = neuHadIsolationMapName  
                 self.neuHadIsolationEffAreas = neuHadIsolationEffAreas 
                 self.phoIsolationMapName     = phoIsolationMapName     
                 self.phoIsolationEffAreas    = phoIsolationEffAreas    


class IsolationCutInputsOOT:
    """
    A container class that holds the names of the isolation maps in the event record
    and the names of the files with the effective area constants for pile-up corrections
    """
    def __init__(self, 
                 TrkIsolationMapName,
                 TrkIsolationEffAreas,
                 PFClusterHCalIsolationMapName,
                 PFClusterHCalIsolationEffAreas,
                 PFClusterECalIsolationMapName,
                 PFClusterECalIsolationEffAreas
                  ):
                 self.TrkIsolationMapName   = TrkIsolationMapName    
                 self.TrkIsolationEffAreas  = TrkIsolationEffAreas  
                 self.PFClusterHCalIsolationMapName  = PFClusterHCalIsolationMapName  
                 self.PFClusterHCalIsolationEffAreas = PFClusterHCalIsolationEffAreas 
                 self.PFClusterECalIsolationMapName     = PFClusterECalIsolationMapName     
                 self.PFClusterECalIsolationEffAreas    = PFClusterECalIsolationEffAreas    


# ==============================================================
# Define individual cut configurations used by complete cut sets
# ==============================================================

# The mininum pt cut is set to 5 GeV
def psetMinPtCut():
    return cms.PSet( 
        cutName = cms.string("MinPtCut"),
        minPt = cms.double(5.0),
        needsAdditionalProducts = cms.bool(False),
        isIgnored = cms.bool(False) 
        )

# Take all particles in the eta ranges 0-ebCutOff and ebCutOff-2.5
def psetPhoSCEtaMultiRangeCut():
    return cms.PSet( 
        cutName = cms.string("PhoSCEtaMultiRangeCut"),
        useAbsEta = cms.bool(True),
        allowedEtaRanges = cms.VPSet( 
            cms.PSet( minEta = cms.double(0.0), 
                      maxEta = cms.double(ebCutOff) ),
            cms.PSet( minEta = cms.double(ebCutOff), 
                      maxEta = cms.double(2.5) )
            ),
        needsAdditionalProducts = cms.bool(False),
        isIgnored = cms.bool(False)
        )

# Configure the cut on the single tower H/E
def psetPhoSingleTowerHadOverEmCut( wpEB, wpEE):
    """
    Arguments: two containers of working point cut values of the type WorkingPoint_*
    """
    return cms.PSet( 
        cutName = cms.string('PhoSingleTowerHadOverEmCut'),
        hadronicOverEMCutValueEB = cms.double( wpEB.hOverECut ),
        hadronicOverEMCutValueEE = cms.double( wpEE.hOverECut ),
        barrelCutOff = cms.double(ebCutOff),
        needsAdditionalProducts = cms.bool(False),
        isIgnored = cms.bool(False)
        )

# Configure the cut on full5x5 sigmaIEtaIEta that uses a ValueMap,
# relying on an upstream producer that creates it. This was necessary
# for photons up to 7.2.0.
def psetPhoFull5x5SigmaIEtaIEtaValueMapCut(wpEB, wpEE):
    """
    Arguments: two containers of working point cut values of the type WorkingPoint_*
    """
    return cms.PSet( 
        cutName = cms.string('PhoFull5x5SigmaIEtaIEtaValueMapCut'),
        cutValueEB = cms.double( wpEB.full5x5_sigmaIEtaIEtaCut ),
        cutValueEE = cms.double( wpEE.full5x5_sigmaIEtaIEtaCut ),
        full5x5SigmaIEtaIEtaMap = cms.InputTag('photonIDValueMapProducer:phoFull5x5SigmaIEtaIEta'),
        barrelCutOff = cms.double(ebCutOff),
        needsAdditionalProducts = cms.bool(True),
        isIgnored = cms.bool(False)
        )



# Configure the cut on R9,
# relying on an upstream producer that creates it. This was necessary
# for photons up to 7.2.0.
def psetPhoR9Cut(wpEB, wpEE):
    """
    Arguments: two containers of working point cut values of the type WorkingPoint_*
    """
    return cms.PSet( 
        cutName = cms.string('PhoR9Cut'),
        cutValueEB = cms.double( wpEB.r9Cut ),
        cutValueEE = cms.double( wpEE.r9Cut ),
        barrelCutOff = cms.double(ebCutOff),
        needsAdditionalProducts = cms.bool(False),
        isIgnored = cms.bool(False)
        )

# Configure the cut on full5x5 sigmaIEtaIEta that uses the native Photon field
# with this variable (works for releases past 7.2.0).
def psetPhoFull5x5SigmaIEtaIEtaCut(wpEB, wpEE):
    """
    Arguments: two containers of working point cut values of the type WorkingPoint_*
    """
    return cms.PSet( 
        cutName = cms.string('PhoFull5x5SigmaIEtaIEtaCut'),
        cutValueEB = cms.double( wpEB.full5x5_sigmaIEtaIEtaCut ),
        cutValueEE = cms.double( wpEE.full5x5_sigmaIEtaIEtaCut ),
        full5x5SigmaIEtaIEtaMap = cms.InputTag('photonIDValueMapProducer:phoFull5x5SigmaIEtaIEta'),
        barrelCutOff = cms.double(ebCutOff),
        needsAdditionalProducts = cms.bool(False),
        isIgnored = cms.bool(False)
        )
#Configure Cut on Smaj
def psetPhoSMajCut(wpEB, wpEE,isoInputs):

    return cms.PSet( 
        cutName = cms.string('PhoSMajCut'), 
        # Both barrel and endcap: cut = c1 + pt*c2
        C1_EB = cms.double( wpEB.smajCut ),
        C2_EB = cms.double( wpEB.smajCut ),
        C1_EE = cms.double( wpEE.smajCut ),
        C2_EE = cms.double( wpEE.smajCut ),
        sMajMap = cms.InputTag( 'photonIDValueMapProducer:phoSmaj'),#isoInputs.PFClusterECalIsolationMapName ),
        barrelCutOff = cms.double(ebCutOff),
        useRelativeIso = cms.bool(False),
        needsAdditionalProducts = cms.bool(True),
        isIgnored = cms.bool(False),
        )
#Configure Cut on Sminf
def psetPhoSMinCut(wpEB, wpEE,isoInputs):

    return cms.PSet( 
        cutName = cms.string('PhoSMinCut'), 
        # Both barrel and endcap: cut = c1 + pt*c2
        C1_EB = cms.double( wpEB.sminCut ),
        C2_EB = cms.double( wpEB.sminCut ),
        C1_EE = cms.double( wpEE.sminCut ),
        C2_EE = cms.double( wpEE.sminCut ),
        sMinMap = cms.InputTag( 'photonIDValueMapProducer:phoSmin'),#isoInputs.PFClusterECalIsolationMapName ),
        barrelCutOff = cms.double(ebCutOff),
        useRelativeIso = cms.bool(False),
        needsAdditionalProducts = cms.bool(True),
        isIgnored = cms.bool(False),
        )

#Configure Cut on Smaj
def psetPhoSMajWithScalingCut(wpEB, wpEE,isoInputs):

    return cms.PSet( 
        cutName = cms.string('PhoSMajWithScalingCut'), 
        # Both barrel and endcap: cut = c1 + pt*c2
        C1_EB = cms.double( wpEB.smajCut_C1 ),
        C2_EB = cms.double( wpEB.smajCut_C2 ),
        C3_EB = cms.double( wpEB.smajCut_C3 ),
        C4_EB = cms.double( wpEB.smajCut_C4 ),
        C5_EB = cms.double( wpEB.smajCut_C5 ),
        C1_EE = cms.double( wpEE.smajCut_C1 ),
        C2_EE = cms.double( wpEE.smajCut_C2 ),
        C3_EE = cms.double( wpEE.smajCut_C3 ),
        C4_EE = cms.double( wpEE.smajCut_C4 ),
        C5_EE = cms.double( wpEE.smajCut_C5 ),
        sMajMap = cms.InputTag( 'photonIDValueMapProducer:phoSmaj'),#isoInputs.PFClusterECalIsolationMapName ),
        barrelCutOff = cms.double(ebCutOff),
        useRelativeIso = cms.bool(False),
        needsAdditionalProducts = cms.bool(True),
        isIgnored = cms.bool(False),
        )

# Configure the cut on the charged hadron isolation that uses
# the linear pt scaling for barrel and endcap
def psetChHadIsoWithEALinScalingCut(wpEB, wpEE, isoInputs):
    """
    Arguments: two containers of working point cut values of the type WorkingPoint_*
    The third argument contains data for isolation calculation.
    """
    return cms.PSet( 
        cutName = cms.string('PhoAnyPFIsoWithEACut'), 
        # Both barrel and endcap: cut = c1 + pt*c2
        C1_EB = cms.double( wpEB.absPFChaHadIsoWithEACut_C1 ),
        C2_EB = cms.double( wpEB.absPFChaHadIsoWithEACut_C2 ),
        C1_EE = cms.double( wpEE.absPFChaHadIsoWithEACut_C1 ),
        C2_EE = cms.double( wpEE.absPFChaHadIsoWithEACut_C2 ),
        anyPFIsoMap = cms.InputTag( isoInputs.chHadIsolationMapName ),
        barrelCutOff = cms.double(ebCutOff),
        useRelativeIso = cms.bool(False),
        needsAdditionalProducts = cms.bool(True),
        isIgnored = cms.bool(False),
        rho = cms.InputTag("fixedGridRhoFastjetAll"),
        effAreasConfigFile = cms.FileInPath( isoInputs.chHadIsolationEffAreas ) 
        )

# Configure the cut on the neutral hadron isolation that uses
# the linear pt scaling for barrel and endcap
def psetNeuHadIsoWithEALinScalingCut( wpEB, wpEE, isoInputs):
    """
    Arguments: two containers of working point cut values of the type WorkingPoint_*
    The third argument contains data for isolation calculation.
    """
    return cms.PSet( 
        cutName = cms.string('PhoAnyPFIsoWithEACut'), # Neutral hadrons isolation block
        # Both barrel and endcap: cut = c1 + pt*c2
        C1_EB = cms.double( wpEB.absPFNeuHadIsoWithEACut_C1 ),
        C2_EB = cms.double( wpEB.absPFNeuHadIsoWithEACut_C2 ),
        C1_EE = cms.double( wpEE.absPFNeuHadIsoWithEACut_C1 ),
        C2_EE = cms.double( wpEE.absPFNeuHadIsoWithEACut_C2 ),
        anyPFIsoMap = cms.InputTag( isoInputs.neuHadIsolationMapName ),
        barrelCutOff = cms.double(ebCutOff),
        useRelativeIso = cms.bool(False),
        needsAdditionalProducts = cms.bool(True),
        isIgnored = cms.bool(False),
        rho = cms.InputTag("fixedGridRhoFastjetAll"),
        effAreasConfigFile = cms.FileInPath( isoInputs.neuHadIsolationEffAreas ) 
        )

# Configure the cut on the neutral hadron isolation that uses
# the exponential pt scaling for barrel and the linear pt scaling for endcap
def psetNeuHadIsoWithEAExpoScalingEBCut(wpEB, wpEE, isoInputs):
    """
    Arguments: two containers of working point cut values of the type WorkingPoint_*
    The third argument contains data for isolation calculation.
    """
    return cms.PSet( 
        cutName = cms.string('PhoAnyPFIsoWithEAAndExpoScalingEBCut'), # Neutral hadrons isolation block
        # Barrel: cut = c1 + expo(pt*c2+c3)
        C1_EB = cms.double( wpEB.absPFNeuHadIsoWithEACut_C1 ),
        C2_EB = cms.double( wpEB.absPFNeuHadIsoWithEACut_C2 ),
        C3_EB = cms.double( wpEB.absPFNeuHadIsoWithEACut_C3 ),
        # Endcap: cut = c1 + pt*c2
        C1_EE = cms.double( wpEE.absPFNeuHadIsoWithEACut_C1 ),
        C2_EE = cms.double( wpEE.absPFNeuHadIsoWithEACut_C2 ),
        anyPFIsoMap = cms.InputTag( isoInputs.neuHadIsolationMapName ),
        barrelCutOff = cms.double(ebCutOff),
        useRelativeIso = cms.bool(False),
        needsAdditionalProducts = cms.bool(True),
        isIgnored = cms.bool(False),
        rho = cms.InputTag("fixedGridRhoFastjetAll"),
        effAreasConfigFile = cms.FileInPath( isoInputs.neuHadIsolationEffAreas ) 
        )

# Configure the cut on the neutral hadron isolation that uses
# the exponential pt scaling for both barrel and endcap
def psetNeuHadIsoWithEAExpoScalingCut(wpEB, wpEE, isoInputs):
    """
    Arguments: two containers of working point cut values of the type WorkingPoint_*
    The third argument contains data for isolation calculation.
    """
    return cms.PSet( 
        cutName = cms.string('PhoAnyPFIsoWithEAAndExpoScalingCut'), # Neutral hadrons isolation block
        # Barrel: cut = c1 + expo(pt*c2+c3)
        C1_EB = cms.double( wpEB.absPFNeuHadIsoWithEACut_C1 ),
        C2_EB = cms.double( wpEB.absPFNeuHadIsoWithEACut_C2 ),
        C3_EB = cms.double( wpEB.absPFNeuHadIsoWithEACut_C3 ),
        # Endcap: cut = cut = c1 + expo(pt*c2+c3)
        C1_EE = cms.double( wpEE.absPFNeuHadIsoWithEACut_C1 ),
        C2_EE = cms.double( wpEE.absPFNeuHadIsoWithEACut_C2 ),
        C3_EE = cms.double( wpEE.absPFNeuHadIsoWithEACut_C3 ),
        anyPFIsoMap = cms.InputTag( isoInputs.neuHadIsolationMapName ),
        barrelCutOff = cms.double(ebCutOff),
        useRelativeIso = cms.bool(False),
        needsAdditionalProducts = cms.bool(True),
        isIgnored = cms.bool(False),
        rho = cms.InputTag("fixedGridRhoFastjetAll"),
        effAreasConfigFile = cms.FileInPath( isoInputs.neuHadIsolationEffAreas ) 
        )

# Configure the cut on the neutral hadron isolation that uses
# the quadratic polynomial pt scaling for both barrel and endcap
def psetNeuHadIsoWithEAQuadScalingCut(wpEB, wpEE, isoInputs):
    """
    Arguments: two containers of working point cut values of the type WorkingPoint_*
    The third argument contains data for isolation calculation.
    """
    return cms.PSet( 
        cutName = cms.string('PhoAnyPFIsoWithEAAndQuadScalingCut'), # Neutral hadrons isolation block
        # Barrel: cut = c1 + pt*c2 + pt*pt*c3
        C1_EB = cms.double( wpEB.absPFNeuHadIsoWithEACut_C1 ),
        C2_EB = cms.double( wpEB.absPFNeuHadIsoWithEACut_C2 ),
        C3_EB = cms.double( wpEB.absPFNeuHadIsoWithEACut_C3 ),
        # Endcap: cut = cut = c1 + pt*c2 + pt*pt*c3
        C1_EE = cms.double( wpEE.absPFNeuHadIsoWithEACut_C1 ),
        C2_EE = cms.double( wpEE.absPFNeuHadIsoWithEACut_C2 ),
        C3_EE = cms.double( wpEE.absPFNeuHadIsoWithEACut_C3 ),
        anyPFIsoMap = cms.InputTag( isoInputs.neuHadIsolationMapName ),
        barrelCutOff = cms.double(ebCutOff),
        useRelativeIso = cms.bool(False),
        needsAdditionalProducts = cms.bool(True),
        isIgnored = cms.bool(False),
        rho = cms.InputTag("fixedGridRhoFastjetAll"),
        effAreasConfigFile = cms.FileInPath( isoInputs.neuHadIsolationEffAreas ) 
         )

# Configure the cut on the photon isolation that uses
# the linear pt scaling for barrel and endcap
def psetPhoIsoWithEALinScalingCut(wpEB, wpEE, isoInputs):
    """
    Arguments: two containers of working point cut values of the type WorkingPoint_*
    The third argument contains data for isolation calculation.
    """
    return cms.PSet( 
        cutName = cms.string('PhoAnyPFIsoWithEACut'), # Photons isolation block
        # Both barrel and endcap: cut = c1 + pt*c2
        C1_EB = cms.double( wpEB.absPFPhoIsoWithEACut_C1 ),
        C2_EB = cms.double( wpEB.absPFPhoIsoWithEACut_C2 ),
        C1_EE = cms.double( wpEE.absPFPhoIsoWithEACut_C1 ),
        C2_EE = cms.double( wpEE.absPFPhoIsoWithEACut_C2 ),
        anyPFIsoMap = cms.InputTag( isoInputs.phoIsolationMapName ),
        barrelCutOff = cms.double(ebCutOff),
        useRelativeIso = cms.bool(False),
        needsAdditionalProducts = cms.bool(True),
        isIgnored = cms.bool(False),
        rho = cms.InputTag("fixedGridRhoFastjetAll"),
        effAreasConfigFile = cms.FileInPath( isoInputs.phoIsolationEffAreas ) 
        )

#==============================================================
# PFCluster Isolations relevant for OOT
#==============================================================

# Configure the cut on the PFClusterECal isolation that uses
# the linear pt scaling for barrel and endcap
def psetPFClusterECalIsoWithEALinScalingCut(wpEB, wpEE, isoInputs):
    """
    Arguments: two containers of working point cut values of the type WorkingPoint_*
    The third argument contains data for isolation calculation.
    """
    return cms.PSet( 
        cutName = cms.string('PhoAnyPFIsoWithEACut'), # Photons isolation block
        # Both barrel and endcap: cut = c1 + pt*c2
        C1_EB = cms.double( wpEB.absPFClusterECalIsoWithEACut_C1 ),
        C2_EB = cms.double( wpEB.absPFClusterECalIsoWithEACut_C2 ),
        C1_EE = cms.double( wpEE.absPFClusterECalIsoWithEACut_C1 ),
        C2_EE = cms.double( wpEE.absPFClusterECalIsoWithEACut_C2 ),
        anyPFIsoMap = cms.InputTag( isoInputs.PFClusterECalIsolationMapName ),
        barrelCutOff = cms.double(ebCutOff),
        useRelativeIso = cms.bool(False),
        needsAdditionalProducts = cms.bool(True),
        isIgnored = cms.bool(False),
        rho = cms.InputTag("fixedGridRhoFastjetAll"),
        effAreasConfigFile = cms.FileInPath( isoInputs.PFClusterECalIsolationEffAreas ) 
        )

# Configure the cut on the PFClusterHCal isolation that uses
# the linear pt scaling for barrel and endcap
def psetPFClusterHCalIsoWithEALinScalingCut(wpEB, wpEE, isoInputs):
    """
    Arguments: two containers of working point cut values of the type WorkingPoint_*
    The third argument contains data for isolation calculation.
    """
    return cms.PSet( 
        cutName = cms.string('PhoAnyPFIsoWithEACut'), # Photons isolation block
        # Both barrel and endcap: cut = c1 + pt*c2
        C1_EB = cms.double( wpEB.absPFClusterHCalIsoWithEACut_C1 ),
        C2_EB = cms.double( wpEB.absPFClusterHCalIsoWithEACut_C2 ),
        C1_EE = cms.double( wpEE.absPFClusterHCalIsoWithEACut_C1 ),
        C2_EE = cms.double( wpEE.absPFClusterHCalIsoWithEACut_C2 ),
        anyPFIsoMap = cms.InputTag( isoInputs.PFClusterHCalIsolationMapName ),
        barrelCutOff = cms.double(ebCutOff),
        useRelativeIso = cms.bool(False),
        needsAdditionalProducts = cms.bool(True),
        isIgnored = cms.bool(False),
        rho = cms.InputTag("fixedGridRhoFastjetAll"),
        effAreasConfigFile = cms.FileInPath( isoInputs.PFClusterHCalIsolationEffAreas ) 
        )

def psetPFClusterHCalIsoEAQuadScalingCut(wpEB, wpEE, isoInputs):
    """                                                                                                   
    Arguments: two containers of working point cut values of the type WorkingPoint_*                     
    The third argument contains data for isolation calculation.                                          
    """

    return cms.PSet(
        cutName = cms.string('PhoAnyPFIsoWithEAAndQuadScalingCut'), # Neutral hadrons isolation block    
        # Barrel: cut = c1 + pt*c2 + pt*pt*c3                                                             
        C1_EB = cms.double( wpEB.absPFClusterHCalIsoWithEACut_C1 ),
        C2_EB = cms.double( wpEB.absPFClusterHCalIsoWithEACut_C2 ),
        C3_EB = cms.double( wpEB.absPFClusterHCalIsoWithEACut_C3 ),
        # Endcap: cut = cut = c1 + pt*c2 + pt*pt*c3                                                       
        C1_EE = cms.double( wpEE.absPFClusterHCalIsoWithEACut_C1 ),
        C2_EE = cms.double( wpEE.absPFClusterHCalIsoWithEACut_C2 ),
        C3_EE = cms.double( wpEE.absPFClusterHCalIsoWithEACut_C3 ),
        anyPFIsoMap = cms.InputTag( isoInputs.PFClusterHCalIsolationMapName ),
        barrelCutOff = cms.double(ebCutOff),
        useRelativeIso = cms.bool(False),
        needsAdditionalProducts = cms.bool(True),
        isIgnored = cms.bool(False),
        rho = cms.InputTag("fixedGridRhoFastjetAll"),
        effAreasConfigFile = cms.FileInPath( isoInputs.PFClusterHCalIsolationEffAreas )

         )


# Configure the cut on the trk isolation that uses                                                                                                                                                                                                                
# the linear pt scaling for barrel and endcap                                                                                                                                                                                                                               
  
def psetTrkIsoWithEALinScalingCut(wpEB, wpEE, isoInputs):
    """                                                                                                                                                                                                                                                                      
    Arguments: two containers of working point cut values of the type WorkingPoint_*                                                                                                                                                                                         
    The third argument contains data for isolation calculation.                                                                                                                                                                                                              
    """
    return cms.PSet(
        cutName = cms.string('PhoAnyPFIsoWithEACut'),
        # Both barrel and endcap: cut = c1 + pt*c2                                                                                                                                                                                                                           
        C1_EB = cms.double( wpEB.absTrkIsoWithEACut_C1 ),
        C2_EB = cms.double( wpEB.absTrkIsoWithEACut_C2 ),
        C1_EE = cms.double( wpEE.absTrkIsoWithEACut_C1 ),
        C2_EE = cms.double( wpEE.absTrkIsoWithEACut_C2 ),
        anyPFIsoMap = cms.InputTag( isoInputs.TrkIsolationMapName ),
        barrelCutOff = cms.double(ebCutOff),
        useRelativeIso = cms.bool(False),
        needsAdditionalProducts = cms.bool(True),
        isIgnored = cms.bool(False),
        rho = cms.InputTag("fixedGridRhoFastjetAll"),
        effAreasConfigFile = cms.FileInPath( isoInputs.TrkIsolationEffAreas )
        )


# ==============================================================
# Define the complete cut sets
# ==============================================================


def configureVIDCutBasedPhoID_V1( wpEB, wpEE, isoInputs ):
    """
    This function configures the full cms.PSet for a VID ID and returns it.
    The inputs: two objects of the type WorkingPoint_V1, one
    containing the cuts for the Barrel (EB) and the other one for the Endcap (EE).
    The third argument contains data for isolation calculation.
    """
    # print "VID: Configuring cut set %s" % wpEB.idName
    parameterSet =  cms.PSet(
        #
        idName = cms.string( wpEB.idName ), # same name stored in the _EB and _EE objects
        cutFlow = cms.VPSet( 
            psetMinPtCut(),                                        # pt cut
            psetPhoSCEtaMultiRangeCut(),                           # eta cut
            psetPhoSingleTowerHadOverEmCut(wpEB,wpEE),             # H/E cut
            psetPhoFull5x5SigmaIEtaIEtaValueMapCut(wpEB,wpEE),     # full 5x5 sigmaIEtaIEta cut
            psetChHadIsoWithEALinScalingCut(wpEB,wpEE,isoInputs),  # charged hadron isolation cut
            psetNeuHadIsoWithEALinScalingCut(wpEB,wpEE,isoInputs), # neutral hadron isolation cut
            psetPhoIsoWithEALinScalingCut(wpEB,wpEE,isoInputs)     # photon isolation cut
            )
        )
    #
    return parameterSet

def configureVIDCutBasedPhoID_V2( wpEB, wpEE, isoInputs ):
    """
    This function configures the full cms.PSet for a VID ID and returns it.
    The inputs: first object is of the type WorkingPoint_V2, second object
    is of the type WorkingPoint_V1, containing the cuts for the Barrel (EB) 
    and the other one for the Endcap (EE).
    The third argument contains data for isolation calculation.

    The V2 with respect to V1 has one change: the neutral hadron isolation
    cut has an exponential pt scaling for the barrel.
    """
    # print "VID: Configuring cut set %s" % wpEB.idName
    parameterSet =  cms.PSet(
        #
        idName = cms.string( wpEB.idName ), # same name stored in the _EB and _EE objects
        cutFlow = cms.VPSet( 
            psetMinPtCut(),                                           # pt cut
            psetPhoSCEtaMultiRangeCut(),                              # eta cut
            psetPhoSingleTowerHadOverEmCut(wpEB,wpEE),                # H/E cut
            psetPhoFull5x5SigmaIEtaIEtaValueMapCut(wpEB,wpEE),        # full 5x5 sigmaIEtaIEta cut
            psetChHadIsoWithEALinScalingCut(wpEB,wpEE,isoInputs),     # charged hadron isolation cut
            psetNeuHadIsoWithEAExpoScalingEBCut(wpEB,wpEE,isoInputs), # neutral hadron isolation cut
            psetPhoIsoWithEALinScalingCut(wpEB,wpEE,isoInputs)        # photon isolation cut
            )
        )
    #
    return parameterSet



def configureVIDCutBasedPhoID_HPT_V1( wpEB, wpEE, isoInputs ):
    """
    This function configures the full cms.PSet for a VID ID and returns it.
    The inputs: first object is of the type WorkingPoint_V2, second object
    is of the type WorkingPoint_V1, containing the cuts for the Barrel (EB) 
    and the other one for the Endcap (EE).
    The third argument contains data for isolation calculation.

    The V2 with respect to V1 has one change: the neutral hadron isolation
    cut has an exponential pt scaling for the barrel.
    """
    # print "VID: Configuring cut set %s" % wpEB.idName
    parameterSet =  cms.PSet(
        #
        idName = cms.string( wpEB.idName ), # same name stored in the _EB and _EE objects
        cutFlow = cms.VPSet( 
            psetMinPtCut(),                                           # pt cut
            psetPhoSCEtaMultiRangeCut(),                              # eta cut
            psetPhoR9Cut(wpEB,wpEE),                                              # r9 cut
            psetPhoSingleTowerHadOverEmCut(wpEB,wpEE),                # H/E cut
            psetPhoFull5x5SigmaIEtaIEtaValueMapCut(wpEB,wpEE),        # full 5x5 sigmaIEtaIEta cut
            psetChHadIsoWithEALinScalingCut(wpEB,wpEE,isoInputs),     # charged hadron isolation cut
            psetNeuHadIsoWithEAExpoScalingEBCut(wpEB,wpEE,isoInputs), # neutral hadron isolation cut
            psetPhoIsoWithEALinScalingCut(wpEB,wpEE,isoInputs)        # photon isolation cut
            )
        )
    #
    return parameterSet

def configureVIDCutBasedPhoID_V3( wpEB, wpEE, isoInputs ):
    """
    This function configures the full cms.PSet for a VID ID and returns it.
    The inputs: first object is of the type WorkingPoint_V2, second object
    is of the type WorkingPoint_V1, containing the cuts for the Barrel (EB) 
    and the other one for the Endcap (EE).
    The third argument contains data for isolation calculation.

    The V3 with respect to V2 has one change: the full5x5 sigmaIEtaIEta
    is taken from the native reco::Photon method and not from a ValueMap
    produced upstream by some producer module.
    """
    # print "VID: Configuring cut set %s" % wpEB.idName
    parameterSet =  cms.PSet(
        #
        idName = cms.string( wpEB.idName ), # same name stored in the _EB and _EE objects
        cutFlow = cms.VPSet( 
            psetMinPtCut(),                                           # pt cut
            psetPhoSCEtaMultiRangeCut(),                              # eta cut
            psetPhoSingleTowerHadOverEmCut(wpEB,wpEE),                # H/E cut
            psetPhoFull5x5SigmaIEtaIEtaCut(wpEB,wpEE),                # full 5x5 sigmaIEtaIEta cut
            psetChHadIsoWithEALinScalingCut(wpEB,wpEE,isoInputs),     # charged hadron isolation cut
            psetNeuHadIsoWithEAExpoScalingEBCut(wpEB,wpEE,isoInputs), # neutral hadron isolation cut
            psetPhoIsoWithEALinScalingCut(wpEB,wpEE,isoInputs)        # photon isolation cut
            )
        )
    #
    return parameterSet

def configureVIDCutBasedPhoID_V4( wpEB, wpEE, isoInputs ):
    """
    This function configures the full cms.PSet for a VID ID and returns it.
    The inputs: first object is of the type WorkingPoint_V2, second object
    is of the type WorkingPoint_V2 as well, first containing the cuts for the 
    Barrel (EB) and the other one for the Endcap (EE).
    The third argument contains data for isolation calculation.

    The V4 with respect to V3 has one change: both barrel and endcap
    use the exponential scaling for the neutral hadron isolation cut
    (in V3 it was only done for the barrel)
    """
    # print "VID: Configuring cut set %s" % wpEB.idName
    parameterSet =  cms.PSet(
        #
        idName = cms.string( wpEB.idName ), # same name stored in the _EB and _EE objects
        cutFlow = cms.VPSet( 
            psetMinPtCut(),                                           # pt cut
            psetPhoSCEtaMultiRangeCut(),                              # eta cut
            psetPhoSingleTowerHadOverEmCut(wpEB,wpEE),                # H/E cut
            psetPhoFull5x5SigmaIEtaIEtaCut(wpEB,wpEE),                # full 5x5 sigmaIEtaIEta cut
            psetChHadIsoWithEALinScalingCut(wpEB,wpEE,isoInputs),     # charged hadron isolation cut
            psetNeuHadIsoWithEAExpoScalingCut(wpEB,wpEE,isoInputs), # neutral hadron isolation cut
            psetPhoIsoWithEALinScalingCut(wpEB,wpEE,isoInputs)        # photon isolation cut
            )
        )
    #
    return parameterSet

def configureVIDCutBasedPhoID_V5( wpEB, wpEE, isoInputs ):
    """
    This function configures the full cms.PSet for a VID ID and returns it.
    The inputs: first object is of the type WorkingPoint_V2, second object
    is of the type WorkingPoint_V2 as well, first containing the cuts for the 
    Barrel (EB) and the other one for the Endcap (EE).
    The third argument contains data for isolation calculation.

    The V5 with respect to V4 has one change: the neutral hadron isolation
    for both barrel and endcap now uses quadratic polynomial scaling.
    """
    # print "VID: Configuring cut set %s" % wpEB.idName
    parameterSet =  cms.PSet(
        #
        idName = cms.string( wpEB.idName ), # same name stored in the _EB and _EE objects
        cutFlow = cms.VPSet( 
            psetMinPtCut(),                                           # pt cut
            psetPhoSCEtaMultiRangeCut(),                              # eta cut
            psetPhoSingleTowerHadOverEmCut(wpEB,wpEE),                # H/E cut
            psetPhoFull5x5SigmaIEtaIEtaCut(wpEB,wpEE),                # full 5x5 sigmaIEtaIEta cut
            psetChHadIsoWithEALinScalingCut(wpEB,wpEE,isoInputs),     # charged hadron isolation cut
            psetNeuHadIsoWithEAQuadScalingCut(wpEB,wpEE,isoInputs),   # neutral hadron isolation cut
            psetPhoIsoWithEALinScalingCut(wpEB,wpEE,isoInputs)        # photon isolation cut
            )
        )
    #
    return parameterSet

def configureVIDCutBasedPhoID_OOT_V1( wpEB, wpEE, isoInputs ):

    parameterSet =  cms.PSet(
        #
        idName = cms.string( wpEB.idName ), # same name stored in the _EB and _EE objects
        cutFlow = cms.VPSet( 
            psetMinPtCut(),                                           # pt cut
            psetPhoSCEtaMultiRangeCut(),                              # eta cut
            psetPhoSingleTowerHadOverEmCut(wpEB,wpEE),                # H/E cut
            psetPhoFull5x5SigmaIEtaIEtaCut(wpEB,wpEE),                # full 5x5 sigmaIEtaIEta cut
            psetPhoSMajWithScalingCut(wpEB,wpEE,isoInputs),
            psetTrkIsoWithEALinScalingCut(wpEB,wpEE,isoInputs),     # charged hadron isolation cut
            psetPFClusterHCalIsoEAQuadScalingCut(wpEB,wpEE,isoInputs),   # neutral hadron isolation cut
            psetPFClusterECalIsoWithEALinScalingCut(wpEB,wpEE,isoInputs)        # photon isolation cut
            )
        )
    #
    return parameterSet



def configureVIDCutBasedPhoID_OOT_V2( wpEB, wpEE, isoInputs ):

    parameterSet =  cms.PSet(
        #
        idName = cms.string( wpEB.idName ), # same name stored in the _EB and _EE objects
        cutFlow = cms.VPSet( 
            psetMinPtCut(),                                           # pt cut
            psetPhoSCEtaMultiRangeCut(),                              # eta cut
            psetPhoSingleTowerHadOverEmCut(wpEB,wpEE),                # H/E cut
            psetTrkIsoWithEALinScalingCut(wpEB,wpEE,isoInputs),     # charged hadron isolation cut
            psetPFClusterHCalIsoEAQuadScalingCut(wpEB,wpEE,isoInputs),   # neutral hadron isolation cut
            psetPFClusterECalIsoWithEALinScalingCut(wpEB,wpEE,isoInputs)        # photon isolation cut
            )
        )
    #
    return parameterSet


def configureVIDCutBasedPhoID_OOT_V3( wpEB, wpEE, isoInputs ):

    parameterSet =  cms.PSet(
        #
        idName = cms.string( wpEB.idName ), # same name stored in the _EB and _EE objects
        cutFlow = cms.VPSet( 
            psetMinPtCut(),                                           # pt cut
            psetPhoSCEtaMultiRangeCut(),                              # eta cut
            psetPhoSingleTowerHadOverEmCut(wpEB,wpEE),                # H/E cut
            psetPhoFull5x5SigmaIEtaIEtaCut(wpEB,wpEE),                # full 5x5 sigmaIEtaIEta cut
            psetTrkIsoWithEALinScalingCut(wpEB,wpEE,isoInputs),     # charged hadron isolation cut
            psetPFClusterHCalIsoEAQuadScalingCut(wpEB,wpEE,isoInputs),   # neutral hadron isolation cut
            psetPFClusterECalIsoWithEALinScalingCut(wpEB,wpEE,isoInputs)        # photon isolation cut
            )
        )
    #
    return parameterSet

def configureVIDCutBasedPhoID_OOT_V4( wpEB, wpEE, isoInputs ):

    parameterSet =  cms.PSet(
        #
        idName = cms.string( wpEB.idName ), # same name stored in the _EB and _EE objects
        cutFlow = cms.VPSet( 
            psetMinPtCut(),                                           # pt cut
            psetPhoSCEtaMultiRangeCut(),                              # eta cut
            psetPhoSMajWithScalingCut(wpEB,wpEE,isoInputs),
            )
        )
    #
    return parameterSet


def configureVIDCutBasedPhoID_OOT_V5( wpEB, wpEE, isoInputs ):

    parameterSet =  cms.PSet(
        #
        idName = cms.string( wpEB.idName ), # same name stored in the _EB and _EE objects
        cutFlow = cms.VPSet( 
            psetMinPtCut(),                                           # pt cut
            psetPhoSCEtaMultiRangeCut(),                              # eta cut
            psetPhoSingleTowerHadOverEmCut(wpEB,wpEE),                # H/E cut
            psetPhoFull5x5SigmaIEtaIEtaCut(wpEB,wpEE),                # full 5x5 sigmaIEtaIEta cut
            psetPhoSMajCut(wpEB,wpEE,isoInputs),
            psetTrkIsoWithEALinScalingCut(wpEB,wpEE,isoInputs),     # charged hadron isolation cut
            psetPFClusterHCalIsoEAQuadScalingCut(wpEB,wpEE,isoInputs),   # neutral hadron isolation cut
            psetPFClusterECalIsoWithEALinScalingCut(wpEB,wpEE,isoInputs)        # photon isolation cut
            )
        )
    #
    return parameterSet



def configureVIDCutBasedPhoID_GED_V6( wpEB, wpEE, isoInputs ):

    parameterSet =  cms.PSet(
        #
        idName = cms.string( wpEB.idName ), # same name stored in the _EB and _EE objects
        cutFlow = cms.VPSet( 
            psetMinPtCut(),                                           # pt cut
            psetPhoSCEtaMultiRangeCut(),                              # eta cut
            psetPhoSingleTowerHadOverEmCut(wpEB,wpEE),                # H/E cut
            psetPhoFull5x5SigmaIEtaIEtaCut(wpEB,wpEE),                # full 5x5 sigmaIEtaIEta cut
            psetPhoSMajCut(wpEB,wpEE,isoInputs),
            psetChHadIsoWithEALinScalingCut(wpEB,wpEE,isoInputs),     # charged hadron isolation cut
            psetNeuHadIsoWithEAQuadScalingCut(wpEB,wpEE,isoInputs),   # neutral hadron isolation cut
            psetPhoIsoWithEALinScalingCut(wpEB,wpEE,isoInputs)        # photon isolation cut
            )
        )
    #
    return parameterSet




def configureVIDCutBasedPhoID_OOT_V7( wpEB, wpEE, isoInputs ):

    parameterSet =  cms.PSet(
        #
        idName = cms.string( wpEB.idName ), # same name stored in the _EB and _EE objects
        cutFlow = cms.VPSet( 
            psetMinPtCut(),                                           # pt cut
            psetPhoSCEtaMultiRangeCut(),                              # eta cut
            psetPhoSingleTowerHadOverEmCut(wpEB,wpEE),                # H/E cut
            psetPhoFull5x5SigmaIEtaIEtaCut(wpEB,wpEE),                # full 5x5 sigmaIEtaIEta cut
            psetPhoSMajCut(wpEB,wpEE,isoInputs),
            psetPhoSMinCut(wpEB,wpEE,isoInputs),
            psetTrkIsoWithEALinScalingCut(wpEB,wpEE,isoInputs),     # charged hadron isolation cut
            psetPFClusterHCalIsoEAQuadScalingCut(wpEB,wpEE,isoInputs),   # neutral hadron isolation cut
            psetPFClusterECalIsoWithEALinScalingCut(wpEB,wpEE,isoInputs)        # photon isolation cut
            )
        )
    #
    return parameterSet



def configureVIDCutBasedPhoID_GED_V8( wpEB, wpEE, isoInputs ):

    parameterSet =  cms.PSet(
        #
        idName = cms.string( wpEB.idName ), # same name stored in the _EB and _EE objects
        cutFlow = cms.VPSet( 
            psetMinPtCut(),                                           # pt cut
            psetPhoSCEtaMultiRangeCut(),                              # eta cut
            psetPhoSingleTowerHadOverEmCut(wpEB,wpEE),                # H/E cut
            psetPhoFull5x5SigmaIEtaIEtaCut(wpEB,wpEE),                # full 5x5 sigmaIEtaIEta cut
            psetPhoSMajCut(wpEB,wpEE,isoInputs),
            psetPhoSMinCut(wpEB,wpEE,isoInputs),
            psetChHadIsoWithEALinScalingCut(wpEB,wpEE,isoInputs),     # charged hadron isolation cut
            psetNeuHadIsoWithEAQuadScalingCut(wpEB,wpEE,isoInputs),   # neutral hadron isolation cut
            psetPhoIsoWithEALinScalingCut(wpEB,wpEE,isoInputs)        # photon isolation cut
            )
        )
    #
    return parameterSet

