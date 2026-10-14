# Lab 5: Static Code Analysis — Issues Report

## Project
Parcel Tracker

## Tools Used
- Pylint
- Bandit
- Flake8

## Issues Identified and Fixed

| No. | Issue | Tool | Severity/Priority | Fix Applied |
|---|---|---|---|---|
| 1 | Mutable default list argument | Pylint | Medium | Replaced `history=[]` with `history=None` and initialized the list inside the function. |
| 2 | Broad exception handling | Pylint | Medium | Replaced `except Exception` with `except KeyError`. |
| 3 | Unsafe subprocess execution using `shell=True` | Bandit | High | Changed the command to a list of arguments and used `shell=False`. |
| 4 | Insecure temporary filename generation | Bandit | Medium | Replaced `tempfile.mktemp()` with `tempfile.NamedTemporaryFile()`. |
| 5 | Insecure random number generator for OTP | Bandit | Low | Replaced `random.randint()` with `secrets.randbelow()`. |
| 6 | Inconsistent function and variable naming | Pylint | Low | Renamed functions and variables using Python's `snake_case` convention. |
| 7 | Missing module and function docstrings | Pylint | Low | Added documentation strings. |
| 8 | Code formatting violations | Flake8 | Low | Corrected spacing, inline comments, and blank lines. |

## Final Analysis Results

- Pylint score: 10.00/10
- Flake8: No reported issues
- Bandit: 3 low-severity findings, 0 medium-severity findings, and 0 high-severity findings
- Program execution: Successful

## Conclusion

Static code analysis helped identify code-quality, formatting, and security-related issues in the parcel-tracking program. The identified high- and medium-priority issues were addressed, and the program was tested again after the changes. The final Pylint score was 10/10, Flake8 reported no issues, and Bandit reported only low-severity findings.