# micheblog

Sample project built with django.

### Requirements

	- Python3
	- Pip
	- Virtualenv

### How to run

After you cloned this repository you need to run the next commands.

	virtualenv .venv
	source .venv/bin/activate
	pip install -r requirements.txt
	./manage.py migrate
	./manage.py createsuperuser # Follow the wizard
	./manage.py runserver # open de browser and sign in with your credentials
