# URL Handling Utility

Stateless normalization pipeline for URLs used at the API ingress layer.

## Pipeline Logic
1. Sanitization: Trims whitespace.
2. Scheme Injection: Defaults to `https://` if no scheme is present.
3. Validation: Verifies `netloc` and `scheme` via `urllib.parse`.
4. Normalization: Lowercases the domain.

## Usage
```python
from utils.url_handler import normalize_url
from exceptions import URLValidationError

try:
    clean_url = normalize_url("EXAMPLE.COM")
except URLValidationError as e:
    # Handle API error response
    pass
```
