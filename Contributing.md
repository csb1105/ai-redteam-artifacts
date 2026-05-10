# Contributing

Thank you for your interest in contributing to **AI Red Team Artifacts**.

This repository is intended to be a high-quality, doctrine-aligned corpus for AI red-team work. Contributions should improve clarity, coverage, or rigor.

## Types of Contributions

- New or refined **adversarial prompts**  
- Additional **baseline capability checks**  
- New **failure-mode reports** with strong evidence  
- Improved **methodology** or **glossaries**  
- Enhanced **tools** for parsing, analysis, or visualization  

## Contribution Guidelines

1. **Discuss first (optional but recommended)**  
   - Open an issue describing what you want to add or change.

2. **Follow the structure**  
   - Place prompts under `prompts/`.  
   - Place sessions under `sessions/`.  
   - Place reports under `reports/`.  
   - Update `libraries/` when adding new failure modes or prompt suites.

3. **Maintain doctrine alignment**  
   - Use existing terminology from `docs/glossaries/failure_modes.md`.  
   - Align severity and reporting with `docs/methodology/`.

4. **Evidence quality**  
   - Include transcript excerpts for any new failure-mode report.  
   - Clearly separate observation from interpretation.

5. **Coding standards**  
   - Prefer simple, readable Python in `tools/`.  
   - Add docstrings and type hints where appropriate.

## Pull Request Checklist

- [ ] All tests (if any) pass.  
- [ ] New files are placed in the correct directories.  
- [ ] Documentation is updated if behavior or doctrine changes.  
- [ ] Commit messages are clear and descriptive.

## License

By contributing, you agree that your contributions will be licensed under the **Apache License 2.0**.
