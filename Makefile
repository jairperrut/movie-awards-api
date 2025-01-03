run-server:
	uvicorn src.api.main:create_app --host 0.0.0.0 --port 8000 --lifespan on

run-tests:
	python -m pytest
