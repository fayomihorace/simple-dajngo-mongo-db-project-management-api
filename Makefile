SHELL := /bin/bash

test:
	# Meant to be ran locally
	# Reuse DB for faster tests, 4 workers, 120s timeout, report the 16 slowest tests, verbose, show local variables
	# cd ess && IS_TESTING=1 pytest --reuse-db -vvl -n auto --maxprocesses=6 --dist worksteal --durations=16 --timeout 120
	cd ess && pytest -s --reuse-db

install:
	cd ess && pip install -U -r requirements.txt

run:
	# For development purposes only!
	cd ess && python manage.py runserver

lint:
	mkdir -p product/pylint
	cd ess && pylint --output-format=text -j 2 main | tee ./pylint/pylint.log || pylint-exit $?
	cd ess && pylint --output-format=text -j 2 main | tee ./pylint/pylint.log || pylint-exit $?
	cd ess && ruff main utils ess

codestyle:
	cd ess && black --check main
	cd ess && black --check utils
	cd ess && black --check ess

migrate:
	cd ess && python manage.py migrate
