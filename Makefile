.PHONY: tests coverage coverage-html devinstall
APP=.
COV=terrarium
OPTS=

help:
	@echo "tests - run tests"
	@echo "coverage - run tests with coverage enabled"
	@echo "coverage-html - run tests with coverage html export enabled"
	@echo "devinstall - install all packages required for development"


tests:
	py.test ${OPTS} ${APP}


coverage:
	py.test --cov=${COV} --cov-report=term-missing ${OPTS} ${APP}


coverage-html:
	py.test --cov=${COV} --cov-report=html ${OPTS} ${APP}


devinstall:
	pip install -e .
	pip install -r resources/requirements-develop.txt
