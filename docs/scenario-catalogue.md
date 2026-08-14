# Scenario Catalogue

The repository uses synthetic scenarios to test whether adaptive grouping can reduce cost while preserving enough sensing quality.

## Example scenarios

| Scenario | Focus |
|---|---|
| Low-demand baseline | Checks whether the policy can reduce unnecessary activity. |
| High-demand corridor | Tests whether the policy preserves quality when demand increases. |
| Weather-complexity case | Tests how reliability and delay affect group formation. |
| Battery-constrained case | Tests whether low-battery nodes are protected. |
| Mixed-priority case | Tests quality-cost balance under changing assumptions. |

## Scenario fields

- `scenario_id`
- `demand`
- `complexity`
- `priority`
- `load`
- `target_quality`

All values are synthetic and normalised between 0 and 1.