"""Command-line runner: reproduce the paper's per-cell results.

Examples
--------
# Run SQLHD on one variant / one model configuration:
python -m sqlhd.runner --variant SGLMD --model GLM-4 --out results/SGLMD_GLM-4.json

# Run the Self-Evaluation baselines on the same generations:
python -m sqlhd.runner --variant SGLMD --model GLM-4 --baseline selfeval_bool
python -m sqlhd.runner --variant SGLMD --model GLM-4 --baseline selfeval_prob

Outputs (results/*.json): per-sample verdict, violated MR, evidence,
confusion counts, P/R/F1/Accuracy, HDN/HDR. These are the per-cell
result files referenced in the paper's Data Availability.
"""
import argparse


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--variant", required=True, choices=["SGLMD", "SGPMD", "BGLMD", "BGPMD"])
    ap.add_argument("--model", required=True)
    ap.add_argument("--baseline", default=None, choices=[None, "selfeval_bool", "selfeval_prob"])
    ap.add_argument("--out", required=True)
    args = ap.parse_args()
    raise SystemExit("TODO: wire dataset loading, detection loop, and result dumping")


if __name__ == "__main__":
    main()
