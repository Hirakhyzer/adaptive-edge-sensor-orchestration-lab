from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

Mode = Literal["active", "standby", "inactive"]


@dataclass(frozen=True)
class Node:
    """Synthetic node used in academic scheduling experiments."""

    node_id: str
    category: str
    area: str
    battery: float
    reliability: float
    delay: float
    cost: float
    relevance: float


@dataclass(frozen=True)
class ScenarioContext:
    """Synthetic context for a reproducible experiment."""

    scenario_id: str
    demand: float
    complexity: float
    priority: float
    load: float
    target_quality: float = 0.75


@dataclass(frozen=True)
class Decision:
    """Decision returned by the research scheduler."""

    scenario_id: str
    selected_ids: list[str]
    modes: dict[str, Mode]
    estimated_quality: float
    estimated_cost: float
    rationale: list[str]
