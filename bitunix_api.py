
import logging
from typing import List, Optional, Tuple
import requests

log = logging.getLogger(__name__)

def fetch_klines(symbol: str, interval_minutes: int, limit: int = 50) -> Optional[List[Tuple[float, float, float, float]]]:
    """Devuelve lista de tuplas (open, high, low, close) ó None si falla."""
    m = {1: "1m", 3: "3m", 5: "5m", 15: "15m", 30: "30m", 60: "1h"}
    interval = m.get(int(interval_minutes), "15m")
    url = "https://fapi.binance.com/fapi/v1/klines"
    params = {"symbol": symbol.upper(), "interval": interval, "limit": limit}
    try:
        r = requests.get(url, params=params, timeout=10)
        r.raise_for_status()
        data = r.json()
        return [(float(x[1]), float(x[2]), float(x[3]), float(x[4])) for x in data]
    except Exception as e:
        log.warning("No se pudieron obtener klines para %s: %s", symbol, e)
        return None
