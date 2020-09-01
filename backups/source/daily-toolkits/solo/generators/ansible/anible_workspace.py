# -*- coding:utf-8 -*-
import subprocess

default_environments = ["production", "test", "performance", "staging"]


def _run_touch(env, file_path_template="inventories/{env}/hosts"):
    # todo think about jinja2 template manner
    subprocess.run(["touch", file_path_template.format(env=env)])


def _run_create_inv_vars(env, parent_folder_template="inventories/{env}", with_hosts_file=True):
    parent_folder = parent_folder_template.format(env)
    if with_hosts_file:
        _run_touch(env, file_path_template=parent_folder + "hosts")
    subprocess.run(["mkdir", "-p", parent_folder + "/group_vars"])
    subprocess.run(["mkdir", "-p", parent_folder + "/host_vars"])


def create_inventory_2(environments=None):
    """
    http://docs.ansible.com/ansible/playbooks_best_practices.html
    Best practices: layout two
    :param environments: different environments name, such as test,staging,prod,performance
    :return: 
    """
    environments = default_environments if environments is None else environments
    subprocess.run(["mkdir", "-p", "inventories"])
    for environment in environments:
        _run_create_inv_vars(env=environment)
        _run_touch(env=environment)


def create_inventory_1(environments=None):
    """
    http://docs.ansible.com/ansible/playbooks_best_practices.html
    Best practices: layout 1
    :param environments: different environments name, such as test,staging,prod,performance
    :return: 
    """
    environments = default_environments if environments is None else environments
    for environment in environments:
        _run_touch(env=environment, file_path_template="{env}")
        _run_create_inv_vars(env=environment, parent_folder_template=".", with_hosts_file=False)


def create_libs_and_plugin():
    for item in ["library", "filter_plugin"]:
        subprocess.run(["mkdir", "-p", item])


def create_role(role_name):
    if role_name is None:
        return
    role_base_path = "roles/" + role_name
    subprocess.run(["mkdir", "-p", role_base_path])
    for item_with_main_yml in ["tasks", "handlers", "files", "vars", "defaults", "meta"]:
        subprocess.run(["mkdir", "-p", role_base_path + "/" + item_with_main_yml])
        subprocess.run(["touch", role_base_path + "/" + item_with_main_yml + "/main.yml"])
    for item_wo_main_yml in ["library", "lookup_plugins", "templates"]:
        subprocess.run(["mkdir", "-p", role_base_path + "/" + item_wo_main_yml])


def init_workspace_recommended_2(environments=None, role_name=None):
    create_inventory_2(environments)
    create_libs_and_plugin()
    create_role(role_name)


def init_workspace_recommended_1(environments=None, role_name=None):
    create_inventory_1(environments)
    create_libs_and_plugin()
    create_role(role_name)


def init_workspace(solution_index=1, environments=None, role_name=None):
    solution_mapping = {
        "1": init_workspace_recommended_1,
        "2": init_workspace_recommended_2,
    }

    solution_mapping.get(solution_index, init_workspace_recommended_1) \
        (environments=environments, role_name=role_name)


if __name__ == '__main__':
    init_workspace(1)
