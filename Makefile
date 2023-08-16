install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	for item in $$(ls -d */ | cut -d "/" -f1); do nose2 -s ./$$item/tests/ ; done

format:	
	black .

lint:
	pylint --disable=R,C --ignore-patterns=test_.*?py ./**/*.py

refactor: format lint

deploy:
	#deploy goes here
		
all: install lint test format deploy