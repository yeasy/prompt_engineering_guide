#!/usr/bin/env python3
"""Deterministic offline grader for grounded question answering."""

from __future__ import annotations


def grade(prediction: object, expected: object) -> dict[str, object]:
    passed = isinstance(prediction, dict) and prediction == expected
    return {
        "pass": passed,
        "score": 1.0 if passed else 0.0,
        "reason": "answer, citations, and abstention match" if passed else "grounding contract mismatch",
    }
