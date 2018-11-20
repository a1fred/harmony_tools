clean:
	rm -rf .mypy_cache build dist harmony_tools.egg-info


test:
	flake8 .
	mypy --ignore-missing-imports .
	python3 setup.py test

install:
	python3 setup.py install

release: test
	python3 setup.py sdist
	twine upload dist/*
