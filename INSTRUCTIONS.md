# Best Practices for Readable and Maintainable Code

- Code is documentation; put in the effort to make it clear.
- Don't repeat yourself. If you find yourself writing the same code multiple times, consider refactoring it into a reusable function or module.
- Use variable names that explain themselves.
- If a fragment of code takes effort to understand, extract it into a function and name the function after what it does.
- Write very small functions, typically only a few lines long.
- Treat any function longer than about six lines as a signal to consider extracting well-named functions. This is a judgment call, not an absolute limit.
- Small functions work only when their names are good, so pay close attention to naming. This approach makes code self-documenting.
- Larger-scale functions should read like a story, allowing the reader to choose which functions to inspect for more detail.
- Use YAGNI (You Aren't Gonna Need It). Do not add functionality until it is necessary.
- Use DRY (DOn't Repeat Yourself). Extract duplicated logic into reusable components—like functions, classes, or variables—to ensure every piece of system behavior has a single, unambiguous source of truth.

# Best Practices for Code Comments

- Comments should not duplicate the code.
- Good comments do not excuse unclear code.
- If you can't write a clear comment, there may be a problem with the code.
- Comments should dispel confusion, not cause it.
- Explain unidiomatic code in comments.
- Include links to external references where they are most helpful.
- Add comments when fixing bugs.
- Use comments to mark incomplete implementations.
