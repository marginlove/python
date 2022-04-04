import requests
from bs4 import BeautifulSoup

fo = open("yw.html", "r", encoding="utf-8")
fileconten = fo.read()
# print(fileconten)
fo.close()
soup = BeautifulSoup(fileconten, 'html.parser')
ywurl = "https://www.gdqy.edu.cn/gqxw1/"

for m in soup.select(".new-list a"):
    url = m['href']
    detailurl = ywurl + url
    print("detailurl：" + detailurl)
    # title = m['title']
    # print("title:" + title)
    # print(m.text)
    title = m.text.split("[")[0]
    pub_time = m.text.split("[")[1]
    print("title:" + title)
    # print("pub_time:" + pub_time)
    # print("title:" + title)
    pub_time = m.text.split("[")[1].replace("]", "").strip()
    print("pub_time:" + pub_time)
    fw = open("xinwen.txt", "a", encoding="utf-8")
    fw_str = title + "," + pub_time + "," + detailurl
    fw.writelines(fw_str)
    fw.close()
