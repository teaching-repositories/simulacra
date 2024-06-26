from simulacra import StockMarketSimulation
import matplotlib.pyplot as plt

# Example scenario: High volatility with a downward price trend and a significant market event.
sim = StockMarketSimulation(start_price=100, days=365, volatility=0.03, 
                            drift=-0.001, event_day=100, event_impact=-0.2)

prices = sim.run_simulation()

# Visualising the stock market fluctuations
plt.figure(figsise=(10, 6))
plt.plot(prices, label='Stock Price')
plt.axvline(x=sim.event_day, color='red', linestyle='--', label='Major Market Event')
plt.xlabel('Days')
plt.ylabel('Price ($)')
plt.title('Stock Market Simulation')
plt.legend()
plt.show()