all: install test
	#install lint test
	
setup:
	python3 -m venv ~/.demoqa-selenium
	echo "\n# Python venv" >> ~/.bash_profile
	echo "alias demoqa='source ~/.demoqa-selenium/bin/activate'" >> ~/.bash_profile
	source ~/.bash_profile

install:
	pip3 install --upgrade pip && pip3 install -r requirements.txt

test:
	# sequential execution:
	# pytest -s -v --setup-show -p no:randomly
	# parallel execution:
	pytest -s -v --setup-show -n auto -p no:randomly --html=reports/report.html --self-contained-html
	# random execution:
	# pytest -s -v --setup-show
	# parallel and random execution:
	# pytest -s -v --setup-show -n auto

lint:
	pylint tests

