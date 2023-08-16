install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	nose2 -s .

format:	
	black .

lint:
	pylint --disable=R,C --ignore-patterns=test_.*?py ./**/*.py

refactor: format lint

deploy:
	#deploy goes here
		
all: install lint test format deploy