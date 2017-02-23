all:
	virtualenv venv
	venv/bin/python setup.py develop

release:
	venv/bin/python setup.py sdist bdist_wheel upload -r pypi

release_test:
	venv/bin/python setup.py sdist bdist_wheel upload -r pypitest
