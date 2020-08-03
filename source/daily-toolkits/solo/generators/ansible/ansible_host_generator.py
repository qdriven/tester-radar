# -*- coding:utf-8 -*-
from jinja2 import Template

ansible_host_template = """
[{{role_name}}]
{% for host in hosts %}
{{host.host_name}} ansible_host={{host.host_ip}} ansible_ssh_user={{host.user}} ansible_ssh_pass={{host.pwd}}
{% endfor %}
"""


def generate_hosts(role_name, host_name_prefix,
                   host_start_ip, hosts_count=1, user="root",
                   pwd="123456"):
    hosts = []
    context_data = {}
    context_data["role_name"] = role_name
    ip_array = host_start_ip.split(".")
    for index in range(hosts_count):
        host = {}
        host["host_name"] = host_name_prefix + str(index + 1)
        ip=ip_array[0:3]
        ip.append(str(int(ip_array[3]) + index))
        host["host_ip"] = ".".join(ip)
        host["user"] = user
        host["pwd"] = pwd
        hosts.append(host)

    context_data["hosts"] = hosts
    template = Template(ansible_host_template)
    result =template.render(context_data)
    print(result)
    return result

