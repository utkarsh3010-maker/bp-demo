# URL Normalization Strategy

## Issue
Invalid URLs are handled inconsistently across the business layer, leading to redundant validation and potential canonicalization mismatches.

## Technical Strategy
Enforce URL normalization at the boundary (ingress point) using a stateless utility function. This prevents the propagation of non-canonical strings into the core business logic.

## Implementation
- Implement a stateless `normalize_url` utility using `urllib.parse`.
- Apply normalization in API controllers or Request DTOs.
- Ensure idempotency and RFC 3986 compliance.
- Reject the stateful `URLProcessor` approach from PR #15 to avoid unnecessary abstraction layers.

## Enforcement
URLs must be canonical before reaching the business layer. This removes the need for repetitive strict validation in downstream services.
