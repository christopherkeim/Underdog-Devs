install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	nose2 -s .

format:	
	black .

lint:
	pylint --recursive=True --disable=R,C --ignore-patterns=test_.*?py .

refactor: format lint

deploy:
	#deploy goes here
		
all: install lint test format deploy