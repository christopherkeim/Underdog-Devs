install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	for item in $(ls); do
		if [ -d $item ] 
		then
	  		nosetests ./$item/tests/
		fi
	done

format:	
	black *.py 

lint:
	pylint --disable=R,C --ignore-patterns=test_.*?py ./**/*.py

refactor: format lint

deploy:
	#deploy goes here
		
all: install lint test format deploy