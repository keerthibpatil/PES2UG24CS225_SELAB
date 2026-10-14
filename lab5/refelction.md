# Lab 5: Static Code Analysis — Reflection

## 1. What did you learn from this lab?
I learned how static code analysis tools help identify code-quality problems, formatting mistakes, and potential security vulnerabilities without executing the code.

## 2. What is the difference between Pylint, Flake8, and Bandit?
- Pylint checks code quality, naming conventions, documentation, and programming practices.
- Flake8 identifies formatting and PEP 8 style violations.
- Bandit identifies potential security risks in Python code.

## 3. What issues did you fix?
I fixed mutable default arguments, broad exception handling, unsafe subprocess execution, insecure temporary filename generation, and the use of a non-cryptographic random number generator for OTP generation. I also corrected formatting issues and added docstrings.

## 4. What were the final analysis results?
- Pylint: 10.00/10
- Flake8: No reported issues
- Bandit: 3 low-severity findings, with no medium- or high-severity findings
- Program execution: Successful

## 5. Why is static code analysis important?
Static code analysis helps developers detect problems early, improve code readability, reduce security risks, and make software easier to maintain. It complements testing but does not replace it.

## Conclusion
This lab helped me understand how to use Pylint, Flake8, and Bandit to improve Python code. After fixing the identified issues, I reran the tools and verified that the program still worked correctly.