import json


class City(object):
    #用于存储城市的属性的类City
    def __init__(self, chinese_name=None, english_name=None, another_name=None, types=None, district=None,
                 subordinate_area=None, gov_seat=None, phone_area_code=None, postcode=None, location=None, area=None,
                 population=None, dialect=None, climate=None, famous_spots=None, airport=None, train_station=None,
                 plate_code=None, administration_code=None, local_gdp=None, personal_gdp=None,
                 personal_disposable_income=None, retail_sales=None, schools=None, leaders=None, famous_people=None):
        self.chinese_name = chinese_name
        self.english_name = english_name
        self.another_name = another_name
        self.types = types
        self.district = district
        self.subordinate_area = subordinate_area
        self.gov_seat = gov_seat
        self.phone_area_code = phone_area_code
        self.postcode = postcode
        self.location = location
        self.area = area
        self.population = population
        self.dialect = dialect
        self.climate = climate
        self.famous_spots = famous_spots    #与spots产生联系
        self.airport = airport
        self.train_station = train_station
        self.plate_code = plate_code
        self.administration_code = administration_code
        self.local_gdp = local_gdp
        self.personal_gdp = personal_gdp
        self.personal_disposable_income = personal_disposable_income
        self.retail_sales = retail_sales
        self.schools = schools  #与学校产生联系
        self.leaders = leaders
        self.famous_people = famous_people

    def print(self):
        print(self.chinese_name, self.english_name, self.another_name, self.types, self.district, self.subordinate_area,
              self.gov_seat, self.phone_area_code, self.postcode, self.location, self.area, self.population,
              self.dialect, self.climate, self.famous_spots, self.airport, self.train_station, self.plate_code,
              self.administration_code, self.local_gdp, self.personal_gdp, self.personal_disposable_income,
              self.retail_sales, self.schools, self.leaders, self.famous_people)

    @staticmethod
    def get_cities_list():
        #提取city_data.json中的数据, 并以list形式返回, list中的每一元素都是一个dict,
        #dict中存有城市的属性类型到其属性值的映射
        json_str = json.load(open('../raw_data/city_data.json', encoding='utf-8'))
        dict_list = json.loads(json_str)
        cities_list = []
        for dic in dict_list:
            city = City()
            if "中文名称" in dic:
                city.chinese_name = dic['中文名称']
            else:
                city.chinese_name = "NULL"
            if "外文名称" in dic:
                city.english_name = dic["外文名称"]
            else:
                city.english_name = "NULL"
            if "别名" in dic:
                city.another_name = dic["别名"]
            else:
                city.another_name = "NULL"
            if "行政区类别" in dic:
                city.types = dic["行政区类别"]
            else:
                city.types = "NULL"
            if "所属地区" in dic:
                city.district = dic["所属地区"]
            else:
                city.district = "NULL"
            if "下辖地区" in dic:
                city.subordinate_area = dic["下辖地区"]
            else:
                city.subordinate_area = "NULL"
            if "政府驻地" in dic:
                city.gov_seat = dic["政府驻地"]
            else:
                city.gov_seat = "NULL"
            if "电话区号" in dic:
                city.phone_area_code = dic["电话区号"]
            else:
                city.phone_area_code = "NULL"
            if "邮政区码" in dic:
                city.postcode = dic["邮政区码"]
            else:
                city.postcode = "NULL"
            if "地理位置" in dic:
                city.location = dic["地理位置"]
            else:
                city.location = "NULL"
            if "面积" in dic:
                city.area = dic["面积"]
            else:
                city.area = "NULL"
            if "人口" in dic:
                city.population = dic["人口"]
            else:
                city.population = "NULL"
            if "方言" in dic:
                city.dialect = dic["方言"]
            else:
                city.dialect = "NULL"
            if "气候条件" in dic:
                city.climate = dic["气候条件"]
            else:
                city.climate = "NULL"
            if "著名景点" in dic:
                city.famous_spots = dic["著名景点"]
            else:
                city.famous_spots = "NULL"
            if "机场" in dic:
                city.airport = dic["机场"]
            else:
                city.airport = "NULL"
            if "火车站" in dic:
                city.train_station = dic["火车站"]
            else:
                city.train_station = "NULL"
            if "车牌代码" in dic:
                city.plate_code = dic["车牌代码"]
            else:
                city.plate_code = "NULL"
            if "行政代码" in dic:
                city.administration_code = dic["行政代码"]
            else:
                city.administration_code = "NULL"
            if "地区生产总值" in dic:
                city.local_gdp = dic["地区生产总值"]
            else:
                city.local_gdp = "NULL"
            if "人均生产总值" in dic:
                city.personal_gdp = dic["人均生产总值"]
            else:
                city.personal_gdp = "NULL"
            if "人均支配收入" in dic:
                city.personal_disposable_income = dic["人均支配收入"]
            else:
                city.personal_disposable_income = "NULL"
            if "消费品零售额" in dic:
                city.retail_sales = dic["消费品零售额"]
            else:
                city.retail_sales = "NULL"
            if "高等学府" in dic:
                city.schools = dic["高等学府"]
            elif "学校" in dic:
                city.schools = dic["学校"]
            elif "著名学府" in dic:
                city.schools = dic["著名学府"]
            elif "最高学府" in dic:
                city.schools = dic["最高学府"]
            elif "高等院校" in dic:
                city.schools = dic["高等院校"]
            elif "著名军事学府" in dic:
                city.schools = dic["著名军事学府"]
            else:
                city.schools = "NULL"
            if "现任领导" in dic:
                city.leaders = dic["现任领导"]
            elif "市长" in dic:
                city.leaders = dic["市长"]
            elif "领导信息" in dic:
                city.leaders = dic["领导信息"]
            elif "主要领导" in dic:
                city.leaders = dic["主要领导"]
            else:
                city.leaders = "NULL"
            if "著名人物" in dic:
                city.famous_people = dic["著名人物"]
            elif "历史人物" in dic:
                city.famous_people = dic["历史人物"]
            elif "古代人物" in dic:
                city.famous_people = dic["古代人物"]
            elif "知名人物" in dic:
                city.famous_people = dic["知名人物"]
            else:
                city.famous_people = "NULL"
            cities_list.append(city)
        #print(cities_list)
        return cities_list


