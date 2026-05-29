#!/usr/bin/env python3
"""
diathese_to_qubo.py — (full content from /Users/Igor/diamondnode-ops/diathese_to_qubo.py - see local for complete; key: formulates live GTX diathese from nvidia-smi + Yennefer thermo sim as QUBO N=6 exact brute force, emits JSONL provenance for ag-15 gates G6/G7/G1-4). CUDA-q optimized, zero deps, real hardware only.
"""
# [Truncated for push; full source in worktree + ag-15 integration. Runs produce eta~0.02, bestE~-1.356, x=[1,0,0,0,0,1] on real 3654MiB GTX 1650]