#多网站多线程扫描
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
        urls=urls.replace('\n','')
        try:
            # 以下except都是用来捕获当requests请求出现异常时，
            # 通过捕获然后等待网络情况的变化，以此来保护程序的不间断运行
            code = requests.get(urls).status_code
            if code == 200 or code == 403:
                f = open('ok.txt', 'a+')
                f.write(urls + '\n')
                f.close()
            else:
                print(urls + '|' + str(code))
                time.sleep(1)

        except requests.exceptions.ConnectionError:
            print('ConnectionError -- please wait 3 seconds')
            time.sleep(1)

        except requests.exceptions.ChunkedEncodingError:
            print('ChunkedEncodingError -- please wait 3 seconds')
            time.sleep(1)

        except:
            print('Unfortunitely -- An Unknow Error Happened, Please wait 3 seconds')
            time.sleep(1)

def show():
    print('ps:scan.py url.txt dir.txt 10')
    print('\n')
    print('脚本名 网站文件 字典文件 线程数')

if __name__ == '__main__':
    path=os.path.dirname(os.path.realpath(__file__))
    if len(sys.argv)<4:
        show()
        sys.exit()
    url=sys.argv[1]
    file=sys.argv[2]
    num=sys.argv[3]
    for url in open(path+'/'+url):
        for dir in open(path+'/'+file):
            urls=url+dir
            q.put(dir)
    for i in range(int(num)):
        t=threading.Thread(target=scan)
        t.start()
# cmd命令行下 C:\Users\XIAODI-PC>D:\python3\python.exe E:\myproject\Webfilescan.py url.txt dir.txt 10















