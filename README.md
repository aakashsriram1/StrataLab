# StrataLab

StrataLab is a project for testing trading and prediction market ideas.

Instead of just trying to predict prices, this project focuses on building a system to:
- try different strategies  
- test them on real data  
- see how they perform under realistic conditions  

---

## What it does

- pulls in market data (stocks or prediction markets)  
- runs simple strategies (momentum, mean reversion, etc.)  
- simulates trades (buy/sell decisions)  
- tracks performance (profit, risk, drawdown)  

---

## Why I built this

Most projects just try to get good predictions.

I wanted to build something closer to how real quant research works:
- test ideas properly  
- understand when they fail  
- not just optimize for best results  

---

## Tech Stack

- Python (data + strategies)  
- Next.js (frontend)  
- FastAPI (backend)  
- Postgres / Supabase (database)  

---

## Current Status

🚧 Still building  

Right now working on:
- setting up data pipeline  
- building first strategy  
- basic backtesting  

---

## Next Steps

- connect real data sources  
- add more strategies  
- improve backtesting (costs, slippage)  
- build simple dashboard
