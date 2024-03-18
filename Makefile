lock:
	pip freeze > requirements.lock

setup:
	pip install -r requirements.txt

sync:
	pip install -r requirements.lock

fmt:
	-black cycle_vae_vc local/scripts

lint:
	-isort cycle_vae_vc local/scripts
	-flake8 cycle_vae_vc local/scripts
	-mypy cycle_vae_vc local/scripts
