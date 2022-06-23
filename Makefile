clean:
	@find . -name "*.pyc" | xargs rm -rf
	@find . -name "*.pyo" | xargs rm -rf
	@find . -name "__pycache__" -type d | xargs rm -rf

lint: clean flake8 check-python-import

flake8:
	@flake8 --show-source src/

check-python-import:
	@isort --check-only src/

fix-python-import:
	@isort src/

run:
	@python run.py

setup-db:
	@alembic upgrade head
