.PHONY: env activate clean lab

PYTHON_VERSION=3.8.1
PYTHON_ENV_NAME=ml-examples
MAKE:=$(MAKE) --no-print-directory
SHELL=bash

# pyenv:
# 	$(info [*] Install pyenv using https://github.com/pyenv/pyenv-installer/raw/master/bin/pyenv-installer...)
# 	@curl -L https://github.com/pyenv/pyenv-installer/raw/master/bin/pyenv-installer 2> /dev/null | bash

env: 
	$(info [*] Download and install python $(PYTHON_VERSION)...)
	@pyenv install --skip-existing $(PYTHON_VERSION)
	@pyenv local $(PYTHON_VERSION) 
	$(info [*] Deleting any existing virtualenv $(PYTHON_ENV_NAME) using python $(PYTHON_VERSION)...)
	@pyenv virtualenv-delete --force $(PYTHON_ENV_NAME); true
	$(info [*] Create virtualenv $(PYTHON_ENV_NAME) using python $(PYTHON_VERSION)...)
	@pyenv virtualenv --force $(PYTHON_VERSION) $(PYTHON_ENV_NAME)
	@$(MAKE) activate
	$(info [*] Install python dependencies...)
	@pip install --upgrade pip
	@pip install pip-tools
	@pip-compile
	@pip-sync
		
activate:
	$(info [*] Activate virtualenv $(PYTHON_ENV_NAME)...)
	$(shell eval "$$(pyenv init -)" && eval "$$(pyenv virtualenv-init -)" && pyenv activate $(PYTHON_ENV_NAME) && pyenv local $(PYTHON_ENV_NAME))

lab:
	$(MAKE) activate
	$(info [*] Start jupyter lab)
	@cd notebooks && jupyter lab

clean:
	$(info [*] Deleting artifacts for $(PYTHON_ENV)...)
	@rm -Rf *.egg .eggs .cache dist build .pytest_cache *.egg-info
	@find -depth -type d -name __pycache__ -exec rm -Rf {} \;
	@find -depth -type d -name .ipynb_checkpoints -exec rm -Rf {} \;
	@find -type f -name '*.pyc' -delete


