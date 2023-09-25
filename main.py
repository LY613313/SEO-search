# 

import requests
import re
import openpyxl as op
from lxml import etree
from module.gettime import nowtime
from colorama import Fore, Back, Style


def Reqseo(domain):
    url = "https://www.aizhan.com/cha/{}/".format(domain)
    headers = {
        'Cookie':'allSites=vipzhilv.com%2C0; _csrf=1ea140cc5011708d870101fc7168208911ffac56005aa024a18cc9aa9649d20ba%3A2%3A%7Bi%3A0%3Bs%3A5%3A%22_csrf%22%3Bi%3A1%3Bs%3A32%3A%228qI0GnsP9JoCN15nOBHxOB9S4ec3Hqor%22%3B%7D; allSites_m=vipzhilv.com%2C0',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36'
    }

    response = requests.get(url, headers=headers)
    response.encoding = response.apparent_encoding
    return response
    """
    with open('res1.html','w',encoding='utf8') as f:
        f.write(response.text)
    """


def Dataparsing(response,domain):
    doc = etree.HTML(response.text, parser = etree.HTMLParser(encoding='utf8'))
    # result = doc.xpath('/html/body/div[4]/div[3]/div[2]/table/tr[2]/td/ul/li[4]/text()')
    name_baiduPC = doc.xpath('/html/body/div[4]/div[3]/div[2]/table/tr[2]/td/ul/li[1]/text()')
    num_baiduPC = doc.xpath('/html/body/div[4]/div[3]/div[2]/table/tr[2]/td/ul/li[1]/a/img/@alt')
    baiduPC = name_baiduPC + num_baiduPC
    print(Fore.YELLOW + nowtime() + "\033[32m The domain of \033[0m" + domain + " \033[32mresult is \033[0m" + baiduPC[0] + baiduPC[1])

    name_baiduyd = doc.xpath('/html/body/div[4]/div[3]/div[2]/table/tr[2]/td/ul/li[2]/text()')
    num_baiduyd = doc.xpath('/html/body/div[4]/div[3]/div[2]/table/tr[2]/td/ul/li[2]/a/img/@alt')
    baiduyd = name_baiduyd + num_baiduyd
    print(Fore.YELLOW + nowtime() + "\033[32m The domain of \033[0m" + domain + " \033[32mresult is \033[0m" + baiduyd[0] + baiduyd[1])
    # /html/body/div[4]/div[3]/div[2]/table/tbody/tr[2]/td/ul/li[2]/a/img
    
    name_360PC = doc.xpath('/html/body/div[4]/div[3]/div[2]/table/tr[2]/td/ul/li[3]/text()')
    num_360PC = doc.xpath('/html/body/div[4]/div[3]/div[2]/table/tr[2]/td/ul/li[3]/a/img/@alt')
    PC360 = name_360PC + num_360PC
    print(Fore.YELLOW + nowtime() + "\033[32m The domain of \033[0m" + domain + " \033[32mresult is \033[0m" + PC360[0] + PC360[1])

    name_shenma = doc.xpath('/html/body/div[4]/div[3]/div[2]/table/tr[2]/td/ul/li[4]/text()')
    num_shema = doc.xpath('/html/body/div[4]/div[3]/div[2]/table/tr[2]/td/ul/li[4]/a/img/@alt')
    shenma = name_shenma + num_shema
    print(Fore.YELLOW + nowtime() + "\033[32m The domain of \033[0m" + domain + " \033[32mresult is \033[0m" + shenma[0] + shenma[1])

    name_sougou = doc.xpath('/html/body/div[4]/div[3]/div[2]/table/tr[2]/td/ul/li[5]/text()')
    num_sougou = doc.xpath('/html/body/div[4]/div[3]/div[2]/table/tr[2]/td/ul/li[5]/a/img/@alt')
    sougou = name_sougou + num_sougou
    print(Fore.YELLOW + nowtime() + "\033[32m The domain of \033[0m" + domain + " \033[32mresult is \033[0m" + sougou[0] + sougou[1])

    name_gugePR = doc.xpath('/html/body/div[4]/div[3]/div[2]/table/tr[2]/td/ul/li[6]/text()')
    num_gugePR = doc.xpath('/html/body/div[4]/div[3]/div[2]/table/tr[2]/td/ul/li[6]/a/img/@alt')
    gugePR = name_gugePR + num_gugePR
    print(Fore.YELLOW + nowtime() + "\033[32m The domain of \033[0m" + domain + " \033[32mresult is \033[0m" + gugePR[0] + gugePR[1])
    num_list = list((num_baiduPC + num_baiduyd + num_360PC + num_shema + num_sougou + num_gugePR))
    # rtlist = [domain,]
    # rtlist = rtlist + num_list
    # print(type(num_list))
    # print(type(rtlist))
    return num_list
    


def savefile(num_list):
    num = 1
    name = input(Fore.YELLOW + nowtime() + "\033[34m Please input the filename to save ( like: demo.xlsx):\033[0m")
    filename = './result/' + name
    wb = op.Workbook()  # 创建工作簿对象
    ws = wb['Sheet']  # 创建子表
    ws.append(['序号', '百度权重', '移动权重','360权重','神马','搜狗','谷歌PR'])
    for i in num_list:
        d = num,i[0],i[1],i[2],i[3],i[4],i[5]
        ws.append(d)
        num += 1
    wb.save(filename)
    print(Fore.YELLOW + nowtime() + "\033[34m Success to save the file of \033[0m" + filename)
    print(Fore.YELLOW + nowtime() + "\033[34m Thank you use the script of SEO search . \033[0m" )


def main():
    print(Fore.YELLOW + nowtime() + " \033[34mWelcome to use the script of SEO Search Script.This script was written in 20230925.\033[0m")
    print(Fore.YELLOW + nowtime() + " \033[34mStart to resolves domain. The result of resolves is id,domain,baiduseo,yidongseo,360seo,shenmaseo,sougouseo,googleseo.\033[0m")
    value = []
    with open('./domain.txt','r') as f:
        for i in f:
            domain = i.strip()
            data = []
            res_list = []
            # domain = "oppo.com"
            restext = Reqseo(domain)
            res_list = Dataparsing(restext,domain)
            value.append(list([domain,] + res_list))
    savefile(value)
            

    """
    data = [domain,]
    data = data.extend(reslist)
    print(type(data))
    
    for i in reslist:
        print(i)
    """

if __name__ == "__main__":
    main()