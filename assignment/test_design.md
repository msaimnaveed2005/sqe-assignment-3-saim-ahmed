# ECP and BVA notes

Project: python-validators/validators, tag 0.35.0, commit
75788ed9e116fe3bf1bb9699f1696e7f7e132067. Source directory: `src/validators/`.

ECP groups inputs expected to produce the same type of result. BVA checks
values at and immediately around limits. The CSV records the expected result
before execution, the technique, and the specific objective for each case.
The public decorated functions return `True` or a falsey `ValidationError`.
The wrapper converts ordinary ValueError and TypeError failures into that
validation-error contract. Tests remove `RAISE_VALIDATION_ERROR` from their
environment to use the normal return mode consistently.

## length.py - length(value, min_val, max_val)

### Saim: SAIM-LEN-01 through SAIM-LEN-10

- Main domain: string length from 3 through 8 inclusive.
- Valid ECP: nonempty strings inside the interval.
- Invalid ECP: empty strings with a positive minimum; lengths outside the range.
- BVA lengths: 2, 3, 4, 7, 8, 9.
- Further ECP: a typical valid string, only a minimum, only a maximum.
- Allocation: six BVA and four ECP cases, ten total.

### Ahmed: AHMED-LEN-01 through AHMED-LEN-10

- Main domain: string length from 1 through 5 inclusive.
- BVA lengths: 0, 1, 2, 4, 5, 6, plus the zero-width interval [0, 0].
- Further ECP: Unicode characters, negative minimum, negative maximum.
- Empty string with [0, 0] is valid in the pinned release; empty input is not
  universally invalid for a length validator.
- Allocation: seven BVA and three ECP cases, ten total.

Unicode length follows Python `len()`, not visual grapheme count. The selected
Unicode example uses one code point per visible character.

## between.py - between(value, min_val, max_val)

### Saim: SAIM-RNG-01 through SAIM-RNG-10

- Main domain: integers from 1 through 65535 inclusive.
- BVA: 0, 1, 2, 65534, 65535, 65536.
- ECP: None, a typical interior value, lower bound only, upper bound only.
- Allocation: six BVA and four ECP cases, ten total.

### Ahmed: AHMED-RNG-01 through AHMED-RNG-10

- Main domain: integers from -5 through 5 inclusive.
- BVA: -6, -5, -4, 4, 5, 6.
- ECP: comparable floating-point values, incomparable bound types, reversed
  bounds, and a numeric-looking string compared with integers.
- Allocation: six BVA and four ECP cases, ten total.

This is a generic comparison validator. The 1-65535 interval is an example
range, not evidence that this function enforces a network protocol.

## mac_address.py - mac_address(value)

### Saim: SAIM-MAC-01 through SAIM-MAC-10

- Valid ECP: lowercase, uppercase, hyphen-separated, and all-zero syntax.
- Invalid ECP: non-hex digits, missing octet, missing separators, empty input.
- BVA: 16 and 18 characters around the standard 17-character representation.
  The valid 17-character examples provide at-boundary cases.
- Allocation: two BVA and eight ECP cases, ten total.

### Ahmed: AHMED-MAC-01 through AHMED-MAC-10

- Valid ECP: mixed-case digits, broadcast syntax, mixed supported separators.
- Invalid ECP: a bad final hex digit, dotted format, leading whitespace,
  integer input, and None.
- BVA: five and seven octets around the required six; valid six-octet examples
  provide the at-boundary cases.
- Allocation: two BVA and eight ECP cases, ten total.

The pinned regex permits a colon or hyphen at each separator, so mixed
separators are accepted. These tests characterize the library, not an invented
stricter format. All-zero and broadcast addresses can pass a syntax validator
without being appropriate for a particular device. No network calls occur.

## Traceability and coverage

There are 60 distinct case IDs, 30 per member and 20 per module: 29 BVA and
31 ECP. Case ID links the CSV row, parametrized pytest item, JUnit result,
result CSV, and Excel row. CSV order 1-60 provides deterministic sequential
execution. All expected values are fixed test data, not computed by calling
the function under test.

The selected library modules contain standalone functions, so no classes were
invented or wrapped to create artificial methods. Coverage is measured for the
three selected modules and reported separately from test counts. Even complete
line/branch coverage does not prove correctness for every possible input.
