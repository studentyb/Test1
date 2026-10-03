"""Two-stage hallucination detection (Algorithm 1 in the paper).

Per sample and per MR: build (Q', D') = sigma(Q, D), obtain the
follow-up artifact from the LLM under test, execute for stage two,
and check OP. Any violation flags the sample and records the MR as
evidence. Stage two is reached only if every applicable stage-one MR
holds. For per-MR ablations, evaluate each MR independently.
"""
from .llm import call_llm, parse_linking, parse_sql
from .execution import exec_sql, BOTTOM
from .mrs import STAGE_ONE, STAGE_TWO


def detect(Q, D, model_cfg, cfg, link_prompt, synth_prompt):
    """Return (verdict, violated_mr, evidence)."""
    SSL = parse_linking(call_llm(model_cfg, link_prompt(Q, D)))
    for name, (sigma, op, valid) in STAGE_ONE.items():
        if not valid(Q, D):
            continue
        Qp, Dp = sigma(Q, D)
        FSL = parse_linking(call_llm(model_cfg, link_prompt(Qp, Dp)))
        if not op(SSL, FSL):
            return ("schema", name, {"SSL": sorted(SSL), "FSL": sorted(FSL)})
    q = parse_sql(call_llm(model_cfg, synth_prompt(Q, SSL, D)))
    R = exec_sql(q, D["db_path"], cfg.compare.float_tol)
    for name, (sigma, op, valid) in STAGE_TWO.items():
        if not valid(Q, D):
            continue
        Qp, Dpp = sigma(Q, D)
        FSL = parse_linking(call_llm(model_cfg, link_prompt(Qp, Dpp)))
        qp = parse_sql(call_llm(model_cfg, synth_prompt(Qp, FSL, Dpp)))
        Rp = exec_sql(qp, Dpp["db_path"], cfg.compare.float_tol)
        if R is BOTTOM or Rp is BOTTOM or not op(R, Rp):
            return ("logic", name, {"R_rows": R, "Rp_rows": Rp})
    return ("clean", None, {})
