VERSION := $(shell grep VERSION pyproject.toml | \
sed -n 1p | \
awk '/VERSION/{print $$NF}' | \
tr -d '"' | \
awk '{print "v"$$0}')

v_test:
	echo $(VERSION)

clean:
	find . -type f -name "*.py[co]" -delete
	find . -type d -name "__pycache__" -delete
	find . -name '*.egg-info' -exec rm -rf {} +
	find . -name '*.egg' -exec rm -rf {} +
	rm -rf .mypy_cache/
	rm -rf .pytest_cache/
	rm -rf build/
	rm -rf dist/
	rm -rf .eggs/

develop:
	poetry install

install:
	poetry install --no-dev

format: clean
	poetry run isort -rc dash_covid19/
	poetry run black dash_covid19/

lint: format
	poetry run pylint dash_covid19/
	poetry check

test: lint
	pytest --webdriver Chrome --headless --ignore=docs --verbose --instafail --mypy --mypy-ignore-missing-imports --doctest-modules --cov=dash_covid19/ --cov-report term

patch: test
	poetry version patch
	git add pyproject.toml
	git commit -m "VERSION bump"
	git tag $(VERSION)
	git push origin master --tags

minor: test
	poetry version minor
	git add pyproject.toml
	git commit -m "VERSION bump"
	git tag $(VERSION)
	git push origin master --tags

major: test
	poetry version major
	git add pyproject.toml
	git commit -m "VERSION bump"
	git tag $(VERSION)
	git push origin master --tags

.PHONY: clean develop install format lint test patch minor major
