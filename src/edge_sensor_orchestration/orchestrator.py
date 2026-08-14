from __future__ import annotations

from .schema import Decision, Node, ScenarioContext


class EdgeSensorOrchestrator:
    def __init__(self, group_size: int = 3) -> None:
        self.group_size = group_size

    def score(self, item: Node, context: ScenarioContext) -> float:
        return round(item.relevance + item.reliability + item.battery - item.cost - context.load, 4)

    def run(self, items: list[Node], context: ScenarioContext) -> Decision:
        ranked = sorted(items, key=lambda item: self.score(item, context), reverse=True)
        group = ranked[: self.group_size]
        ids = [item.node_id for item in group]
        return Decision(
            scenario_id=context.scenario_id,
            selected_ids=ids,
            modes={item.node_id: ("active" if item.node_id in ids else "standby") for item in items},
            estimated_quality=round(sum(max(0.0, self.score(item, context)) for item in group) / max(1, self.group_size), 3),
            estimated_cost=round(sum(item.cost for item in group), 3),
            rationale=["ranked items", "formed group", "computed metrics"],
        )
