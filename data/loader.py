import yfinance as yf

class MarketDataLoader :
  """
  Module responsable de la récupération des prix réels sur Yahoo Finance.
  """

  def get_spot_price (self,ticker_symbol:str) -> float:
    """
    Récupère le dernier prix d'un actif.
    Ex : 'AAPL' pour Apple, 'MC.PA' pour LVMH, '^FCHI' pour le CAC40.
    """
    #On crée un objet Ticker pour l'action demandée 
    ticker=yf.Ticker(ticker_symbol)
    
    #On télécharge l'historique d'aujourd'hui
    data=ticker.history(period="1d")
    
    #On extrait le dernier prix de clôture (Close)
    #.iloc signifie prendre la dernière ligne du tableau
    price=data['Close'].iloc[-1]
  
    return float(price)
