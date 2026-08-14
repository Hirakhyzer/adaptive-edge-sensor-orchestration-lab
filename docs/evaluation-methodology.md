# Evaluation Methodology

The evaluation compares multiple policies under identical synthetic scenarios.

## Baselines

| Policy | Description |
|---|---|
| Full-use baseline | Uses every available candidate as the reference cost. |
| Random group | Chooses a fixed-size group without context scoring. |
| Adaptive group | Ranks candidates using relevance, reliability, battery, delay, cost, and scenario context. |

## Metrics

| Metric | Meaning |
|---|---|
| Quality score | Estimated usefulness of the selected group. |
| Cost reduction | Reduction compared with the full-use baseline. |
| Group size | Number of selected candidates. |
| Balance | Whether the same candidates are overused across scenarios. |

## Reporting rules

- Use the same scenario set across policies.
- Report all assumptions and random seeds.
- Avoid deployment claims from synthetic results.
- Treat results as research evidence, not operational certification.
