# Assignment 3 - Summary report

**Group members:** Saim and Ahmed.  
**Prepared and locally verified:** October 18, 2026.  
**Assignment due date:** October 21, 2026.

## Project and scope

The selected open-source Python project is **python-validators/validators**,
licensed under MIT. The group package contains a clone of release 0.35.0 at
commit `75788ed9e116fe3bf1bb9699f1696e7f7e132067`. The original project source,
license, tests, and Git history are preserved. New assignment work is kept
under `assignment/`, with a root `pytest-assignment.ini` configuration.

The selected modules are `length.py`, `between.py`, and `mac_address.py`.
Each exposes a standalone public validation function. The new tests call those
functions from the cloned `src/validators` tree, verified by an import-path
check. No replacement application or artificial wrapper class is required.

## Prepared allocation and techniques

| Member | length() | between() | mac_address() | Total |
| --- | ---: | ---: | ---: | ---: |
| Saim | 10 | 10 | 10 | 30 |
| Ahmed | 10 | 10 | 10 | 30 |
| Total | 20 | 20 | 20 | 60 |

The test plan contains **29 BVA cases and 31 ECP cases**. It covers inclusive
range and length limits, invalid partitions, absent values, configuration
errors, Unicode length, MAC syntax, and type mismatches. All expected results
are specified in the external CSV before execution. The Excel workbook
documents the same 60 case IDs, owners, arguments, expectations, techniques,
objectives, order, observed return types, and results.

## Automation and local results

Python 3.12.14 was used with pytest 8.3.5, pytest-xdist 3.6.1, pytest-order 1.3.0,
and coverage 7.6.1. The original cloned package was installed in editable mode.

- Full new sequential suite: **60 passed**.
- Full new parallel suite, two workers: **60 passed**.
- Member suites: **30 passed for Saim; 30 passed for Ahmed**.
- Smoke suite: **12 passed**.
- BVA suite: **29 passed**.
- ECP suite: **31 passed**.
- Ordered parallel groups: **20 passed in each of length, between, and MAC**.
- Original upstream tests for the three selected modules: **30 passed**.
- Selected-module coverage: **34/34 executable statements and 18/18 branches**.

The sequential run verified exact CSV case order 1-60. The group runner verified
length before between before MAC while using parallel workers inside each
group. Parallel runs do not guarantee global case completion order.

Evidence is saved in `reports/`: JUnit XML, a result CSV joined by case ID,
execution output, environment details, and coverage HTML/XML/JSON. Coverage
applies only to the three selected modules. Shared helpers, decorators, and
other library modules are outside that coverage claim.

## Issues encountered and resolutions

The sandbox's Windows Git TLS backend could not acquire credentials. Cloning
with the OpenSSL backend succeeded without disabling TLS verification.
Owner-only temporary directories also caused sandbox permission failures;
local verification used a temporary-directory permission workaround outside
the deliverable. Dependency installation and editable local installation then
succeeded in an isolated virtual environment.

Pytest configuration was placed at the repository root to ensure the documented
commands collect only the 60 new assignment cases. The original upstream
configuration remains intact. Separate original-module runs verify that the
selected upstream tests still pass.

## Items to complete before submission

The software and documentation above were prepared with assistant help. Case
allocation and generated reports do not prove personal student contributions.

- Saim's actual review notes and genuine commit SHA(s): **Pending**.
- Ahmed's actual review notes and genuine commit SHA(s): **Pending**.
- Actual setup recording at `assignment/setup_demo.mp4`: **Pending**.
- Public group repository URL:
  https://github.com/msaimnaveed2005/sqe-assignment-3-saim-ahmed
- Repository visibility: **Public, verified**.
- Submission of the URL on GCR: **Pending**.

Both members must review and understand the work, record their real actions,
and finish the remaining items before submission. Update this report with the
actual contribution and recording details. Do not update the repository after
the assignment's due date.
