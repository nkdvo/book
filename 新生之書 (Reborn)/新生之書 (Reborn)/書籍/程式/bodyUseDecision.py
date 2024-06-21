# -*- coding: UTF-8
import uniout


def bodyUseDecision(main, zoomIn, change, changePosition, UNIT_COUNT):
    useGroupIndex = changePosition / UNIT_COUNT         # 動爻位置 所在的 卦的 組 是 用黨。
    #                                                                                                      # 動爻位置 不在的 卦的 組 是 體黨。
    # 卦 → 5行 → 5行生克 → 上卦、下卦 的 生克關係 → 體黨、用黨 的 生克關係 → 吉凶。
    print("主卦，" + str(main) + " → " + str(result(main, UNIT_COUNT, useGroupIndex)))
    print("互卦，" + str(zoomIn) + " → " + str(result(zoomIn, UNIT_COUNT, useGroupIndex)))
    print("變卦，" + str(change) + " → " + str(result(change, UNIT_COUNT, useGroupIndex)))


def result(graph, UNIT_COUNT, useGroupIndex):
    KIND = {
        "[True, True, True]": "金",
        "[True, True, False]": "金",
        "[True, False, True]": "火",
        "[True, False, False]": "木",
        "[False, True, True]": "木",
        "[False, True, False]": "水",
        "[False, False, True]": "土",
        "[False, False, False]": "土",
    }                                   # 卦 → 5行
    BORN = ["金", "水", "木", "火", "土", "金"]   # 生，金 → 水 → 木 → 火 → 土 → 金
    HURT = ["水", "火", "金", "木", "土", "水"]   # 克，水 → 火 → 金 → 木 → 土 → 水
    upKind = ""
    relationship = []
    for i in range(len(graph) / UNIT_COUNT):
        downKind = upKind
        upGraph = str(graph[i * UNIT_COUNT:(i+1) * UNIT_COUNT])
        if (upGraph in KIND) is False:
            relationship.append("錯誤")
            break
        upKind = KIND[upGraph]
        if downKind != "":
            if (upKind in BORN) is False:
                relationship.append("錯誤")
                break
            elif (upKind in HURT) is False:
                relationship.append("錯誤")
                break
            elif downKind == upKind:
                relationship.append("平")
            elif i == useGroupIndex:
                if BORN[BORN.index(upKind)+1] == downKind:
                    relationship.append("大吉")
                elif BORN[BORN.index(downKind)+1] == upKind:
                    relationship.append("小凶")
                elif HURT[HURT.index(upKind)+1] == downKind:
                    relationship.append("大凶")
                elif HURT[HURT.index(downKind)+1] == upKind:
                    relationship.append("小吉")
                else:
                    relationship.append("錯誤")
                    break
            else:
                if BORN[BORN.index(upKind)+1] == downKind:
                    relationship.append("小凶")
                elif BORN[BORN.index(downKind)+1] == upKind:
                    relationship.append("大吉")
                elif HURT[HURT.index(upKind)+1] == downKind:
                    relationship.append("小吉")
                elif HURT[HURT.index(downKind)+1] == upKind:
                    relationship.append("大凶")
                else:
                    relationship.append("錯誤")
                    break
    if len(relationship) == 1:
        relationship = relationship[0]
    return relationship
