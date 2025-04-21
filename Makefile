.PHONY: run, test

all: dev

dev: 
	uv run granian --host 0.0.0.0 --port 8000 --interface asgi --workers 1 src.svc_example.views:app

test:
	uv run --group test pytest tests/