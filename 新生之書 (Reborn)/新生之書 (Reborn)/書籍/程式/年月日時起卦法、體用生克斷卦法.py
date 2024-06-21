# -*- coding: UTF-8
from datetime import datetime
from shakeDecisionSetting import UNIT_COUNT, GROUP_KIND_MAX, UNIT_MAX
from graph import graph
from bodyUseDecision import bodyUseDecision


# 年月日時起卦法、體用生克斷卦法
def yearMonthDayHourMethod():
    # 年月日時起卦法
    now = datetime.now()                                # 現在時間
    upNumber = now.year + now.month + now.day           # 上卦數 = 年 + 月 + 日
    downNumber = upNumber + now.hour                    # 下卦數 = 上卦數 + 時
    changeNumber = (upNumber + downNumber)              # 動爻數 = 上卦數 + 下卦數
    # print("年月日時起卦法、體用生克斷卦法，上卦數 " + str(upNumber) + "，下卦數 " + str(downNumber) + "，動爻數 " + str(changeNumber))
    main, zoomIn, change, changePosition = graph(upNumber, downNumber, changeNumber, UNIT_COUNT, GROUP_KIND_MAX, UNIT_MAX)
    # 體用生克斷卦法
    bodyUseDecision(main, zoomIn, change, changePosition, UNIT_COUNT)


yearMonthDayHourMethod()
