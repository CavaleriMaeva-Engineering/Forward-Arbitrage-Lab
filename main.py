from data.loader import MarketDataLoader
from core.arbitrage import ArbitrageScanner

def main():
  loader=MarketDataLoader()
  scanner=ArbitrageScanner()
  ticker="AAPL" #On test sur Apple
  r=0.05        #Taux sans risque à 5%
  tau=1.0       #Durée de 1 an
  print (f"---Analyse d'arbitrage sur {ticker}---")

  #Récupération du prix réel
  try: 
    spot_price=loader.get_spot_price(ticker)
    print(f"prix spot actuel (St) : {spot_price:.2f}€")
  except Exception as e:
    print(f"Erreur lors de la récupération des données : {e}")
    return 

  #Simulation d'un prix de marché pour le forward K.
  #Dans la réalité on lirait ce prix sur un carnet d'ordres.
  #Ici on va tester le CAS 1 en imaginant un prix trop cher.
  market_forward_price=spot_price*1.15 #Imaginons un prix 15% plus haut

  print(f"Prix du contrat forward sur le marché (K) : {market_forward_price:.2f}€")
  print("-"*40)

  #Lancement du scan d'arbitrage
  resultat=scanner.scan(spot_price,market_forward_price,r,tau)
  print(resultat)

if __name__=="__main__":
  main()
