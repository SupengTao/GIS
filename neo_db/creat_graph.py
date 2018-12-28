# -*- coding: utf-8 -*-

import config
from neo4j.v1 import GraphDatabase     #使用neo4j的官方驱动包, pip install neo4j-driver
from requiredClasses import City
from requiredClasses import River
from requiredClasses import School
from requiredClasses import Spot


class DatabaseObject(object):
    #类DatabaseObject用于连接neo4j并执行数据操作
    def __init__(self, uri, user, password):
        #使用数据库uri以及帐号,密码实例化数据库对象
        self._driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        #关闭数据库
        self._driver.close()

    def create_hello_world(self):
        #此函数以及下面的函数仅用于测试数据库是否连接上了
        with self._driver.session() as session:
            session.write_transaction(self._create_node)
            print("Hello World Node created")

    @staticmethod
    def _create_node(tx):
        tx.run("MERGE (n:HelloWorld {message: 'HelloWorld'})")

    def create_cities(self):
        #使用city_data.json中的数据创建城市结点, 该城市结点所具有的属性类型见类City中所示
        cities_list = City.get_cities_list()
        with self._driver.session() as session:
            for city in cities_list:
                session.run("MERGE (n:城市 {中文名称:$chinese_name, 外文名称:$english_name, 别名:$other_name, "
                            "行政区类别:$types, 所属地区:$district, 下辖地区:$sub_area, 政府驻地:$gov_seat, "
                            "电话区号:$phone_area_code, 邮政区码:$postcode, 地理位置:$location, 面积:$area, "
                            "人口:$population, 方言:$dialect, 气候条件:$climate, 著名景点:$famous_spots, "
                            "机场:$airport, 火车站:$train_station, 车牌代码:$plate_code, "
                            "行政代码:$administration_code, 地区生产总值:$local_gdp, 人均生产总值:$personal_gdp, "
                            "人均支配收入:$personal_disposable_income, 消费品零售额:$retail_sales, 高等学府:$schools, "
                            "领导信息:$leaders, 著名人物:$famous_people})",
                            chinese_name=city.chinese_name, english_name=city.english_name,
                            other_name=city.another_name, types=city.types, district=city.district,
                            sub_area=city.subordinate_area, gov_seat=city.gov_seat,
                            phone_area_code=city.phone_area_code, postcode=city.postcode, location=city.location,
                            area=city.area, population=city.population, dialect=city.dialect, climate=city.climate,
                            famous_spots=city.famous_spots, airport=city.airport, train_station=city.train_station,
                            plate_code=city.plate_code, administration_code=city.administration_code,
                            local_gdp=city.local_gdp, personal_gdp=city.personal_gdp,
                            personal_disposable_income=city.personal_disposable_income, retail_sales=city.retail_sales,
                            schools=city.schools, leaders=city.leaders, famous_people=city.famous_people
                            )
                #city.print()

    def create_rivers(self):
        # 使用river_data.json中的数据创建河流结点, 该河流结点所具有的属性类型见类River中所示
        rivers_list = River.get_rivers_list()
        with self._driver.session() as session:
            for river in rivers_list:
                session.run("MERGE (n:河流 {中文名称:$chinese_name, 外文名称:$english_name, 别称:$other_name, "
                            "所属水系:$river_system, 地理位置:$location, 流经地区:$flow_area, 发源地:$river_origin, "
                            "主要支流:$main_branches, 河长:$length, 流域面积:$river_area, 平均流量:$avg_flux, "
                            "流入海域:$sea_field, 河口:$river_mouth, 著名景点:$famous_spots})",
                            chinese_name=river.chinese_name, english_name=river.english_name,
                            other_name=river.other_name, river_system=river.river_system, location=river.location,
                            flow_area=river.flow_area, river_origin=river.river_origin,
                            main_branches=river.main_branches, length=river.river_length, river_area=river.river_area,
                            avg_flux=river.avg_flux, sea_field=river.sea_field, river_mouth=river.river_mouth,
                            famous_spots=river.famous_spots)

    def create_schools(self):
        # 使用school_data.json中的数据创建高等学府结点, 该高等学府结点所具有的属性类型见类School中所示
        schools_list = School.get_schools_list()
        with self._driver.session() as session:
            for school in schools_list:
                session.run("MERGE (n:高等学府 {中文名称:$chinese_name, 英文名:$english_name, 简称:$short_name, "
                            "创办时间:$establish_time, 类别:$school_category, 类型:$school_type, 属性:$school_attribute,"
                            "主管部门:$admin_department, 现任领导:$leaders, 专职院士:$academician, "
                            "本科专业:$bachelor_majors, 硕士点:$master_points, 博士点:$doctor_points, "
                            "博士后:$post_doctor_points, 国家重点学科:$key_subjects, 院系设置:$departments_settings, "
                            "校训:$school_motto, 校歌:$school_song, 校庆日:$school_festival, 地址:$address, "
                            "院校代码:$school_code, 主要奖项:$major_awards, 知名校友:$notable_alumni})",
                            chinese_name=school.chinese_name, english_name=school.english_name,
                            short_name=school.short_name, establish_time=school.establish_time,
                            school_category=school.school_category, school_type=school.school_type,
                            school_attribute=school.school_attribute, admin_department=school.admin_department,
                            leaders=school.leaders, academician=school.academician,
                            bachelor_majors=school.bachelor_majors, master_points=school.master_points,
                            doctor_points=school.doctor_points, post_doctor_points=school.post_doctor_points,
                            key_subjects=school.key_subjects, departments_settings=school.departments_settings,
                            school_motto=school.school_motto, school_song=school.school_song,
                            school_festival=school.school_festival, address=school.address,
                            school_code=school.school_code, major_awards=school.major_awards,
                            notable_alumni=school.notable_alumni)

    def create_spots(self):
        # 使用spot_data.json中的数据创建地点结点, 该地点结点所具有的属性类型见类Spot中所示
        spots_list = Spot.get_spots_list()
        with self._driver.session() as session:
            for spot in spots_list:
                #spot.print()
                session.run("MERGE (n:地点 {中文名称:$chinese_name, 外文名称:$english_name, 地理位置:$location, "
                            "占地面积:$area, 开放时间:$open_time, 门票价格:$ticket_price, 著名景点:$tourist_attractions, "
                            "景区类型:$spot_type, 景点级别:$spot_level, 所属国家:$country, 所属城市:$city, "
                            "建议游玩时长:$tour_time, 适宜游玩季节:$tour_season})", chinese_name=spot.chinese_name,
                            english_name=spot.english_name, location=spot.location, area=spot.area,
                            open_time=spot.open_time, ticket_price=spot.ticket_price,
                            tourist_attractions=spot.tourist_attractions, spot_type=spot.spot_type,
                            spot_level=spot.spot_level, country=spot.located_country, city=spot.located_city,
                            tour_time=spot.tour_time, tour_season=spot.tour_season)

    def clear(self):
        #由于json中的数据十分乱, 造成了有些结点连"中文名称"属性都没有, 这就是无用结点, 这个函数把这些结点删掉
        with self._driver.session() as session:
            session.run("MATCH (n)"
                        "WHERE n.中文名称 = 'NULL'"
                        "DELETE n")

    def city_2_city(self):
        with self._driver.session() as session:
            session.run("MERGE (n:城市群类型 {名称:'珠三角城市群'})")
            listofcity = '广州、深圳 、珠海、佛山、东莞、惠州、中山、江门、肇庆'.split('、')
            for city in listofcity:
                session.run("MATCH (n:城市)"
                            "MATCH (m:城市群类型 {名称: $grou})"
                            "WHERE n.中文名称 CONTAINS $city "
                            "MERGE (n)-[:城市联系]->(m)", city=city, grou='珠三角城市群')
            records = session.run("MATCH (n:城市群类型 {名称: $grou}) "
                                  "MATCH (m:城市) "
                                  "WHERE (n)--(m) "
                                  "return m.中文名称", grou='珠三角城市群')
            concity = [record["m.中文名称"] for record in records]
            str1 = concity[0]
            for i in concity:
                if (i != str1):
                    session.run("match (n), (m) "
                                "where n.中文名称=$str1 and m.中文名称=$str2 "
                                "merge (n)-[:城市群 {名称:'珠三角城市群'}]-(m)", str1=str1, str2=i)
                    str1=i

        with self._driver.session() as session:
            session.run("MERGE (n:城市群类型 {名称:'京津冀城市群'})")
            listofcity = '北京、天津、保定、唐山、石家庄、廊坊、秦皇岛、张家口、承德、沧州、衡水、邢台、邯郸、安阳'.split('、')
            for city in listofcity:
                session.run("MATCH (n:城市)"
                            "MATCH (m:城市群类型 {名称: $grou})"
                            "WHERE n.中文名称 CONTAINS $city "
                            "MERGE (n)-[:城市联系]->(m)", city=city, grou='京津冀城市群')
            records = session.run("MATCH (n:城市群类型 {名称: $grou}) "
                                  "MATCH (m:城市) "
                                  "WHERE (n)--(m) "
                                  "return m.中文名称", grou='京津冀城市群')
            concity = [record["m.中文名称"] for record in records]
            str1 = concity[0]
            for i in concity:
                if (i != str1):
                    session.run("match (n), (m) "
                                "where n.中文名称=$str1 and m.中文名称=$str2 "
                                "merge (n)-[:城市群 {名称:'京津冀城市群'}]-(m)", str1=str1, str2=i)
                    str1 = i

        with self._driver.session() as session:
            session.run("MERGE (n:城市群类型 {名称:'长三角城市群'})")
            listofcity = '上海、南京、无锡、常州、苏州、南通、盐城、扬州、镇江、泰州、杭州、宁波、嘉兴、湖州、绍兴、金华、舟山、台州、合肥、芜湖、马鞍山、铜陵、安庆、滁州、池州、宣城'.split('、')
            for city in listofcity:
                session.run("MATCH (n:城市)"
                            "MATCH (m:城市群类型 {名称: $grou})"
                            "WHERE n.中文名称 CONTAINS $city "
                            "MERGE (n)-[:城市联系]->(m)", city=city, grou='长三角城市群')
            records = session.run("MATCH (n:城市群类型 {名称: $grou}) "
                                  "MATCH (m:城市) "
                                  "WHERE (n)--(m) "
                                  "return m.中文名称", grou='长三角城市群')
            concity = [record["m.中文名称"] for record in records]
            str1 = concity[0]
            for i in concity:
                if (i != str1):
                    session.run("match (n), (m) "
                                "where n.中文名称=$str1 and m.中文名称=$str2 "
                                "merge (n)-[:城市群 {名称:'长三角城市群'}]-(m)", str1=str1, str2=i)
                    str1 = i
        with self._driver.session() as session:
            session.run("MERGE (n:城市群类型 {名称:'长江中游城市群'})")
            listofcity = '武汉、黄石、黄冈、鄂州、孝感、咸宁、仙桃、天门、潜江、襄阳、宜昌、荆州、荆门、长沙、岳阳、' \
                         '益阳、常德、株洲、湘潭、娄底、郴州、衡阳、南昌、九江、景德镇、上饶、鹰潭、新余、宜春、萍乡、' \
                         '抚州、吉安、合肥、六安、芜湖、安庆、马鞍山、池州、铜陵、黄山'.split('、')
            for city in listofcity:
                session.run("MATCH (n:城市)"
                            "MATCH (m:城市群类型 {名称: $grou})"
                            "WHERE n.中文名称 CONTAINS $city "
                            "MERGE (n)-[:城市联系]->(m)", city=city, grou='长江中游城市群')
            records = session.run("MATCH (n:城市群类型 {名称: $grou}) "
                                  "MATCH (m:城市) "
                                  "WHERE (n)--(m) "
                                  "return m.中文名称", grou='长江中游城市群')
            concity = [record["m.中文名称"] for record in records]
            str1 = concity[0]
            for i in concity:
                if (i != str1):
                    session.run("match (n), (m) "
                                "where n.中文名称=$str1 and m.中文名称=$str2 "
                                "merge (n)-[:城市群 {名称:'长江中游城市群'}]-(m)", str1=str1, str2=i)
                    str1 = i
        with self._driver.session() as session:
            session.run("MERGE (n:城市群类型 {名称:'成渝城市群'})")
            listofcity = '成都、自贡、泸州、德阳、绵阳、遂宁、内江、乐山、南充、眉山、宜宾、广安、达州、雅安、资阳'.split('、')
            for city in listofcity:
                session.run("MATCH (n:城市)"
                            "MATCH (m:城市群类型 {名称: $grou})"
                            "WHERE n.中文名称 CONTAINS $city "
                            "MERGE (n)-[:城市联系]->(m)", city=city, grou='成渝城市群')
            records = session.run("MATCH (n:城市群类型 {名称: $grou}) "
                                  "MATCH (m:城市) "
                                  "WHERE (n)--(m) "
                                  "return m.中文名称", grou='成渝城市群')
            concity = [record["m.中文名称"] for record in records]
            str1 = concity[0]
            for i in concity:
                if (i != str1):
                    session.run("match (n), (m) "
                                "where n.中文名称=$str1 and m.中文名称=$str2 "
                                "merge (n)-[:城市群 {名称:'成渝城市群'}]-(m)", str1=str1, str2=i)
                    str1 = i
            session.run("match (n:城市群类型), (m:地点 {中文名称:'黄山'}) detach delete n, m")

    def river_2_city(self):
        #创建河流到城市的联系:流经
        with self._driver.session() as session:
            #若河流的属性类型"流经地区"含有城市的属性类型"中文名称", 那么该河流就流经该城市
            session.run("MATCH (n:城市)"
                        "MATCH (m:河流)"
                        "WHERE m.流经地区 CONTAINS n.中文名称 OR m.发源地 CONTAINS n.中文名称 OR m.地理位置 CONTAINS "
                        "n.中文名称 "
                        "MERGE (m)-[:流经]->(n)")

    def school_2_city(self):
        #创建学校到城市的联系:坐落于
        with self._driver.session() as session:
            #若高等学府的"地址"中包含城市的"中文名称", 或者城市的"高等学府"中包含高等学府的"中文名称"
            #或者城市的"高等学府"中包含高等学府的"简称", 并且"简称"不为空, 那么该学校就坐落于该城市
            session.run("MATCH (n:城市) "
                        "MATCH (m:高等学府) "
                        "WHERE m.地址 CONTAINS n.中文名称 OR n.高等学府 CONTAINS m.中文名称 "
                        "OR ((n.高等学府 CONTAINS m.简称) AND (m.简称 <> 'NULL')) "
                        "MERGE (m)-[:坐落于]->(n)")    #这个会出现一个大学指向两个地方的情况, 比如:新疆大学同时指向了阿克苏地区与乌鲁木齐, 这是因为新疆大学的地址包含"乌鲁木齐", 而阿克苏地区的高等学府中有新疆大学科技学院(阿克苏校区)

    def spot_2_city(self):
        #创建地点到城市的联系
        with self._driver.session() as session:
            #若该地点的"地理位置"包含城市的"中文名称", 那么该地点就"位于"该城市
            session.run("MATCH (n:城市) "
                        "MATCH (m:地点) "
                        "WHERE m.地理位置 CONTAINS n.中文名称 "
                        "MERGE (m)-[:位于]->(n)")

    def university_connection(self):
        #创建结点211, 985, C9, 并与相应学校创建联系
        with self._driver.session() as session:
            session.run("MERGE (n:大学属性 {标签:'985平台'})")
            session.run("MERGE (n:大学属性 {标签:'211工程'})")
            session.run("MERGE (n:大学属性 {标签:'C9'})")
            session.run("MERGE (n:大学属性 {标签:'985工程'})")
            session.run("match (n:高等学府) "
                        "match (m:大学属性 {标签:'985平台'}) "
                        "where n.属性 contains '985平台' "
                        "merge (n)-[:属于]->(m)")
            session.run("match (n:高等学府), (m {标签:'211工程'}) "
                        "where n.属性 contains '211' "
                        "merge (n)-[:属于]->(m)")
            session.run("match (n:高等学府), (m {标签:'C9'}) "
                        "where n.属性 contains 'C9' or n.属性 contains '九校联盟' "
                        "merge (n)-[:属于]->(m)")
            session.run("match (n:高等学府), (m {标签:'985工程'}) "
                        "where n.属性 contains '985工程'"
                        "merge (n)-[:属于]->(m)")

    def remove_null_attribute(self):
        #可以把属性值为"NULL"的属性全部去掉, 该函数尚未完成, 只用了一个属性做测试
        with self._driver.session() as session:
            session.run("MATCH (n {别名: 'NULL'}) REMOVE n.别名")
            session.run("MATCH (n {行政区类别: 'NULL'}) REMOVE n.行政区类别")
            session.run("MATCH (n {所属地区: 'NULL'}) REMOVE n.所属地区")
            session.run("MATCH (n {下辖地区: 'NULL'}) REMOVE n.下辖地区")
            session.run("MATCH (n {政府驻地: 'NULL'}) REMOVE n.政府驻地")
            session.run("MATCH (n {电话区号: 'NULL'}) REMOVE n.电话区号")
            session.run("MATCH (n {邮政区码: 'NULL'}) REMOVE n.邮政区码")
            session.run("MATCH (n {地理位置: 'NULL'}) REMOVE n.地理位置")
            session.run("MATCH (n {面积: 'NULL'}) REMOVE n.面积")
            session.run("MATCH (n {人口: 'NULL'}) REMOVE n.人口")
            session.run("MATCH (n {方言: 'NULL'}) REMOVE n.方言")
            session.run("MATCH (n {气候条件: 'NULL'}) REMOVE n.气候条件")
            session.run("MATCH (n {著名景点: 'NULL'}) REMOVE n.著名景点")
            session.run("MATCH (n {机场: 'NULL'}) REMOVE n.机场")
            session.run("MATCH (n {火车站: 'NULL'}) REMOVE n.火车站")
            session.run("MATCH (n {车牌代码: 'NULL'}) REMOVE n.车牌代码")
            session.run("MATCH (n {行政代码: 'NULL'}) REMOVE n.行政代码")
            session.run("MATCH (n {地区生产总值: 'NULL'}) REMOVE n.地区生产总值")
            session.run("MATCH (n {人均生产总值: 'NULL'}) REMOVE n.人均生产总值")
            session.run("MATCH (n {人均支配收入: 'NULL'}) REMOVE n.人均支配收入")
            session.run("MATCH (n {消费品零售额: 'NULL'}) REMOVE n.消费品零售额")
            session.run("MATCH (n {高等学府: 'NULL'}) REMOVE n.高等学府")
            session.run("MATCH (n {领导信息: 'NULL'}) REMOVE n.领导信息")
            session.run("MATCH (n {著名人物: 'NULL'}) REMOVE n.著名人物")
            session.run("MATCH (n {经纬度: 'NULL'}) REMOVE n.经纬度")
            session.run("MATCH (n {别称: 'NULL'}) REMOVE n.别称")
            session.run("MATCH (n {所属水系: 'NULL'}) REMOVE n.所属水系")
            session.run("MATCH (n {地理位置: 'NULL'}) REMOVE n.地理位置")
            session.run("MATCH (n {流经地区: 'NULL'}) REMOVE n.流经地区")
            session.run("MATCH (n {发源地: 'NULL'}) REMOVE n.发源地")
            session.run("MATCH (n {主要支流: 'NULL'}) REMOVE n.主要支流")
            session.run("MATCH (n {河长: 'NULL'}) REMOVE n.河长")
            session.run("MATCH (n {流域面积: 'NULL'}) REMOVE n.流域面积")
            session.run("MATCH (n {平均流量: 'NULL'}) REMOVE n.平均流量")
            session.run("MATCH (n {流入海域: 'NULL'}) REMOVE n.流入海域")
            session.run("MATCH (n {河口: 'NULL'}) REMOVE n.河口")
            session.run("MATCH (n {著名景点: 'NULL'}) REMOVE n.著名景点")

            session.run("MATCH (n {英文名: 'NULL'}) REMOVE n.英文名")
            session.run("MATCH (n {简称: 'NULL'}) REMOVE n.简称")
            session.run("MATCH (n {创办时间: 'NULL'}) REMOVE n.创办时间")
            session.run("MATCH (n {类别: 'NULL'}) REMOVE n.类别")
            session.run("MATCH (n {类型: 'NULL'}) REMOVE n.类型")
            session.run("MATCH (n {属性: 'NULL'}) REMOVE n.属性")
            session.run("MATCH (n {主管部门: 'NULL'}) REMOVE n.主管部门")
            session.run("MATCH (n {现任领导: 'NULL'}) REMOVE n.现任领导")
            session.run("MATCH (n {专职院士: 'NULL'}) REMOVE n.专职院士")
            session.run("MATCH (n {本科专业: 'NULL'}) REMOVE n.本科专业")
            session.run("MATCH (n {硕士点: 'NULL'}) REMOVE n.硕士点")
            session.run("MATCH (n {博士点: 'NULL'}) REMOVE n.博士点")
            session.run("MATCH (n {博士后: 'NULL'}) REMOVE n.博士后")
            session.run("MATCH (n {国家重点学科: 'NULL'}) REMOVE n.国家重点学科")
            session.run("MATCH (n {院系设置: 'NULL'}) REMOVE n.院系设置")
            session.run("MATCH (n {校训: 'NULL'}) REMOVE n.校训")
            session.run("MATCH (n {校歌: 'NULL'}) REMOVE n.校歌")
            session.run("MATCH (n {校庆日: 'NULL'}) REMOVE n.校庆日")
            session.run("MATCH (n {地址: 'NULL'}) REMOVE n.地址")
            session.run("MATCH (n {院校代码: 'NULL'}) REMOVE n.院校代码")
            session.run("MATCH (n {主要奖项: 'NULL'}) REMOVE n.主要奖项")
            session.run("MATCH (n {知名校友: 'NULL'}) REMOVE n.知名校友")

            session.run("MATCH (n {外文名称: 'NULL'}) REMOVE n.外文名称")
            session.run("MATCH (n {占地面积: 'NULL'}) REMOVE n.占地面积")
            session.run("MATCH (n {地理位置: 'NULL'}) REMOVE n.地理位置")
            session.run("MATCH (n {开放时间: 'NULL'}) REMOVE n.开放时间")
            session.run("MATCH (n {门票价格: 'NULL'}) REMOVE n.门票价格")
            session.run("MATCH (n {著名景点: 'NULL'}) REMOVE n.著名景点")
            session.run("MATCH (n {景区类型: 'NULL'}) REMOVE n.景区类型")
            session.run("MATCH (n {景点级别: 'NULL'}) REMOVE n.景点级别")
            session.run("MATCH (n {所属国家: 'NULL'}) REMOVE n.所属国家")
            session.run("MATCH (n {所属城市: 'NULL'}) REMOVE n.所属城市")
            session.run("MATCH (n {建议游玩时长: 'NULL'}) REMOVE n.建议游玩时长")
            session.run("MATCH (n {适宜游玩季节: 'NULL'}) REMOVE n.适宜游玩季节")

            #若要删除所有的属性, 就需要一个一个像上面一样用各个属性来替代"占地面积",
            #可以使用一张表, 存储所有的属性, 并对表遍历, 把下面的attribute域当做参数.
            #然而上面的想法是不可行的, 因为neo4j不允许将属性类型当做参数, 这也是导致了我写的所有代码都显得十分蠢的原因
            #由于neo4j的语法限制, 很多相似的语句都无法无法利用循环实现, 只能一个一个敲
            #session.run("MATCH (n {$attribute: 'NULL'})"
            #           "REMOVE n.$attribute")

example = DatabaseObject(config.neo_ip, config.user, config.pwd)    #创建数据库实例并连接数据库, 这里的uri, 用户名和密码都需要调整
                                                                       #我这里用了本地数据库的1帐号密码
#创建4种类型的结点
example.create_cities()
example.create_rivers()
example.create_schools()
example.create_spots()
#清除无用结点
example.clear()
#创建4种联系
example.river_2_city()
example.school_2_city()
example.spot_2_city()
example.city_2_city()
example.university_connection()
example.remove_null_attribute()
