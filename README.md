# Bitunix Futures Alerts Bot (15m + 5m confirm)

Bot en Python para Render/Railway que:
- Escanea Futuros de Bitunix (estructura preparada; puedes completar endpoints).
- Detecta patrones (CHoCH, SFP, Retest, Momentum) en 15m y confirma en 5m.
- Envía alertas a Telegram.

## Variables de entorno
- TELEGRAM_TOKEN
- CHAT_ID
- TF_MAIN (default: 15m)
- TF_CONFIRM (default: 5m)
- MARKET (default: futures)

## Despliegue en Render
1) Crear **Web Service** (o **Background Worker** si prefieres).
2) Subir este repo/zip.
3) En *Build Command*: `pip install -r requirements.txt`
4) En *Start Command*: `python main.py`
5) Añadir variables de entorno (TOKEN, CHAT_ID, etc.).

> Nota: Incluye un servidor HTTP mínimo (salud `/health`) para Render y una tarea en segundo plano que ejecuta el motor.
