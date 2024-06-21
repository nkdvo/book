# -*- coding: UTF-8
from datetime import datetime
from shakeDecisionSetting import UNIT_COUNT, GROUP_KIND_MAX, UNIT_MAX
from graph import graph
from bodyUseDecision import bodyUseDecision


# 時分起卦法、體用生克斷卦法
def hourMinMethod():
    # 時分起卦法
    now = datetime.now()                                # 現在時間
    upNumber = now.hour                                 # 上卦數 = 現在時間的 小時
    downNumber = now.minute                             # 下卦數 = 現在時間的 分鐘
    changeNumber = (upNumber + downNumber)              # 動爻數 = 上卦數 + 下卦數
    # print("時分起卦法、體用生克斷卦法，上卦數 " + str(upNumber) + "，下卦數 " + str(downNumber) + "，動爻數 " + str(changeNumber))
    main, zoomIn, change, changePosition = graph(upNumber, downNumber, changeNumber, UNIT_COUNT, GROUP_KIND_MAX, UNIT_MAX)
    # 體用生克斷卦法
    bodyUseDecision(main, zoomIn, change, changePosition, UNIT_COUNT)


hourMinMethod()
