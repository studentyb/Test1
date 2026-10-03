"""LLM invocation layer: SL() and Synth() (paper Section 3.6).

Both artifacts are produced by the LLM under test itself:
  - SL(Q, D)      -> schema linking as JSON pairs  (prompts/schema_linking.txt)
  - Synth(Q, SSL, D) -> SQL query                  (prompts/sql_synthesis.txt)

The pair-validation judge (paper 3.3) uses prompts/pair_validation.txt.
Exact prompts ship in ./prompts and are frozen per release.
"""
import json


def call_llm(model_cfg, prompt: str) -> str:
    """Single generation call, temperature 0. TODO: wire your backend."""
    raise NotImplementedError


def parse_linking(raw: str):
    """Parse the LLM's JSON artifact into a set of (table, column) pairs."""
    obj = json.loads(raw)
    return {(e["table"].lower(), e["column"].lower()) for e in obj["pairs"]}


def parse_sql(raw: str) -> str:
    """Strip markdown fences if present; return the SQL text."""
    raise NotImplementedError
