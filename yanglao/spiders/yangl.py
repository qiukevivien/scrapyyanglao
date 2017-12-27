# -*- coding: utf-8 -*-
import scrapy
import pymysql
import time
import json
import os
import urllib.request
from urllib.parse import urlparse



class YanglSpider(scrapy.Spider):
    name = 'yangl'
    allowed_domains = ['www.yanglao.com.cn']
    #start_urls = ['http://www.yanglao.com.cn/resthome']
    start_urls = ['http://www.yanglao.com.cn/resthome_' + str(x) for x in range(1,1653,1)]

    def database(self,Region_list):
        connect = pymysql.connect(
            user = "root",
            password = "xxxx",  #连接数据库，不会的可以看我之前写的连接数据库的文章
            port = 3306,
            host = "x.x.x.x",
            db = "yanglao",
            charset = "utf8mb4",
            cursorclass=pymysql.cursors.DictCursor
            )
        con = connect.cursor()  #获取游标
        con.execute("use yanglao")

        sql_list = [ '("'+l+'")' for l in Region_list]
        insert_value = ','.join(sql_list)
        sql = '''insert into url (url) values''' + insert_value
        print(sql)
        con.execute(sql)
        connect.commit()
        time.sleep(1)


    def parse(self, response):
        '''
        filename = response.url.split("/")[-2]
        nt = 'resthome'
        while nt:
            #insert mysql nt
            print(nt)
            urls = "http://www.yanglao.com.cn" + nt[0]
            print(urls)
            response =
            nt = response.xpath('//a[contains(.,"下一页")]/@href').extract()
            '''
        Region_list = response.xpath('//li[re:test(@class, "rest-item")]//a[re:test(@class, "pic")]/@href').extract()
        self.database(Region_list)

