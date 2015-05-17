How to do new release?
======================

1. In ``setup.py`` update version number.

2. In ``CHANGES.rst`` write new entry explaining what was changed in new
   release.

3. Run following commands::

       mktmpenv
       cd -
       rm -r dist
       pip install setuptools twine wheel tox --upgrade
       tox
       python setup.py sdist bdist_wheel
       python setup.py register
       twine upload dist/*
       git commit
       git tag 0.2
       git push origin tag 0.2
