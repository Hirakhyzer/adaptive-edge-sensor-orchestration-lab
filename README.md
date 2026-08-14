<p align="center">
  <img src="assets/banner.svg" alt="Adaptive Edge Sensor Orchestration Lab banner" width="100%" />
</p>

<h1 align="center">Adaptive Edge Sensor Orchestration Lab</h1>

<p align="center">
  <b>Academic AIoT research prototype for adaptive edge sensing, group selection, and energy-quality trade-off analysis using synthetic scenarios.</b>
</p>

<p align="center">
  <img alt="Status" src="https://img.shields.io/badge/status-research--prototype-7C3AED?style=for-the-badge" />
  <img alt="Python" src="https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge&logo=python&logoColor=white" />
  <img alt="AIoT" src="https://img.shields.io/badge/AIoT-Edge--Sensing-06B6D4?style=for-the-badge" />
  <img alt="License" src="https://img.shields.io/badge/license-MIT-green?style=for-the-badge" />
</p>

---

## Overview

**Adaptive Edge Sensor Orchestration Lab** studies how edge intelligence can form compact sensing groups under changing synthetic smart-city scenarios. The project focuses on energy-aware scheduling, quality preservation, candidate ranking, and reproducible evaluation.

This is a research and teaching repository. It uses synthetic examples only and does not operate real devices or make deployment claims.

---

## Research Question

> Can adaptive edge sensing reduce estimated cost while preserving useful sensing quality?

---

## Research Objectives

| Objective | Description |
|---|---|
| Adaptive group selection | Choose a compact group instead of using every candidate. |
| Energy-quality trade-off | Compare estimated cost with expected sensing quality. |
| Context awareness | Use synthetic demand, complexity, priority, and load variables. |
| Reproducible evaluation | Compare strategies with shared assumptions and documented metrics. |

---

## Architecture

<p align="center">
  <img src="assets/sensor-orchestration-architecture.svg" alt="Adaptive edge sensing architecture" width="96%" />
</p>

---

## Workflow

<p align="center">
  <img src="assets/workflow.svg" alt="Research workflow" width="96%" />
</p>

```text
Synthetic context -> candidate ranking -> compact group -> metric report
```

---

## Dashboard Concept

<p align="center">
  <img src="assets/dashboard.svg" alt="Energy-quality dashboard" width="96%" />
</p>

---

## Quick Start

```bash
git clone https://github.com/Hirakhyzer/adaptive-edge-sensor-orchestration-lab.git
cd adaptive-edge-sensor-orchestration-lab
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\\Scripts\\activate
python -m pip install -e .
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
│   ├── workflow.svg
│   └── dashboard.svg
├── data/
│   └── README.md
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
│   └── evaluation.py
└── tests/
    └── test_orchestration.py
```

---

## Responsible AIoT Boundary

This repository is for synthetic experimentation, research, and education. Real-world use would require safety, privacy, cybersecurity, and governance review.

---

## License

Released under the [MIT License](LICENSE).

---

## Author

Created by **Hira Khyzer** as an academic AIoT and smart-city sensing research prototype.