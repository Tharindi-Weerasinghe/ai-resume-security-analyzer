import re
import tldextract

def extract_urls(text):

    pattern = r'(https?://[^\s]+|www\.[^\s]+)'
    return re.findall(pattern, text)


def analyze_urls(text):

    urls = extract_urls(text)

    risky = []

    for url in urls:

        domain = tldextract.extract(url).domain

        risk = "LOW"

        # simple phishing heuristics
        if len(url) > 75:
            risk = "HIGH"
        elif any(word in url.lower() for word in ["login", "verify", "secure", "update"]):
            risk = "MEDIUM"
        elif domain in ["bit", "tinyurl", "cuttly"]:
            risk = "HIGH"

        risky.append({
            "url": url,
            "risk": risk
        })

    return risky