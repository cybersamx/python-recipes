VENV := .venv
PYTHON := $(VENV)/bin/python3
PIP := $(VENV)/bin/pip
VIRTUAL_ENV := python3 -m venv

# Colorized print
BOLD := $(shell tput bold)
RED := $(shell tput setaf 1)
BLUE := $(shell tput setaf 4)
RESET := $(shell tput sgr0)

# Default target

.PHONY: all
all: run

# If virtual environment has been set up, we won't see the activate file.
$(VENV)/bin/activate: requirements.txt
	@echo "$(BOLD)$(BLUE)Setting up virtual environment $(VENV).$(RESET)"
	$(VIRTUAL_ENV) $(VENV)
	$(PIP) install -r requirements.txt
	@echo "$(BOLD)$(BLUE)Installed a virtual environment called $(VENV).$(RESET)"

# Phony target for running the virtual environment setup
.PHONY: venv
venv: $(VENV)/bin/activate

##@ run: Run the program.

.PHONY: run
run: venv lint
	@echo "$(BOLD)$(BLUE)Build the python project.$(RESET)"
	$(PYTHON) main.py

##@ lint: Run a linter against the project

.PHONY: lint
lint:
	@echo "$(BOLD)$(BLUE)Run linter against the python project.$(RESET)"
	flake8 *.py

##@ clean: Clean output files and build cache

.PHONY: clean
clean:
	@echo "$(BOLD)$(RED)Removing build cache.$(RESET)"
	rm -rf __pycache__
	find . -type f -name '*.pyc' -delete

##@ help: Help

.PHONY: help
help: Makefile
	@-echo " Usage:\n  make $(BLUE)<target>$(RESET)"
	@-echo
	@-sed -n 's/^##@//p' $< | column -t -s ':' | sed -e 's/[^ ]*/ &/2'
