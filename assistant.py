#!/usr/bin/python3
# code=utf-8

from wxpy import *
from pro import *

bot = Bot()
pro = Pro()


class Assistant:
    def __init__(self):
        pass

    def ReplyGroup(self, msg):
        user = str(msg.member)[9:]
        print(user)
        if len(msg.text) == 8 and msg.text == "@xiao.an":
            print(user)
            answer = "@" + user + " 此人已死，有事烧纸！"
            msg.reply(answer)
        else:
            text = str(msg.text)[8:]
            print(text)
            ans = pro.find(text)
            print(ans)
            answer = "@" + user + ans
            msg.reply(answer)

    def Reply(self, msg):
        if len(msg.text) == 0:
            return
        question = msg.text
        gailou = question.find("盖楼")
        kanjia = question.find("砍价")
        if gailou == -1 :
            if kanjia == -1:
                return

        msg.reply("家里茅草屋都倒了，还帮你盖什么楼")
        return

