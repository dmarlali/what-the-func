from pathlib import Path
import shutil


MARKER = "<!-- what-the-func:start -->"
REPOSITORY_ROOT = Path(__file__).resolve().parent.parent
SKILL_SOURCE = REPOSITORY_ROOT / ".agents" / "skills" / "what-the-func"


def install_managed_instructions(source, destination, instructions_path):
    managed_text = source.read_text(encoding="utf-8").replace(
        "{{INSTRUCTIONS_PATH}}",
        instructions_path.as_posix(),
    )

    if not destination.exists():
        destination.write_text(managed_text, encoding="utf-8")
        return

    existing_text = destination.read_text(encoding="utf-8")
    if MARKER in existing_text:
        existing_text = replace_managed_section(existing_text, managed_text)
    else:
        existing_text = f"{existing_text.rstrip()}\n\n{managed_text}"

    destination.write_text(existing_text, encoding="utf-8")


def replace_managed_section(existing_text, managed_text):
    start = existing_text.index(MARKER)
    end = existing_text.index("<!-- what-the-func:end -->", start)
    end += len("<!-- what-the-func:end -->")
    return f"{existing_text[:start]}{managed_text.strip()}{existing_text[end:]}"


def install_skill(destination):
    shutil.copytree(SKILL_SOURCE, destination, dirs_exist_ok=True)


def main():
    home = Path.home()
    codex_root = home / ".codex"
    claude_root = home / ".claude"
    codex_data = codex_root / "what-the-func"
    claude_data = claude_root / "what-the-func"
    codex_skills = home / ".agents" / "skills"
    claude_skills = claude_root / "skills"

    for directory in (
        codex_root,
        claude_root,
        codex_data,
        claude_data,
        codex_skills,
        claude_skills,
    ):
        directory.mkdir(parents=True, exist_ok=True)

    instructions_source = REPOSITORY_ROOT / "INSTRUCTIONS.md"
    codex_instructions = codex_data / "INSTRUCTIONS.md"
    claude_instructions = claude_data / "INSTRUCTIONS.md"
    shutil.copy2(instructions_source, codex_instructions)
    shutil.copy2(instructions_source, claude_instructions)

    install_managed_instructions(
        REPOSITORY_ROOT / ".install" / "AGENTS.md",
        codex_root / "AGENTS.md",
        codex_instructions,
    )
    install_managed_instructions(
        REPOSITORY_ROOT / ".install" / "CLAUDE.md",
        claude_root / "CLAUDE.md",
        claude_instructions,
    )
    install_skill(codex_skills / "what-the-func")
    install_skill(claude_skills / "what-the-func")


if __name__ == "__main__":
    main()
