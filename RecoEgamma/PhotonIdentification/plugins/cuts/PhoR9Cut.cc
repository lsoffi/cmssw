#include "PhysicsTools/SelectorUtils/interface/CutApplicatorBase.h"
#include "DataFormats/EgammaCandidates/interface/Photon.h"

class PhoR9Cut : public CutApplicatorBase {
public:
  PhoR9Cut(const edm::ParameterSet& c);
  
  result_type operator()(const reco::PhotonPtr&) const final;

  double value(const reco::CandidatePtr& cand) const final;

  CandidateType candidateType() const final { 
    return PHOTON; 
  }

private:
  float _cutValueEB;
  float _cutValueEE;
  float _barrelCutOff;
};

DEFINE_EDM_PLUGIN(CutApplicatorFactory,
		  PhoR9Cut,
		  "PhoR9Cut");

PhoR9Cut::PhoR9Cut(const edm::ParameterSet& c) :
  CutApplicatorBase(c),
  _cutValueEB(c.getParameter<double>("cutValueEB")),
  _cutValueEE(c.getParameter<double>("cutValueEE")),
  _barrelCutOff(c.getParameter<double>("barrelCutOff")) {
}

CutApplicatorBase::result_type 
PhoR9Cut::
operator()(const reco::PhotonPtr& cand) const{  

  // Figure out the cut value
  const float r9CutValue = 
    ( std::abs(cand->superCluster()->eta()) < _barrelCutOff ? 
      _cutValueEB : _cutValueEE );

  // Apply the cut and return the result
  return cand->r9() > r9CutValue;
}

double PhoR9Cut::
value(const reco::CandidatePtr& cand) const {
  reco::PhotonPtr pho(cand);
  return pho->r9();
}