class YangISpider(scrapy.Spider):
    name = 'yangi'
    allowed_domains = ['www.yanglao.com.cn']

    connect = pymysql.connect(
        user="root",
        password="xxxx",  # 连接数据库，不会的可以看我之前写的连接数据库的文章
        port=3306,
        host="x.x.x.x",
        db="yanglao",
        charset="utf8mb4",
        cursorclass=pymysql.cursors.DictCursor
    )
    con = connect.cursor()  # 获取游标
    con.execute("use yanglao")
    sql = 'select * from url where status = 0 limit 10000'
    # limit 是为了测试方便
    con.execute(sql)
    result = con.fetchall()
    start_urls = []
    for i in result:
        # print(i['url'])
        temp = ['http://www.yanglao.com.cn' + i['url']]
        start_urls = start_urls + temp
    #print(start_urls)
    #start_urls = ['http://www.yanglao.com.cn/resthome']




    def parse(self, response):
        '''
        filename = response.url.split("/")[-2]
        nt = 'resthome'
        while nt:
            #insert mysql nt
            print(nt)
            urls = "http://www.yanglao.com.cn" + nt[0]
            print(urls)
            response =
            nt = response.xpath('//a[contains(.,"下一页")]/@href').extract()
            '''
        #Region_list = response.xpath('//li[re:test(@class, "rest-item")]//a[re:test(@class, "pic")]/@href').extract()
        #self.database(Region_list)
        print("+++++++++++++++++++++++++spider is runing~!++++++++++++++++++++")

        self.path = urlparse(response.url).path
        print(self.path)
        self.src_name = response.xpath('//div[re:test(@class,"inst-summary")]/h1/text()').extract()
        if len(self.src_name) == 1:
            self.name = self.src_name[0]
        elif len(self.src_name) == 2:
            self.name = self.src_name[1]
        else:
            print("养老院H1标签，取养老院名称出错，请检查～")
            exit()
        print(self.name)
        self.tel = self.tran(response.xpath('//div[re:test(@class,"inst-summary")]/ul/li[re:test(@class,"phone")]/span/text()').extract()).replace(' ','').replace('\'','"')
        #self.src_base = response.xpath('//div[re:test(@class,"base-info")]/div[re:test(@class,"cont")]/ul/li/text()').extract()
        self.place = self.tran(response.xpath(
            '//div[re:test(@class,"base-info")]/div[re:test(@class,"cont")]/ul/li[re:test(em/text(),"所在地区")]/text()').extract()).replace(' ','').replace('\'','"')
        self.place_list = self.place.split('-')
        self.province = self.place_list[0].strip('\n').strip('\t')
        self.city = self.place_list[1].strip('\n').strip('\t')
        if len(self.place_list) >2:
            self.county = self.place_list[2].strip('\n').strip('\t')
        self.type = self.tran(response.xpath(
            '//div[re:test(@class,"base-info")]/div[re:test(@class,"cont")]/ul/li[re:test(em/text(),"机构类型")]/text()').extract()).replace(' ','').replace('\'','"')
        self.nature = self.tran(response.xpath(
            '//div[re:test(@class,"base-info")]/div[re:test(@class,"cont")]/ul/li[re:test(em/text(),"机构性质")]/text()').extract()).replace(' ','').replace('\'','"')
        self.corporation = self.tran(response.xpath(
            '//div[re:test(@class,"base-info")]/div[re:test(@class,"cont")]/ul/li[re:test(em/text(),"负  责  人")]/text()').extract()).replace(' ','').replace('\'','"')
        self.founding_time = self.tran(response.xpath(
            '//div[re:test(@class,"base-info")]/div[re:test(@class,"cont")]/ul/li[re:test(em/text(),"成立时间")]/text()').extract()).replace(' ','').replace('\'','"')
        self.area = self.tran(response.xpath(
            '//div[re:test(@class,"base-info")]/div[re:test(@class,"cont")]/ul/li[re:test(em/text(),"占地面积")]/text()').extract()).replace(' ','').replace('\'','"')
        self.bed_number = self.tran(response.xpath(
            '//div[re:test(@class,"base-info")]/div[re:test(@class,"cont")]/ul/li[re:test(em/text(),"床位数")]/text()').extract()).replace(' ','').replace('\'','"')
        self.collect_object = self.tran(response.xpath(
            '//div[re:test(@class,"base-info")]/div[re:test(@class,"cont")]/ul/li[re:test(em/text(),"收住对象")]/text()').extract()).replace(' ','').replace('\'','"')
        self.toll_range = self.tran(response.xpath(
            '//div[re:test(@class,"base-info")]/div[re:test(@class,"cont")]/ul/li[re:test(em/text(),"收费区间")]/text()').extract()).replace(' ','').replace('\'','"')
        self.special_service = self.tran(response.xpath(
            '//div[re:test(@class,"base-info")]/div[re:test(@class,"cont")]/ul/li[re:test(em/text(),"特色服务")]/text()').extract()).replace(' ','').replace('\'','"')
        self.contacts = self.tran(response.xpath(
            '//div[re:test(@class,"contact-info")]/div[re:test(@class,"cont")]/ul/li[re:test(em/text(),"联  系  人")]/text()').extract()).replace(' ','').replace('\'','"')
        self.address = self.tran(response.xpath(
            '//div[re:test(@class,"contact-info")]/div[re:test(@class,"cont")]/ul/li[re:test(em/text(),"地        址")]/text()').extract()).replace(' ','').replace('\'','"')
        self.website = self.tran(response.xpath('//div[re:test(@class,"contact-info")]/div[re:test(@class,"cont")]/ul/li[re:test(em/text(),"网        址")]/a/text()').extract()).replace(' ','').replace('\'','"')
        self.traffic = self.tran(response.xpath(
            '//div[re:test(@class,"contact-info")]/div[re:test(@class,"cont")]/ul/li[re:test(@class,"traffic")]/text()').extract()).replace(' ','').replace('\'','"')
        self.introduction =self.tran(response.xpath(
            '//div[re:test(@class,"inst-intro")]/div[re:test(@class,"cont")]').extract()).replace(' ','').replace('\'','"')
        self.charge_standard =self.tran(response.xpath(
            '//div[re:test(@class,"inst-charge")]/div[re:test(@class,"cont")]').extract()).replace(' ','').replace('\'','"')
        self.facilities = self.tran(response.xpath(
            '//div[re:test(@class,"facilities")]/div[re:test(@class,"cont")]').extract()).replace(' ','').replace('\'','"')
        self.service = self.tran(response.xpath(
            '//div[re:test(@class,"service")]/div[re:test(@class,"cont")]').extract()).replace(' ','').replace('\'','"')
        self.notice = self.tran(response.xpath(
            '//div[re:test(@class,"inst-notes")]/div[re:test(@class,"cont")]').extract()).replace(' ','').replace('\'','"')
        self.inst_photos = response.xpath('//div[re:test(@class,"inst-photos")]/div[re:test(@class,"cont")]/ul/li/a/@href').extract()
        self.database()


    def tran(self,obj):
        if len(obj)>0:
            return obj[0]
        else:
            return ''

    def database(self):
        sql_info = "insert into info (name,tel,province, city , county , type , nature , corporation , founding_time ,  area ,bed_number, collect_object ,toll_range , special_service ,  contacts , address  , website , traffic , introduction , charge_standard, facilities , service, notice) Values('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')" %(self.name,self.tel,self.province, self.city , self.county , self.type , self.nature , self.corporation , self.founding_time ,  self.area ,self.bed_number, self.collect_object ,self.toll_range , self.special_service ,  self.contacts , self.address  , self.website , self.traffic , self.introduction , self.charge_standard, self.facilities , self.service, self.notice)
        #print(sql_info)
        self.con.execute(sql_info)
        self.connect.commit()
        sql_select = "select * from info where name = '%s'" %(self.name)
        self.con.execute(sql_select)
        result = self.con.fetchone()
        for l in self.inst_photos:
            sql_image = "insert into image (url,info,status) VALUES ('%s','%s','%s')" %(l,result['id'],0)
            self.con.execute(sql_image)
            self.connect.commit()
        #sql_result = "update url set status = '1' where id = %s" %(r['id'])
        sql_url = "select * from url where url = '%s'" %(self.path)
        self.con.execute(sql_url)
        result_path = self.con.fetchone()
        self.con.execute("update url set status = %s where id = %s" %('1',result_path['id']))
        self.connect.commit()
        #time.sleep(1)

