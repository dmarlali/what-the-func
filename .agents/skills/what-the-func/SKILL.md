---
name: what-the-func
description: Audit a repository for readable, maintainable code using the user's shared coding rules. Use when asked to audit, review, or inspect a codebase for naming, duplication, function clarity and size, unnecessary functionality, or comment quality. Report findings first; do not edit code unless the user later selects findings to fix.
---

# What the Func

Audit the requested repository against the shared coding rules available in the active agent instructions.

## Audit

1. Read the shared rules and any instructions that apply within the target repository.
2. Identify first-party source and test code. Exclude dependencies, generated files, vendored code, caches, and build output.
3. Inspect enough of the repository to support the requested scope. Prefer complete coverage for small repositories; use a representative sample for large repositories and say what was and was not reviewed.
4. Evaluate naming, duplication, function clarity and size, unnecessary functionality, and comment quality. Judge function size by focus and level of abstraction, not by line count. Report function names that are a bare verb with no object.
5. Report findings without modifying files.

## Report

Order findings by severity and practical impact. Give each finding:

- a stable number so the user can select it later;
- severity (`high`, `medium`, or `low`);
- an exact file and line location;
- the applicable shared rule;
- concrete evidence and why it affects readability or maintainability;
- a focused suggested improvement.

Avoid style-only findings that lack a clear maintenance cost. Mention positive patterns only when they help explain coverage or why no findings were reported. End with coverage, excluded areas, and any limitations.

If there are no actionable findings, say so plainly and still state the coverage.

## Fix Selected Findings

Only modify code after the user explicitly selects findings to fix. Preserve behavior, keep the change limited to those findings, and follow repository instructions. Run the most relevant available checks and report what changed and what was verified.
