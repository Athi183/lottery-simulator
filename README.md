# **Betting Simulation: A Probability Game**

This repository contains a Python script that simulates a simple betting game where a player bets on a number, and a random lucky draw determines the outcome. The script tracks the player's account balance over time and visualizes the results using Matplotlib.

## **Game Rules**
1. The player places a random bet between 1 and 10.
2. A random lucky number between 1 and 10 is generated.
3. If the bet matches the lucky number:
   - The player wins ₹900 (minus ₹100 bet amount, net gain of ₹800).
4. If the bet doesn't match:
   - The player loses ₹100.
5. The game is played for different durations:
   - **1 week** (7 games)
   - **1 month** (30 games)
   - **1 year** (365 games)

## **Features**
- Simulates betting outcomes for varying time periods.
- Tracks and displays the player's account balance after each game.
- Visualizes the results using line graphs.

## **Requirements**
- Python 3.6 or higher.
- Required modules: 
  - `random` (built-in)
  - `matplotlib`

Install Matplotlib using:
```bash
pip install matplotlib
```

## **How It Works**
1. The program initializes the player's account balance to ₹0.
2. It simulates games for 7 days, 30 days, and 365 days.
3. After each game, the account balance is updated based on the outcome.
4. A line graph is plotted to show how the account balance changes over time.

## **Visualization**
- The graph's x-axis represents the number of games played.
- The y-axis shows the account balance.
- Separate graphs are generated for each time period (week, month, year).

## **Insights**
- This script demonstrates probability in action.
- It highlights the financial risks of gambling over time.
- Users can observe trends and understand the mathematical expectation of the game.

