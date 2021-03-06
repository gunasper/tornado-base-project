pyenv = python3

run: 
	$(pyenv) project_name/app.py

run-prod: 
	$(pyenv) project_name/app.py --prod

deps:
	$(pyenv) -m pip install -r requirements --user

docker-deps:
	sudo apt install -y docker.io

docker-start:
	cp ~/.ssh/id_rsa .
	sudo docker build --rm -t project_image . --build-arg build=$(shell date +%s)
	sudo docker rm -f project_container; sudo docker run --restart always -e LANG=C.UTF-8 -p 5000:5000 --name="project_container" -d project_image;

clear:
	find . | grep -E "(__pycache__|\.pyc|\.pyo$)" | xargs rm -rf

