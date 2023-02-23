import sys
import os
import requests
import threading
import queue
import time

q=queue.Queue()

def scan():
    while not q.empty():
        dir=q.get()
        urls=url+dir
        urls=urls.replace('\n','')
        code=requests.get(urls,headers=headers).status_code
        rep=requests.get(urls,headers=headers)
        time.sleep(5)
        if code==200:
            i=rep.text.find("safedog")
            x=rep.text.find("403</a>错误")
            if x!=-1:
                print(urls+"|"+str(code))
            if i==-1:
                print(urls+"|"+str(code))
        else:
            time.sleep(1)

def show():
    print('ps:scan.py http://www.baidu.com dir.txt 10')
    print('\n')
    print('脚本名 网站地址 字典文件 线程数')

if __name__ == '__main__':
    path=os.path.dirname(os.path.realpath(__file__))
    if len(sys.argv)<4:
        show()
        sys.exit()
    url=sys.argv[1]
    file=sys.argv[2]
    num=sys.argv[3]
    for dir in open(path+'/'+file):
        q.put(dir)
    for i in range(int(num)):
        t=threading.Thread(target=scan)
        t.start()