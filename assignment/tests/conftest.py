"""Use external CSV rows as separately identified, marked, ordered cases."""
import csv
import json
from pathlib import Path

import pytest
import validators

ROOT = Path(__file__).resolve().parents[2]


def pytest_sessionstart(session):
    """Prove the tests use the cloned source, not an installed PyPI copy."""
    source = Path(validators.__file__).resolve()
    expected = ROOT / "src" / "validators" / "__init__.py"
    if source != expected:
        raise pytest.UsageError(f"Expected local source {expected}, but imported {source}")


@pytest.fixture(autouse=True)
def default_return_mode(monkeypatch):
    """Do not let an external environment variable change the public contract."""
    monkeypatch.delenv("RAISE_VALIDATION_ERROR", raising=False)


def pytest_generate_tests(metafunc):
    if "case" not in metafunc.fixturenames:
        return
    with (ROOT / "assignment/data/test_cases.csv").open(encoding="utf-8", newline="") as f:
        rows = list(csv.DictReader(f))
    if len({row["id"] for row in rows}) != len(rows):
        raise pytest.UsageError("CSV case IDs must be unique")
    if len({int(row["order"]) for row in rows}) != len(rows):
        raise pytest.UsageError("CSV case orders must be unique")
    parameters = []
    for row in rows:
        if row["module"] != metafunc.module.MODULE:
            continue
        if row["owner"] not in {"Saim", "Ahmed"}:
            raise pytest.UsageError(f"Invalid owner for {row['id']}")
        if row["expected"] not in {"True", "ValidationError"}:
            raise pytest.UsageError(f"Invalid expected result for {row['id']}")
        if row["technique"] not in {"BVA", "ECP"}:
            raise pytest.UsageError(f"Invalid technique for {row['id']}")
        row["value"] = json.loads(row["input_json"])
        row["kwargs"] = json.loads(row["kwargs_json"])
        marks = [
            pytest.mark.regression,
            pytest.mark.order(int(row["order"])),
            getattr(pytest.mark, row["owner"].lower()),
            getattr(pytest.mark, "boundary" if row["technique"] == "BVA" else "ecp"),
        ]
        if row["smoke"] == "yes":
            marks.append(pytest.mark.smoke)
        parameters.append(pytest.param(row, id=row["id"], marks=marks))
    if not parameters:
        raise pytest.UsageError(f"No CSV cases for {metafunc.module.MODULE}")
    metafunc.parametrize("case", parameters)
