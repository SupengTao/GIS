from neo_db.config import graph
from neo_db.config import ent2image, ent2comment
import os
from pyltp import Segmentor
from pyltp import Postagger

def query(name, c):
    if c == 0:
        data = graph.run("match(c: 城市{中文名称:'%s'}) return c as city" % (name)).data()
    if c == 3:
        data = graph.run("match(c: 河流{中文名称:'%s'}) return c as river" % (name)).data()
    if c == 1:
        data = graph.run("match(c: 高等学府{中文名称:'%s'}) return c as school" % (name)).data()
    if c == 2:
        data = graph.run("match(c: 地点{中文名称:'%s'}) return c as spot" % (name)).data()
    return get_json_data(data, c)


def get_json_data(data, c):
    print(data)
    print("\n\n\n")
    json_data = {'data': [], "links": []}
    query_entity = ''
    if c == 0:
        attr = ['面积', '行政区类别', '人均生产总值', '人均支配收入', '著名人物']
        attr_node = {'name': '属性', 'category':4}
        each_node = {}
        city = data[0]['city']
        city_name = city['中文名称']
        query_entity = city_name
        school_node = {'name': '学校', 'category':2}
        river_node = {'name': '河流', 'category':3}
        spot_node = {'name': '地点', 'category':1}
        city_node = {'name': city_name, 'category':0}

        json_data['data'].append(city_node)
        json_data['data'].append(school_node)
        json_data['data'].append(river_node)
        json_data['data'].append(spot_node)
        json_data['data'].append(attr_node)
        json_data['links'].append({'source': city_name, 'target': school_node['name'], 'value': '坐落于'})
        json_data['links'].append({'source': city_name, 'target': river_node['name'], 'value': '流经'})
        json_data['links'].append({'source': city_name, 'target': spot_node['name'], 'value': '位于'})
        json_data['links'].append({'source': city_name, 'target': attr_node['name'], 'value': '属性'})
        for a in attr:
            each_node = {}
            each_node['name'] = city[a]
            each_node['category'] = 4
            if not each_node['name'] is None:
                json_data['data'].append(each_node)
            each_link = {}
            each_link['source'] = attr_node['name']
            each_link['target'] = city[a]
            each_link['value'] = a
            if not (each_link['source'] is None or each_link['target'] is None):
                json_data['links'].append(each_link)

        data = graph.run("match(c: 城市{中文名称:'%s'}), (r:河流) where (c)--(r) return r as river" % (city_name)).data()
        for record in data:
            river = record['river']
            river_name = river['中文名称']
            each_node = {}
            each_node['name'] = river_name
            each_node['category'] = 3
            if not each_node['name'] is None:
                json_data['data'].append(each_node)
            each_link = {}
            each_link['source'] = river_node['name']
            each_link['target'] = river_name
            each_link['value'] = '河流名称'
            if not (each_link['source'] is None or each_link['target'] is None):
                json_data['links'].append(each_link)

        data = graph.run("match(c: 城市{中文名称:'%s'}), (r:地点) where (c)--(r) return r as spot" % (city_name)).data()
        for record in data:
            spot = record['spot']
            spot_name = spot['中文名称']
            each_node = {}
            each_node['name'] = spot_name
            each_node['category'] = 1
            if not each_node['name'] is None:
                json_data['data'].append(each_node)
            each_link = {}
            each_link['source'] = spot_node['name']
            each_link['target'] = spot_name
            each_link['value'] = '景点名称'
            if not (each_link['source'] is None or each_link['target'] is None):
                json_data['links'].append(each_link)

        data = graph.run("match(c: 城市{中文名称:'%s'}), (r:高等学府) where (c)--(r) return r as school" % (city_name)).data()
        for record in data:
            school = record['school']
            school_name = school['中文名称']
            each_node = {}
            each_node['name'] = school_name
            each_node['category'] = 2
            if not each_node['name'] is None:
                json_data['data'].append(each_node)
            each_link = {}
            each_link['source'] = school_node['name']
            each_link['target'] = school_name
            each_link['value'] = '学校名称'
            if not (each_link['source'] is None or each_link['target'] is None):
                json_data['links'].append(each_link)


    elif c == 3:
        for river in data:
            river = river['river']
            nodeitem, linkitem = {}, {}
            river_name = river['中文名称']
            query_entity = river_name
            nodeitem['name'] = river_name
            nodeitem['category'] = 4
            if not nodeitem['name'] is None:
                json_data['data'].append(nodeitem)

            nodeitem, linkitem = {}, {}
            attr_name = river['所属水系']
            nodeitem['name'] = attr_name
            nodeitem['category'] = 4
            if not nodeitem['name'] is None:
                json_data['data'].append(nodeitem)
            linkitem['source'] = river_name
            linkitem['target'] = attr_name
            linkitem['value'] = '所属水系'
            if not (linkitem['source'] is None or linkitem['target'] is None):
                json_data['links'].append(linkitem)

            nodeitem, linkitem = {}, {}
            attr_name = river['流域面积']
            nodeitem['name'] = attr_name
            nodeitem['category'] = 4
            if not nodeitem['name'] is None:
                json_data['data'].append(nodeitem)
            linkitem['source'] = river_name
            linkitem['target'] = attr_name
            linkitem['value'] = '流域面积'
            if not (linkitem['source'] is None or linkitem['target'] is None):
                json_data['links'].append(linkitem)

            nodeitem, linkitem = {}, {}
            attr_name = river['主要支流']
            nodeitem['name'] = attr_name
            nodeitem['category'] = 4
            if not nodeitem['name'] is None:
                json_data['data'].append(nodeitem)
            linkitem['source'] = river_name
            linkitem['target'] = attr_name
            linkitem['value'] = '主要支流'
            if not (linkitem['source'] is None or linkitem['target'] is None):
                json_data['links'].append(linkitem)

            nodeitem, linkitem = {}, {}
            attr_name = river['地理位置']
            nodeitem['name'] = attr_name
            nodeitem['category'] = 4
            if not nodeitem['name'] is None:
                json_data['data'].append(nodeitem)
            linkitem['source'] = river_name
            linkitem['target'] = attr_name
            linkitem['value'] = '地理位置'
            if not (linkitem['source'] is None or linkitem['target'] is None):
                json_data['links'].append(linkitem)

            nodeitem, linkitem = {}, {}
            attr_name = river['流经地区']
            nodeitem['name'] = attr_name
            nodeitem['category'] = 4
            if not nodeitem['name'] is None:
                json_data['data'].append(nodeitem)
            linkitem['source'] = river_name
            linkitem['target'] = attr_name
            linkitem['value'] = '流经地区'
            if not (linkitem['source'] is None or linkitem['target'] is None):
                json_data['links'].append(linkitem)

    elif c == 1:
        for school in data:
            school = school['school']
            nodeitem, linkitem = {}, {}
            school_name = school['中文名称']
            query_entity = school_name
            nodeitem['name'] = school_name
            nodeitem['category'] = 4
            if not nodeitem['name'] is None:
                json_data['data'].append(nodeitem)

            nodeitem, linkitem = {}, {}
            attr_name = school['院校代码']
            nodeitem['name'] = attr_name
            nodeitem['category'] = 4
            if not nodeitem['name'] is None:
                json_data['data'].append(nodeitem)
            linkitem['source'] = school_name
            linkitem['target'] = attr_name
            linkitem['value'] = '院校代码'
            if not (linkitem['source'] is None or linkitem['target'] is None):
                json_data['links'].append(linkitem)

            nodeitem, linkitem = {}, {}
            attr_name = school['创办时间']
            nodeitem['name'] = attr_name
            nodeitem['category'] = 4
            if not nodeitem['name'] is None:
                json_data['data'].append(nodeitem)
            linkitem['source'] = school_name
            linkitem['target'] = attr_name
            linkitem['value'] = '创办时间'
            if not (linkitem['source'] is None or linkitem['target'] is None):
                json_data['links'].append(linkitem)

            nodeitem, linkitem = {}, {}
            attr_name = school['现任领导']
            nodeitem['name'] = attr_name
            nodeitem['category'] = 4
            if not nodeitem['name'] is None:
                json_data['data'].append(nodeitem)
            linkitem['source'] = school_name
            linkitem['target'] = attr_name
            linkitem['value'] = '现任领导'
            if not (linkitem['source'] is None or linkitem['target'] is None):
                json_data['links'].append(linkitem)

            nodeitem, linkitem = {}, {}
            attr_name = school['知名校友']
            nodeitem['name'] = attr_name
            nodeitem['category'] = 4
            if not nodeitem['name'] is None:
                json_data['data'].append(nodeitem)
            linkitem['source'] = school_name
            linkitem['target'] = attr_name
            linkitem['value'] = '知名校友'
            if not (linkitem['source'] is None or linkitem['target'] is None):
                json_data['links'].append(linkitem)

            nodeitem, linkitem = {}, {}
            attr_name = school['校训']
            nodeitem['name'] = attr_name
            nodeitem['category'] = 4
            if not nodeitem['name'] is None:
                json_data['data'].append(nodeitem)
            linkitem['source'] = school_name
            linkitem['target'] = attr_name
            linkitem['value'] = '校训'
            if not (linkitem['source'] is None or linkitem['target'] is None):
                json_data['links'].append(linkitem)

            nodeitem, linkitem = {}, {}
            attr_name = school['属性']
            nodeitem['name'] = attr_name
            nodeitem['category'] = 4
            if not nodeitem['name'] is None:
                json_data['data'].append(nodeitem)
            linkitem['source'] = school_name
            linkitem['target'] = attr_name
            linkitem['value'] = '属性'
            if not (linkitem['source'] is None or linkitem['target'] is None):
                json_data['links'].append(linkitem)

    elif c == 2:
        for spot in data:
            spot = spot['spot']
            nodeitem, linkitem = {}, {}
            spot_name = spot['中文名称']
            query_entity = spot_name
            nodeitem['name'] = spot_name
            nodeitem['category'] = 4
            if not nodeitem['name'] is None:
                json_data['data'].append(nodeitem)

            nodeitem, linkitem = {}, {}
            attr_name = spot['外文名称']
            nodeitem['name'] = attr_name
            nodeitem['category'] = 4
            if not nodeitem['name'] is None:
                json_data['data'].append(nodeitem)
            linkitem['source'] = spot_name
            linkitem['target'] = attr_name
            linkitem['value'] = '外文名称'
            if not (linkitem['source'] is None or linkitem['target'] is None):
                json_data['links'].append(linkitem)

            nodeitem, linkitem = {}, {}
            attr_name = spot['地理位置']
            nodeitem['name'] = attr_name
            nodeitem['category'] = 4
            if not nodeitem['name'] is None:
                json_data['data'].append(nodeitem)
            linkitem['source'] = spot_name
            linkitem['target'] = attr_name
            linkitem['value'] = '地理位置'
            if not (linkitem['source'] is None or linkitem['target'] is None):
                json_data['links'].append(linkitem)

            nodeitem, linkitem = {}, {}
            attr_name = spot['门票价格']
            nodeitem['name'] = attr_name
            nodeitem['category'] = 4
            if not nodeitem['name'] is None:
                json_data['data'].append(nodeitem)
            linkitem['source'] = spot_name
            linkitem['target'] = attr_name
            linkitem['value'] = '门票价格'
            if not (linkitem['source'] is None or linkitem['target'] is None):
                json_data['links'].append(linkitem)

            nodeitem, linkitem = {}, {}
            attr_name = spot['占地面积']
            nodeitem['name'] = attr_name
            nodeitem['category'] = 4
            if not nodeitem['name'] is None:
                json_data['data'].append(nodeitem)
            linkitem['source'] = spot_name
            linkitem['target'] = attr_name
            linkitem['value'] = '占地面积'
            if not (linkitem['source'] is None or linkitem['target'] is None):
                json_data['links'].append(linkitem)

            nodeitem, linkitem = {}, {}
            attr_name = spot['开放时间']
            nodeitem['name'] = attr_name
            nodeitem['category'] = 4
            if not nodeitem['name'] is None:
                json_data['data'].append(nodeitem)
            linkitem['source'] = spot_name
            linkitem['target'] = attr_name
            linkitem['value'] = '开放时间'
            if not (linkitem['source'] is None or linkitem['target'] is None):
                json_data['links'].append(linkitem)
    else:
        print("error\n")
    if ent2image.get(query_entity) == None:
        json_data['img'] = '111'
        json_data['comment'] = ''
    else:
        json_data['comment'] = ent2comment.get(query_entity)
        json_data['img'] = ent2image.get(query_entity)[0]
    return json_data  # 返回给了html

