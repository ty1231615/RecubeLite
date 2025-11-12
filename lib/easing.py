import math

def ease_out_expo(t: float) -> float:
    """イージング関数: EaseOutExpo
    t: 0.0〜1.0 の進行度を入力
    戻り値: 補間後の値（0.0〜1.0）
    """
    if t >= 1:
        return 1
    return 1 - math.pow(2, -10 * t)
