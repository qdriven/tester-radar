# -*- coding:utf-8 -*-
"""
Different Generators for productivity

- gitbook
"""
import os

from jinja2 import Environment, Template
from jinja2 import PackageLoader

generator_env = Environment(loader=PackageLoader(package_name='generators',
                                                 package_path='templates'))


def render_template_to_file(template_path, context_data, output_path=os.getcwd() + '/output.md'):
    template = generator_env.get_template(template_path)
    result = template.render(context_data)
    with open(output_path, 'w') as output:
        output.write(result)


def rendered_template(template_content, context):
    return Template(template_content).render(context)


def rendered_template(template_path, context_data):
    template = generator_env.get_template(template_path)
    result = template.render(context_data)
    return result
