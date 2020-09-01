# -*- coding:utf-8 -*-

"""
Query Parameter Generator For JAVA:
uuid=3100&ip=56.122.0.105&telephone=18621326306&telVerifyCode=ghnx&token_type=test
&fp_outerCode=test&fp_deviceId=test117&fp_expireTime=123456
&fp_isSimulator=1&fp_errCode=ggb&isRoot=1&status=1&visitTime=123456&userId=gct900
"""

qp = """
uuid=3100&ip=56.122.0.105&telephone=18621326306&telVerifyCode=ghnx&token_type=test
&fp_outerCode=test&fp_deviceId=test117&fp_expireTime=123456
&fp_isSimulator=1&fp_errCode=ggb&isRoot=1&status=1&visitTime=123456&userId=gct900
"""


def parse_query_parameters(content):
    query_list = content.split("&")
    query_keys=[]
    for item in query_list:
        kv_pair = item.split("=")
        query_keys.append(kv_pair[0])
    return query_keys

def generate_entity(key_list):
    template = "private String {key};"
    for key in key_list:
        print(template.format(key=key.replace("\n","")))

def generate(content):
    generate_entity(parse_query_parameters(content))


if __name__ == '__main__':
    generate(qp)