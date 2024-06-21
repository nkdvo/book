# -*- coding: UTF-8
def graph(upNumber, downNumber, changeNumber, UNIT_COUNT, GROUP_KIND_MAX, UNIT_MAX):
    up = divmod(upNumber, GROUP_KIND_MAX)[1]                    # 上卦 = 上卦數 除以8的 餘數。
    down = divmod(downNumber, GROUP_KIND_MAX)[1]                # 下卦 = 下卦數 除以8的 餘數。
    changePosition = divmod(changeNumber-1, UNIT_MAX)[1]        # 動爻位置 = 動爻數 除以6的 餘數。
    main = upDownToMain(up, down, UNIT_COUNT, GROUP_KIND_MAX)   # 主卦 = 上卦、下卦，先天八卦數 → 卦象。
    main = main                                                 # 已知，主卦，事情的開始、事情的主體。
    zoomIn = mainToZoomIn(main, UNIT_COUNT)                     # 可知，互卦，事情的中間發展。
    change = mainToChange(main, changePosition)                 # 可知，變卦，事情的結果。
    return main, zoomIn, change, changePosition


def upDownToMain(up, down, UNIT_COUNT, GROUP_KIND_MAX):
    upGraph = list(bin(divmod(GROUP_KIND_MAX - up, GROUP_KIND_MAX)[1]))[2:]
    upGraph = [False] * (UNIT_COUNT - len(upGraph)) + upGraph
    downGraph = list(bin(divmod(GROUP_KIND_MAX - down, GROUP_KIND_MAX)[1]))[2:]
    downGraph = [False] * (UNIT_COUNT - len(downGraph)) + downGraph
    return [(i == "1") for i in (downGraph + upGraph)]


def mainToZoomIn(main, UNIT_COUNT):
    zoomIn = []
    for i in range(1, len(main) - UNIT_COUNT):
        zoomIn += main[i:(i + UNIT_COUNT)]
    return zoomIn


def mainToChange(main, changePosition):
    change = list(main)
    change[changePosition] = not(change[changePosition])
    return change
