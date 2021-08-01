# PepTrader & PepCoder
# 一切从兴趣开始...
# It all starts with interests...
# I am PepCoder
# This is a Windows version of BT Trackers Updater via Python 3.6.6
# Original work belongs to @zmr, you can find his original work at
# 最初代码源来自于 @zmr，您可以在以下网址找到其最初的作品版本
# https://gitee.com/Zero_gitee/UpdateTrackers
# Trackers的代码源是来自于： https://github.com/XIU2/TrackersListCollection


import bs4
import requests
import logging
import os
import time
import html5lib

# 全局配置：
# url_trackers_best = "https://trackerslist.com/all.txt"  # 这个是普通版的，可以用在其它BT用户端上
url_trackers_best = "https://trackerslist.com/all_aria2.txt"  # 这个是aria2友好版，为aria2专门设计的
aria2_config = "D:\\soft\\Motrix\\resources\\engine\\aria2.conf"    # 设定好您的aira2所在位置，因为每个人放aria2的文件夹都不一样。
logFile = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'logger.log')

# 配置日志参数
logging.basicConfig(filename=logFile,
                    format="%(asctime)s \n%(message)s",
                    datefmt="%Y-%m-%d %H:%M:%S",
                    filemode='w',
                    level=40)


def log(level, message):
    "写日志"
    logging.log(level, message)
    return


def getTrackers(url):
    "更新Trackers"
    t = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    log(logging.DEBUG, "更新Trackers【开始】{0}\n url = {1}".format(t, url))
    try:
        # 获取最新数据
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                          'AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/67.0.3396.99 Safari/537.36'
        }
        response = requests.get(url, headers=headers).content
        soup = bs4.BeautifulSoup(response, 'html5lib')  # 解析
        all_trackers = soup.find(name='body').get_text()  # 复制
        print(all_trackers)
        log(logging.DEBUG, "更新Trackers【结束】{0}".format(all_trackers))
        return all_trackers
    except BaseException as e:
        log(logging.ERROR, "更新Trackers【异常】{0}".format(e))
        return None


def update_config(all_trackers):
    "更新aria2.conf文件 bt-tracker=all_trackers"
    try:
        btTrackerIndex = -1
        cfgList = list()
        with open(aria2_config, 'r', encoding='utf8') as cfgFile:
            lines = cfgFile.readlines()
            cfgList = list(lines)
            print(cfgList)
            for line in cfgList:
                if line.startswith("bt-tracker="):  # 在.conf里遍历寻找这一行设置
                    btTrackerIndex = cfgList.index(line)
                    break
            if btTrackerIndex >= 0:
                cfgList.pop(btTrackerIndex)
                if btTrackerIndex - 1 >= 0 and cfgList[btTrackerIndex - 1].startswith("#更新于"):
                    cfgList.pop(btTrackerIndex - 1)
                    btTrackerIndex = btTrackerIndex - 1
            else:
                btTrackerIndex = 0

        cfgList.insert(btTrackerIndex, "bt-tracker="+all_trackers+"\n")  # 覆盖写入更新内容
        update_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        cfgList.insert(btTrackerIndex, "#更新于"+update_time+"\n")

        with open("D:\\soft\\Motrix\\resources\\engine\\aria2.conf", "w", encoding='utf8') as cfgFile:  # 存储
            cfgFile.writelines(cfgList)

        return True
    except BaseException as e:
        log(logging.ERROR, "更新aria2.conf文件【异常】{0}".format(e))
        return False


def reset_config():
    "aria2c --conf-path=D:\soft\Motrix\resources\engine\aria2.conf"
    try:
        os.system("aria2c.exe --conf-path=" + aria2_config)
    except BaseException as e:
        log(logging.ERROR, "重新载入配置文件【异常】{0}".format(e))
        return False


# 配置日志输出级别
logger = logging.getLogger()
logger.setLevel(logging.ERROR)

# 开始更新操作
log(logging.DEBUG, "开始更新操作【开始】")
all_trackers = getTrackers(url_trackers_best)
update_config(all_trackers)
#reset_config()
log(logging.DEBUG, "开始更新操作【结束】\n")
