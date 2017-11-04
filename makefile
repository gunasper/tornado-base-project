pyenv = python3.5

run: 
	$(pyenv) project/app.py
	
deps:
	$(pyenv) -m pip install -r requirements
	
clear:
	find . | grep -E "(__pycache__|\.pyc|\.pyo$)" | xargs rm -rf

