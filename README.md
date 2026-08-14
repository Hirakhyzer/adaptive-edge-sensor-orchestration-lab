<p align="center">
  <img src="assets/banner.svg" alt="Adaptive Edge Sensor Orchestration Lab banner" width="100%" />
</p>

<h1 align="center">Adaptive Edge Sensor Orchestration Lab</h1>

<p align="center">
  <b>An academic AIoT research prototype for adaptive sensor group selection, edge scheduling, and energy-quality trade-off analysis in synthetic smart-city sensing scenarios.</b>
</p>

<p align="center">
  <img alt="Status" src="https://img.shields.io/badge/status-research--prototype-7C3AED?style=for-the-badge" />
  <img alt="Python" src="https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge&logo=python&logoColor=white" />
  <img alt="AIoT" src="https://img.shields.io/badge/AIoT-Edge--Sensing-06B6D4?style=for-the-badge" />
  <img alt="Smart Cities" src="https://img.shields.io/badge/Smart--Cities-Energy--Aware-10B981?style=for-the-badge" />
  <img alt="License" src="https://img.shields.io/badge/license-MIT-green?style=for-the-badge" />
</p>

---

## Overview

**Adaptive Edge Sensor Orchestration Lab** studies how edge intelligence can decide which sensors should remain active, standby, or inactive under changing urban sensing conditions. The project focuses on **adaptive sensor group selection**, **energy-aware scheduling**, **sensing-quality preservation**, and **reproducible evaluation**.

The repository is designed as an academic scaffold for AIoT, edge AI, smart-city sensing, and sustainable computing. It uses synthetic scenarios and does not make deployment claims.

---

## Research Question

> **Can adaptive edge orchestration reduce sensing energy cost while preserving sufficient sensing quality for smart-city analytics?**

---

## Research Objectives

| Objective | Description |
|---|---|
| Adaptive sensor selection | Select a useful sensor group instead of activating every available sensor. |
| Energy-quality trade-off | Balance reduced energy cost with coverage, reliability, and latency needs. |
| Edge scheduling | Assign active, standby, or inactive modes to each sensor. |
| Context awareness | Adapt to traffic density, weather, battery level, reliability, and network load. |
| Reproducible evaluation | Compare static, random, and adaptive policies under shared synthetic scenarios. |

---

## Edge Orchestration Architecture

<p align="center">
  <img src="assets/sensor-orchestration-architecture.svg" alt="Adaptive edge sensor orchestration architecture" width="96%" />
</p>

```mermaid
flowchart LR
    A[Urban Context] --> B[Edge Orchestrator]
    C[Sensor Registry] --> B
    D[Energy State] --> B
    E[Network State] --> B
    B --> F[Selected Sensor Group]
    F --> G[Sensing Task]
    G --> H[Quality and Energy Metrics]
    H --> I[Policy Feedback]
    I --> B
```

---

## Adaptive Selection Workflow

<p align="center">
  <img src="assets/adaptive-selection-workflow.svg" alt="Adaptive sensor selection workflow" width="96%" />
</p>

| Step | Purpose |
|---|---|
| Observe context | Read synthetic urban state such as traffic density, weather, priority, and network load. |
| Score sensors | Estimate utility from coverage, reliability, battery, latency, and sensing relevance. |
| Select group | Choose a compact group that meets a quality target with lower energy cost. |
| Schedule modes | Assign active, standby, or inactive status for each sensor. |
| Evaluate trade-off | Report energy saving, quality score, latency risk, and sensor-use balance. |

---

## Energy-Quality Dashboard Concept

<p align="center">
  <img src="assets/energy-quality-dashboard.svg" alt="Energy-quality dashboard for adaptive edge sensing" width="96%" />
</p>

---

## Quick Start

```bash
git clone https://github.com/Hirakhyzer/adaptive-edge-sensor-orchestration-lab.git
cd adaptive-edge-sensor-orchestration-lab
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\\Scripts\\activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python examples/run_orchestration_demo.py
pytest
```

---

## Repository Structure

```text
adaptive-edge-sensor-orchestration-lab/
├── assets/
│   ├── banner.svg
│   ├── sensor-orchestration-architecture.svg
│   ├── adaptive-selection-workflow.svg
│   └── energy-quality-dashboard.svg
├── data/
│   └── scenario_templates.json
├── docs/
│   ├── research-background.md
│   ├── system-design.md
│   ├── evaluation-methodology.md
│   ├── responsible-aiot-boundary.md
│   └── scenario-catalogue.md
├── examples/
│   └── run_orchestration_demo.py
├── src/edge_sensor_orchestration/
│   ├── schema.py
│   ├── orchestrator.py
│   ├── simulation.py
│   └── evaluation.py
└── tests/
    └── test_orchestration.py
```

---

## Responsible AIoT Boundary

This repository is for synthetic experimentation, research, and education. It does not operate real devices, control physical infrastructure, collect personal data, or provide deployment instructions. Any real-world use would require safety, privacy, cybersecurity, and governance review.

---

## Expected Contributions

- A reusable AIoT framework for adaptive sensor group selection.
- A simple edge orchestration policy for energy-aware sensing.
- Synthetic scenarios for evaluating sensor scheduling decisions.
- Metrics for energy-quality trade-offs, latency risk, and sensor utilisation fairness.
- Research documentation for sustainable and responsible urban sensing.

---

## License

Released under the [MIT License](LICENSE).

---

## Author

Created by **Hira Khyzer** as an academic AIoT and smart-city sensing research prototype.