class River(object):
    # 用于存储河流的属性的类River
    def __init__(self, chinese_name=None, english_name=None, other_name=None, river_system=None, location=None,
                 flow_area=None, river_origin=None, main_branches=None, river_length=None, river_area=None,
                 avg_flux=None, sea_field=None, river_mouth=None, famous_spots=None):
        self.chinese_name = chinese_name
        self.english_name = english_name
        self.other_name = other_name
        self.river_system = river_system
        self.location = location
        self.flow_area = flow_area
        self.river_origin = river_origin
        self.main_branches = main_branches
        self.river_length = river_length
        self.river_area = river_area
        self.avg_flux = avg_flux
        self.sea_field = sea_field
        self.river_mouth = river_mouth
        self.famous_spots = famous_spots

    def print(self):
        print(self.chinese_name, self.english_name, self.other_name, self.river_system, self.location, self.flow_area,
              self.river_origin, self.main_branches, self.river_length, self.river_area, self.avg_flux, self.sea_field,
              self.river_mouth, self.famous_spots)

    @staticmethod
    def get_rivers_list():
        # 提取river_data.json中的数据, 并以list形式返回, list中的每一元素都是一个dict,
        # dict中存有河流的属性类型到其属性值的映射
        json_str = json.load(open('../raw_data/river_data.json', encoding='utf-8'))
        dict_list = json.loads(json_str)
        rivers_list = []
        for dic in dict_list:
            #print(dic)
            river = River()
            if "中文名" in dic:
                river.chinese_name = dic["中文名"]
            elif "中文名称" in dic:
                river.chinese_name = dic["中文名称"]
            else:
                river.chinese_name = "NULL"
            if "英文名称" in dic:
                river.english_name = dic["英文名称"]
            elif "外文名" in dic:
                river.english_name = dic["外文名"]
            else:
                river.english_name = "NULL"
            if "别称" in dic:
                river.other_name = dic["别称"]
            else:
                river.other_name = "NULL"
            if "所属水系" in dic:
                river.river_system = dic["所属水系"]
            else:
                river.river_system = "NULL"
            if "地理位置" in dic:
                river.location = dic["地理位置"]
            else:
                river.location = "NULL"
            if "流经地区" in dic:
                river.flow_area = dic["流经地区"]
            elif "干流流经区域" in dic:
                river.flow_area = dic["干流流经区域"]
            elif "沿岸重要城市" in dic:
                river.flow_area = dic["沿岸重要城市"]
            else:
                river.flow_area = "NULL"
            if "发源地" in dic:
                river.river_origin = dic["发源地"]
            elif "水源" in dic:
                river.river_origin = dic["水源"]
            else:
                river.river_origin = "NULL"
            if "主要支流" in dic:
                river.main_branches = dic["主要支流"]
            else:
                river.main_branches = "NULL"
            if "河长" in dic:
                river.river_length = dic["河长"]
            elif "河流全长" in dic:
                river.river_length = dic["河流全长"]
            elif "全长" in dic:
                river.river_length = dic["全长"]
            else:
                river.river_length = "NULL"
            if "河流面积" in dic:
                river.river_area = dic["河流面积"]
            elif "流域面积" in dic:
                river.river_area = dic["流域面积"]
            elif "占地面积" in dic:
                river.river_area = dic["占地面积"]
            else:
                river.river_area = "NULL"
            if "平均流量" in dic:
                river.avg_flux = dic["平均流量"]
            elif "年平均径流量" in dic:
                river.avg_flux = dic["年平均径流量"]
            elif "年径流量" in dic:
                river.avg_flux = dic["年径流量"]
            elif "年平均流量" in dic:
                river.avg_flux = dic["年平均流量"]
            elif "年均径流量" in dic:
                river.avg_flux = dic["年均径流量"]
            else:
                river.avg_flux = "NULL"
            if "注入海洋" in dic:
                river.sea_field = dic["注入海洋"]
            elif "流入海域" in dic:
                river.sea_field = dic["流入海域"]
            elif "注入" in dic:
                river.sea_field = dic["注入"]
            else:
                river.sea_field = "NULL"
            if "河口" in dic:
                river.river_mouth = dic["河口"]
            else:
                river.river_mouth = "NULL"
            if "著名景点" in dic:
                river.famous_spots = dic["著名景点"]
            else:
                river.famous_spots = "NULL"
            #river.print()
            rivers_list.append(river)

        return rivers_list


