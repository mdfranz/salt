'''
Process json with the jinja2 templating engine

This renderer will take a json file with the jinja template and render it to a
high data format for salt states.
'''

import json
import os

# Import Third Party libs
from jinja2 import Template


def render(template, env='', sls=''):
    '''
    Render the data passing the functions and grains into the rendering system
    '''
    if not os.path.isfile(template):
        return {}

    passthrough = {}
    passthrough['salt'] = __salt__
    passthrough['grains'] = __grains__
    passthrough['env'] = env
    passthrough['sls'] = sls

    template = Template(open(template, 'r').read())
    json_data = template.render(**passthrough)

    return json.loads(json_data)
