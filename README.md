# Forward-Arbitrage-Lab
*Implementation of a No-Arbitrage pricing engine for Forward contracts.*

## 1. Presentation
This project was developed during my second year at **Télécom SudParis** as part of an independent study on Quantitative Finance.
The objective of this library is to implement the **Forward-Spot Parity** relationship and build a monitoring tool capable of detecting arbitrage opportunities using real-time market data.

## 2. Theoretical Framework
The pricing model assumes a storable underlying asset with no dividends and the absence of transaction costs. According to the **No-Arbitrage Assumption (AOA)**, the forward price $F(t,T)$ is uniquely determined by the cost of carry:

$$F(t,T) = S_t \cdot e^{r(T-t)}$$

The engine evaluates market deviations ($K$) from this theoretical value to identify two types of arbitrage:
* **Cash-and-Carry ($K > F_{theoretical}$):** Exploiting overvalued forwards by shorting the contract, borrowing at the risk-free rate, and purchasing the spot asset.
* **Reverse Cash-and-Carry ($K < F_{theoretical}$):** Exploiting undervalued forwards by longing the contract and shorting the spot asset.

## 3. Project Structure
The repository is organized following professional modular standards:
* **`core/pricer.py`**: Mathematical implementation of continuous compounding and pricing formulas.
* **`core/arbitrage.py`**: Analytical engine for comparing market prices and calculating potential $V_T > 0$ profits.
* **`data/loader.py`**: Real-time market data integration using the **yfinance API**.
* **`main.py`**: Execution hub connecting data streams to the pricing engine.

## 4. Implementation Details
* **Language**: Python 3.x
* **Libraries**: `numpy` for vectorized mathematical operations, `yfinance` for financial data ingestion.
* **Architecture**: Object-Oriented Programming (OOP) to ensure modularity and scalability for future asset classes (e.g., dividend-paying stocks).

---
**Career Objective:** Aspiring Quantitative Researcher / Developer. Currently seeking an internship in Quantitative Finance starting in **Fall 2026**.

**Contact**: Maéva Cavaleri - cavalerimaeva@gmail.com
