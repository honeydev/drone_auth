# test/setup/start/install/

lint:
	flake8 --config=setup.cfg && cd frontend && yarn lint

install:
	pipenv install
	cd frontend && yarn install && yarn build --mode development
