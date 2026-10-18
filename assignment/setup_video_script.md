# Setup recording checklist (about 3-4 minutes)

Create a real screen recording with your own recorder. Save it as
`assignment/setup_demo.mp4`. This guide is not a recorded setup video.
The class PDF requires a short setup demonstration; it does not prescribe a
particular recorder or require narrated audio.

## 0:00-0:35 - Saim: selected open-source project

Show the upstream repository, its MIT license, and the selected tag 0.35.0.
Show the cloning command, then the local source tree. Run `git remote -v` and
`git rev-parse HEAD` to demonstrate the original source and pinned commit.
Explain that the new assignment files are under `assignment/`.

## 0:35-1:25 - Saim: local setup

In a terminal at the repository root, show the Python 3.12 version, create a
fresh virtual environment, install `assignment/requirements.txt`, and install
the cloned project with `pip install --no-build-isolation -e .`. Use the exact
virtual-environment commands in the README. Show `validators.__file__` pointing
to the clone's `src/validators/__init__.py`.

## 1:25-2:15 - Ahmed: test design and data

Open `assignment/data/test_cases.csv` and `assignment/test_cases.xlsx`.
Explain one BVA example (e.g. length 2, 3, 4 around minimum 3) and one ECP
example (e.g. an invalid hexadecimal octet). Show each person's 30 case IDs.
Explain that CSV supplies executable test data and Excel documents the cases.

## 2:15-3:15 - Both: execution

Run the full assignment suite and show its result. Run Saim's and Ahmed's
member suites. Demonstrate the smoke suite and two-worker parallel execution.
Show the sequential ID order and explain how the group runner waits for each
module before starting the next one. Parallel cases may finish in any order.

## 3:15-3:45 - Both: evidence and submission

Show the summary report, actual contribution commits, setup video file, and
public group repository. Check that the Excel sheet, CSV, configuration, notes,
and final reports are all present. Submit the repository link on GCR before
the due date; the PDF prohibits repository updates after October 21, 2026.

Only show actual completed actions. If you replay an existing terminal result,
identify it as a replay rather than claiming a new live run.
