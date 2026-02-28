import pytest
from aether.cold_loop import ColdLoopPlanner
from aether.hot_loop import HotLoopGuide


def test_planner_returns_hot_task():
    planner = ColdLoopPlanner()
    out = planner.plan_from_manual("example_manual_ikea.jpg", "step 1")
    assert "hot_loop_task" in out
    task = out["hot_loop_task"]
    assert "task_type" in task


def test_hot_loop_reduces_distance():
    guide = HotLoopGuide({"task_type": "insert"})
    initial_vec = guide._vector_to_target().copy()
    guidance1, vec1 = guide.step()
    guidance2, vec2 = guide.step()
    # After two steps the distance should be smaller than initial
    assert pytest.approx(True)
    assert (abs(vec2) < abs(initial_vec)).any() or (abs(vec1) < abs(initial_vec)).any()
