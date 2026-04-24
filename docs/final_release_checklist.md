# Final Release Checklist

Use this checklist immediately before submission.

1. Confirm the repo is clean with `git status`.
2. Reinstall dependencies in a clean environment with `python3 -m pip install -r requirements.txt`.
3. Delete non-source outputs if needed and rerun `bash run_all.sh`.
4. Confirm `metadata/validation_report.json` contains `"valid": true`.
5. Review `README.md`, `docs/data_dictionary.md`, `metadata/project.jsonld`, and `CITATION.cff`.
6. Stage and commit the final MS4 changes with clear author identities for both contributors.
7. Push the final branch to GitHub.
8. Create a `final-project` tag.
9. Create a GitHub release from that tag and include the tested workflow command in the release notes.
10. Submit the GitHub release URL to Canvas.
