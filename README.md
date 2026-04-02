# StrataLab
 
> Quantitative research platform for simulating, testing, and evaluating trading and prediction market strategies under uncertainty.
 
![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=flat-square&logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-In%20Development-F59E0B?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-10B981?style=flat-square)
![Markets](https://img.shields.io/badge/Markets-Equities%20%7C%20Prediction-6366F1?style=flat-square)
 
---
 
## What is StrataLab?
 
StrataLab is a personal quantitative research platform that bridges **financial markets** (equities, crypto) and **prediction markets** (Kalshi, Polymarket). The goal is not simply to predict market movements — it's to build infrastructure for structured experimentation: ingesting data, generating probabilistic signals, running realistic backtests, and rigorously evaluating when and why strategies fail.
 
Core focus areas:
- **Calibrated probability forecasting** on prediction market outcomes
- **Signal research** for swing/momentum strategies on equities and crypto
- **Walk-forward backtesting** with realistic slippage, transaction costs, and regime awareness
- **Uncertainty quantification** — tracking model confidence, not just accuracy
- **Experiment infrastructure** — every run is logged, reproducible, and comparable
 
---
 
## Demo
 
> 🚧 Dashboard in progress — deploying after Phase 3 research validation
 
<!-- Add screenshot or GIF here once dashboard is live -->
<!-- ![StrataLab Dashboard](assets/demo.gif) -->
 
---
 
## Project Goals
 
| Goal | Description |
|------|-------------|
| 📊 Research | Identify edges in prediction markets using external data (economic releases, news, polling) |
| 📈 Equities | Build and validate swing trading signals on stocks and crypto |
| 🧪 Rigor | Every strategy must pass walk-forward validation before being considered real |
| 🔁 Reproducibility | Any experiment reproducible from a single command via MLflow |
| 🖥️ Dashboard | Live public dashboard showing real calibration curves, P&L, and strategy monitor |
 
---
 
 
## Roadmap
 
### Phase 1 — Prediction Market Research Core 
- [ ] Kalshi + Polymarket data ingestion
- [ ] External feature pipeline (economic releases, news, weather)
- [ ] Logistic regression + XGBoost probability models
- [ ] Brier score and calibration curve evaluation
- [ ] First live market forecast with tracked accuracy
 
### Phase 2 — Backtesting Engine + Equities 
- [ ] Yahoo Finance + crypto data pipeline
- [ ] Signal library: momentum, mean-reversion, volume-based
- [ ] Walk-forward backtester with realistic costs
- [ ] Signal decay analysis over rolling windows
- [ ] Paper trading execution scaffold
 
### Phase 3 — Infrastructure Hardening 
- [ ] MLflow experiment tracking across all runs
- [ ] Regime detection layer (HMM or rolling volatility)
- [ ] Prefect pipeline orchestration
- [ ] Unit + integration test coverage
- [ ] Clean reproducible repo structure
 
### Phase 4 — Dashboard + Live Deployment 
- [ ] React dashboard with live calibration curves and P&L
- [ ] Strategy monitor with regime overlay
- [ ] Public deployment (Vercel + Railway or similar)
- [ ] Optional: live execution on real capital once edge confirmed
 
---
 
## Tech Stack
 
| Layer | Tools |
|-------|-------|
| Core | Python 3.11+, pandas, numpy, scipy |
| ML | scikit-learn, XGBoost, statsmodels |
| Data | DuckDB, Polars, Yahoo Finance API, Kalshi API, Polymarket API |
| Tracking | MLflow |
| Orchestration | Prefect |
| Dashboard | React, Recharts (or Streamlit for rapid iteration) |
| Testing | pytest |
| Infra | GitHub Actions, Docker (planned) |
 
---
 
## Key Concepts
 
**Walk-forward validation** — Rather than a simple train/test split, strategies are tested by repeatedly training on historical data and evaluating on the next unseen window. This mirrors real-world conditions and catches overfitting that standard backtests miss.
 
**Calibration** — A model that says "70% probability" should be right about 70% of the time. StrataLab tracks Brier scores and calibration curves throughout, not just accuracy.
 
**Signal decay analysis** — Every signal has an expiry date. StrataLab measures how quickly each signal's predictive edge degrades over time, informing position sizing and retraining schedules.
 
**Regime detection** — Markets behave differently in trending vs. mean-reverting, high vs. low volatility environments. A regime layer selects strategies based on the current market state rather than using a one-size-fits-all approach.
 
**When models fail** — The project explicitly documents failure modes: sensitivity to assumptions, out-of-sample degradation, and regime breakdowns. Understanding failure is more valuable than optimizing for performance.
 
---
 
## Getting Started
 
### Prerequisites
- Python 3.11+
- A Kalshi account (for prediction market data)
- `pip` or `uv`
 
### Installation
 
```bash
git clone https://github.com/YOUR_USERNAME/stratalab.git
cd stratalab
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```
 
### Environment Variables
 
```bash
cp .env.example .env
# Fill in your API keys:
# KALSHI_API_KEY=
# POLYMARKET_API_KEY=
# (Yahoo Finance works without a key)
```
 
### Run your first experiment
 
```bash
# Pull prediction market data
python -m ingestion.kalshi --market economic_releases
 
# Train a baseline model and log to MLflow
python -m models.prediction_market.baseline --log
 
# View experiment results
mlflow ui
```
 
---
 
## Research Log
 
Experiments and findings are documented in [`/research`](./research/). Each notebook includes:
- A written hypothesis
- Data sources and feature set used
- Model parameters and evaluation metrics
- Conclusion and next steps
 
This mirrors how actual quantitative research teams operate — every idea is testable and every result is recorded.
 
---
 
## Skills Demonstrated
 
This project was built to demonstrate practical competency across multiple disciplines:
 
- **Data Engineering** — API ingestion, pipeline orchestration, feature engineering at scale
- **Machine Learning** — Probabilistic forecasting, calibration, XGBoost, model evaluation beyond accuracy
- **Quantitative Finance** — Backtesting methodology, performance attribution, risk-adjusted returns, regime modeling
- **Software Engineering** — Modular architecture, reproducible experiments, testing, clean version control
- **Product Thinking** — End-to-end system from raw data to live interactive dashboard
 
