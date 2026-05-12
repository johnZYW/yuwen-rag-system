# Security and privacy note

This public repository has been prepared for portfolio and competition review.

The following items were intentionally excluded before publication:

- API keys and credential files
- Google service account JSON files
- local SQLite memory databases
- audio recordings and generated voice files
- macOS metadata files
- generated embedding caches
- large/private slides and personal documents
- non-public source articles or working datasets

Use environment variables for credentials. Never commit `.env`, `keys/`, `API_key/`, or service-account JSON files.

Recommended local variables:

```bash
export OPENAI_API_KEY="your_key_here"
export ELEVENLABS_API_KEY="your_key_here"
export GOOGLE_APPLICATION_CREDENTIALS="/absolute/path/to/google-service-account.json"
```
