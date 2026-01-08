from core.pricer import ForwardPricer

class ArbitrageScanner :
  """
  Ce module compare le prix du marché avec le prix théorique 
  pour identifier des opportunités d'argent gratuit (arbitrage).
  """

  def __init__(self) : 
  #initialisation de la calculatrice de prix juste 
  self.pricer=ForwardPricer() 

  def scan(self,spot,market_price,r,tau):
    """
    Compare le prix affiché sur le marché (market_price) avec le prix juste théorique.
    """
    #1. Calcul du prix que le marché devrait afficher 
    theoritical_price=self.pricer.calculate_forward_price(spot,r,tau)
    #2. Comparaison 
    # CAS 1 : Le marché est trop cher (K>St/Z)
    if market_price>theoritical_price :
      gain=market_price-theoritical_price
      return f"Opportunité d'arbitrage ! Le prix est trop haut. Profit potentiel : {gain:.2f}€"
    # CAS 2 : Le marché est trop bas (K<St/Z)
    if market_price<theoritical_price :
      gain=theoritical_price-market_price
      return f"Opportunité d'arbitrage ! Le prix est trop bas. Profit potentiel : {gain:.2f}€"
    else :
      return "Le prix est juste. Pas d'arbitrage possible."
