call python setup.py register -r "%1"
call python setup.py sdist bdist_wheel upload -r "%1"
call python .\setup.py upload_docs -r "%1"