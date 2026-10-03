"""Evaluation metrics (paper Section 4.5).

Confusion-based: Precision / Recall / F1 / Accuracy against labels
derived from gold SQL + schema (evaluation only; never used at
detection time). Count-based: HDN and HDR (analysis only).
Also implements the per-cell error-budget derivation of RQ1 (2).
"""

def confusion(labels, verdicts):
    """labels/verdicts: per-sample booleans (True = hallucinated)."""
    tp = sum(l and v for l, v in zip(labels, verdicts))
    fp = sum((not l) and v for l, v in zip(labels, verdicts))
    fn = sum(l and (not v) for l, v in zip(labels, verdicts))
    tn = sum((not l) and (not v) for l, v in zip(labels, verdicts))
    return tp, fp, fn, tn


def prf(tp, fp, fn):
    p = tp / (tp + fp) if tp + fp else 0.0
    r = tp / (tp + fn) if tp + fn else 0.0
    f = 2 * p * r / (p + r) if p + r else 0.0
    return p, r, f


def hdn(detections_per_mr):
    """HDN of an MR or class = number of violations it caught."""
    return detections_per_mr


def hdr(mr_hdn, parent_hdn):
    """HDR = HDN_i / HDN_parent (parent != 0)."""
    return mr_hdn / parent_hdn if parent_hdn else 0.0
