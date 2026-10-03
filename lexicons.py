"""Lexicons and parsing utilities (paper Section 3.3, "Lexicons").

Sources (fixed, compiled from Spider/BIRD TRAINING splits only):
  - comparative lexicon: ~120 English comparatives
  - synonyms/antonyms: WordNet (NLTK), sense-filtered by the LLM judge
  - prefix set: {"Tell me", "Show me", "List", ...}
  - SC adjunct templates: ~30 domain-neutral adjuncts
"""
import nltk  # noqa: F401  (WordNet via nltk.corpus.wordnet)

# TODO: replace with the shipped lexicon files (lexicons/comparatives.txt etc.)
COMPARATIVE_LEXICON = {"older than", "younger than", "greater than", "more than",
                       "less than", "lower than", "higher than", "exceeds"}
PREFIX_SET = ["Tell me", "Show me", "List", "Find"]
SC_ADJUNCTS = ["if possible", "please", "in your answer"]


def find_comparatives(question: str):
    """POS-pattern + lexicon matching for comparative words/phrases."""
    raise NotImplementedError  # TODO: POS tag + multiword pattern matching


def synonym_candidates(word: str):
    """WordNet synonyms; the LLM judge decides acceptance (paper 3.3)."""
    raise NotImplementedError


def antonym_candidates(word: str):
    raise NotImplementedError


def schema_non_synonyms(entity: str, schema_entities):
    """ENSR replacements drawn from the same schema (guaranteed non-synonym)."""
    raise NotImplementedError
