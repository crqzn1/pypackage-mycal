## mlcal

### build
```bash
$ pip install wheel
$ python setup.py sdist bdist_wheel
```

### upload 
```bash
$ pip install twine
$ twine check dist/*
$ twine upload --repository-url https://test.pypi.org/legacy/ dist/*
```

### install
https://test.pypi.org/project/mycal/
```bash
$ pip install -i https://test.pypi.org/simple/ mycal
```

