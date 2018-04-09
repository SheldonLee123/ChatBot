# coding:utf-8

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

import pynlpir

pynlpir.open()
s = '聊天机器人到底该怎么做呢?'
segments = pynlpir.segment(s)
for segment in segments:
	print segment[0], '\t', segment[1]

pynlpir.close()
