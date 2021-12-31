clean:
	@find . -name "*.pyc" | xargs rm -rf
	@find . -name "*.pyo" | xargs rm -rf
	@find . -name "__pycache__" -type d | xargs rm -rf

lint: clean flake8 check-python-import

flake8:
	@poetry run flake8 --show-source src/

check-python-import:
	@poetry run isort --check-only src/

fix-python-import:
	@poetry run isort src/

run:
	@poetry run python run.py

setup-db:
	@poetry run alembic upgrade head
