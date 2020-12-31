# 爬取国家药监总局化妆品生产许可证相关数据
"""
如何使用requests：
1、指定url
2、UA伪装
3、发起请求，参数处理
4、获取响应数据
5、持久化存储
"""
"""  url=http://scxk.nmpa.gov.cn:81/xk/
 根据url获取响应数据？观察是否等于目标数据？ NO
 1、获取id：http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsList  响应结果中有id
 动态加载数据，
 2、目标详情数据，每个id不同：http://scxk.nmpa.gov.cn:81/xk/itownet/portal/dzpz.jsp?id=cee2b965ed094da4821080f0bea8570f
 ---详情页动态加载数据，不能直接get请求数据获取到
 ---继续分析--F12--XH--看接口返回数据是否符合预期---http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsById---Post请求，携带参数不同
 3、批量获取公司id，拼接url，爬取目标数据
"""
import requests
import json
import os
if __name__ == '__main__':

    # 批量获取id值
    url='http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsList'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
    }
    # 获取存储企业id
    id_list = []
    # 存储所有企业的详情数据
    all_data_list = []
    # 动态获取所有页面数据
    for page in range(1,10):
        page=str(page)
        data={'on':'true','page':page,'pageSize':15,'productNam':'','conditionType':'1','applyname':'','applysn':''  }

        json_ids=requests.post(url=url,headers=headers,data=data).json()
        for dic in json_ids['list']:
           id_list.append(dic['ID'])
           print(id_list)
    # 获取企业详情数据
    post_url='http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsById'
    for id in id_list:
        data={'id':id}
        detail_json= requests.post(url=post_url,headers=headers,data=data).json()
        all_data_list.append(detail_json)
    # 持久化存储
    fp=open('./allData.json','w',encoding='utf-8')
    json.dump(all_data_list,fp=fp,ensure_ascii=False)

