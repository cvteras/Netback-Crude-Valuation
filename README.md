# Netback-Crude-Valuation
Netback represents the per-barrel cash margin after deducting all direct costs—blending, treating, conversion, distillation, and fiscal charges (e.g., processing, production taxes)—from the realized sales price of crude. 


**Netback** is a core metric for crude valuation and is especially relevant in:

Benchmarking upstream asset performance across geographies and crude types.

Evaluating economic viability of crude supply options.

Supporting market-based pricing differentials, particularly when negotiating crude sales or substitutions.

Importantly, netback is not universal—it is refinery- and operation-specific, highly dependent on:

The refiner's configuration (e.g., complexity, conversion capacity).

Throughput rates, utilization, and yield profiles.

Location, which affects logistics costs and applicable fiscal regimes.

Thus, while it serves as a proxy for economic efficiency per barrel, netback must be contextualized within the refiner's actual processing environment for meaningful comparison or decision-making.
____________________________________________________________________________________________________________________________________________________________________________________________

Use in Refinery Optimization
Refiners use netback in scenario-based optimization models to evaluate and rank different crude options:

Scenario Analysis: Crudes are compared relative to a benchmark (e.g., WTI, Brent) by simulating how each would perform under varying operational and market conditions.

LP Modeling: Yield profiles, product pricing, and unit constraints are modeled to calculate netbacks and identify the most profitable feedstock.

Dynamic Strategy: Refineries adjust crude slates over time, selecting barrels that maximize netback-adjusted refining margins.

_____________________________________________________________________________

## Structure

- `code/` — Contains the code scripts of MLR, MLP and NARX (deducted).
- `data/` — Contains sample datasets

_____________________________________________________________________________

## Tech Stack

| Category | Technologies |
| :------: | :----------- |
| **Programming Language** | ![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white) |
| **Data Manipulation & Analysis** | ![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)

_____________________________________________________________________________

**Disclaimer**

This repository is intended solely for educational and illustrative purposes. 

It contains only publicly available or hypothetical information and does not use or disclose any proprietary, confidential, or commercially sensitive data, breaching no NDAs, non-Compete or other agreements


