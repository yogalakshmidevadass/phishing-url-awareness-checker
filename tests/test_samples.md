# Manual Test Results

Python version used: fill in after running | Operating system: fill in | Date: fill in

| # | Input | Expected observation | Actual result (fill after run) | Pass/Fail |
|---|---|---|---|---|
| 1 | `https://www.example.com/login` | No listed warning signs; this is not a safety guarantee. | | |
| 2 | `http://192.0.2.10/account` | IP-like hostname and HTTP warnings. | | |
| 3 | `http://example.com@sample.invalid/login` | `@` symbol and HTTP warnings. | | |
| 4 | `https://a.b.c.d.e.example.invalid/path` | Many hostname segments warning. | | |
| 5 | `https://xn--example.invalid/` | Punycode-style hostname warning. | | |

## Additional checks
- Empty input should print `No URL entered.`
- `www.example.com` is treated as HTTP because the scheme is missing.
- `http://[bad` should return a malformed-format message without crashing.
- Type `q` to quit the interactive loop.

## Notes
After testing, write 2-3 lines in your own words about what you learned and anything that surprised you. Record the actual output honestly.
