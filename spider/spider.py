# -*- coding: utf-8 -*-
import json
import bs4
import re
from bs4 import BeautifulSoup
import requests

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.10 Safari/537.36'}

city_path = 'D:\\CKG\\raw_data\\all_city.txt'
river_path = 'D:\\CKG\\raw_data\\river.txt'
school_path = 'D:\\CKG\\raw_data\\all_school.txt'
spot_path = 'D:\\CKG\\raw_data\\all_spot.txt'


class spider():
    def __init__(self):
        self.headers = headers
    def get_citys(self):
        citys = []
        with open (city_path, 'r') as f:
            lines = f.readlines()
            for line in lines:
                citys.extend(line.split())
        return citys
    def get_rivers(self):
        rivers = []
        with open(river_path, 'r') as f:
            lines = f.readlines()
            for line in lines:
                rivers.extend(line.split('、'))
        return rivers
    def get_schools(self):
        schools = []
        with open (school_path, 'r') as f:
            lines = f.readlines()
            for line in lines:
                schools.extend(line.split())
        return schools
    def get_spots(self):
        spots = []
        with open (spot_path, 'r') as f:
            lines = f.readlines()
            for line in lines:
                spots.extend(line.split())
        return spots
    def prepare(self):
        start_url = 'https://baike.baidu.com/item/'
        citys = self.get_citys()
        rivers = self.get_rivers()
        schools = self.get_schools()
        all_spots = self.get_spots()
        city_urls = [start_url + city for city in citys]
        river_urls = [start_url + river for river in rivers]
        school_urls = [start_url + school for school in schools]
        spot_urls = [start_url + spot for spot in all_spots]
        return city_urls, river_urls, school_urls, spot_urls


    def get_data(self,url,headers):
        try:
            r = requests.get(url,headers = headers)
            r.raise_for_status()
        except requests.RequestException as e:
            print(e)
            return None
        else:
            html = r.text.encode(r.encoding).decode()
            soup = BeautifulSoup(html,'lxml')
            name = soup.find_all('dt',class_= 'basicInfo-item name')
            values = soup.find_all('dd',class_= 'basicInfo-item value')
            names = list(map(lambda key:key.text.replace('\xa0',''), name))
            values = list(map(lambda value: re.sub('\\n\[.*]', '',value.text.strip()), values))
            data = list(zip(names, values))
            data = {name:value for name, value in data}
            return data
    def run(self,city_urls, school_urls, spot_urls, river_urls):
        all_city_data = []
        city_urls, school_urls, spot_urls, river_urls = self.prepare()
        for idx, url in enumerate(city_urls):
            data = self.get_data(url, headers)
            all_city_data.append(data)
            print("finish {}\{}".format(idx, len(city_urls)-1))

        all_school_data = []
        for idx, url in enumerate(school_urls):
            data = self.get_data(url, headers)
            all_school_data.append(data)
            print("finish {}\{}".format(idx, len(school_urls)-1))

        all_spot_data = []
        for idx, url in enumerate(spot_urls):
            data = self.get_data(url, headers)
            if data is None:
                continue
            all_spot_data.append(data)
            print("finish {}\{}".format(idx, len(spot_urls)-1))

        all_river_data = []
        for idx, url in enumerate(river_urls):
            data = self.get_data(url, headers)
            all_river_data.append(data)
            print("finish {}\{}".format(idx, len(river_urls)-1))
        return all_city_data,all_school_data,all_spot_data,all_river_data

    def data2json(self,data,prefix,all_city_data,all_school_data,all_spot_data,all_river_data):
        all_city_data,all_school_data,all_spot_data,all_river_data = self.run()
        data_json = json.dumps(data,ensure_ascii=False)
        json.dump(data_json,open('E:\\{}_data.json'.format(prefix), 'w'))
    def json2data(self,prefix):
        data_json = json.load(open('E:\\{}_data.json'.format(prefix)))
        return json.loads(data_json)

    def crawl(self):
        city_urls, school_urls, spot_urls, river_urls = self.prepare()
        self.run(city_urls, school_urls, spot_urls, river_urls)

if __name__ == '__main__':
    spider = spider()
    spider.crawl()
#for relaiton extraction
#spot2city = {}
#for city in city_data:
#    try:
#        spots = city.get('著名景点').split('、')[:-1]
#        for spot in spots:
#            spot2city[spot] = city.get('中文名称')
#    except:
#        pass

#实体1， 实体2， 关系， 种类1， 种类2
#relation1 = '位于'
#relation2 = '著名景点'
#type1 = '景点'
#type2 = '城市'
#relation_path1 = './spot_city_relation.txt'
#relation_path2 = './city_spot_relation.txt'
#f1 = open(relation_path1, 'w')
#f2 = open(relation_path2, 'w')
#for spot in all_spot:
#    try:
#        city = spot2city[spot]
#        if '中山' in city or '威海' in city or '，' in spot or ',' in spot:
#            print(spot)
#            continue
#        f1.write("{},{},{},{},{}\n".format(spot,city,relation1,type1,type2))
#        f2.write("{},{},{},{},{}\n".format(city,spot,relation2,type2,type1))
#    except:
#        print(city)
#f1.close()
#f2.close()