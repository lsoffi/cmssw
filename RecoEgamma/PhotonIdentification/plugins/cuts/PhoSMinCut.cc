#include "PhysicsTools/SelectorUtils/interface/CutApplicatorWithEventContentBase.h"
#include "DataFormats/EgammaCandidates/interface/Photon.h"
#include "RecoEgamma/EgammaTools/interface/EffectiveAreas.h"


class PhoSMinCut : public CutApplicatorWithEventContentBase {
public:
  PhoSMinCut(const edm::ParameterSet& c);
  
  result_type operator()(const reco::PhotonPtr&) const final;

  void setConsumes(edm::ConsumesCollector&) final;
  void getEventContent(const edm::EventBase&) final;

  double value(const reco::CandidatePtr& cand) const final;

  CandidateType candidateType() const final { 
    return PHOTON; 
  }

private:
  // Cut values
  float _C1_EB;
  float _C1_EE;

  // Configuration
  float _barrelCutOff;
  // The isolations computed upstream
  edm::Handle<edm::ValueMap<float> > _sMinMap;


  constexpr static char sMin_[] = "sMin";

};

constexpr char PhoSMinCut::sMin_[];


DEFINE_EDM_PLUGIN(CutApplicatorFactory,
		  PhoSMinCut,
		  "PhoSMinCut");

PhoSMinCut::PhoSMinCut(const edm::ParameterSet& c) :
  CutApplicatorWithEventContentBase(c),
  _C1_EB(c.getParameter<double>("C1_EB")),
  _C1_EE(c.getParameter<double>("C1_EE")),
  _barrelCutOff(c.getParameter<double>("barrelCutOff"))
{
  
  edm::InputTag maptag = c.getParameter<edm::InputTag>("sMinMap");
  contentTags_.emplace(sMin_,maptag);

}

void PhoSMinCut::setConsumes(edm::ConsumesCollector& cc) {
  auto sMin = 
    cc.consumes<edm::ValueMap<float> >(contentTags_[sMin_]);
  contentTokens_.emplace(sMin_,sMin);

}

void PhoSMinCut::getEventContent(const edm::EventBase& ev) {  
  ev.getByLabel(contentTags_[sMin_],_sMinMap);

}

CutApplicatorBase::result_type 
PhoSMinCut::
operator()(const reco::PhotonPtr& cand) const{  

  // in case we are by-value
  const std::string& inst_name = contentTags_.find(sMin_)->second.instance();
  edm::Ptr<pat::Photon> pat(cand);
  float sminval = -1.0;
  if( _sMinMap.isValid() && _sMinMap->contains( cand.id() ) ) {
    sminval = (*_sMinMap)[cand];
  } else if ( _sMinMap.isValid() && _sMinMap->idSize() == 1 &&
              cand.id() == edm::ProductID() ) {
    // in case we have spoofed a ptr
    //note this must be a 1:1 valuemap (only one product input)
    sminval = _sMinMap->begin()[cand.key()];
  } else if ( _sMinMap.isValid() ){ // throw an exception
    sminval = (*_sMinMap)[cand];
  }

  // Figure out the cut value
  // The value is generally pt-dependent: C1 + pt * C2
  const double absEta = std::abs(cand->superCluster()->eta());
  const float sMinCutValue = 
    ( absEta < _barrelCutOff ? 
      _C1_EB 
      : 
      _C1_EE 
      );
  

  const float sMin =  _sMinMap.isValid() ? sminval : pat->userFloat(inst_name);
  //  std::cout<<"inside cuts: "<<sMin<< " cut value: "<<sMinCutValue<<std::endl;
  // Apply the cut and return the result
  // Scale by pT if the relative isolation is requested but avoid division by 0
  return sMin < sMinCutValue;
}

double PhoSMinCut::
value(const reco::CandidatePtr& cand) const {
  reco::PhotonPtr pho(cand);

  // in case we are by-value
  const std::string& inst_name = contentTags_.find(sMin_)->second.instance();
  edm::Ptr<pat::Photon> pat(cand);
  float sminval = -1.0;
  if( _sMinMap.isValid() && _sMinMap->contains( cand.id() ) ) {
    sminval = (*_sMinMap)[cand];
  } else if ( _sMinMap.isValid() && _sMinMap->idSize() == 1 &&
              cand.id() == edm::ProductID() ) {
    // in case we have spoofed a ptr
    //note this must be a 1:1 valuemap (only one product input)
    sminval = _sMinMap->begin()[cand.key()];
  } else if ( _sMinMap.isValid() ){ // throw an exception
    sminval = (*_sMinMap)[cand];
  }

  // Figure out the cut value
  // The value is generally pt-dependent: C1 + pt * C2
  double absEta = std::abs(pho->superCluster()->eta());  
  
  float sMin =_sMinMap.isValid() ? sminval : pat->userFloat(inst_name);

  // Divide by pT if the relative isolation is requested

  // Apply the cut and return the result
  return sMin;
}
