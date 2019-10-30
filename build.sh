pip install -r requirements/build.txt -r requirements/prod.txt --index-url http://localhost:8081/repository/pypi/simple
python setup.py sdist bdist_wheel
