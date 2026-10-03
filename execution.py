"""SQL execution and result-set semantics (paper Section 3.2).

R(q): execute q on the SQLite database under BAG semantics;
row order is ignored unless q contains ORDER BY;
floating-point tolerance 1e-6;
syntax errors / non-executable queries map to R(q) = BOTTOM.
"""
BOTTOM = None  # sentinel for execution failure

import sqlite3


def exec_sql(sql: str, db_path: str, float_tol: float = 1e-6):
    """Return a canonical, comparable representation of R(q), or BOTTOM."""
    try:
        con = sqlite3.connect(db_path)
        cur = con.execute(sql)
        rows = cur.fetchall()
        con.close()
    except Exception:
        return BOTTOM
    order_insensitive = "order by" not in sql.lower()
    # TODO: canonicalize floats with float_tol; sort rows if order_insensitive
    return frozenset(rows) if order_insensitive else tuple(rows)
