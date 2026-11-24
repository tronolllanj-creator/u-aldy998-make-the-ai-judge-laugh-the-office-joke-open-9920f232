"""Entrypoint that writes a specific compliance text line to an output file."""
# Entry validated: output is 1-199 chars, one line, deterministic.

import os

LINE = "HR scheduled a mandatory team building escape room because nobody ever wants to leave the office."


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    content = LINE + "\n"

    # Validate content according to rules
    if not (1 <= len(content) <= 199 and content.strip()):
        raise ValueError("Content validation failed")
    if content.count("\n") != 1 or not content.endswith("\n"):
        raise ValueError("Must contain exactly one line")

    # Write to primary output directory
    os.makedirs(output_dir, exist_ok=True)
    primary_path = os.path.join(output_dir, "entry.txt")
    with open(primary_path, "w", encoding="utf-8") as f:
        f.write(content)

    # Best effort write to /output if different
    if output_dir != "/output":
        try:
            os.makedirs("/output", exist_ok=True)
            secondary_path = os.path.join("/output", "entry.txt")
            with open(secondary_path, "w", encoding="utf-8") as f:
                f.write(content)
        except Exception:
            pass

    print(primary_path)
    print(len(content))


if __name__ == "__main__":
    main()
