dev-setup:
	sudo apt-get update
	sudo pip3 install virtualenv
	sudo apt-get install python3-dev python3-venv
	python3 -m venv .venv
	( \
		. .venv/bin/activate; \
		 pip install --upgrade pip \
		pip install -r requirements.txt; \
	)

up:
	cd docker; \
	docker-compose up

up-detached:
	cd docker; \
	docker-compose up -d

down:
	cd docker; \
	docker-compose down