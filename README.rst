.. image:: https://travis-ci.org/sirex/exportrecipe.svg
   :target: https://travis-ci.org/sirex/exportrecipe

.. image:: https://coveralls.io/repos/sirex/exportrecipe/badge.svg
   :target: https://coveralls.io/r/sirex/exportrecipe

----

This is a Buildout recipe, that can export buildout configuration to JSON file.
Later this exported file can be used to get exported settings and use them in
your project.

Buildout provides extensive functionality for managing configuration, but does
not have tools to use this configuration anywhere else outside Buildout itself.
This recipe exports all settings to JSON file, allowing to use configuration
parameters outside Buildout.


Usage
=====

.. code-block:: cfg

    [buildout]
    parts = settings

    [settings]
    recipe = exportrecipe
    website-url = http://example.com/

This will generate ``settings.json`` file in your buildout directory with following content:

.. code-block:: json

    {
      "website-url": "http://localhost:8000/"
    }

``exportrecipe`` will export all parameters from recipe's section, except
``recipe`` parameter.

Now you can use this file for example in your ``settings.py``:
    
.. code-block:: python

    import json

    with open('settings.json') as f:
        settings = json.load(f)

    WEBSITE_URL = settings['website-url']

Also you can use a helper:

.. code-block:: python

    import exportrecipe

    config = exportrecipe.load('settings.json')

    WEBSITE_URL = config.website_url

It is possible to change destination of exported file using ``destination``
option:

.. code-block:: cfg

    [buildout]
    parts = settings

    [settings]
    recipe = exportrecipe
    destination = somewhereelse.json
    website-url = http://example.com/

This will generate ``somewhereelse.json`` file with following content:

.. code-block:: json

    {
      "destination": "somewhereelse.json",
      "website-url": "http://localhost:8000/"
    }
