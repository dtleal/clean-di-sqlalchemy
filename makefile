all: style wily test

install_pre_commit:
	pre-commit install

export_requirements:
	poetry export -f requirements.txt > requirements.txt --without-hashes

clean_pycache:
	find . -type d -name __pycache__ -exec rm -r {} \+

style:
	poetry run flake8 *.md Makefile --select=W291

test:
	poetry run pytest -s -l -vvv tests/ --cov src/ --cov-fail-under=0 --cov-report xml --cov-report term:skip-covered

wily:
	poetry run wily build src/
	poetry run wily diff -a --no-detail src/

run:
	poetry run gunicorn -w 2 -k uvicorn.workers.UvicornWorker --timeout 120 --chdir src main:app

debug:
	poetry run uvicorn --host 127.0.0.1 --port 8000 --reload --log-level debug --app-dir src main:app
