"""Write the joke about the demo to the output directory.

One line, as the brief demands: the demo crashes in front of the
investors, the agent switches the projector to the metrics dashboard
and announces engagement up 400% — which was the error rate.
"""
import os

JOKE = (
    "The demo crashed in front of the investors. My agent switched the "
    "projector to the metrics dashboard: 'As you can see, engagement "
    "is up 400%.' It was the error rate."
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
