# Sentinel patch — persist digests for the Content Engine

Sentinel currently emails each weekly digest and saves nothing. This patch makes the
GitHub Action also commit each digest to `digests/YYYY-MM-DD.md` in the Xavor-Sentinel
repo, which is where the Content Engine's Stage 0 fetches its monthly corpus from.

Two small changes in the `farafteraz/Xavor-Sentinel` repo:

## 1. `sentinel.py` — add after `send_email(...)` in `main()`

```python
    # Persist the digest so the monthly Content Engine can pick it up.
    os.makedirs("digests", exist_ok=True)
    digest_path = f"digests/{today.strftime('%Y-%m-%d')}.md"
    with open(digest_path, "w") as f:
        f.write(f"SENTINEL x XAVOR — WEEKLY DIGEST [{date_range}]\n\n{digest}\n")
    print(f"Digest saved to {digest_path}")
```

## 2. `.github/workflows/sentinel.yml` — add a commit step after "Run Sentinel",
and give the job write permission:

```yaml
permissions:
  contents: write
```

```yaml
      - name: Commit digest
        run: |
          git config user.name "sentinel"
          git config user.email "actions@github.com"
          git add digests/
          git commit -m "Weekly digest $(date -u +%Y-%m-%d)" || echo "nothing to commit"
          git push
```

That's the whole patch. After the next Sunday run, `python run.py` here will find the
digests automatically. Until then, pass `--corpus <file>`.
