"""MR registry: name -> (sigma, OP, valid) (paper Section 3.2).

OP is a predicate on (source_output, followup_output):
  stage one compares schema linkings (sets of (table, column));
  stage two compares executed result sets (bot = execution failure).
The 17 MRs are exactly those of Table 1 in the paper.
"""
from . import transforms as T


def op_eq(a, b):   return a == b
def op_neq(a, b):  return a != b
def op_subset(a, b):  return a <= b     # FSL <= SSL for RC; R <= R' for CRE
def op_supset(a, b):  return a >= b     # R >= R' for CWR

STAGE_ONE = {
    # name: (sigma, op, valid)
    "SROCW": (T.srocw, op_eq,   lambda Q: has_comparative(Q)),
    "AROCW": (T.arocw, op_eq,   lambda Q: has_comparative(Q)),
    "ESR":   (T.esr,   op_eq,   lambda Q: has_entity(Q)),
    "ENSR":  (T.ensr,  op_neq,  lambda Q, D: has_schema_non_synonym(Q, D)),
    "RC":    (T.rc,    op_subset, lambda Q: has_conditional(Q)),
    "OS":    (T.os_,   op_eq,   lambda Q: has_irrelevant(Q)),
    "SC":    (T.sc,    op_eq,   lambda Q: True),
    "DSR":   (T.dsr,   op_neq,  lambda Q, D: has_comparable_schema(D)),
}

STAGE_TWO = {
    "PI":    (T.pi,   op_eq,    lambda Q: True),
    "PR":    (T.pr,   op_eq,    lambda Q: has_prefix(Q)),
    "PS":    (T.ps,   op_eq,    lambda Q: has_prefix(Q)),
    "SROE":  (T.sroe, op_eq,    lambda Q: has_extremum(Q)),
    "AROE":  (T.aroe, op_neq,   lambda Q: has_extremum(Q)),
    "CRU":   (T.cru,  op_eq,    lambda Q: has_comparative(Q)),
    "CRE":   (T.cre,  op_subset, lambda Q: has_natural_broader(Q)),
    "CWR":   (T.cwr,  op_supset, lambda Q: has_natural_narrower(Q)),
    "DR":    (T.dr,   op_neq,   lambda Q, D: has_other_database(D)),
}

ALL_MRS = {**{k: (1, v) for k, v in STAGE_ONE.items()},
           **{k: (2, v) for k, v in STAGE_TWO.items()}}


def has_comparative(Q): raise NotImplementedError
def has_entity(Q): raise NotImplementedError
def has_schema_non_synonym(Q, D): raise NotImplementedError
def has_conditional(Q): raise NotImplementedError
def has_irrelevant(Q): raise NotImplementedError
def has_comparable_schema(D): raise NotImplementedError
def has_prefix(Q): raise NotImplementedError
def has_extremum(Q): raise NotImplementedError
def has_natural_broader(Q): raise NotImplementedError
def has_natural_narrower(Q): raise NotImplementedError
def has_other_database(D): raise NotImplementedError
