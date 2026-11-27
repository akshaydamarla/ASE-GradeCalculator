# Python Grade Calculator

## Aim
To develop a Python grade calculator, write unit tests, and automate execution,
linting, and testing with GitHub Actions.

## Features
- Calculates the average of student marks.
- Assigns grades: A (90-100), B (80-89), C (70-79), D (60-69), F (below 60).
- Validates empty mark lists and marks outside 0-100.

## Run locally
```bash
python calculator.py
```
Enter marks separated by spaces, for example: `80 90 100`.

## Install development tools and run checks
```bash
python -m pip install -r requirements-dev.txt
python calculator.py
flake8 calculator.py tests
pytest -v
```

## GitHub Actions
The workflow at `.github/workflows/python-ci.yml` runs automatically on every
push and pull request. It checks out the repository, sets up Python 3.12,
installs pytest and flake8, executes the calculator, runs Flake8, and runs
the unit tests with Pytest.

## Upload to GitHub
Create an empty GitHub repository, then run:
```bash
git init
git add .
git commit -m "Add Python grade calculator with CI"
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/YOUR-REPOSITORY.git
git push -u origin main
```
Open the repository's **Actions** tab to view the actual workflow run.

## Expected result
- Calculator example (`80 90 100`): Average = 90.00, Grade = A.
- Pytest: 5 tests passed.
- Flake8: no style errors.
- GitHub Actions: all steps should show a green check when the push workflow
  completes successfully.

Note: The expected GitHub Actions result above is not a live GitHub run. A real
workflow result is available only after pushing this project to your repository.
