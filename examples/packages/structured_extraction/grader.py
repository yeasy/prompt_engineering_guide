#!/usr/bin/env python3
"""Deterministic offline grader for structured extraction."""

from __future__ import annotations


def grade(prediction: object, expected: object) -> dict[str, object]:
    passed = isinstance(prediction, dict) and prediction == expected
    return {
        "pass": passed,
        "score": 1.0 if passed else 0.0,
        "reason": "exact structured match" if passed else "prediction differs from expected JSON",
    }
