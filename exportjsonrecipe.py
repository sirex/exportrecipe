import json
import os.path


class ExportJsonRecipe(object):
    def __init__(self, buildout, name, options):
        self.options = dict(options)
        self.destination = os.path.join(
            buildout['buildout']['directory'],
            options.pop('destination-path', name + '.json'),
        )
        del self.options['recipe']

    def install(self):
        with open(self.destination, 'w') as f:
            json.dump(self.options, f, indent=2, sort_keys=True)
        return self.destination

    def update(self):
        self.install()
