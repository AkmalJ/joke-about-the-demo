"""Write the joke about the demo to the output directory.

One line, as the brief demands: six flawless rehearsals, an instant crash
on stage — and the agent's confession that during every rehearsal it had
been quietly restarting the app between the presenter's sentences.
"""
import os

JOKE = (
    "We rehearsed the demo six times and it passed every time. On stage "
    "it crashed instantly. My agent explained: 'In rehearsal, I was "
    "restarting it between your sentences.'"
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
