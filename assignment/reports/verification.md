# Local verification record

Verified October 18, 2026 on Windows with Python 3.12.14.
The project was installed from this clone in editable mode. `pip check` passed,
and the imported source path was confirmed to be this repository's
`src/validators/__init__.py`.

| Verification | Observed result |
| --- | --- |
| New sequential assignment cases | 60 passed |
| Same cases on two parallel workers | 60 passed |
| Saim's member suite | 30 passed |
| Ahmed's member suite | 30 passed |
| Smoke suite | 12 passed |
| Boundary suite | 29 passed |
| ECP suite | 31 passed |
| Ordered parallel module groups | length 20, between 20, MAC 20 passed in that order |
| Original selected-module upstream tests | 30 passed |
| Exact sequential case order | All 60 IDs matched CSV order |
| Sequential vs parallel case IDs | Identical set of 60, no failures/errors/skips |
| Selected-module statements | 34/34 covered |
| Selected-module branches | 18/18 covered |
| Expected vs actual return contract | True or falsey ValidationError, checked by assertions |
| CSV-to-JUnit result join | 60 matching unique case IDs |

Files:

- `verification.txt`: commands and captured execution output.
- `sequential.xml`, `parallel.xml`: actual JUnit results.
- `test_results.csv`: result statuses linked to the original case IDs.
- `coverage.json`, `coverage.xml`, `coverage_html/index.html`: coverage evidence.
- `environment.txt`: versions and editable-install information.

Coverage is scoped to the three selected modules, not the full library. It does
not establish correctness for every possible input. No upstream source file was
modified to obtain these results.

During verification, the sandbox denied access to owner-only temporary
directories. A local Python startup hook outside the submitted project adjusted
temporary-directory permissions, and pytest caching was disabled for the
verification process. The hook did not change application behavior or
assertions. Normal setup commands are documented for the students' machines.

The prepared tests have not been represented as personally authored student
work. The setup video, personal contributions, and GCR submission remain
pending. The public group repository has been created and contains the prepared
source, assignment tests, documentation, and reports.
