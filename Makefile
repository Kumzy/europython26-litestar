SHELL := /bin/bash
# =============================================================================
# Variables
# =============================================================================

.DEFAULT_GOAL:=help
.ONESHELL:
.EXPORT_ALL_VARIABLES:
MAKEFLAGS += --no-print-directory

# Define colors and formatting
BLUE := $(shell printf "\033[1;34m")
GREEN := $(shell printf "\033[1;32m")
RED := $(shell printf "\033[1;31m")
YELLOW := $(shell printf "\033[1;33m")
NC := $(shell printf "\033[0m")
INFO := $(shell printf "$(BLUE)ℹ$(NC)")
OK := $(shell printf "$(GREEN)✓$(NC)")
WARN := $(shell printf "$(YELLOW)⚠$(NC)")
ERROR := $(shell printf "$(RED)✖$(NC)")

.PHONY: help
help:                                               ## Display this help text for Makefile
	@awk 'BEGIN {FS = ":.*##"; printf "\nUsage:\n  make \033[36m<target>\033[0m\n"} /^[a-zA-Z0-9_-]+:.*?##/ { printf "  \033[36m%-15s\033[0m %s\n", $$1, $$2 } /^##@/ { printf "\n\033[1m%s\033[0m\n", substr($$0, 5) } ' $(MAKEFILE_LIST)


# =============================================================================
# Developer Utils
# =============================================================================
.PHONY: install-uv
install-uv:                                         ## Install latest version of uv
	@echo "${INFO} Installing uv..."
	@curl -LsSf https://astral.sh/uv/install.sh | sh >/dev/null 2>&1
	@echo "${OK} UV installed successfully"

.PHONY: install
install:                                            ## Install project deps (npm + uv) and prek git hooks
	@echo "${INFO} Starting installation..."
	@npm install
	@uv sync
	@uv run prek install
	@echo "${OK} Installation complete!"

.PHONY: upgrade
upgrade:                                            ## Upgrade all dependencies to the latest stable versions
	@echo "${INFO} Updating all dependencies..."
	@uv lock --upgrade
	@npm update
	@echo "${OK} Dependencies updated"

.PHONY: clean
clean:                                              ## Cleanup temporary build artifacts
	@echo "${INFO} Cleaning working directory..."
	@rm -rf dist/ .pytest_cache .ruff_cache .slidev >/dev/null 2>&1
	@find . -name '__pycache__' -not -path './node_modules/*' -exec rm -rf {} + >/dev/null 2>&1
	@echo "${OK} Working directory cleaned"

.PHONY: destroy
destroy: clean                                      ## Destroy the virtual environment and node_modules
	@echo "${INFO} Destroying virtual environment and node_modules..."
	@rm -rf .venv node_modules
	@echo "${OK} Environments destroyed"


# =============================================================================
# Slides
# =============================================================================
.PHONY: dev
dev:                                                ## Start Slidev dev server (http://localhost:3030)
	@npm run dev

.PHONY: build
build:                                              ## Build the static deck -> dist/ (the "does it still build?" check)
	@echo "${INFO} Building deck..."
	@npm run build
	@echo "${OK} Deck built to dist/"

.PHONY: export-pdf
export-pdf:                                         ## Export the deck to PDF -> dist/slides.pdf
	@echo "${INFO} Exporting deck to PDF..."
	@npm run export-pdf
	@echo "${OK} PDF exported to dist/slides.pdf"


# =============================================================================
# Tests, Linting, Formatting
# =============================================================================
.PHONY: prek
prek:                                               ## Run prek hooks on all files (prek.toml)
	@uv run prek run --all-files

.PHONY: test
test:                                               ## Run the example tripwire tests (pytest)
	@echo "${INFO} Running test cases..."
	@uv run pytest --quiet
	@echo "${OK} Tests passed"

.PHONY: lint
lint:                                               ## Run all linting (oxlint + ruff + pyright)
	@echo "${INFO} Running linters..."
	@npm run lint
	@uv run ruff check examples
	@uv run pyright
	@echo "${OK} Linting passed"

.PHONY: fix
fix:                                                ## Run formatting scripts (oxfmt + ruff format)
	@echo "${INFO} Running code formatters..."
	@npm run fmt
	@uv run ruff format examples
	@echo "${OK} Code formatting complete"
