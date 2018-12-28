# -*- coding: utf-8 -*-

from py2neo import Graph
import json

neo_ip = "bolt://172.26.19.123:7687"
user = "neo4j"
pwd = "jhyj1jiaren"
graph = Graph(neo_ip, username=user, password=pwd)    # 1、different of between Graph and Graph Database

ent2comment = json.loads(json.load(open('./raw_data/comments_data.json')))
ent2image = json.loads(json.load(open('./raw_data/image_data.json')))
