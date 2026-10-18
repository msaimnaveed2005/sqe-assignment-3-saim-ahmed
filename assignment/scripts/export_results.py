"""Join a completed JUnit report to the CSV plan using stable test IDs."""
import csv
from pathlib import Path
import sys
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
report = Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT / "reports/sequential.xml"
with (ROOT / "data/test_cases.csv").open(encoding="utf-8", newline="") as stream:
    cases = list(csv.DictReader(stream))
observed = {}
for test in ET.parse(report).iter("testcase"):
    identifier = test.attrib["name"].split("[", 1)[-1].rstrip("]")
    if identifier in observed:
        raise ValueError(f"Duplicate report ID: {identifier}")
    state = "Passed"
    if test.find("failure") is not None or test.find("error") is not None:
        state = "Failed"
    elif test.find("skipped") is not None:
        state = "Skipped"
    observed[identifier] = state
if set(observed) != {row["id"] for row in cases}:
    raise ValueError("Report IDs do not exactly match the CSV test plan")
output = ROOT / "reports/test_results.csv"
with output.open("w", encoding="utf-8", newline="") as stream:
    writer = csv.DictWriter(stream, fieldnames=["id", "owner", "module", "expected", "status"])
    writer.writeheader()
    for case in cases:
        writer.writerow({key: observed[case["id"]] if key == "status" else case[key]
                         for key in writer.fieldnames})
print(f"Exported {len(cases)} cases to {output}")
