"""Central configuration (paper Section 4.3, 4.5).

All settings that affect results live here so that a run is fully
described by one configuration file. Nothing in the detector is tuned
on development results (paper, "Tuning and aggregation").
"""
from dataclasses import dataclass, field
from typing import Dict


@dataclass
class ModelConfig:
    """One LLM under test (paper Table: five configurations)."""
    name: str                    # e.g. "GLM-4", "ChatGPT", "TA-SQL+GLM-4"
    backend: str                 # "openai-api" | "zhipu-api" | "local-vllm" | "agent"
    endpoint: str = ""           # API base URL or local model path
    model_id: str = ""           # e.g. "gpt-3.5-turbo"
    temperature: float = 0.0     # fixed at 0 (paper Section 4.5)
    max_tokens: int = 2048
    extra: Dict = field(default_factory=dict)  # agent-specific (TA-SQL)


@dataclass
class CompareConfig:
    """Comparison semantics (paper Section 3.2)."""
    float_tol: float = 1e-6      # floating-point tolerance for R(q)
    order_insensitive: bool = True   # unless ORDER BY present


@dataclass
class RunConfig:
    model: ModelConfig
    compare: CompareConfig = field(default_factory=CompareConfig)
    judge_model: ModelConfig = None   # pair-validation judge (paper 3.3)
    prompts_dir: str = "prompts"
