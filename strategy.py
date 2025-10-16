# Lógica de señal (simplificada para pruebas). Se completará con CHoCH/SFP/Retest/Momentum.

from typing import Optional, Tuple, Dict, Any

# Parámetros por defecto
EMA_FAST = 20
EMA_SLOW = 50
RSI_LEN  = 14
RSI_MIN_LONG  = 53.0
RSI_MAX_SHORT = 47.0

def analyze_candle_15m_and_confirm_5m(candle15: Dict[str, Any],
                                      candle5: Dict[str, Any]) -> Optional[Tuple[str, str]]:
    """Devuelve (direction, reason) o None.
    Placeholder de demostración: genera LONG si close_15m > open_15m y confirma si close_5m > open_5m.
    Similar para SHORT.
    """
    if not candle15 or not candle5:
        return None
    c15o, c15c = float(candle15.get("open", 0)), float(candle15.get("close", 0))
    c5o, c5c   = float(candle5.get("open", 0)), float(candle5.get("close", 0))

    if c15c > c15o and c5c > c5o:
        return ("LONG", "Momentum sencillo: 15m y 5m verdes")
    if c15c < c15o and c5c < c5o:
        return ("SHORT", "Momentum sencillo: 15m y 5m rojas")
    return None
