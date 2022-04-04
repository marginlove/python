# -*- coding: utf-8 -*-
#必须安装requests模块、bs4
import requests
import pandas as pd
from bs4 import BeautifulSoup
from collections import defaultdict
from dateutil.relativedelta import relativedelta
from datetime import datetime
import numpy as np
class weather_data:
    def __init__(self, city, start_year, end_year, start_month=1, end_month=12):
        self.myear=start_year #设定开始的年
        self.city = city
        self.start_time = datetime.strptime(f"{start_year}-{start_month}", '%Y-%m')
        self.end_time = datetime.strptime(f"{end_year}-{end_month}", '%Y-%m')
    def _get_original_html(self):
        url = f"https://tianqi.911cha.com/{self.city}/{self.start_time.year}-{self.start_time.month}.html"
        print(url)
        header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36"}  # 填写自己浏览器内容
        response = requests.get(url, headers=header)
        return response.content.decode("utf-8")
    def _parse_data(self):
        # 一次解析一个月
        soup = BeautifulSoup(self.html, "html.parser")
        data = defaultdict(dict)
        for n, tr in enumerate(soup.find_all("tr")):
            if n == 0:
                continue
            if n % 2 != 0:
                date = tr.find("a").get_text()
                # 创建字典
                data[date]["Day"] = {str(self.start_time.year) + '-' + key: con.get_text() for key, con in zip(['time', 'image', 'weather', 'temperature', 'humidity', 'wind_force', 'wind_scale', 'precipitation', 'sendible_temperature', 'cloud_amount'], tr.find_all("td"))}
            else:
                data[date]["Night"] = {key: con.get_text() for key, con in zip(
                    ['time', 'image', 'weather', 'temperature', 'humidity', 'wind_force', 'wind_scale',
                     'precipitation', 'sendible_temperature', 'cloud_amount'], tr.find_all("td"))}
        return data

    def main(self):
        data = []
        while self.start_time <= self.end_time:
            self.html = self._get_original_html()
            data.append(self._parse_data())
            self.start_time += relativedelta(months=1)
        return data
result = []
if __name__ == "__main__":
    T = weather_data(city="ningbo", start_year=2019, end_year=2020, start_month=1, end_month=10)#实例化类，并设定抓取参数
    with open('weather_dict.txt', 'w', encoding='UTF-8') as f:
        for line in T.main():
            result.append(line)
            f.writelines(str(line))
key_list = []
key2_list = []
val_list = []
val3_list = []
val5_list = []
for data in result:
    key_value = list(data.keys())
    key_list.append(key_value)
    val_value = list(data.values())
    val_list.append(val_value)

for i in key_list:
    key2_list = key2_list + i;
# 下面全是对val值进行操作
for val2 in val_list:
    for val3 in val2:
        val3_value = list(val3.values())
        val3_list.append(val3_value)

for nu in range(len(val3_list)):
    for val4 in val3_list[nu]:
        val5 = list(val4.values())
        val6 = ['0' if i == '-' else i for i in val5]  # 把降雨的-改成0，工作需要
        val5_list.append(val6)
data_key = pd.DataFrame(key2_list)  # 日期
f=1 #自定义标记，用来确定时间
ttime=T.myear #提取开始的年
for i in range(data_key.size):  #自动获取时间，设置天气的年月日时间信息
    if f==1  :     #f=1表示开始的年
        data_key.loc[i]=str(ttime)+'年'+data_key.loc[i]
        f=f+1
    elif data_key.loc[i,0]=='1月1日': # f<>1且遇到1月1日表示新的年来了
         ttime=int(ttime)+1   # 年增加
         data_key.loc[i] = str(ttime) + '年' + data_key.loc[i]
         f=f+1
    else:
        data_key.loc[i] = str(ttime) + '年' + data_key.loc[i]
        f=f+1
data_val = pd.DataFrame(val5_list)  # 气象信息，可以根据自己需要对这个变量进行修改
temp = data_val[3].str.strip('℃') # 去除符号
humd = data_val[4].str.strip('%') # 去除符号
rain = data_val[7].str.strip('mm') # 去除符号
weather = pd.DataFrame([temp, humd, rain]).T
# 保留奇数行，删除偶数行
day = weather[weather.index % 2 == 0].reset_index(drop=True)  # 白天数据
# 保留偶数行，删除奇数行
night = weather[weather.index % 2 == 1].reset_index(drop=True)  # 晚上数据
fin = pd.concat([data_key, night, day], axis=1)
fin.columns=['时间','夜间温度','夜间湿度','晚上降水量','白天温度','白天湿度','白天降水量']   #设定列标签
fin.to_csv('气象.csv', encoding="utf_8_sig")
