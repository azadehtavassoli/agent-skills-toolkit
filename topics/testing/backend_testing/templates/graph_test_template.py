import pytest


def test_graph_topology_contains_expected_nodes():
    graph = build_graph()

    node_names = set(graph.nodes.keys())

    assert "ValidateContext" in node_names
    assert "ClassifyIntent" in node_names


@pytest.mark.asyncio
async def test_graph_fails_closed_on_missing_workspace(compiled_graph):
    state = {
        "request_id": "req-1",
        "workspace_id": "",
        "intent": "qa",
        "payload": {"query": "hello"},
        "route": None,
        "status": "ok",
        "result": {},
        "errors": [],
        "meta": {},
    }

    with pytest.raises(ValueError):
        await compiled_graph.ainvoke(state)


@pytest.mark.asyncio
async def test_graph_returns_expected_route(compiled_graph):
    state = {
        "request_id": "req-1",
        "workspace_id": "ws-1",
        "intent": "qa",
        "payload": {"query": "hello"},
        "route": None,
        "status": "ok",
        "result": {},
        "errors": [],
        "meta": {},
    }

    result = await compiled_graph.ainvoke(state)

    assert result["route"] == "qa"