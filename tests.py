import six
import json
import mock
import unittest

import exportrecipe


class RecipeTests(unittest.TestCase):
    def recipe_install(self, buildout, name, options):
        handle = six.StringIO()
        open = mock.mock_open()
        open.return_value.__enter__.return_value = handle
        recipe = exportrecipe.ExportRecipe(buildout, name, options)
        with mock.patch('exportrecipe.open', open, create=True):
            recipe.install()
        return open, handle.getvalue()

    def test_no_params(self):
        buildout = {'buildout': {'directory': '/tmp'}}
        name = 'settings'
        options = {
            'recipe': 'exportrecipe',
        }
        open, content = self.recipe_install(buildout, name, options)
        open.assert_called_once_with('/tmp/settings.json', 'w')
        self.assertEqual(json.loads(content), {})

    def test_with_params(self):
        buildout = {'buildout': {'directory': '/tmp'}}
        name = 'settings'
        options = {
            'recipe': 'exportrecipe',
            'option': 'value',
        }
        open, content = self.recipe_install(buildout, name, options)
        open.assert_called_once_with('/tmp/settings.json', 'w')
        self.assertEqual(json.loads(content), {'option': 'value'})

    def test_destination(self):
        buildout = {'buildout': {'directory': '/tmp'}}
        name = 'settings'
        options = {
            'recipe': 'exportrecipe',
            'destination': 'somewhereelse.json',
        }
        open, content = self.recipe_install(buildout, name, options)
        open.assert_called_once_with('/tmp/somewhereelse.json', 'w')
        self.assertEqual(json.loads(content), {'destination': 'somewhereelse.json'})


class HelperTests(unittest.TestCase):
    def test_load(self):
        with mock.patch('exportrecipe.open', mock.mock_open(read_data='{"option": "value"}'), create=True):
            config = exportrecipe.load('settings.json')
        self.assertEqual(config.option, 'value')
