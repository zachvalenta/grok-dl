.PHONY: test

help:
	@echo
	@echo "======================================================================"
	@echo
	@echo "test:       run tests"
	@echo "venv:       show Poetry environment info"
	@echo "deps:       list prod dependencies"
	@echo
	@echo "======================================================================"
	@echo

test:
	poetry run pytest -v

venv:
	poetry env info

deps:
	poetry show --tree
