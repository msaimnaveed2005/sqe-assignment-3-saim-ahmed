# Assignment 3 - Unit Test Automation

**Group: Saim and Ahmed. Due: October 21, 2026.**

This work tests three modules in a real clone of
[python-validators/validators](https://github.com/python-validators/validators).
It adds testing and documentation to that existing project. The original
project's README, MIT license, source, and tests remain intact.

## Step 1 - Identify and clone the open-source project

Selected release: **0.35.0**. Original commit:
`75788ed9e116fe3bf1bb9699f1696e7f7e132067`.

The supplied repository has already been cloned at that release and put on a
local `assignment-3` branch. Its original remote is named `upstream`. Its `.git`
history is retained in the ZIP. To reproduce the starting point independently:

```powershell
git clone --branch 0.35.0 --single-branch https://github.com/python-validators/validators.git
cd validators
git switch -c assignment-3
git remote rename origin upstream
```

For the supplied package, extract the ZIP, open the `validators_assignment`
folder, and continue below. Keep the hidden `.git` directory. Run commands from
the repository root, which contains `pyproject.toml` and `ASSIGNMENT.md`.

## Step 2 - Set up the local environment

Use Python **3.12**, Git, and a terminal. The commands avoid activation scripts:

```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r assignment/requirements.txt
.\.venv\Scripts\python.exe -m pip install --no-build-isolation -e .
.\.venv\Scripts\python.exe -c "import validators; print(validators.__version__); print(validators.__file__)"
```

The version should be `0.35.0`. The printed module path must end in this clone's
`src/validators/__init__.py`. Editable installation connects Python to the local
source. The assignment tests independently verify this path.

On macOS/Linux use `python3.12 -m venv .venv`, then `.venv/bin/python` in place
of `.\.venv\Scripts\python.exe`.

## Step 3 - Review the selected modules and test design

| Existing module | Function under test | Saim | Ahmed | Total |
| --- | --- | ---: | ---: | ---: |
| `src/validators/length.py` | `length()` | 10 | 10 | 20 |
| `src/validators/between.py` | `between()` | 10 | 10 | 20 |
| `src/validators/mac_address.py` | `mac_address()` | 10 | 10 | 20 |
| Total | | 30 | 30 | 60 |

These modules expose standalone functions. There is no selected application
class whose additional methods are being omitted. Each member has 10 cases
for each selected function and module. `test_design.md` explains equivalence
class partitioning (ECP) and boundary value analysis (BVA).

Case ownership here is a prepared allocation. It is not a claim that Saim or
Ahmed has already authored, reviewed, or committed the work. See
`task_allocation.md` for actual contribution recording.

## Step 4 - Execute the automated tests

Use the virtual-environment Python from Step 2. For readability, `python` in the
commands below means that same executable. Run these from the repository root.

```text
python -m pytest -c pytest-assignment.ini -v
python -m pytest -c pytest-assignment.ini -m saim -v
python -m pytest -c pytest-assignment.ini -m ahmed -v
python -m pytest -c pytest-assignment.ini -m smoke -v
python -m pytest -c pytest-assignment.ini -m boundary -v
python -m pytest -c pytest-assignment.ini -m ecp -v
python -m pytest -c pytest-assignment.ini -m length -v
python -m pytest -c pytest-assignment.ini -m between -v
python -m pytest -c pytest-assignment.ini -m mac -v
```

The complete assignment suite has 60 cases. Each member's suite has 30, each
module suite has 20, smoke has 12, BVA has 29, and ECP has 31. `regression`
selects all 60. Marker expressions such as `saim and boundary` also work.

Each test receives a CSV row as a parameter, calls the original function, and
asserts either the literal `True` or a falsey `ValidationError` object. Invalid
values are not assumed to return the literal Boolean `False`.

To run the upstream project's original tests for the same three modules:

```text
python -m pytest tests/test_length.py tests/test_between.py tests/test_mac_address.py -q
```

Use `-c pytest-assignment.ini` for the new work. Running pytest without that
option invokes upstream configuration and its broader test suite, which can
require upstream optional dependencies. The assignment does not claim to test
every module in the library.

## Step 5 - Review CSV and Excel test cases

- Executable data: `assignment/data/test_cases.csv` (60 rows).
- Excel documentation: `assignment/test_cases.xlsx` (the same 60 IDs).
- Results exported from JUnit: `assignment/reports/test_results.csv`.

Every Excel row has an owner, module, input, arguments, expected result,
technique, objective, execution order, observed return type, and test status.
This supplies more than the required four externally driven test cases per
member. JSON inside the CSV cells preserves values such as integers, strings,
floats, and null without ambiguous conversion.

The tests read CSV, not Excel. If you edit the CSV, update the corresponding
Excel rows. Regenerate the result CSV after a full run as shown below. An old
Excel result is a snapshot of the documented run, not a live test result.

## Step 6 - Demonstrate parallelism, order, and reports

```text
python -m pytest -c pytest-assignment.ini -n 2 -v
python assignment/run_suites.py
python assignment/run_suites.py --parallel
python assignment/run_suites.py --parallel --member saim
python assignment/run_suites.py --parallel --member ahmed
python -m pytest -c pytest-assignment.ini -v --junitxml=assignment/reports/sequential.xml
python -m pytest -c pytest-assignment.ini -n 2 --junitxml=assignment/reports/parallel.xml
python assignment/scripts/export_results.py
```

Sequential case order is CSV order 1-60: length 1-20, between 21-40, MAC 41-60.
Within a module Saim's 10 cases precede Ahmed's 10. `pytest-order` enforces the
numeric order on a sequential run. The group runner waits for length to finish,
then starts between, then MAC, and stops on a failure. Its `--parallel` option
runs two workers inside each group. It also works from another current folder.

Parallel execution can finish cases in any order. Do not claim strict global
case order and concurrent execution in the same run. Cases are independent and
do not share changing state. Use the sequential command to demonstrate strict
case order, and the group runner to demonstrate ordered groups with parallel
cases.

Optional selected-module coverage:

```text
python -m coverage run --rcfile=assignment/.coveragerc -m pytest -c pytest-assignment.ini
python -m coverage report --rcfile=assignment/.coveragerc
python -m coverage html --rcfile=assignment/.coveragerc
python -m coverage xml --rcfile=assignment/.coveragerc
```

Coverage reports apply to the three selected source modules. They do not imply
complete coverage of shared decorators, helpers, other modules, or all possible
input types. See `reports/verification.md` for the measured results.

## Step 7 - Record the setup video and complete individual work

Follow `setup_video_script.md` to record an actual setup demonstration. Save
the recording as `assignment/setup_demo.mp4`. A written script is not the
required video. Each member should review their 30 cases, run their own suites,
write their review notes, and make their own meaningful Git commits.

`task_allocation.md` names the responsibilities and separates prepared work
from evidence that your group still needs to produce. `summary_report.md`
contains the technical summary and explicit remaining submission items.

## Step 8 - Publish the group repository and submit

The public group repository is:
https://github.com/msaimnaveed2005/sqe-assignment-3-saim-ahmed

The prepared project is published on `main`. Its preparation upload
does not count as evidence that both members personally reviewed or contributed
the work. Each member should clone the group repository, review their allocated
cases, and make meaningful commits for their actual work:

```text
git clone https://github.com/msaimnaveed2005/sqe-assignment-3-saim-ahmed.git
cd sqe-assignment-3-saim-ahmed
git switch -c YOUR_CONTRIBUTION_BRANCH
```

Use a descriptive branch name for each member's work and merge the reviewed
changes into `main`. Add the real video, Excel sheet, notes, final
reports, and both members' contributions before submitting the URL on GCR.
Check public access in a signed-out browser. The PDF says no repository updates
are allowed after **October 21, 2026**; do not assume an unspecified cutoff time.

## Requirement checklist

| PDF requirement | Artifact or action |
| --- | --- |
| Existing open-source Python project and local setup | Original cloned source, upstream history, editable install |
| Recorded setup video | Record with `setup_video_script.md`; recording still required |
| Three modules and ECP/BVA notes | Source modules above and `test_design.md` |
| 5-10 tests per person for selected functions/modules | 10 per member per selected module, 60 total |
| Excel cases with externally consumed data | `test_cases.xlsx` and `data/test_cases.csv` |
| Parallel execution, groups, parameterization, and order | pytest configuration, CSV loader, group runner |
| Actual individual contributions | Each member's genuine review/work and Git commits still required |
| Summary report | `summary_report.md`; add video and group repository details |
| Public repository URL on GCR | Public group repository created; GCR submission still required |
