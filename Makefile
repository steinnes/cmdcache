all:
	virtualenv venv
	venv/bin/python setup.py develop

clean:
	rm -rf dist/

release: clean
	venv/bin/python setup.py sdist bdist_wheel
	twine upload dist/*.tar.gz
	twine upload dist/*.whl

release_test:
	venv/bin/python setup.py sdist bdist_wheel upload -r pypitest
