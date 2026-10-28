"""Educational, text-only phishing URL awareness checker.

This program never opens URLs or sends data over the network.
It identifies a small set of visible warning signs; it cannot prove safety.
"""
import re
from urllib.parse import urlparse


INFO_PREFIXES = (
    "No URL entered.",
    "Could not identify a hostname.",
    "This text is not a valid URL format.",
    "No listed warning signs found.",
)


def inspect_url(raw_url: str) -> list[str]:
    """Return warning messages for selected patterns in URL text."""
    url = raw_url.strip()
    findings: list[str] = []

    if not url:
        return ["No URL entered."]

    candidate = url if "://" in url else "http://" + url

    try:
        parsed = urlparse(candidate)
        host = (parsed.hostname or "").lower()
    except ValueError:
        return ["This text is not a valid URL format."]

    if not host:
        return ["Could not identify a hostname."]

    if "@" in candidate:
        findings.append("Contains an @ symbol; inspect carefully.")

    if len(url) > 100:
        findings.append("Unusually long URL (over 100 characters).")

    # This is a pattern check, not full IP-address validation.
    if re.fullmatch(r"(?:\d{1,3}\.){3}\d{1,3}", host):
        findings.append("Uses an IP address instead of a familiar domain.")

    labels = [part for part in host.split(".") if part]
    if len(labels) >= 5:
        findings.append("Contains many hostname segments/subdomains.")

    if "xn--" in host:
        findings.append("Contains a punycode-style hostname.")

    if parsed.scheme.lower() == "http":
        findings.append("Uses HTTP. HTTPS alone does not prove trust.")

    if not findings:
        findings.append(
            "No listed warning signs found. This does NOT prove safety."
        )

    return findings


def has_warnings(findings: list[str]) -> bool:
    """Return True when findings contain actual warning signs."""
    return not any(findings[0].startswith(prefix) for prefix in INFO_PREFIXES)


def main() -> None:
    """Run an interactive loop until the user chooses to quit."""
    print("EWB Phishing URL Awareness Checker")
    print("Text checks only - this program does not open URLs.")
    print("Type q to quit. Use the workbook's sample strings for testing.")

    while True:
        raw_url = input("\nEnter a sample URL (or type q to quit): ")
        if raw_url.strip().lower() in {"q", "quit", "exit"}:
            print("Goodbye! Stay alert online.")
            break

        findings = inspect_url(raw_url)
        print("\nResult:")
        for item in findings:
            print("- " + item)

        if has_warnings(findings):
            print(f"\nREVIEW CAREFULLY: {len(findings)} warning sign(s) found.")

        print("Never enter passwords from unexpected links.")


if __name__ == "__main__":
    main()
