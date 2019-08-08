import re, requests

url = 'https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.8971'
response = requests.get(url, verify=False)
stations = re.findall(r'([\u4e00-\u9fa5]+)\|([A-Z]+)', response.text)
station_codes = dict(stations)
station_names = dict(zip(station_codes.values(), station_codes.keys()))
