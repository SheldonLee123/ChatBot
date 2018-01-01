# coding: utf-8

import os
import time
import yuyinhecheng
import Turing
import yuyinshibie


tok = yuyinshibie.get_access_token()

switch = True
while switch:
    os.system('arecord -f S16_LE -d 3 -r 16000 -D "plughw:1,0" /home/sheldon/Documents/ChatBot/Pi3\(baidu+tuling\)/record/test.wav')
    time.sleep(0.5)
    info = yuyinshibie.asr_main("record/test.wav",tok)
    print "sheldon:"+info

    '''
    if '关闭'.encode("utf-8") in info:
        while True:
            os.system('arecord -D "plughw:1" -f S16_LE -r 16000 -d 10 /home/sheldon/Documents/ChatBot/Pi3\(baidu+tuling\)/record/test.wav')
            time.sleep(10)

            info = yuyinshibie.asr_main("/home/sheldon/Documents/ChatBot/Pi3\(baidu+tuling\)/record/test.wav",tok)
            if '开启'.encode("utf-8") in info:
                break

                url = "http://tsn.baidu.com/text2audio?tex=开启成功&lan=zh&cuid=B8-27-EB-BA-24-14&ctp=1&tok="+tok+"&per=3"
                os.system('mpg123 "%s"'%url)


            elif '暂停'.encode("utf-8") in info:
                url = "http://tsn.baidu.com/text2audio?tex=开始暂停&lan=zh&cuid=B8-27-EB-BA-24-14&ctp=1&tok="+tok+"&per=3"
                os.system('mpg123 "%s"'%url)
                time.sleep(10)

                url = "http://tsn.baidu.com/text2audio?tex=暂停结束&lan=zh&cuid=B8-27-EB-BA-24-14&ctp=1&tok="+tok+"&per=3"
                os.system('mpg123 "%s"'%url)
                continue


            else:
                tex = Turling.Turling(info)
                url = yuyinhecheng.yuyinhecheng_api(tok,tex)
                os.system('mpg123 "%s"'%url)
                time.sleep(0.5)
    '''

    tex = Turing.Turing(info)
    url = yuyinhecheng.yuyinhecheng_api(tok,tex)
    os.system('mpg123 "%s"'%url)
    time.sleep(0.5)
