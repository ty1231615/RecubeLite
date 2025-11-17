import math

"""
    t: 0.0〜1.0 の進行度を入力
    戻り値: 補間後の値（0.0〜1.0）
"""

def no_easing(t: float) -> float:
    return t

def ease_out_expo(t: float) -> float:

    if t >= 1:
        return 1
    return 1 - math.pow(2, -10 * t)

def easeOutQuart(t):
    return 1 - math.pow(1 - t, 4);
