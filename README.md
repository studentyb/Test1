
## Contents (inventory)

| Path | Description | Paper section |
|---|---|---|
| `README.md` | this file | — |
| `sqlhd/config.py` | model/compare/run configuration (temperature 0; no tunable detector thresholds) | §4.3, §4.5 |
| `sqlhd/lexicons.py` | comparative lexicon (~120 entries, from Spider/BIRD *train* splits), prefix set, SC adjunct templates, WordNet synonym/antonym utilities | §3.3 |
| `sqlhd/transforms.py` | the 17 MR input transformations sigma | §3.4, §3.5, Table 1 |
| `sqlhd/mrs.py` | MR registry: name -> (sigma, OP, valid); stage-one and stage-two sets | §3.2 |
| `sqlhd/llm.py` | LLM invocation: SL() (schema linking as JSON pairs), Synth() (SQL), pair-validation judge calls | §3.6, §3.3 |
| `sqlhd/execution.py` | R(q): SQLite execution, bag semantics, order-insensitive unless ORDER BY, float tolerance 1e-6, bottom on failure | §3.2 |
| `sqlhd/detector.py` | Algorithm 1: two-stage detection with per-MR evidence | §3.6 |
| `sqlhd/metrics.py` | Precision/Recall/F1/Accuracy, HDN/HDR, confusion counts | §4.5 |
| `sqlhd/runner.py` | CLI to reproduce any paper cell (variant x configuration x method) | §5 |
| `prompts/schema_linking.txt` | SL prompt (frozen) | §3.6 |
| `prompts/sql_synthesis.txt` | Synth prompt (frozen) | §3.6 |
| `prompts/pair_validation.txt` | pair-validation judge prompt + checklist | §3.3 |
| `data/` | mutated variants (SGLMD, SGPMD, BGLMD, BGPMD) or the generation scripts that produce them from Spider/BIRD dev splits | §4.2 |
| `results/` | per-cell result JSON files used in the paper's tables and figures | §5 |

## Setup

```bash
pip install -r requirements.txt
python -c "import nltk; nltk.download('wordnet'); nltk.download('averaged_perceptron_tagger')"
```

## Reproducing the paper's results

All generation uses temperature 0; the detector has no tunable
thresholds (see "Tuning and aggregation", paper §4.5).

```bash
# SQLHD on one cell:
python -m sqlhd.runner --variant SGLMD --model GLM-4 --out results/SGLMD_GLM-4.json

# Self-Evaluation baselines on the same generations:
python -m sqlhd.runner --variant SGLMD --model GLM-4 --baseline selfeval_bool --out results/SGLMD_GLM-4_bool.json
python -m sqlhd.runner --variant SGLMD --model GLM-4 --baseline selfeval_prob --out results/SGLMD_GLM-4_prob.json
```

Labels for evaluation are derived from the benchmarks' gold SQL and
schema (paper §4.5): (i) linking references tables/columns absent from
the schema, or (ii) the executed result differs from the executed gold
SQL under the comparison semantics of §3.2. Labels are used for
evaluation only; detection never requires gold SQL.

## Notes

- TA-SQL+GLM-4 is run through its agent interface with GLM-4 as the backbone.
- Qwen2.5-32B is served locally; the other models are called through
  their official APIs with the endpoints recorded in `sqlhd/config.py`.
- The four mutated variants share their source questions (paper §4.5);
  report per-variant metrics, do not pool.


