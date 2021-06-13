.PHONY: test

help:
	@echo
	@echo "======================================================================"
	@echo
	@echo "repl:       open REPL w/ bypthon"
	@echo "test:       run tests"
	@echo "venv:       show Poetry environment info"
	@echo "deps:       list prod dependencies"
	@echo
	@echo "======================================================================"
	@echo

repl:
	export PYTHONSTARTUP='./repl.py' && poetry run bpython

test:
	poetry run pytest -v

venv:
	poetry env info

deps:
	poetry show --tree
