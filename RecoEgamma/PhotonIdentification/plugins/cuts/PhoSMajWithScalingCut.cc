#include "PhysicsTools/SelectorUtils/interface/CutApplicatorWithEventContentBase.h"
#include "DataFormats/EgammaCandidates/interface/Photon.h"
#include "RecoEgamma/EgammaTools/interface/EffectiveAreas.h"


class PhoSMajWithScalingCut : public CutApplicatorWithEventContentBase {
public:
  PhoSMajWithScalingCut(const edm::ParameterSet& c);
  
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
  float _C2_EB;
  float _C3_EB;
  float _C4_EB;
  float _C5_EB;
  float _C1_EE;
  float _C2_EE;
  float _C3_EE;
  float _C4_EE;
  float _C5_EE;

  // Configuration
  float _barrelCutOff;
  // The isolations computed upstream
  edm::Handle<edm::ValueMap<float> > _sMajMap;


  constexpr static char sMaj_[] = "sMaj";

};

constexpr char PhoSMajWithScalingCut::sMaj_[];


DEFINE_EDM_PLUGIN(CutApplicatorFactory,
		  PhoSMajWithScalingCut,
		  "PhoSMajWithScalingCut");

PhoSMajWithScalingCut::PhoSMajWithScalingCut(const edm::ParameterSet& c) :
  CutApplicatorWithEventContentBase(c),
  _C1_EB(c.getParameter<double>("C1_EB")),
  _C2_EB(c.getParameter<double>("C2_EB")),
  _C3_EB(c.getParameter<double>("C3_EB")),
  _C4_EB(c.getParameter<double>("C4_EB")),
  _C5_EB(c.getParameter<double>("C5_EB")),
  _C1_EE(c.getParameter<double>("C1_EE")),
  _C2_EE(c.getParameter<double>("C2_EE")),
  _C3_EE(c.getParameter<double>("C3_EE")),
  _C4_EE(c.getParameter<double>("C4_EE")),
  _C5_EE(c.getParameter<double>("C5_EE")),
  
  _barrelCutOff(c.getParameter<double>("barrelCutOff"))
{
  
  edm::InputTag maptag = c.getParameter<edm::InputTag>("sMajMap");
  contentTags_.emplace(sMaj_,maptag);

}

void PhoSMajWithScalingCut::setConsumes(edm::ConsumesCollector& cc) {
  auto sMaj = 
    cc.consumes<edm::ValueMap<float> >(contentTags_[sMaj_]);
  contentTokens_.emplace(sMaj_,sMaj);

}

void PhoSMajWithScalingCut::getEventContent(const edm::EventBase& ev) {  
  ev.getByLabel(contentTags_[sMaj_],_sMajMap);

}

CutApplicatorBase::result_type 
PhoSMajWithScalingCut::
operator()(const reco::PhotonPtr& cand) const{  

  // in case we are by-value
  const std::string& inst_name = contentTags_.find(sMaj_)->second.instance();
  edm::Ptr<pat::Photon> pat(cand);
  float smajval = -1.0;
  if( _sMajMap.isValid() && _sMajMap->contains( cand.id() ) ) {
    smajval = (*_sMajMap)[cand];
  } else if ( _sMajMap.isValid() && _sMajMap->idSize() == 1 &&
              cand.id() == edm::ProductID() ) {
    // in case we have spoofed a ptr
    //note this must be a 1:1 valuemap (only one product input)
    smajval = _sMajMap->begin()[cand.key()];
  } else if ( _sMajMap.isValid() ){ // throw an exception
    smajval = (*_sMajMap)[cand];
  }

  // Figure out the cut value
  // The value is generally pt-dependent: C1 + pt * C2
  const double absEta = std::abs(cand->superCluster()->eta());
  const float pt = cand->pt();
  float sMajCutValue=999.;

  if (absEta < _barrelCutOff && absEta>0.8)sMajCutValue= _C1_EB + _C2_EB*(absEta-0.8) + _C3_EB*exp(_C4_EB*pt+_C5_EB);
  if (absEta<0.8)sMajCutValue= _C1_EB + _C3_EB*exp(_C4_EB*pt+_C5_EB);
  if (absEta > _barrelCutOff)sMajCutValue= _C1_EE + _C2_EE*(absEta-0.8) + _C3_EE*exp(_C4_EE*pt+_C5_EE);
  
  //  std::cout<<_C1_EB<<" "<<_C2_EB<<" "<<_C3_EB<<" "<<_C4_EB<<" "<<_C5_EB<<std::endl;

  const float sMaj =  _sMajMap.isValid() ? smajval : pat->userFloat(inst_name);
  //  std::cout<<"inside cuts: "<<sMaj<< " cut value: "<<sMajCutValue<<std::endl;
  // Apply the cut and return the result
  // Scale by pT if the relative isolation is requested but avoid division by 0
  return sMaj < sMajCutValue;
}

double PhoSMajWithScalingCut::
value(const reco::CandidatePtr& cand) const {
  reco::PhotonPtr pho(cand);

  // in case we are by-value
  const std::string& inst_name = contentTags_.find(sMaj_)->second.instance();
  edm::Ptr<pat::Photon> pat(cand);
  float smajval = -1.0;
  if( _sMajMap.isValid() && _sMajMap->contains( cand.id() ) ) {
    smajval = (*_sMajMap)[cand];
  } else if ( _sMajMap.isValid() && _sMajMap->idSize() == 1 &&
              cand.id() == edm::ProductID() ) {
    // in case we have spoofed a ptr
    //note this must be a 1:1 valuemap (only one product input)
    smajval = _sMajMap->begin()[cand.key()];
  } else if ( _sMajMap.isValid() ){ // throw an exception
    smajval = (*_sMajMap)[cand];
  }

  // Figure out the cut value
  // The value is generally pt-dependent: C1 + pt * C2
  double absEta = std::abs(pho->superCluster()->eta());  
  
  float sMaj =_sMajMap.isValid() ? smajval : pat->userFloat(inst_name);

  // Divide by pT if the relative isolation is requested

  // Apply the cut and return the result
  return sMaj;
}
