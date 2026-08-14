from edge_sensor_orchestration import EdgeSensorOrchestrator, Node, ScenarioContext

items = [
    Node("node_a", "visual", "zone_a", 0.92, 0.88, 80.0, 1.20, 0.96),
    Node("node_b", "environment", "zone_b", 0.70, 0.83, 50.0, 0.70, 0.65),
    Node("node_c", "edge", "zone_c", 0.86, 0.91, 40.0, 0.95, 0.94),
    Node("node_d", "weather", "zone_d", 0.58, 0.79, 60.0, 0.55, 0.58),
]

context = ScenarioContext("synthetic_context_001", 0.88, 0.62, 0.80, 0.36)
decision = EdgeSensorOrchestrator(group_size=3).run(items, context)

print("Scenario:", decision.scenario_id)
print("Selected group:", ", ".join(decision.selected_ids))
print("Quality score:", decision.estimated_quality)
print("Estimated cost:", decision.estimated_cost)
