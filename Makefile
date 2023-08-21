install:
	poetry install

test:
	nose2 -s .

format:	
	black .

lint:
	ruff .

refactor: format lint

deploy:
	#deploy goes here
		
all: install lint test format deploy