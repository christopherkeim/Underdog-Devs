install:
	poetry install

test:
	poetry run nose2 -s .

format:	
	poetry run black .

lint:
	poetry run ruff .

refactor: format lint

deploy:
	#deploy goes here
		
all: install lint test format deploy