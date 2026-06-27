#!/usr/bin/env python3
"""Pick the best PENDING guests to approve, ranked by TOTAL score across all sponsors.
Usage: python approve_batch.py --config config.json [--dir .] (--count N | --target GOING_TARGET)"""
import json, csv, os, argparse
ap = argparse.ArgumentParser()
ap.add_argument("--config", required=True); ap.add_argument("--dir", default=".")
ap.add_argument("--count", type=int, help="how many pending to approve")
ap.add_argument("--target", type=int, help="desired total 'going' headcount (count = target - current going)")
ap.add_argument("--out", default="approval-batch.csv")
A = ap.parse_args()
C = json.load(open(A.config)); SP = [s["name"] for s in C["sponsors"]]
REC = json.load(open(os.path.join(A.dir, "leads-ranked.json")))
going = [r for r in REC if r["status"] == "going"]; pending = [r for r in REC if r["status"] == "pending"]
N = A.count if A.count else (A.target - len(going) if A.target else 0)
if N <= 0: raise SystemExit(f"Nothing to do: going={len(going)}. Pass --count N or --target > going.")
for r in pending: r["total"] = sum(int(r[s]) for s in SP)
vr = {"V": 0, "P": 1, "U": 2, "": 3}
elig = [r for r in pending if r["type"] != "Employee"]
elig.sort(key=lambda r: (-r["total"], vr.get(r.get("verified", ""), 3), -int(r["best"]), r["name"].lower()))
top = elig[:N]
cols = ["approve_rank", "total", "name", "email", "company", "title"] + SP + ["type", "verified", "vflag", "linkedin"]
with open(os.path.join(A.dir, A.out), "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=cols); w.writeheader()
    for i, r in enumerate(top, 1):
        row = {k: r.get(k, "") for k in cols}; row["approve_rank"] = i; row["total"] = r["total"]; w.writerow(row)
print(f"going={len(going)} pending={len(pending)} -> approve {len(top)} (=> {len(going)+len(top)} going)")
print(f"cutoff total={top[-1]['total'] if top else 'n/a'}; wrote {A.out}")
staff = [r for r in pending if r["type"] == "Employee"]
if staff: print(f"NOTE: {len(staff)} pending sponsor-staff excluded — approve separately:", ", ".join(r["name"] for r in staff[:10]))
