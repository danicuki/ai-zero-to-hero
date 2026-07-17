"""toktool — how many tokens is this, and how many cents?

Run from the repo root:

    uv run projects/toktool/toktool.py "some text"
    uv run projects/toktool/toktool.py --file README.md --model gemini-3.5-flash
    uv run projects/toktool/toktool.py "hello" --out 500
"""

from pathlib import Path
from typing import Optional

import typer
from dotenv import load_dotenv
from google import genai
from rich.console import Console
from rich.table import Table

REPO_ROOT = Path(__file__).resolve().parents[2]
load_dotenv(REPO_ROOT / ".env")

console = Console()
app = typer.Typer(add_completion=False, help=__doc__)

# USD per 1M tokens. From resources/providers.md — verify against the pricing
# page, this moves fast.
PRICING = {
    "gemini-3.5-flash": {"in": 1.50, "out": 9.00, "cached_in": 0.15},
    "gemini-3.1-pro": {"in": 2.00, "out": 12.00, "cached_in": 0.20},
    "gemini-2.5-flash-lite": {"in": 0.10, "out": 0.40, "cached_in": 0.01},
}
DEFAULT_MODEL = "gemini-3.5-flash"


def count_tokens(client: genai.Client, model: str, text: str) -> int:
    """Return the number of input tokens `model` will see for `text`.

    TODO(day-1): implement me with the Gemini count_tokens API.
    """
    client = genai.Client()

    total_tokens = client.models.count_tokens(
        model=model,
        contents=text
    )

    return total_tokens.total_tokens

def estimate_cost(model: str, in_tokens: int, out_tokens: int, cached: bool = False) -> float:
    """Cost in USD for a single call of in_tokens -> out_tokens."""
    p = PRICING[model]
    in_rate = p["cached_in"] if cached else p["in"]
    return (in_tokens * in_rate + out_tokens * p["out"]) / 1_000_000


def load_text(text: Optional[str], file: Optional[Path]) -> str:
    if file:
        return file.read_text()
    if text:
        return text
    raise typer.BadParameter("give me TEXT or --file")


@app.command()
def main(
    text: Optional[str] = typer.Argument(None, help="Text to tokenize."),
    file: Optional[Path] = typer.Option(
        None, "--file", "-f", exists=True, dir_okay=False, help="Read text from a file instead."
    ),
    model: str = typer.Option(DEFAULT_MODEL, "--model", "-m", help=f"One of: {', '.join(PRICING)}"),
    out_tokens: int = typer.Option(500, "--out", help="Assumed output tokens, for the cost estimate."),
) -> None:
    if model not in PRICING:
        raise typer.BadParameter(f"unknown model {model!r}; known: {', '.join(PRICING)}")

    content = load_text(text, file)
    client = genai.Client()  # reads GEMINI_API_KEY from the environment

    n = count_tokens(client, model, content)

    table = Table(title=f"{model} — {n:,} input tokens", title_justify="left")
    table.add_column("Scenario")
    table.add_column("Cost (USD)", justify="right")
    table.add_row(
        f"{n:,} in + {out_tokens:,} out",
        f"${estimate_cost(model, n, out_tokens):.6f}",
    )
    table.add_row(
        f"{n:,} cached in + {out_tokens:,} out",
        f"${estimate_cost(model, n, out_tokens, cached=True):.6f}",
    )
    console.print(table)


if __name__ == "__main__":
    app()
