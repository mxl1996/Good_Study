import pymysql
from faker import Faker

conn = pymysql.connect(host="10.1.35.47", port=3306, user="root", password="1qaz@WSX", db="d_report_2.2.2_test",
                       charset="utf8")

cursor = conn.cursor()
sql1 = """drop table if exists faker_user"""
sql2 = """
create table faker_user(
pid int primary key auto_increment,
username varchar(20),
password varchar(20),
address varchar(35) 
)
"""
cursor.execute(sql1)
cursor.execute(sql2)
fake = Faker("zh-CN")
# 根据自己需要设置生成数据以及插入条数
for i in range(1000):
    sql = """insert into faker_user(username,password,address) 
    values('%s','%s','%s')""" % (fake.name(), fake.password(special_chars=False), fake.address())
    print('姓名:' + fake.name() + '|密码:' + fake.password(special_chars=False) + '|地址:' + fake.address())
    cursor.execute(sql)

conn.commit()
cursor.close()
conn.close()
""" 基础信息类 """
# 生成身份证号
fake.ssn()
# 随机公司服务名
fake.bs()
# 随机公司名（长）
fake.company()
# 随机公司名（短）
fake.company_prefix()
# 公司性质，如'信息有限公司'
fake.company_suffix()
# 随机信用卡到期日，如'03/30'
fake.credit_card_expire()
# 生成完整信用卡信息
fake.credit_card_full()
# 信用卡号
fake.credit_card_number()
# 信用卡类型
fake.credit_card_provider()
# 信用卡安全码
fake.credit_card_security_code()
# 随机职位
fake.job()
# 女性名
fake.first_name_female()
# 男性名
fake.first_name_male()
# 随机生成全名
fake.name()
# 男性全名
fake.name_female()
# 女性全名
fake.name_male()
# 随机生成手机号
fake.phone_number()
# 随机生成手机号段，如139
fake.phonenumber_prefix()
""" 地理信息类"""
# 市县
fake.city_suffix()
# 国家
fake.country()
# 国家编码
fake.country_code()
# 区
fake.district()
# 地理坐标
fake.geo_coordinate()
# 地理坐标（维度）
fake.latitude()
# 地理坐标精度
fake.longitude()
# 邮编
fake.postcode()
# 省份
fake.province()
# 详细地址
fake.address()
# 街道地址
fake.street_address()
# 街道名
fake.street_name()
# 街、路
fake.street_suffix()
""" 邮件信息类"""
# 生成域名
fake.domain_name()
# 域词
fake.domain_word()
# 随机IP4地址
fake.ipv4()
# 随机IP6地址
fake.ipv6()
# 随机Mac地址
fake.mac_address()
# 网址域名后缀
fake.tld()
# 随机uri地址
fake.uri()
# 网址文件后缀
fake.uri_page()
# 随机url地址
fake.url()
# 随机用户名
fake.user_name()
# 随机url地址
fake.image_url()
"""
浏览器信息类
chrome()：随机生成Chrome的浏览器user_agent信息
firefox()：随机生成FireFox的浏览器user_agent信息
internet_explorer()：随机生成IE的浏览器user_agent信息
opera()：随机生成Opera的浏览器user_agent信息
safari()：随机生成Safari的浏览器user_agent信息
linux_platform_token()：随机Linux信息
user_agent()：随机user_agent信息

-数字信息
numerify()：三位随机数字
random_digit()：0~9随机数
random_digit_not_null()：1~9的随机数
random_int()：随机数字，默认0~9999，可以通过设置min,max来设置
random_number()：随机数字，参数digits设置生成的数字位数
pyfloat()：随机Float数字
pyint()：随机Int数字（参考random_int()参数）
pydecimal()：随机Decimal数字（参考pyfloat参数）
-文本加密
pystr()：随机字符串
random_element()：随机字母
random_letter()：随机字母
paragraph()：随机生成一个段落
paragraphs()：随机生成多个段落
sentence()：随机生成一句话
sentences()：随机生成多句话，与段落类似
text()：随机生成一篇文章
word()：随机生成词语
words()：随机生成多个词语，用法与段落，句子，类似
binary()：随机生成二进制编码
boolean()：True/False
language_code()：随机生成两位语言编码
locale()：随机生成语言/国际 信息
md5()：随机生成MD5
null_boolean()：NULL/True/False
password()：随机生成密码,可选参数：length：密码长度；special_chars：是否能使用特殊字符；digits：是否包含数字；upper_case：是否包含大写字母；lower_case：是否包含小写字母
sha1()：随机SHA1
sha256()：随机SHA256
uuid4()：随机UUID
-
"""
