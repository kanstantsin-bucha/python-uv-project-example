.PHONY: run, test

all: run

run: 
	uv run ./src/svc_example/asgi.py

test:
	uv run --group test pytest tests/