"""Demo runner for Project Aether (scaffold).

This script demonstrates the Cold Loop -> Hot Loop flow using stubs and
simulations. It is intentionally lightweight so you can run it on a laptop
without heavy model dependencies.
"""
from aether.cold_loop import ColdLoopPlanner
from aether.hot_loop import HotLoopGuide
from aether.utils.audio import speak


def run_demo():
    # Cold loop: parse a mocked manual image and produce a hot loop task
    planner = ColdLoopPlanner()
    planned = planner.plan_from_manual("example_manual_ikea.jpg", "I'm on Step 1")
    explanation = planned.get("explanation")
    hot_task = planned.get("hot_loop_task")

    speak(f"Planner: {explanation}")

    # Hot loop: instantiate a guide and run a short simulated loop
    guide = HotLoopGuide(hot_task)

    speak("Starting hot loop guidance. I'll give short instructions now.")
    for i in range(12):
        guidance, vec = guide.step()
        # If the guide returns final message string
        if isinstance(guidance, str) and guidance.lower().startswith("peg inserted"):
            speak(guidance)
            break
        speak(guidance)

    speak("Demo complete.")


if __name__ == "__main__":
    run_demo()
