#此脚本为单个网站多线程扫描
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
        code=requests.get(urls).status_code
        if code==200 or code==403:
            f=open('ok.txt','a+')
            f.write(urls+'\n')
            f.close()
        else:
            print(urls+'|'+str(code))
            time.sleep(1)

def show():
    print('ps:scan.py http://www.xiaodi8.com dir.txt 10')
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
#在cmd命令行 C:\Users\XIAODI-PC>E:\myproject\venv\Scripts\python.exe E:\myproject\Webfilescan.py http://tp1.swjtu.edu.cn/ dir.txt 10








