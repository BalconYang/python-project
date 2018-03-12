# -*- coding: utf-8 -*-
# 借用和风api获取天气信息，主要涉及requests，json
import json
import requests
id = input('请输入和风id：\n') # 和风官网申请账号
api_url = 'https://free-api.heweather.com/s6/weather/forecast?location=CN101180112&key=' + id
r = requests.get(api_url)
json_data = r.json()
location = json_data['HeWeather6'][0]['basic']['location']
wind_dir = json_data['HeWeather6'][0]['daily_forecast'][0]['wind_dir']
wind_spd = json_data['HeWeather6'][0]['daily_forecast'][0]['wind_spd']
tmp_max = json_data['HeWeather6'][0]['daily_forecast'][0]['tmp_max']
tmp_min = json_data['HeWeather6'][0]['daily_forecast'][0]['tmp_min']
print(location)
print(wind_dir)
print(wind_spd)
print(tmp_max)
print(tmp_min)
