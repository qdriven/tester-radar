#!/usr/bin/env python
# -*- coding: utf-8 -*-


def parse_status():
    with open('./status2.txt','r') as status:
        lines = status.readlines()
        for line in lines:
            parsed_line = line.split(",")
            parsed_line=parsed_line[1:]
            print(parsed_line[0].split(":")[0]+"\n")
            for new_element in parsed_line:
                print(new_element.split(":")[1])

parse_status()