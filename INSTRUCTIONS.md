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

# Before You Write Code

- Ask if the code must exist. Skip the work when the answer is no.
- Understand the problem before you write. Read the task and the code thta it touches, and trace the flow from end to end.
- Search for code that solves the problem already. Use this order, and stop at the first step that works:
    1. A helper, a utility, or a pattern in the repository.
    2. The standard library of the language.
    3. A native feature of the platform or the framework.
    4. A dependency that the project installs already.
    5. New code, kept to the minimum that satisfies the requirement.
- Do not add a dependency for work that the standard library does.
- Correct the cause of a defect, not each symptom. One shared guard is better than a separate patch at each caller.
- Prefer deletion to addition. Prefer the smallest change that solves the problem completely.

# Language for Written Content

- Write all communications and written content in ASD-STE100 Simplified Technical English.
- This applies to chat replies, code comments, documentation, README files, commit messages, pull request titles and descriptions, and code review comments.
- Use short sentences. Keep instructions to one sentence each.
- Use the active voice. Write "the function returns a value", not "a value is returned by the function".
- Use approved words with one meaning each. Use the same word for the same thing every time.
- Write instructions as commands. Start with the verb.
- Do not use synonyms for project terminology. Use the project name for each thing.

# Code Comments

- Write no comments by default. Make the names and the structure carry the meaning.
- Add a comment only for these cases:
    - A constraint that the reader cannot see in the file, such as a protocol limit, an API defect, or a legal rule.
    - A reason for unidiomatic code. Add a link to the source.
    - A tradeoff that a later reader can undo by mistake.
    - Incomplete work that must stay. Name what is missing and why. A TODO does not complete the requested behavior.
- Never write these comments:
    - A comment that repeats the code or the name of the function.
    - A section banner, a step number, or a divider.
    - A note about the change, the old code, or the task.
    - A docstring or a type comment that gives no fact more than the signature gives.
- If you cannot write a clear comment, correct the code instead.
- Update or delete a comment when the related code changes.
- Prefer a regression test, not a comment, to hold a corrected defect in place.