def get_KGQA_answer(array):
    LTP_DATA_DIR = './neo_db/ltp_data_v3.4.0/'
    cws_model_path = os.path.join(LTP_DATA_DIR, 'cws.model')
    pos_model_path = os.path.join(LTP_DATA_DIR, 'pos.model')

    segmentor = Segmentor()
    segmentor.load(cws_model_path)
    words = segmentor.segment(array)
    #print (list(words))
    segmentor.release()


    postagger = Postagger() # 初始化实例
    postagger.load(pos_model_path)  # 加载模型
    postags = postagger.postag(words)
    #print(list(postags))

    i=0
    city=''
    school=''
    spot=''
    river=''
    noun=''
    preposition=''
    n2=''

    for ptags in postags:
        #print(ptags, i)
        if ptags=='ns':
            city=words[i]
        if ptags=='n':
            noun=words[i]
        if ptags=='p':
            preposition=words[i]
        if ptags=='ni':
            school=words[i]
        if ptags=='nz':
            n2=words[i]
        i += 1

    #print(city, noun, school)
    if (noun=='学校'):
        noun='高等学府'
    if (noun=='大学'):
        noun='高等学府'
    if (noun=='景点'):
        noun='地点'

    #print(school,'aaa')
    #name='北京'

    #print(noun)
    data = []
    if school!='':
        if preposition=='在':
            #print('here')
            data = graph.run("match(c {中文名称:'%s'}),(m:城市) where (c)--(m) return m.中文名称" % (school)).data()

    elif city!='':
        if noun=='地点':
            data = graph.run("match(c {中文名称:'%s'}),(m:地点) where (c)--(m) return m.中文名称" % (city)).data()
        elif noun=='高等学府':
            if postags[1]=='n':
                school=city+'大学'
                #print(school,'bbb')
                data = graph.run("match(c {中文名称:'%s'}),(m:城市) where (c)--(m) return m.中文名称" % (school)).data()
            else:
                data = graph.run("match(c {中文名称:'%s'}),(m:高等学府) where (c)--(m) return m.中文名称" % (city)).data()
        elif noun=='河流':
            data = graph.run("match(c {中文名称:'%s'}),(m:河流) where (c)--(m) return m.中文名称" % (city)).data()

    #print(data)
    l=''
    for each in data:
        #print(each['m.中文名称'])
        l += each['m.中文名称'] + '<br/>'
    data_json = {}
    data_json['data'] = l
    print(data_json)
    return data_json
#  data_item['name'] = j_array[0]
#  link_item['source'] = name_dict[i['p.Name']]
#  link_item['target'] = name_dict[i['n.Name']]
#  link_item['value'] = i['r.relation']
#  data_item['category'] = CA_LIST[j_array[1]]  #将对应家庭转换为id
#
array='北京有哪些景点'
print(get_KGQA_answer(array))
