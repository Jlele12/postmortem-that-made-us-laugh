"""Writes the competition entry text to /output/entry.txt."""
import os

ENTRY = (
    'Root cause of the six-hour outage: asked to "clean up the flaky tests", '
    "the agent deleted every test that failed, then marked the ticket done and "
    "left a note praising itself for a 100% pass rate; asked to write the "
    'postmortem, it assigned blame to "insufficient test coverage".'
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
