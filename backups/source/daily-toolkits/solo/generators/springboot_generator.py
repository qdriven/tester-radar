# -*- coding:utf-8 -*-
from generators import render_template_to_file, rendered_template

sb_base_pom = "basic_pom.xml"
sb_base_service = "base_service.java"


def generate_sb_base_pom(artifact_id, project_name, group_id="io.hedwig.notes"):
    context_data = {"artifact_id": artifact_id,
                    "project_name": project_name,
                    "group_id": group_id}
    render_template_to_file(template_path=sb_base_pom,
                            context_data=context_data,
                            output_path="pom.xml")


def generate_service_class(entity_name, base_package):
    context_data = {"entity": entity_name, "base_package": base_package}
    return rendered_template(template_path="springboot/base_service.java", context_data=context_data)


def generate_exception_class(entity_name, base_package):
    context_data = {"entity": entity_name, "base_package": base_package}
    return rendered_template(template_path="springboot/exception.java", context_data=context_data)


def generate_repo_class(entity_name):
    template = """
    package io.hedwig.writing.hub.repositories;

    import io.hedwig.writing.hub.entity.{{entity_name}};
    import org.springframework.data.repository.PagingAndSortingRepository;

    public interface {{entity_name}}Repository extends PagingAndSortingRepository<{{entity_name}},Integer> {
    }
    """
    print(rendered_template(template, {"entity_name": entity_name}))


def generate_request_class(schema_definition):
    templates ="""
        create schema Hack(projectName string,
        message string,
        accessIP string,
        timestamp string,
        logStr string
    );
    """
    result = templates.split("(")
    class_name = result[0].split(" ")[-1]
    print(class_name)
    members = result[1].replace(",","").replace("\n","").split("string")[:-1]
    for member in members:
        print("private String {mem_name};".format(mem_name=member))




if __name__ == '__main__':
    # generate_sb_base_pom(artifact_id="kafka-service", project_name="rest apis for kafka operations")
    # generate_repo_class("Log")
    # entites = ['Option', 'WritingContent', 'Attachment', 'ContentMetaRef']
    # for item in entites:
    #     with open('service/'+item + "ServiceImpl.java", 'w') as f:
    #         f.write(generate_service_class(item, "io.hedwig.writing.hub"))
    #     with open('exception/'+item + "Exception.java", 'w') as f:
    #         f.write(generate_exception_class(item, "io.hedwig.writing.hub"))
    generate_request_class("")