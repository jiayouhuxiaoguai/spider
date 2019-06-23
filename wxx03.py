import os       
import sys      
    
def search(path,name):

    for root, dirs, files in os.walk(path):  
        if name in dirs or name in files:
            flag = 1      
            root = str(root)
            dirs = str(dirs)
            return os.path.join(root, dirs)
    return -1


path = input('c:/Users/Administrator/Desktop/day03.py')
print('http')
name = sys.stdin.readline().rstrip() 
answer = search(path,name)
if answer == -1:
    print("查无此文件")
else:
    print(answer)


import requests
url = 'http://www.image-net.org/api/text/imagenet.syns'
response = requests.get(url)
HTML=response.text
USES=HTML.split('\n')
lines=HTML.split('\n')

for url in USES:
    response = requests.get(url)
    content = response.content
    name = erl.split('/')[-1]
    with open(name,'wb')as f:
        f.write(content)