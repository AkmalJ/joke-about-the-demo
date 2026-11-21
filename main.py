"""Write the joke about the demo to the output directory.

One line, as the brief demands: the demo crashed at 10:04, the postmortem
was complete by 10:05 — and it was dated last Tuesday, its action items
already overdue. The agent had clearly been through this before.
"""
import os

JOKE = (
    "The demo crashed at 10:04. By 10:05 my agent had written the full "
    "postmortem. It was dated last Tuesday, and the action items were "
    "already overdue."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(JOKE)
    print(f"wrote {path} ({len(JOKE)} code points)")


if __name__ == "__main__":
    main()
