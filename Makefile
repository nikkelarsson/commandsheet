PROJECT = commandsheet
PYTHON = python3
TESTSUITE = pytest
REQUIREMENTS_DEV = requirements/dev.txt

.PHONY: clean
clean:
	rm -rf dist/
	rm -rf build/
	rm -rf *.egg-info

.PHONY: twine
twine:
	$(PYTHON) -m pip install twine

.PHONY: install
install: clean uninstall
	$(PYTHON) -m pip install .

.PHONY: editable
editable: clean uninstall
	$(PYTHON) -m pip install --editable .

.PHONY: uninstall
uninstall: clean
	$(PYTHON) -m pip uninstall $(PROJECT)

.PHONY: dev
dev:
	$(PYTHON) -m pip install --requirement $(REQUIREMENTS_DEV)

.PHONY: test
test:
	coverage run

.PHONY: tox
tox:
	tox

.PHONY: lint
lint:
	flake8 $(PROJECT)/

.PHONY: build
build: clean
	$(PYTHON) -m build

.PHONY: check
check: build
	twine check dist/*

.PHONY: upload
upload: check
	twine upload dist/*
