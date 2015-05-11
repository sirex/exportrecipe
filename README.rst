This is a Buildout recipe, that can export section options to JSON file. Later this exported file can be used to get
exported settings and use them in your project.


Usage
=====

.. code-block:: cfg

    [buildout]
    parts = settings

    [settings]
    recipe = exportjsonrecipe
    website_url = http://example.lt/

This will generate ``settings.json`` file in your buildout directory with following content:

.. code-block:: json

    {
      "website_url": "http://localhost:8000/"
    }

Now you can use this file for example in your ``settings.py``:
    
.. code-block:: python

    import json

    with open('settings.json') as f:
        settings = json.load(f)

    WEBSITE_URL = settings['website_url']
