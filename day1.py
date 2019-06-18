import requests
#请求百度，需要注意：一定要带上http/https
response=requests.get('http://www.baidu.com')
print(response)
print(response.text)
print(response.headers)
#模拟伪造一个浏览器
headers = {'User_Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:55.0) Gecko/20100101 Firefox/55.0'}
response=requests.get('http://www.baidu.com',headers=headers)
print(response.text)
print(response.headers)

from selenium import webdriver

drive = webdriver.Firefox()
drive.get('http://ww.baidu.com')