from urllib.parse import urlparse, urlunparse
from exceptions import URLValidationError

def normalize_url(url: str) -> str:
    url = url.strip()
    if not url:
        raise URLValidationError("URL cannot be empty")

    if not (url.startswith("http://") or url.startswith("https://")):
        url = f"https://{url}"

    parsed = urlparse(url)
    
    if not parsed.netloc or not parsed.scheme:
        raise URLValidationError(f"Invalid URL structure: {url}")

    # Lowercase the domain to ensure idempotency
    normalized_parsed = parsed._replace(netloc=parsed.netloc.lower())
    
    return urlunparse(normalized_parsed)
