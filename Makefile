LOG_LEVEL ?=info
LOG_FORMAT ?=standard
PYTHONPATH =?$(pwd)

.PHONY:	install
install:
	pip install -r requirements.txt  --root-user-action

.PHONY:	test-cov
test-cov:
	pytest --cov=src/pyglog --cov-report=term tests/unit

.PHONY:	test-cov-html
test-cov-html:
	pytest --cov=src/pyglog --cov-report=html tests/unit

.PHONY:	build
build:
	make clean && python -m build

.PHONY: clean
clean:
	rm -rf dist/ build/ *.egg-info
	find . -name "__pycache__" -type d -exec rm -rf {} +
	find . -name "*.pyc" -exec rm -f {} +
	find . -name "*.pyo" -exec rm -f {} +

.PHONY:	lint
lint:
	ruff check --fix && ruff format

.PHONY:	check
check:
	ruff check --watch

.PHONY:	publish
publish:
	twine upload --verbose dist/*	

.PHONY:	log-info-standard
log-info-standard:
	LOG_LEVEL=info LOG_FORMAT=standard python main.py

.PHONY:	log-info-ecs
log-info-ecs:
	LOG_LEVEL=info LOG_FORMAT=ecs python main.py

.PHONY:	log-info
log-info:
	make log-info-standard && \
	make log-info-ecs

.PHONY:	log-error-standard
log-error-standard:
	LOG_LEVEL=error LOG_FORMAT=standard python main.py

.PHONY:	log-fatal-ecs
log-fatal-ecs:
	LOG_LEVEL=fatal LOG_FORMAT=ecs python main.py

.PHONY:	log-error-ops
log-error-ops:
	LOG_LEVEL=error LOG_FORMAT=opensearch python main.py