# Stubs de conexión a Bitunix (rellenar endpoints reales en siguiente iteración)
# Mantiene la estructura para 15m + confirmación 5m

from typing import List, Dict, Any

async def list_futures_pairs() -> List[str]:
    # TODO: implementar con endpoint público de Bitunix
    # Retornar una lista de símbolos, por ejemplo: ["ADAUSDT", "BTCUSDT"]
    # Placeholder mínimo para pruebas:
    return ["ADAUSDT", "BTCUSDT"]

async def fetch_klines_rest(symbol: str, interval: str, limit: int = 200) -> list:
    # TODO: implementar REST histórico
    # Debe devolver lista de velas con [open_time, open, high, low, close, volume, close_time]
    return []

async def last_closed_candle(symbol: str, interval: str) -> Dict[str, Any]:
    # TODO: usar WS o REST para obtener la última vela **cerrada**
    # Estructura de retorno esperada:
    # {"open_time":..., "open":..., "high":..., "low":..., "close":..., "volume":...}
    return {}
