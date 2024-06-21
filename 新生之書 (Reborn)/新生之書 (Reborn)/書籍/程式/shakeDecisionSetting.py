# -*- coding: UTF-8
TYPE_MAX = 2                                # 1爻 有機率出現 2種可能（陰、陽）
UNIT_COUNT = 3                              # 1八卦 = 3爻
GROUP_COUNT = 2                             # 64卦 = 2八卦
GROUP_KIND_MAX = pow(TYPE_MAX, UNIT_COUNT)  # 八卦 總共有 8種 卦
UNIT_MAX = GROUP_COUNT * UNIT_COUNT         # 上八卦 + 下八卦 = 6爻