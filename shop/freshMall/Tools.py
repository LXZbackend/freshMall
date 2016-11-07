#coding=utf-8
# 这是一个工具类
def remove_repeat(mylist):
	newlist = []
	for temp in mylist:
		if  temp not in newlist:
			newlist.append(temp)
	return newlist