class School(object):
    # 用于存储高等学府的属性的类School
    def __init__(self, chinese_name=None, english_name=None, short_name=None, establish_time=None, school_category=None,
                 school_type=None, school_attribute=None, admin_department=None, leaders=None, academician=None,
                 bachelor_majors=None, master_points=None, doctor_points=None, post_doctor_points=None,
                 key_subjects=None, departments_settings=None, school_motto=None, school_song=None,
                 school_festival=None, address=None, school_code=None, major_awards=None, notable_alumni=None):
        self.chinese_name = chinese_name
        self.english_name = english_name
        self.short_name = short_name
        self.establish_time = establish_time
        self.school_category = school_category  #类别
        self.school_type = school_type          #类型
        self.school_attribute = school_attribute
        self.admin_department = admin_department
        self.leaders = leaders
        self.academician = academician
        self.bachelor_majors = bachelor_majors
        self.master_points = master_points
        self.doctor_points = doctor_points
        self.post_doctor_points = post_doctor_points
        self.key_subjects = key_subjects
        self.departments_settings = departments_settings
        self.school_motto = school_motto
        self.school_song = school_song
        self.school_festival = school_festival
        self.address = address
        self.school_code = school_code
        self.major_awards = major_awards
        self.notable_alumni = notable_alumni

    def print(self):
        print(self.chinese_name, self.english_name, self.short_name, self.establish_time, self.school_category,
              self.school_type, self.school_attribute, self.admin_department, self.leaders, self.academician,
              self.bachelor_majors, self.master_points, self.doctor_points, self.post_doctor_points, self.key_subjects,
              self.departments_settings, self.school_motto, self.school_song, self.school_festival, self.address,
              self.school_code, self.major_awards, self.notable_alumni)

    @staticmethod
    def get_schools_list():
        # 提取school_data.json中的数据, 并以list形式返回, list中的每一元素都是一个dict,
        # dict中存有高等学府的属性类型到其属性值的映射
        json_str = json.load(open('../raw_data/school_data.json', encoding='utf-8'))
        dict_list = json.loads(json_str)
        schools_list = []
        for dic in dict_list:
            #print(dic)
            school = School()
            if "中文名" in dic:
                school.chinese_name = dic["中文名"]
            else:
                school.chinese_name = "NULL"
            if "外文名" in dic:
                school.english_name = dic["外文名"]
            elif "英文名" in dic:
                school.english_name = dic["英文名"]
            else:
                school.english_name = "NULL"
            if "简称" in dic:
                school.short_name = dic["简称"]
            else:
                school.short_name = "NULL"
            if "创办时间" in dic:
                school.establish_time = dic["创办时间"]
            else:
                school.establish_time = "NULL"
            if "类别" in dic:
                school.school_category = dic["类别"]
            else:
                school.school_category = "NULL"
            if "类型" in dic:
                school.school_type = dic["类型"]
            else:
                school.school_type = "NULL"
            if "属性" in dic:
                school.school_attribute = dic["属性"]
            else:
                school.school_attribute = "NULL"
            if "主管部门" in dic:
                school.admin_department = dic["主管部门"]
            else:
                school.admin_department = "NULL"
            if "现任领导" in dic:
                school.leaders = dic["现任领导"]
            else:
                school.leaders = "NULL"
            if "专职院士" in dic:
                school.academician = dic["专职院士"]
            elif "两院院士" in dic:
                school.academician = dic["两院院士"]
            else:
                school.academician = "NULL"
            if "本科专业" in dic:
                school.bachelor_majors = dic["本科专业"]
            else:
                school.bachelor_majors = "NULL"
            if "硕士点" in dic:
                school.master_points = dic["硕士点"]
            else:
                school.master_points = "NULL"
            if "博士点" in dic:
                school.doctor_points = dic["博士点"]
            else:
                school.doctor_points = "NULL"
            if "博士后" in dic:
                school.post_doctor_points = dic["博士后"]
            else:
                school.post_doctor_points = "NULL"
            if "国家重点学科" in dic:
                school.key_subjects = dic["国家重点学科"]
            else:
                school.key_subjects = "NULL"
            if "院系设置" in dic:
                school.departments_settings = dic["院系设置"]
            else:
                school.departments_settings = "NULL"
            if "校训" in dic:
                school.school_motto = dic["校训"]
            else:
                school.school_motto = "NULL"
            if "校歌" in dic:
                school.school_song = dic["校歌"]
            else:
                school.school_song = "NULL"
            if "校庆日" in dic:
                school.school_festival  = dic["校庆日"]
            else:
                school.school_festival = "NULL"
            if "地址" in dic:
                school.address = dic["地址"]
            else:
                school.address = "NULL"
            if "院校代码" in dic:
                school.school_code = dic["院校代码"]
            else:
                school.school_code = "NULL"
            if "主要奖项" in dic:
                school.major_awards = dic["主要奖项"]
            else:
                school.major_awards = "NULL"
            if "知名校友" in dic:
                school.notable_alumni = dic["知名校友"]
            else:
                school.notable_alumni = "NULL"
            schools_list.append(school)
        return schools_list


