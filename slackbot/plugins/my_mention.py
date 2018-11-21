from slackbot.bot import respond_to
from slackbot.bot import listen_to
from slackbot.bot import default_reply

from libs import my_functions

@respond_to("メンション")
def mention_func(message):
    message.reply("「メンション」されました")

@listen_to("テスト")
def listen_func(message):
    message.send("「テスト」発言を検知しました")
    message.reply("発言者")

@listen_to("週報")
def listen_func_2(message):
    report = my_functions.peReport()
    # print(report)
    message.send(report)
