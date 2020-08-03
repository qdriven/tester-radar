# -*- coding:utf-8 -*-
import os
import subprocess

import sys
from jinja2 import Template

koan_documents = """
# {koan_header}
- usage
```{language}
{code_content}
//result
{code_result}
```
"""


def node_run(source_file):
    result = subprocess.call(["node", source_file])
    return result.stdout


def generate_koans(koan_desc, source_file, run_shell=node_run, language="javascript"):
    current_path = os.getcwd()
    print(current_path)
    with open(os.path.join(current_path, source_file), 'r') as f:
        code_content = f.readlines()

    context = {"koan_header": koan_desc,
               "language": language,
               "code_content": code_content,
               "code_result": run_shell(source_file)
               }
    template = Template(koan_documents)
    print(template.render(context))


if __name__ == '__main__':
    source_file = sys.argv[1]
    koan_header = sys.argv[2]
    if sys.argv[3]:
        language = sys.argv[3]
    else:
        language = "javascript"
    generate_koans(koan_header, source_file, language=language)
