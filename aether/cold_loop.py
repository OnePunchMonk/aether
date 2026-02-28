"""Cold Loop planner stub.

This module simulates a high-level planner that would normally call a
large multimodal model (e.g., Gemini) to parse a manual/diagram and return
a simple machine-readable `hot_loop_task` dict used by the Hot Loop.

Replace `ColdLoopPlanner.plan_from_manual` with a real API call to Gemini
or another LLM when integrating.
"""
from typing import Dict, Any
import os


class ColdLoopPlanner:
    """A simple planner that produces a hot_loop_task from an image path and a note.

    For demonstration we return a deterministic sample when the filename
    contains certain keywords; otherwise a generic 'pick-and-place' task.
    """

    def plan_from_manual(self, image_path: str, user_note: str) -> Dict[str, Any]:
        # In a real system, encode the image and call Gemini API here.
        filename = os.path.basename(image_path or "").lower()

        if "ikea" in filename or "manual" in filename:
            return {
                "explanation": "Insert four wooden pegs into the long plank holes.",
                "hot_loop_task": {
                    "task_type": "insert",
                    "hand_object_prompt": "wooden peg, small dowel",
                    "target_object_prompt": "long plank, wooden board",
                    "target_sub_object_prompt": "small circular hole, peg hole",
                },
            }

        # Generic fallback
        return {
            "explanation": "Pick up the small object and place it in the box.",
            "hot_loop_task": {
                "task_type": "place",
                "hand_object_prompt": "small object, token",
                "target_object_prompt": "box, container",
                "target_sub_object_prompt": "opening, slot",
            },
        }


def demo():
    planner = ColdLoopPlanner()
    print(planner.plan_from_manual("example_manual_ikea.jpg", "I'm on Step 1"))


if __name__ == "__main__":
    demo()
