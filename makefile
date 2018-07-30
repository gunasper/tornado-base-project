pyenv = python3

run: 
	$(pyenv) project_name/app.py
	
deps:
	$(pyenv) -m pip install -r requirements

docker-deps:
	sudo apt install -y docker.io

docker-deps:
	cp ~/.ssh/id_rsa .
	sudo docker build --rm -t search_api_image . --build-arg build=$(date)
	sudo docker rm -f search_api_container; sudo docker run -e LANG=C.UTF-8 -p 8000:8000 --name="search_api_container" -d search_api_image;

clear:
	find . | grep -E "(__pycache__|\.pyc|\.pyo$)" | xargs rm -rf

