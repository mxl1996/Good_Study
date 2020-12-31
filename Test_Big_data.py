from faker import Faker  # 引入库
import os
import shutil

# coding=utf-8


# 字段值列表
'''
| 字段名             | 中文名               | 类型          | 备注及样例         |
| ------------------ | -------------------- | ------------- | ------------------ |
| evt_id             | 事件编号             | varchar(100)  |                    |
| cvg_sts_cd         | 汇入状态代码         | varchar(10)   | c                  |
| act_opn_bbk_org_id | 账户开户分行机构编号 | varchar(20)   | bck\|mph\|dsk\|iex |
| act_opn_org_id     | 账户开户机构编号     | varchar(20)   |                    |
| trx_dt             | 交易日期             | date          | yyyy-mm-dd         |
| trx_set            | 交易套号             | varchar(20)   |                    |
| bus_srl_nbr        | 业务流水号           | varchar(20)   |                    |
| cvg_prcp           | 汇入本金             | decimal(18,2) |                    |
| pay_eac_id         | 付方户口编号         | varchar(100)  |                    |
| rcv_eac_id         | 收方户口编号         | varchar(100)  |                    |
| rcv_cust_id        | 收方客户编号         | varchar(50)   |                    |
| spc_act_id         | 指定账户编号         | varchar(100)  |                    |
| trsit_eac_id       | 过渡户口编号         | varchar(100)  |                    |
| pay_bnk_no         | 付方行号             | varchar(20)   |                    |
| rtr_tms            | 重试次数             | integer       |                    |
| err_tms            | 错误次数             | integer       |                    |
| clr_mth_cd         | 清算方式代码         | varchar(10)   | dl                 |
| dw_etl_dt          | 翻牌日期             | date          | yyyy-mm-dd         |
| dw_upd_dt          | 更新日期             | date          | yyyy-mm-dd         |
| dw_upd_tm          | 更新时间             | time(0)       | hh:mm:ss           |
| dw_job_seq         | 作业序号             | byteint       | 1                  |

'''



fake = Faker(locale='zh_cn')  # 添加本地化
fake.seed(10000)  # 设置随机数种子，每次生成的数据一致

baseDir = '../data/'  # 基础目录
if not os.path.isdir(baseDir):
    os.mkdir(baseDir)

# 数据初始化
fileName = 'brtl_bc_rtl_cvr_trx_evt'  # 文件名

evt_id = 10000000  # 事件编号
cvg_sts_cd = 'c'  # 汇入状态代码
act_opn_bbk_org_id = 'bck'  # 账户开户分行机构编号  bck\|mph\|dsk\|iex
act_opn_org_id = 12  # 账户开户机构编号
trx_dt = fake.date(pattern="%Y-%m-%d", end_datetime=None)  # 交易日期
trx_set = 10000  # 交易套号
bus_srl_nbr = 1000000  # 业务流水号
cvg_prcp = fake.pyfloat()  # 汇入本金
pay_eac_id = fake.credit_card_number(card_type=None)  # 付方户口编号
rcv_eac_id = fake.credit_card_number(card_type=None)  # 收方户口编号
rcv_cust_id = 10000  # 收方客户编号
spc_act_id = 10000  # 指定账户编号
trsit_eac_id = 10000  # 过渡户口编号
pay_bnk_no = 10000  # 付方行号
rtr_tms = fake.pyint()  # 重试次数
err_tms = fake.pyint()  # 错误次数
clr_mth_cd = 'd1'  # 清算方式代码
dw_etl_dt = fake.date(pattern="%Y-%m-%d", end_datetime=None)  # 翻牌日期
dw_upd_dt = fake.date(pattern="%Y-%m-%d", end_datetime=None)  # 更新日期
dw_upd_tm = fake.time(pattern="%H:%M:%S")  # 更新时间
dw_job_seq = 1  # 作业序号

# fake.ssn(min_age=18, max_age=90) 身份证号码


# womanName=fake.name_male() #生成女性名
# idCard=fake.ssn()  #身份证号
# phone=fake.phone_number() #手机号


datafileBaseDir = '%s%s' % (baseDir, fileName)  # 数据文件基础目录
if not os.path.isdir(datafileBaseDir):
    os.mkdir(datafileBaseDir)
else:
    shutil.rmtree(datafileBaseDir)
    os.mkdir(datafileBaseDir)

# 分区日期
partitionDateBase = '2018010'
dateDay = 1
endDay = 7

# 每个文件记录数
count = 100

while dateDay <= endDay:
    dateDay = dateDay + 1
    partitionDate = '%s%s%s' % ('date_day=', partitionDateBase, dateDay)  # 分区时间
    partitionDateDir = '%s%s%s' % (datafileBaseDir, '/', partitionDate)

    if not os.path.isdir(partitionDateDir):
        os.mkdir(partitionDateDir)
    else:
        shutil.rmtree(partitionDateDir)
        os.mkdir(partitionDateDir)

    dirAndFileName = '%s%s%s%s' % (partitionDateDir, '/', fileName, '.txt')
    print('%s\n' % dirAndFileName)

    n = 0
    currentCount = count * (dateDay - 1)  # 每个文件其实开始时间
    while n <= count:  # 执行100次
        n += 1  # 每执行1次之后加1

        # 数据加工逻辑
        evt_id = 10000000 + n + currentCount  # 事件编号
        trx_dt = fake.date(pattern="%Y-%m-%d", end_datetime=None)  # 交易日期
        trx_set = 10000 + n + currentCount  # 交易套号
        bus_srl_nbr = 1000000 + n + currentCount  # 业务流水号
        cvg_prcp = fake.pyfloat()  # 汇入本金
        pay_eac_id = fake.credit_card_number(card_type=None)  # 付方户口编号
        rcv_eac_id = fake.credit_card_number(card_type=None)  # 收方户口编号
        rtr_tms = fake.pyint()  # 重试次数
        err_tms = fake.pyint()  # 错误次数
        dw_etl_dt = fake.date(pattern="%Y-%m-%d", end_datetime=None)  # 翻牌日期
        dw_upd_dt = fake.date(pattern="%Y-%m-%d", end_datetime=None)  # 更新日期
        dw_upd_tm = fake.time(pattern="%H:%M:%S")  # 更新时间

        fileContent = "%s" % evt_id, ",%s" % cvg_sts_cd, ",%s" % act_opn_bbk_org_id, ",%s" % act_opn_org_id, ",%s" % trx_dt, ",%s" % trx_set, ",%s" % bus_srl_nbr, ",%s" % cvg_prcp, ",%s" % pay_eac_id, ",%s" % rcv_eac_id, ",%s" % rcv_cust_id, ",%s" % spc_act_id, ",%s" % trsit_eac_id, ",%s" % pay_bnk_no, ",%s" % rtr_tms, ",%s" % err_tms, ",%s" % clr_mth_cd, ",%s" % dw_etl_dt, ",%s" % dw_upd_dt, ",%s" % dw_upd_tm, ",%s" % dw_job_seq + "\n"

        with open(dirAndFileName, 'a') as file:  # 追加模式
            file.writelines(fileContent)