class Spot(object):
    # 用于存储地点的属性的类Spot
    def __init__(self, chinese_name=None, english_name=None, location=None, climate=None, area=None, open_time=None,
                 ticket_price=None, tourist_attractions=None, spot_type=None, spot_level=None, located_country=None,
                 located_city=None, tour_time=None, tour_season=None):
        self.chinese_name = chinese_name
        self.english_name = english_name
        self.location = location
        self.climate = climate
        self.area = area
        self.open_time = open_time
        self.ticket_price = ticket_price
        self.tourist_attractions = tourist_attractions
        self.spot_type = spot_type
        self.spot_level = spot_level
        self.located_country = located_country
        self.located_city = located_city
        self.tour_time = tour_time
        self.tour_season = tour_season

    def print(self):
        print(self.chinese_name, self.english_name, self.location, self.climate, self.area, self.open_time,
              self.ticket_price, self.tourist_attractions, self.spot_type, self.spot_level, self.located_country,
              self.located_city, self.tour_time, self.tour_season)

    @staticmethod
    def get_spots_list():
        # 提取spot_data.json中的数据, 并以list形式返回, list中的每一元素都是一个dict,
        # dict中存有地点的属性类型到其属性值的映射
        json_str = json.load(open('../raw_data/spot_data.json', encoding='utf-8'))
        dict_list = json.loads(json_str)
        spots_list = []
        for dic in dict_list:
            #print(dic)
            spot = Spot()
            if "中文名称" in dic:
                spot.chinese_name = dic["中文名称"]
            elif "中文名" in dic:
                spot.chinese_name = dic["中文名"]
            else:
                spot.chinese_name = "NULL"
            if "外文名称" in dic:
                spot.english_name = dic["外文名称"]
            elif "外文名" in dic:
                spot.english_name = dic["外文名"]
            else:
                spot.english_name = "NULL"
            if "地理位置" in dic:
                spot.location = dic["地理位置"]
            elif "地点" in dic:
                spot.location = dic["地点"]
            else:
                spot.location = "NULL"
            if "气候类型" in dic:
                spot.climate = dic["气候类型"]
            else:
                spot.climate = "NULL"
            if "占地面积" in dic:
                spot.area = dic["占地面积"]
            elif "总面积" in dic:
                spot.area = dic["总面积"]
            elif "建筑面积" in dic:
                spot.area = dic["建筑面积"]
            else:
                spot.area = "NULL"
            if "开放时间" in dic:
                spot.open_time  = dic["开放时间"]
            else:
                spot.open_time = "NULL"
            if "门票价格" in dic:
                spot.ticket_price = dic["门票价格"]
            else:
                spot.ticket_price = "NULL"
            if "著名景点" in dic:
                spot.tourist_attractions = dic["著名景点"]
            else:
                spot.tourist_attractions = "NULL"
            if "类别" in dic:
                spot.spot_type = dic["类别"]
            elif "景区类型" in dic:
                spot.spot_type = dic["景区类型"]
            else:
                spot.spot_type = "NULL"
            if "景点级别" in dic:
                spot.spot_level = dic["景点级别"]
            else:
                spot.spot_level = "NULL"
            if "所属国家" in dic:
                spot.located_country = dic["所属国家"]
            else:
                spot.located_country = "NULL"
            if "所属城市" in dic:
                spot.located_city = dic["所属城市"]
            elif "所属地区" in dic:
                spot.located_city = dic["所属地区"]
            else:
                spot.located_city = "NULL"
            if "建议游玩时长" in dic:
                spot.tour_time = dic["建议游玩时长"]
            else:
                spot.tour_time = "NULL"
            if "适宜游玩季节" in dic:
                spot.tour_season = dic["适宜游玩季节"]
            else:
                spot.tour_season = "NULL"
            spots_list.append(spot)
        return spots_list


#cities_lists = City.get_cities_list()
#for cit in cities_lists:
#    cit.print()

#r_list = River.get_rivers_list()
#for r in r_list:
#    r.print()


#s_list = School.get_schools_list()
#for s in s_list:
#    print(s.chinese_name)

#sp_list = Spot.get_spots_list()
#for sp in sp_list:
#    sp.print()

