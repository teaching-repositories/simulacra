# Stock Market Simulation

## Purpose

This simulation models the fluctuations of stock prices, enabling students to explore financial market dynamics and develop basic trading strategies. It serves as a practical tool for understanding the principles of market speculation and risk management.

## Parameters

- `start_price`: The initial price of the stock.
- `days`: The duration of the simulation.
- `volatility`: The measure of price fluctuations, indicating how much the price can vary day-to-day.
- `drift`: Represents the overall trend in stock prices, whether upward or downward.
- `event_day`: Specifies the day on which a major market event occurs (optional).
- `event_impact`: The magnitude of the event’s impact on stock prices, positive for beneficial events and negative for detrimental ones.

**Example Code**

```python
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
```

## Conducting Visual Analysis Using the Simulation:

Experiment! Use the simulation to explore and test various scenarios. Adjust parameters, try different strategies, and analyse the outcomes to gain deeper insights into resource management under fluctuating conditions.

- **Baseline Scenario Without Disruptions**: Begin by simulating the price path without any disruptions to establish a baseline for comparison with more complex scenarios.
  
- **Labeling and Annotations**: Ensure that your plots clearly show the days on the x-axis and price on the y-axis. Use lines or markers to indicate the day of the event or the implementation of a trading strategy.

- **Interactive Exploration**: If tools are available, adjust parameters such as volatility and drift dynamically to observe how these changes affect the price simulation. This can help in understanding the immediate effects of each parameter.

- **Comparative Analysis**: Conduct side-by-side comparisons of scenarios with different levels of volatility or different strategies to visually assess their impact. This can make it easier to understand which conditions or strategies lead to the most favorable outcomes.  Consider calculating and comparing statistics such as the average price before and after a disruption event to quantify its impact.

## Task-Specific Guidance

### Investigate How Volatility Affects Stock Price Stability

Begin by analysing how different levels of volatility impact the stability of stock prices and the potential for investment gains or losses. Questions to Consider:

  - How do changes in volatility affect the frequency and magnitude of price swings?

  - What implications does increased volatility have on the risk and potential returns of stock investments?

### Simulate a Major Market Event and Analyse Its Impact

Set up scenarios where a significant market event affects stock prices on a specific day. Adjust the impact of these events to observe varying outcomes. Questions to Consider:

  - How does the market respond to positive versus negative events?

  - Analyse the recovery or further decline in stock prices following the event. What does this tell you about market sentiment and investor behavior?

### (Optional) Develop and Test Trading Strategies

Explore basic trading strategies such as "buy and hold", "moving average crossover", or "momentum-based" strategies. Implement these strategies in your simulation to test their effectiveness over time. Questions to Consider:

  - Which strategy performs best under stable versus volatile market conditions?

  - How do these strategies perform in response to the simulated market events?


  ## Model Formulation

The formula used in the `StockMarketSimulation` class simulates stock price movements by incorporating volatility, a directional trend (drift), and the impact of specific market events. Here’s a detailed explanation of the components of the formula:

1. **Volatility and Drift:** Similar to the Resource Fluctuations Simulation, the stock price changes are driven by daily volatility and drift. Each day, the stock price undergoes a random change determined by a normal distribution centered around the `drift` (which can be positive or negative to represent an overall upward or downward trend) and spread according to the `volatility` (which accounts for the unpredictability or risk associated with the stock). This is mathematically modeled as:
   \[
   \text{Random Change} = \text{Normal}(\text{Drift}, \text{Volatility})
   \]
   The new price for each day is then calculated as:
   \[
   \text{New Price} = \text{Previous Price} \times (1 + \text{Random Change})
   \]

2. **Market Event Impact:** If there is a significant market event planned for a specific day (`event_day`), the stock price is adjusted to reflect the impact of this event using the `event_impact`, which is applied as a multiplicative factor. This adjusts the price in response to the event:
   \[
   \text{New Price} = \text{Previous Price} \times (1 + \text{Event Impact})
   \]

### Relation to Classical Models

The simulation model described in the `StockMarketSimulation` class aligns closely with the principles of the **Geometric Brownian Motion (GBM)** model used in financial mathematics to model the prices of financial instruments like stocks and commodities:

- **Geometric Brownian Motion:** The use of a random change modeled with a normal distribution where the stock price is updated by multiplying the previous price by \(1 + \text{Random Change}\) is characteristic of GBM. In GBM, prices are assumed to follow a log-normal distribution, ensuring that they remain positive and reflect realistic financial scenarios where prices are multiplicative.

- **Event Modeling:** The handling of specific market events by applying a multiplicative impact on the stock price for a particular day resembles a **jump-diffusion model**. This type of model is often used to incorporate sudden, significant changes in price due to external factors (such as corporate news, geopolitical events, etc.), which aren’t captured by the standard GBM.

Overall, the simulation combines elements from established financial models to allow for dynamic and realistic modeling of stock prices, accommodating both the continuous aspect of daily price changes and discrete events that can significantly affect market conditions. This approach is quite common in financial market simulations used for educational purposes, trading strategy development, and risk management.