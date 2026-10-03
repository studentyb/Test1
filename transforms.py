"""The 17 input transformations sigma (paper Sections 3.4-3.5, Table 1).

Every function maps (Q, D) -> (Q', D') for one MR. Applicability
predicates (the `valid` of the MR triple) are attached in mrs.py.
Pair validation (paper 3.3) is applied to every generated pair BEFORE
it enters the detection pipeline.
"""
from .lexicons import (COMPARATIVE_LEXICON, PREFIX_SET, SC_ADJUNCTS)


# ----- Stage one: schema linking (sigma acts on the question text) -----

def srocw(Q, D):   # SSL = FSL
    raise NotImplementedError

def arocw(Q, D):   # SSL = FSL
    raise NotImplementedError

def esr(Q, D):     # SSL = FSL
    raise NotImplementedError

def ensr(Q, D):    # SSL != FSL
    raise NotImplementedError

def rc(Q, D):      # FSL subseteq SSL
    raise NotImplementedError

def os_(Q, D):     # SSL = FSL
    raise NotImplementedError

def sc(Q, D):      # SSL = FSL
    raise NotImplementedError

def dsr(Q, D):     # SSL != FSL ; sigma(Q,D) = (Q, D')
    raise NotImplementedError


# ----- Stage two: logical synthesis -----

def pi(Q, D):      # R(q) = R(q')
    raise NotImplementedError

def pr(Q, D):      # R(q) = R(q')
    raise NotImplementedError

def ps(Q, D):      # R(q) = R(q')
    raise NotImplementedError

def sroe(Q, D):    # R(q) = R(q')
    raise NotImplementedError

def aroe(Q, D):    # R(q) != R(q')
    raise NotImplementedError

def cru(Q, D):     # R(q) = R(q')
    raise NotImplementedError

def cre(Q, D):     # R(q) subseteq R(q')
    raise NotImplementedError

def cwr(Q, D):     # R(q) supseteq R(q')
    raise NotImplementedError

def dr(Q, D):      # R(q) != R(q') ; sigma(Q,D) = (Q, D'')
    raise NotImplementedError
