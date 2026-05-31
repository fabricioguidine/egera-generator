# Architecture

`egera-generator` is a small Python tool that filters a list of Portuguese words
by prefix, applying Unicode (NFC) normalization so accented characters behave
consistently across platforms.

## Components

### `gerador.py` (entrypoint)

- `normaliza(s)` — pure function; returns the NFC-normalized form of a string so
  that visually identical accented words compare equal regardless of how they
  were encoded.
- `carrega(path=OUT)` — reads a word-list file (UTF-8), stripping blank lines and
  normalizing each entry. Defaults to `palavras_completas.txt` next to the script.
- `gerar(prefixo, palavras)` — pure function; normalizes the prefix and returns
  the words that start with it.
- `main(argv=None)` — argparse CLI: positional `prefixo` (optional) and
  `--arquivo` (defaults to `OUT`). Loads, filters, and writes each match to
  stdout. Returns the result list.

### `gerar_todas_palavras.py` (auxiliary)

Standalone helper that regenerates `palavras_completas.txt` (placeholder logic:
all length-2 combinations over a Portuguese alphabet), writing UTF-8 output to a
path resolved relative to the script.

### `palavras_completas.txt`

The default versioned word list consumed by `gerador.py`.

## Data flow

```
palavras_completas.txt (or --arquivo)
            |
        carrega()  -> normalized list[str]
            |
        gerar(prefixo, ...)  -> filtered list[str]
            |
          stdout
```

## Cross-platform strategy

- **Paths**: `OUT` is `Path(__file__).resolve().parent / "palavras_completas.txt"`,
  anchoring file access to the script directory rather than the caller's working
  directory, with OS-correct separators.
- **Encoding**: files are opened with explicit `encoding="utf-8"`, and text is
  NFC-normalized so accents are handled uniformly on Linux, macOS, and Windows.
- **stdout**: `sys.stdout.reconfigure(encoding="utf-8")` runs inside a guarded
  `try/except (AttributeError, ValueError)`, replacing the older
  `sys.stdout = io.TextIOWrapper(sys.stdout.buffer, ...)` hack, so non-UTF-8
  consoles (notably Windows) print accented output without crashing.

## Testing strategy

`tests/test_gerador.py` exercises the public functions and the real CLI:

- Unit tests for `normaliza`, `gerar` (prefix filtering, empty prefix, accent
  normalization) and `carrega` (reading + normalization) using a `tmp_path`
  word file.
- End-to-end tests that spawn `gerador.py` via `subprocess` with `sys.executable`,
  passing `--arquivo` to a synthetic temp file and asserting stdout contents and
  exit codes (including the missing-file error case).

`tests/conftest.py` puts the repo root on `sys.path` so `import gerador` works.
The suite is hermetic (no network, `tmp_path` only) and OS-agnostic, and CI runs
it on Ubuntu, macOS, and Windows across Python 3.11-3.13.
