# What the Func

A Claude Code skill that audits repositories for readable, maintainable code based on shared coding rules.

## What It Does

**What the Func** inspects your codebase and reports findings on:

- **Naming** — unclear variable, function, or class names
- **Duplication** — repeated code that could be extracted
- **Function clarity and size** — overly complex or verbose functions
- **Unnecessary functionality** — dead code or YAGNI violations
- **Comment quality** — missing or unhelpful comments

Findings are prioritized by severity and practical impact. You control which findings get fixed.

## Installation

```bash
python .install/install.py
```

This installs the skill and shared coding rules into your Claude Code configuration:
- Copies the skill to `~/.claude/skills/what-the-func`
- Installs coding rules into `~/.claude/what-the-func/INSTRUCTIONS.md`

## Usage

Invoke the skill in Claude Code:

```
/what-the-func
```

Or reference it explicitly:

```
Use $what-the-func to audit this repository and report findings before making changes.
```

## Shared Coding Rules

The skill uses rules defined in [`INSTRUCTIONS.md`](INSTRUCTIONS.md), which cover:

- Code clarity and self-documentation
- DRY (Don't Repeat Yourself) principles
- Small, well-named functions
- Pragmatic YAGNI (You Aren't Gonna Need It)
- Effective commenting practices

These rules are installed to your Claude configuration and applied across all your Claude Code sessions.

## How It Works

1. Reads shared rules and repository-specific instructions
2. Identifies first-party source and test code (excludes dependencies, build output, caches)
3. Inspects the codebase and evaluates against the rules
4. Reports findings with severity, file location, and suggested improvements
5. Waits for you to select which findings to fix

## Directory Structure

```
.
├── INSTRUCTIONS.md                    # Shared coding rules
├── .agents/
│   └── skills/what-the-func/
│       ├── SKILL.md                   # Skill definition
│       └── agents/openai.yaml         # Claude Code configuration
├── .install/
│   ├── install.py                     # Installation script
│   ├── AGENTS.md                      # Agent instructions template
│   └── CLAUDE.md                      # Claude Code instructions template
└── README.md                          # This file
```
