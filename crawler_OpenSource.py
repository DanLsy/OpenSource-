import requests
from bs4 import BeautifulSoup  # 用于HTML解析
import time
import random
import pandas as pd
import os  # 用于操作文件系统
# 初始化空列表，用于存储爬取的数据
t_list = []  # 项目名列表
r_list = []  # readme列表
l_list = []  # liscense列表
c_list = []  # conduct列表
s_list = []  # stars列表
w_list = []  # watch列表
link_list = []  #link列表
l1_list= []  #language1列表
l2_list= []  #language2列表
l3_list= []  #language3列表
l4_list= []  #language4列表
str = ['daily','weekly','monthly']
#按日、月、年不同排行榜爬取三个网页
for str1 in str:
    #根网页请求头
    headers = {
        'authority': 'github.com',
        'cache-control': 'max-age=0',
        'sec-ch-ua': '^\\^',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '^\\^Windows^\\^',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-user': '?1',
        'sec-fetch-dest': 'document',
        'referer': 'https://github.com/',
        'accept-language': 'zh-CN,zh;q=0.9',
        'cookie': '_gh_sess=VtMzgCqb8bpPln9z9HwK41decARAVRZ6fgJZ7EobUXfT4rD4GNTSh6Hbp2W5mESG7PlrxXc2dJqmpiPFSE25OuP8DoI07ADM9OVEnM0RJ1030pAq9YxJyxY0S8jGipOSJgSyJUrBkK1glrMCFMMblfklQvZWZBkkk8gNBJhSBpEeuPZ^%^2F8aKXvMQqcyDAVN3knG^%^2FOMc74W^%^2BfZ^%^2FAfwBj2rwVyxI^%^2BLqCnxSJsmo8l53x6HVxNAkeTdlWBeyzBfcemQeN5NoqF6bFa8Of^%^2BjkAWbZQA^%^3D^%^3D--D^%^2F5GtG7rlSh0kJ69--eDremcxpaWkXnc94dl9U^%^2FA^%^3D^%^3D; _octo=GH1.1.2086256431.1640709908; logged_in=no; tz=Asia^%^2FShanghai',
        'if-none-match': 'W/^\\^31a7eed40bdd84984ae3b0512357ccfc^\\^',
    }
    #请求根网页
    response = requests.get('https://github.com/trending?since='+ str1, headers=headers, verify=False, proxies={'http':'http://127.0.0.1:1086'})
    #设置最大retries数
    requests.DEFAULT_RETRIES = 5

    #生成bs4对象
    soup=BeautifulSoup(response.text,'lxml')

    if(response.status_code == 200):
        print("父网页请求成功!")
        # 使用BeautifulSoup解析HTML页面 

    #防止过多https链接导致爬虫失败
    s = requests.session()
    s.keep_alive = False

    soup = BeautifulSoup(response.text, 'html.parser')
    
    article_all = soup.find_all('article',class_="Box-row")

    for article in article_all:
        #提取programmingLanguage(编程语言)
        try:
            language = article.find('div',class_='f6 color-fg-muted mt-2').find_next('span').text.strip()
            if language==None:
                print("1")
            else:
                print(language)
        except AttributeError:
            language=None
        #存入语言
        l1_list.append(language)  
        l1_list = list(filter(None, l1_list))
    #访问子网页
    title = soup.find_all('h2',class_='h3 lh-condensed')
    for ti in title:
        #拼接子网页URL
        a = ti.find('a').text.strip().replace("\n", "")
        #b = "https://github.com/" + a.replace(" ","")
        #请求子网页
        headers1 = {
            'authority': 'github.com',
            'cache-control': 'max-age=0',
            'sec-ch-ua': '^\\^',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '^\\^Windows^\\^',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-user': '?1',
            'sec-fetch-dest': 'document',
            'referer': 'https://github.com/trending',
            'accept-language': 'zh-CN,zh;q=0.9',
            'cookie': '_gh_sess=VtMzgCqb8bpPln9z9HwK41decARAVRZ6fgJZ7EobUXfT4rD4GNTSh6Hbp2W5mESG7PlrxXc2dJqmpiPFSE25OuP8DoI07ADM9OVEnM0RJ1030pAq9YxJyxY0S8jGipOSJgSyJUrBkK1glrMCFMMblfklQvZWZBkkk8gNBJhSBpEeuPZ^%^2F8aKXvMQqcyDAVN3knG^%^2FOMc74W^%^2BfZ^%^2FAfwBj2rwVyxI^%^2BLqCnxSJsmo8l53x6HVxNAkeTdlWBeyzBfcemQeN5NoqF6bFa8Of^%^2BjkAWbZQA^%^3D^%^3D--D^%^2F5GtG7rlSh0kJ69--eDremcxpaWkXnc94dl9U^%^2FA^%^3D^%^3D; _octo=GH1.1.2086256431.1640709908; logged_in=no; tz=Asia^%^2FShanghai',
        }
        response = requests.get("https://github.com/" + a.replace(" ",""), headers=headers1, verify=False, proxies={'http':'http://127.0.0.1:1086'})

        if(response.status_code == 200): #子网页请求成功!
            print("request successfully!")
            #c = str(a.replace(" ","").replace('/','_'))
            #保存子网页
            with open(a.replace(" ","").replace('/','_') +".html",'w',encoding = 'utf-8') as f:
                f.write(response.text)
            soup=BeautifulSoup(response.text,'lxml')
            title=soup.find('strong', class_="mr-2 flex-self-stretch").find('a').text.strip().replace("\n", "")
            if title==None:
                print("1")
            else:
                print(title)
            #存储到列表
            t_list.append(title)
            t_list = list(filter(None, t_list))
            #license
            try:
                license_title =soup.find('a', class_='Link--muted', href=lambda x: x and 'blob/main/LICENSE' in x)
                license = license_title.text.strip()
                if license==None:
                    print("1")
                else:
                    print(license)
            except AttributeError:
                license=None
                print(license)
            l_list.append(license)
            #获取项目的相关信息
            div_all=soup.find_all('div',class_='Layout-sidebar')
            for div in div_all:
                #readme
                try:
                    # readme = div.find('div', class_='mt-2').find_next('svg',class_="octicon octicon-book mr-2").text.strip()
                    readme_title = div.find('a', {'href': '#readme-ov-file'})
                    readme = readme_title.text.strip()
                    # print(f'Readme Title: {readme_title_text}')
                    if readme==None:
                        print("1")
                    else:
                        print(readme)
                except AttributeError:
                    readme=None
                # #license
                # try:
                #     # license_title = div.find('a', {'href': '#AGPL-3.0-1-ov-file'})
                #     # license_title = div.find('a', class_='Link--muted', href=lambda x: x and 'LICENSE.txt' in x)
                #     # license = license_title.text.strip()
                #     # license_title = div.find('a', class_='Link--muted', href=lambda x: x and 'blob/main/LICENSE' in x)
                #     license_title = div.find('div', class_='mt-2').find_next('a', class_='Link--muted')
                #     license = license_title.text.strip()
                #     if license==None:
                #         print("1")
                #     else:
                #         print(license)
                # except AttributeError:
                #     license=None
                #     print(license)
                
                # #conduct
                # try:
                #     # conduct_title = div.find('svg', class_='octicon octicon-pulse mr-2')
                #     # conduct = conduct_title.text.strip()
                #     conduct_div = div.find('div', class_='mb-3')
                #     conduct_link = conduct_div.find('a',class_='Link--secondary no-underline d-inline-block', href=lambda x: x and 'activity' in x)
                #     conduct = conduct_link.find('span').text.strip()
                 
                #     if conduct==None:
                #         print("1")
                #     else:
                #         print(conduct)
                # except AttributeError:
                #     conduct=None
                #stars
                try:
                    star_link = div.find('a', class_='Link Link--muted', href=lambda x: x and 'stargazers' in x)
                    #stars = star_link.text.strip().replace(',', '')  # 提取 star 数量并去除逗号
                    star_count = star_link.find_next('strong').text.strip()
                    stars = f'{star_count} stars'
                    if stars==None:
                        print("1")
                    else:
                        print(stars)
                except AttributeError:
                    stars=None
                #watch
                try:
                    watch_link = div.find('a', class_='Link Link--muted', href=lambda x: x and 'watchers' in x)
                    # watch = watch_link.text.strip().replace(',', '')  # 提取 watch 数量并去除逗号
                    watch_count = watch_link.find_next('strong').text.strip()
                    watch = f'{watch_count} staring'
                    if watch==None:
                        print("1")
                    else:
                        print(watch)
                except AttributeError:
                    watch=None
                #link
                try:
                    #link = div.find('a', class_='Link--muted', href=lambda x: x and 'forks' in x)
                    link = div.find('a', class_='Link Link--muted', href=lambda x: x and 'forks' in x)
                    #link = link.text.strip().replace(',', '')  # 提取 link 数量并去除逗号
                    link_count = link.find_next('strong').text.strip()
                    link=f'{link_count} forks'
                    if link==None:
                        print("1")
                    else:
                        print(link)
                except AttributeError:
                    link=None
                

                r_list.append(readme)
                # l_list.append(license)
                # c_list.append(conduct)
                s_list.append(stars)
                w_list.append(watch)
                link_list.append(link)
                r_list = list(filter(None, r_list))
                #l_list = list(filter(None, l_list))
                #w_list = list(filter(None, w_list))
                s_list = list(filter(None, s_list))
                c_list = list(filter(None, c_list))
                link_list = list(filter(None, link_list))
            








            #设置爬取休眠时间
            second=random.randrange(3,5)
            time.sleep(second)
            # data=pd.DataFrame(data={"title":t_list,"readme":r_list,"star":s_list,"watch":w_list,"share":l_list})
            # data.to_excel("github_trending_test1_lsy_"+str1+".xlsx", index=False)
        else: #请求子网页失败！
            print("error!")         
    # data=pd.DataFrame(data={"title":t_list,"readme":r_list,"license":l_list,"conduct":c_list,"star":s_list,
    #                         "watch":w_list,"share":link_list,"language_1":l1_list})
    data=pd.DataFrame(data={"title":t_list,"readme":r_list,"license":l_list,"star":s_list,
                            "watch":w_list,"share":link_list,"language_1":l1_list})
    data.to_excel("github_trending_test1_lsy_"+str1+".xlsx", index=False)
    # data1=pd.DataFrame(data={"title":t_list})
    # data2=pd.DataFrame(data={"readme":r_list})
    # data3=pd.DataFrame(data={"license":l_list})
    # data4=pd.DataFrame(data={"conduct":c_list})
    # data5=pd.DataFrame(data={"star":s_list})
    # data6=pd.DataFrame(data={"watch":w_list})
    # data7=pd.DataFrame(data={"share":link_list})
    # data8=pd.DataFrame(data={"language_1":l1_list})
    # data1.to_excel("github_trending_test1_lsy_title_"+str1+".xlsx", index=False)
    # data2.to_excel("github_trending_test1_lsy_readme_"+str1+".xlsx", index=False)
    # data3.to_excel("github_trending_test1_lsy_license_"+str1+".xlsx", index=False)
    # data4.to_excel("github_trending_test1_lsy_conduct_"+str1+".xlsx", index=False)
    # data5.to_excel("github_trending_test1_lsy_star_"+str1+".xlsx", index=False)
    # data6.to_excel("github_trending_test1_lsy_watch_"+str1+".xlsx", index=False)
    # data7.to_excel("github_trending_test1_lsy_share_"+str1+".xlsx", index=False)
    # data8.to_excel("github_trending_test1_lsy_language_"+str1+".xlsx", index=False)


    # 打印当前工作目录
    print("当前工作目录:", os.getcwd())
    # # 打印文件是否存在
    print("文件是否存在:", os.path.isfile("github_trending_test1_lsy_"+str1+".xlsx"))
    # 初始化空列表，用于存储爬取的数据
    t_list = []  # 项目名列表
    r_list = []  # readme列表
    l_list = []  # liscense列表
    c_list = []  # conduct列表
    s_list = []  # stars列表
    w_list = []  # watch列表
    link_list = []  #link列表
    l1_list= []  #language1列表
    l2_list= []  #language2列表
    l3_list= []  #language3列表
    l4_list= []  #language4列表
