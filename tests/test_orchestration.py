from edge_sensor_orchestration import EdgeSensorOrchestrator, Node, ScenarioContext


def test_orchestrator_returns_requested_group_size():
    items = [
        Node("a", "type", "zone", 0.9, 0.9, 10.0, 0.2, 0.9),
        Node("b", "type", "zone", 0.8, 0.8, 12.0, 0.3, 0.8),
        Node("c", "type", "zone", 0.7, 0.7, 14.0, 0.4, 0.7),
    ]
    context = ScenarioContext("case", 0.8, 0.5, 0.7, 0.2)
    decision = EdgeSensorOrchestrator(group_size=2).run(items, context)

    assert len(decision.selected_ids) == 2
    assert decision.estimated_quality >= 0
    assert decision.estimated_cost > 0
