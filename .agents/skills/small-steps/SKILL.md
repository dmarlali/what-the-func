---
name: small-steps
description: Plan and make a change as small steps that the user reviews and commits one at a time.
disable-model-invocation: true
---

The user gives a task: a bug, a feature, or a refactor.

1. Read the code that the task touches. Trace the flow from end to end.
2. If the expected result is not clear, propose it in 3–5 bullets and wait for the user.
3. Do only the task that the user names. List other problems that you find under "Not done". Do not ask about them.
4. Ask only about decisions that change behavior or the API.
   For implementation details, choose a sensible default and list it as an assumption in the plan.
5. Make a plan with small steps:
   - Each step does one thing and keeps all tests green.
   - Each step is small enough to review in a few minutes.
   - Put a refactor that makes the change easier in its own step, before the change.
   - Use TDD when the step changes behavior.
6. Write the plan in this format:

   ## Goal
   One or two sentences about the result.

   ## Assumptions
   One line each.

   ## Steps
   ### 1. <what the step does>
   - Files: <files that change>
   - Test: <the test that proves the step>

   ## Not done
   One line each.

7. After approval, do one step. Then stop and show:
   - what changed and why, in 2–3 lines,
   - the test result,
   - a proposed commit message.
8. Wait for the user to review and commit. Then do the next step.
