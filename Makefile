.PHONY: test

help:
	@echo
	@echo "======================================================================"
	@echo
	@echo "repl:       open REPL w/ bypthon"
	@echo "test:       run unit tests"
	@echo "doc:        run doctests"
	@echo "venv:       show Poetry environment info"
	@echo "deps:       list prod dependencies"
	@echo
	@echo "======================================================================"
	@echo

repl:
	export PYTHONSTARTUP='./repl.py' && poetry run bpython

test:
	poetry run pytest -v

doc:
	poetry run python -m doctest -v chapter_3.py

venv:
	poetry env info

deps:
	poetry show --tree
