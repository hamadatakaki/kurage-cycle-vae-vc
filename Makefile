lock:
	pip freeze > requirements.lock

setup:
	pip install -r requirements.txt

sync:
	pip install -r requirements.lock

fmt:
	black cycle-vae-vc local/scripts