class YangPSpider(scrapy.Spider):
    name = 'yangp'
    allowed_domains = ['www.yanglao.com.cn']

    connect = pymysql.connect(
        user="root",
        password="xxxx",  # 连接数据库，不会的可以看我之前写的连接数据库的文章
        port=3306,
        host="x.x.x.x",
        db="yanglao",
        charset="utf8mb4",
        cursorclass=pymysql.cursors.DictCursor
    )
    con = connect.cursor()  # 获取游标
    con.execute("use yanglao")
    sql = 'select * from image where status = 0 limit 5000'
    # limit 是为了测试方便
    con.execute(sql)
    result = con.fetchall()
    start_urls = []
    head = "http://www.yanglao.com.cn"
    for r in result:
        start_urls = start_urls + [head+r['url']]







    def parse(self, response):
        print("+++++++++++++++++++++++++spider is runing~!++++++++++++++++++++")
        print(self.settings.attributes.keys())
        url_image = response.xpath('//div[re:test(@class,"layout")]/div[re:test(@class,"image-view")]/div[re:test(@id,"imagebox")]/div[re:test(@class,"image")]/img/@src').extract()[0]
        print(url_image)
        path_list = url_image.split('/')[3:]
        path_base = '/opt/code/yanglao'
        for p in path_list:
            os.chdir(path_base)
            if ".jpg" not in p:
                if not os.path.exists(p):
                    #print(p)
                    os.mkdir(p)
                path_base = path_base + '/' + p
        print(path_base + '/'  + path_list[-1])
        res = urllib.request.urlretrieve(url_image,path_base + '/' + path_list[-1])
        if res:
            url_update = response.url.replace('http://www.yanglao.com.cn', '')
            sql_picture = "update image set status = 1 , image = '" + res[0] + "' where url = '" + url_update +"'"
            print(sql_picture)
            self.con.execute(sql_picture)
            self.connect.commit()

        #time.sleep(1)
