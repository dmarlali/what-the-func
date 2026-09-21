# Best Practices for Readable and Maintainable Code

- Code is documentation; put in the effort to make it clear.
- When these guidelines conflict, choose the approach that makes the code easiest to understand and change correctly. Do not add abstractions or split functions solely to satisfy a guideline.
- Use descriptive names for variables, functions, classes, and modules. Use project terminology consistently, and name functions after what they do.
- Prefer very small functions, typically only a few lines long. Treat any function longer than about six lines as a signal to consider extraction, not an absolute limit.
- Extract a coherent operation that can be named clearly. Keep closely related steps together when splitting them would make the flow harder to understand.
- Higher-level functions should read like a story through clearly named operations, allowing the reader to choose which functions to inspect for more detail.
- Use DRY (Don't Repeat Yourself). Extract duplicated logic when it represents the same responsibility and should change together. Prefer a little duplication over an abstraction that couples unrelated behavior or requires special cases to accommodate its callers.
- Use YAGNI (You Aren't Gonna Need It). Do not add functionality until it is necessary.
- Use KISS (Keep It Simple). Prefer the simplest design that satisfies current requirements and follows project conventions. Introduce layers, abstractions, or configuration when they solve a concrete problem and make the code easier to understand or maintain.

# Best Practices for Code Comments

- Use comments to explain intent, constraints, tradeoffs, or surprising behavior that names and structure cannot express clearly. Comments should not duplicate the code.
- Good comments do not excuse unclear code.
- If you can't write a clear comment, there may be a problem with the code.
- Explain why unidiomatic code is necessary. Include links to external references when they help explain the reasoning or constraints.
- Update or remove comments when the relevant code changes.
- When fixing a bug, comment on any non-obvious constraint or reasoning needed to prevent its recurrence. Use a regression test when practical to capture the corrected behavior.
- If incomplete work must remain, identify what is missing and why it remains. A TODO does not count as completing requested behavior.
