
# Bitunix Futures Alerts Bot (15m + 5m confirm)

Bot de ejemplo en **Python** para ejecutar en **Render** como *Background Worker*.
- Dependencias livianas (sin `numpy/pandas`) para evitar fallos de build.
- Envia alertas a **Telegram**. Lógica demo lista para pruebas.

## Variables de entorno (Render → Environment)
- `TELEGRAM_TOKEN` — Token del bot (BotFather)
- `CHAT_ID` — Chat ID destino
- `SYMBOLS` — Opcional, símbolos separados por coma. Ej: `BTCUSDT,ETHUSDT`
- `TF_MAIN` — Opcional, minutos (default `15`)
- `TF_CONFIRM` — Opcional, minutos (default `5`)

## Despliegue en Render
1) **New → Background Worker** (no Web Service).
2) Conecta tu repo.
3) **Build Command**
```
pip install -r requirements.txt
```
4) **Start Command**
```
python main.py
```
5) Agrega las variables de entorno y Deploy.

> Si usas Web Service, debes implementar un servidor que escuche en `$PORT`. Este ejemplo usa **long polling** y por eso se recomienda *Background Worker*.
