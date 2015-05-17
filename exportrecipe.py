import json
import os.path
import collections


class ExportRecipe(object):
    def __init__(self, buildout, name, options):
        self.options = dict(options)
        self.destination = os.path.join(
            buildout['buildout']['directory'],
            options.pop('destination', name + '.json'),
        )
        del self.options['recipe']

    def install(self):
        with open(self.destination, 'w') as f:
            json.dump(self.options, f, indent=2, sort_keys=True)
        return self.destination

    def update(self):
        self.install()  # pragma: nocover


def load(path):
    with open(path) as f:
        data = json.load(f)
    Config = collections.namedtuple('Config', data.keys())
    return Config(**data)
