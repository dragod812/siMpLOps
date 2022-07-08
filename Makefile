.ONESHELL:
SHELL := /bin/bash

run:
	source venv/bin/activate && \
	# run some command

test:
	source venv/bin/activate && \
	# run some command

install:
	source venv/bin/activate && \
	python -m pip install -r requirements.txt

venv:
	python3 -m pip install --upgrade pip
	python3 -m pip install -U virtualenv
	python3 -m virtualenv venv
	chmod +x venv/bin/activate
	make install

