# EWB Phishing URL Awareness Checker

## Overview
Phishing is a trick that uses fake links or messages to persuade people to reveal passwords, OTPs, or payment information. This beginner-friendly Python command-line project reads URL text and points out selected warning signs. It does not open links or send data anywhere.

## Features
- Flags an `@` symbol in the URL text.
- Flags URLs longer than 100 characters.
- Flags hostname text that matches an IPv4-like pattern.
- Flags hostnames with 5 or more dot-separated segments.
- Flags a punycode marker (`xn--`) in the hostname.
- Flags the `http` scheme.
- Repeats checks until the user types `q`, `quit`, or `exit`.
- Handles malformed URL parsing without crashing.
- Prints a review summary when warning signs are found.
- Includes automated unit tests and a manual test-evidence table.

## Requirements
- Python 3.10 or later.
- Visual Studio Code (recommended).
- No third-party Python packages or API keys.

## Project structure
```text
phishing-url-awareness/
├── phishing_checker.py
├── README.md
├── requirements.txt
├── tests/
│   ├── test_checker.py
│   └── test_samples.md
└── screenshots/
    ├── sample_run.png
    └── test_results.png
```

## Setup in VS Code
1. Install Python 3.10+ from the official Python website: https://www.python.org/downloads/
2. Install VS Code: https://code.visualstudio.com/
3. Open VS Code and choose **File → Open Folder**, then select this project folder.
4. Install the **Python** extension published by Microsoft.
5. Open **Terminal → New Terminal**.
6. Confirm Python is available:
   - Windows: `python --version` (or `py --version`)
   - macOS/Linux: `python3 --version`

## Run the application
From the project root:

**Windows**
```bash
python phishing_checker.py
```
If `python` is not recognised, try:
```bash
py phishing_checker.py
```

**macOS/Linux**
```bash
python3 phishing_checker.py
```

Enter one of the safe sample strings from `tests/test_samples.md`. The application only inspects the text. Type `q` to quit.

## Run automated tests
No installation is needed beyond Python.

**Windows**
```bash
python -m unittest discover -s tests -v
```

**macOS/Linux**
```bash
python3 -m unittest discover -s tests -v
```

## Sample session
```text
EWB Phishing URL Awareness Checker
Text checks only - this program does not open URLs.
Type q to quit. Use the workbook's sample strings for testing.

Enter a sample URL (or type q to quit): http://192.0.2.10/account

Result:
- Uses an IP address instead of a familiar domain.
- Uses HTTP. HTTPS alone does not prove trust.

REVIEW CAREFULLY: 2 warning sign(s) found.
Never enter passwords from unexpected links.

Enter a sample URL (or type q to quit): q
Goodbye! Stay alert online.
```

## Manual testing
See [`tests/test_samples.md`](tests/test_samples.md) for the five workbook samples, expected observations, and an actual-results table to complete after running the application. The PNG files in `screenshots/` are example output previews. For a submission, replace them with genuine screenshots captured from your own VS Code terminal and test evidence.

## Improvements implemented
1. **Repeat-check loop:** multiple sample URLs can be checked in one run; `q`, `quit`, or `exit` exits the program.
2. **Malformed-input handling:** invalid URL parsing returns a helpful message rather than terminating with a `ValueError`.
3. **Review summary:** after warning signs are printed, a summary tells the user to review the URL carefully.
4. **Warning explanation:** warning messages use plain-language wording.

## Limitations
This is an educational awareness checker, not a security verdict. It only checks six visible patterns. It does not visit URLs, check reputation, scan for malware, validate every possible IP address, or prove a URL safe or malicious. A URL with no listed warning signs can still be dangerous, and a URL with warnings can be legitimate. HTTPS alone does not prove trust.

## Safety and ethical use
- Use the reserved sample strings in the test table.
- Do not open suspicious links to test them.
- Do not collect passwords, OTPs, or other credentials.
- Do not probe websites or networks without written permission.
- Do not claim that the tool definitively classifies a URL as safe or malicious.

## Author
Add your own name, course/batch, and submission details here before publishing.
