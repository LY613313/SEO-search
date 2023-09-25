# 此函数用于获取实时时间
import datetime


def nowtime():
    time = datetime.datetime.now().strftime('%Y-%m-%d  %H:%M:%S')
    return '[ ' + time + ' ]'