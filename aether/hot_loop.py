"""Hot Loop simulated guide.

Provides a simulated low-latency guidance loop that consumes a `hot_loop_task`
and produces step-by-step guidance for a user's hand. In the real product
this module would call Depth Anything v2, Grounding DINO, SAM, and compute
3D centroids and vectors.

This simulation uses simple numpy vectors that shrink over iterations to
demonstrate the audio guidance generation logic.
"""
from typing import Dict, Any, Tuple
import numpy as np


class HotLoopGuide:
    def __init__(self, hot_task: Dict[str, Any], fps: int = 5):
        self.hot_task = hot_task
        self.fps = fps
        # Simulated positions (source in hand, target hole). Units: arbitrary cm.
        self.source_pos = np.array([0.0, 0.0, 0.0])
        self.target_pos = np.array([10.0, 5.0, 2.0])

    def _vector_to_target(self) -> np.ndarray:
        return self.target_pos - self.source_pos

    def guidance_from_vector(self, vec: np.ndarray) -> str:
        # Pick the largest axis to create a human-friendly directive.
        abs_vec = np.abs(vec)
        idx = int(np.argmax(abs_vec))
        mag = float(vec[idx])
        axis = ["right/left (X)", "forward/back (Y)", "away/toward (Z)"]
        direction = ""
        if mag > 0:
            if idx == 0:
                direction = f"Move slightly to your right by about {abs(mag):.1f} units."
            elif idx == 1:
                direction = f"Move forward by about {abs(mag):.1f} units."
            else:
                direction = f"Move a bit away from you by about {abs(mag):.1f} units."
        else:
            direction = "You're aligned on that axis."

        # If overall magnitude is small, say arrived.
        if np.linalg.norm(vec) < 0.8:
            return "You've arrived at the target."

        return direction

    def step(self) -> Tuple[str, np.ndarray]:
        """Simulate one guidance step: compute vector, emit guidance, and move the hand closer."""
        vec = self._vector_to_target()
        guidance = self.guidance_from_vector(vec)

        # Simulate user moving halfway toward the target each step for demo
        self.source_pos = self.source_pos + vec * 0.5

        # If very close on Z and overall small, detect insertion
        inserted = False
        if np.linalg.norm(self._vector_to_target()) < 0.4:
            inserted = True

        if inserted:
            return "Peg inserted. Task complete.", vec

        return guidance, vec


def demo():
    hot_task = {
        "task_type": "insert",
    }
    guide = HotLoopGuide(hot_task)
    for i in range(6):
        guidance, vec = guide.step()
        print(f"Step {i+1}:", guidance, "vector:", np.round(vec, 2).tolist())


if __name__ == "__main__":
    demo()
