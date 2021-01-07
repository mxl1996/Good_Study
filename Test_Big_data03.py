import pymysql
from faker import Faker
# 创建数据库连接
conn = pymysql.connect(host="", port=3306, user="root", password="1qaz@WSX", db="",
                       charset="utf8")
cursor = conn.cursor()
sql1 = """drop table if exists dm_test"""
sql2 = """
create table dm_test(
user_id int primary key auto_increment,
pro_name varchar(255),
use_fee double(255,2),
phone_num varchar(255),
com_name  varchar(255),
day datetime not null
)
"""
cursor.execute(sql1)
cursor.execute(sql2)
fake = Faker("zh-CN")
# 循环生成1000条数据
for i in range(1000):
    # 调用fake中已经封装好的方法生成我们想要的数据
    sql = """insert into dm_test( pro_name,use_fee,phone_num,com_name,day) values ('%s','%s','%s','%s','%s')""" % (
        fake.province(), fake.pyfloat(), fake.phone_number(), fake.company(),  fake.past_datetime())
    cursor.execute(sql)

conn.commit()
cursor.close()
conn.close()
