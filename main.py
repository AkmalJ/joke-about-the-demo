"""Write the joke about the demo to the output directory.

One line, as the brief demands: the demo crashes in front of everyone,
the agent does not fix it — it rebrands the error page as the new
landing page. Which, it turns out, already had a waitlist.
"""
import os

JOKE = (
    "The demo crashed in front of everyone. My agent didn't fix it — "
    "it rebranded the error page as our new landing page. It already "
    "had a waitlist."
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
