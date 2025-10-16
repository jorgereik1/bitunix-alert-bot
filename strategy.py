
from typing import Optional
from statistics import mean

def _calc_signal(ohlc):
    closes = [c for _,_,_,c in ohlc]
    if len(closes) < 12:
        return None
    ma10 = mean(closes[-10:])
    last = closes[-1]
    if last > ma10:
        return "BUY"
    if last < ma10:
        return "SELL"
    return None

def evaluate(symbol: str, tf_main_ohlc, tf_confirm_ohlc) -> Optional[str]:
    s1 = _calc_signal(tf_main_ohlc) if tf_main_ohlc else None
    s2 = _calc_signal(tf_confirm_ohlc) if tf_confirm_ohlc else None
    if s1 and s2 and s1 == s2:
        return s1
    return None
