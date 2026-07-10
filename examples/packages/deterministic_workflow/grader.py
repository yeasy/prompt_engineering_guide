#!/usr/bin/env python3
"""Deterministic offline grader for an ordered workflow plan."""

from __future__ import annotations


def grade(prediction: object, expected: object) -> dict[str, object]:
    passed = isinstance(prediction, dict) and prediction == expected
    return {
        "pass": passed,
        "score": 1.0 if passed else 0.0,
        "reason": "status and ordered steps match" if passed else "workflow status or step order differs",
    }
