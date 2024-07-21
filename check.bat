python -m pytest --cov=src --cov-report=xml
python -m pytest --cov=src --cov-report=html:results/coverage.html
bandit -r src -x src/test_* -f html -o results/bandit-report.html
del "results\coverage.html\.gitignore"
