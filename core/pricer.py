import numpy as np

class ForwardPricer :
  """
  Moteur de clacul pour les prix de produits dérivés (Forwards).
  Ce module traduit les formules d'abscence d'opportunité d'arbitrage (AOA).
  """

  def calculate_discount_factor(self,r,tau):
    """
    Calcule le facteur d'actualisation Z(t,T).
    - r : taux d'intérêt sans risque 
    - taux : T-t temps restant jusqu'à l'échéance (en années)
    """
    return np.exp(-r*tau)
  
  def calculate_froward_price(self,spot,r,tau):
    """
    Calcule le prix forward théorique F(t,T).
    - spot : prix actuel de l'actif sur le marché (St)
    """
    z=self.calculate_discount_factor(r,tau)
    return spot/z
  
  def calculate_prepaid_forward_price(self, spot):
    """
    Calcule le prix du prepaid forward.
    En l'abscence de dividendes, le prix prépayé est égale au prix spot.
    """
    return spot
    
