# -*- coding:utf-8 -*-
from jinja2 import Template

table_ddl_template = """
CREATE TABLE `{{table_name}}` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  {% for item in columns %}
    `{{item.name}}`  {{item.type}} DEFAULT {{item.default_value}},
  {% endfor %}
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8 COLLATE=utf8_bin

"""


def generate_table_ddl(schema_definition={}):
    template = Template(table_ddl_template)
    context_data = {"table_name": schema_definition["description"], "columns": []}
    column_properties = schema_definition["properties"]
    for k, v in column_properties.items():
        item = {}
        item["name"] = k
        item["type"] = _type_convertor(v["type"])
        if str(k).lower().find("timestamp") >= 0:
            item["type"] = "timestamp"
        else:
            item["type"] = _type_convertor(v["type"])
            item["default_value"] = "NULL"

        context_data["columns"].append(item)
    result = template.render(context_data)
    print(result)
    return result


def _type_convertor(schema_type):
    type_mapping = {
        "string": "varchar(255)",
        "number": "float(15,2)",
        "integer": "varchar(255)"
    }
    return type_mapping.get(schema_type, "varchar(255)")


if __name__ == '__main__':
    #     schema_definition = {
    #   "$schema": "http://json-schema.org/draft-04/schema#",
    #   "description": "HugeFields",
    #   "type": "object",
    #   "properties": {
    #     "requestId":{
    #       "type":"string",
    #       "key":True
    #     },
    #     "eventId": {
    #       "type": "string",
    #     },
    #     "userId": {
    #       "type": "string"
    #     },
    #     "timestamp": {
    #       "type": "number"
    #     },
    #     "userIp": {
    #       "type": "string"
    #     },
    #     "field0": {
    #       "type": "string"
    #     },
    #     "field1": {
    #       "type": "string"
    #     },
    #     "field2": {
    #       "type": "string"
    #     },
    #     "field3": {
    #       "type": "string"
    #     },
    #     "field4": {
    #       "type": "string"
    #     },
    #     "field5": {
    #       "type": "string"
    #     },
    #     "field6": {
    #       "type": "string"
    #     },
    #     "field7": {
    #       "type": "string"
    #     },
    #     "field8": {
    #       "type": "string"
    #     },
    #     "field9": {
    #       "type": "string"
    #     },
    #     "field10": {
    #       "type": "string"
    #     },
    #     "field11": {
    #       "type": "string"
    #     },
    #     "field12": {
    #       "type": "string"
    #     },
    #     "field13": {
    #       "type": "string"
    #     },
    #     "field14": {
    #       "type": "string"
    #     },
    #     "field15": {
    #       "type": "string"
    #     },
    #     "field16": {
    #       "type": "string"
    #     },
    #     "field17": {
    #       "type": "string"
    #     },
    #     "field18": {
    #       "type": "string"
    #     },
    #     "field19": {
    #       "type": "string"
    #     },
    #     "field20": {
    #       "type": "string"
    #     },
    #     "field21": {
    #       "type": "string"
    #     },
    #     "field22": {
    #       "type": "string"
    #     },
    #     "field23": {
    #       "type": "string"
    #     },
    #     "field24": {
    #       "type": "string"
    #     },
    #     "field25": {
    #       "type": "string"
    #     },
    #     "field26": {
    #       "type": "string"
    #     },
    #     "field27": {
    #       "type": "string"
    #     },
    #     "field28": {
    #       "type": "string"
    #     },
    #     "field29": {
    #       "type": "string"
    #     },
    #     "field30": {
    #       "type": "string"
    #     },
    #     "field31": {
    #       "type": "string"
    #     },
    #     "field32": {
    #       "type": "string"
    #     },
    #     "field33": {
    #       "type": "string"
    #     },
    #     "field34": {
    #       "type": "string"
    #     },
    #     "field35": {
    #       "type": "string"
    #     },
    #     "field36": {
    #       "type": "string"
    #     },
    #     "field37": {
    #       "type": "string"
    #     },
    #     "field38": {
    #       "type": "string"
    #     },
    #     "field39": {
    #       "type": "string"
    #     },
    #     "field40": {
    #       "type": "string"
    #     },
    #     "field41": {
    #       "type": "string"
    #     },
    #     "field42": {
    #       "type": "string"
    #     },
    #     "field43": {
    #       "type": "string"
    #     },
    #     "field44": {
    #       "type": "string"
    #     },
    #     "field45": {
    #       "type": "string"
    #     },
    #     "field46": {
    #       "type": "string"
    #     },
    #     "field47": {
    #       "type": "string"
    #     },
    #     "field48": {
    #       "type": "string"
    #     },
    #     "field49": {
    #       "type": "string"
    #     },
    #     "field50": {
    #       "type": "string"
    #     },
    #     "field51": {
    #       "type": "string"
    #     },
    #     "field52": {
    #       "type": "string"
    #     },
    #     "field53": {
    #       "type": "string"
    #     },
    #     "field54": {
    #       "type": "string"
    #     },
    #     "field55": {
    #       "type": "string"
    #     },
    #     "field56": {
    #       "type": "string"
    #     },
    #     "field57": {
    #       "type": "string"
    #     },
    #     "field58": {
    #       "type": "string"
    #     },
    #     "field59": {
    #       "type": "string"
    #     },
    #     "field60": {
    #       "type": "string"
    #     },
    #     "field61": {
    #       "type": "string"
    #     },
    #     "field62": {
    #       "type": "string"
    #     },
    #     "field63": {
    #       "type": "string"
    #     },
    #     "field64": {
    #       "type": "string"
    #     },
    #     "field65": {
    #       "type": "string"
    #     },
    #     "field66": {
    #       "type": "string"
    #     },
    #     "field67": {
    #       "type": "string"
    #     },
    #     "field68": {
    #       "type": "string"
    #     },
    #     "field69": {
    #       "type": "string"
    #     },
    #     "field70": {
    #       "type": "string"
    #     },
    #     "field71": {
    #       "type": "string"
    #     },
    #     "field72": {
    #       "type": "string"
    #     },
    #     "field73": {
    #       "type": "string"
    #     },
    #     "field74": {
    #       "type": "string"
    #     },
    #     "field75": {
    #       "type": "string"
    #     },
    #     "field76": {
    #       "type": "string"
    #     },
    #     "field77": {
    #       "type": "string"
    #     },
    #     "field78": {
    #       "type": "string"
    #     },
    #     "field79": {
    #       "type": "string"
    #     },
    #     "field80": {
    #       "type": "string"
    #     },
    #     "field81": {
    #       "type": "string"
    #     },
    #     "field82": {
    #       "type": "string"
    #     },
    #     "field83": {
    #       "type": "string"
    #     },
    #     "field84": {
    #       "type": "string"
    #     },
    #     "field85": {
    #       "type": "string"
    #     },
    #     "field86": {
    #       "type": "string"
    #     },
    #     "field87": {
    #       "type": "string"
    #     },
    #     "field88": {
    #       "type": "string"
    #     },
    #     "field89": {
    #       "type": "string"
    #     },
    #     "field90": {
    #       "type": "string"
    #     },
    #     "field91": {
    #       "type": "string"
    #     },
    #     "field92": {
    #       "type": "string"
    #     },
    #     "field93": {
    #       "type": "string"
    #     },
    #     "field94": {
    #       "type": "string"
    #     },
    #     "field95": {
    #       "type": "string"
    #     },
    #     "field96": {
    #       "type": "string"
    #     },
    #     "field97": {
    #       "type": "string"
    #     },
    #     "field98": {
    #       "type": "string"
    #     },
    #     "field99": {
    #       "type": "string"
    #     }
    #   }
    # }

    scheme_definition = {
        "$schema": "http://json-schema.org/draft-04/schema#",
        "description": "AllTypes",
        "type": "object",
        "properties": {
            "eventId": {
                "type": "string"
            },
            "requestId": {
                "type": "string",
                "index": True
            },
            "intType": {
                "type": "integer"
            },
            "numberType": {
                "type": "number"
            }, "timestampType": {
                "type": "number"
            }
        }
    }

    generate_table_ddl(schema_definition=scheme_definition)
