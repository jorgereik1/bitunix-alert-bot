import os
import asyncio
from aiohttp import web
from dotenv import load_dotenv
from telegram_alerts import send_telegram_message
from bitunix_api import list_futures_pairs, last_closed_candle
from strategy import analyze_candle_15m_and_confirm_5m

load_dotenv()

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN", "")
CHAT_ID        = os.getenv("CHAT_ID", "")
TF_MAIN        = os.getenv("TF_MAIN", "15m")
TF_CONFIRM     = os.getenv("TF_CONFIRM", "5m")

async def engine_loop():
    await asyncio.sleep(2)
    if TELEGRAM_TOKEN and CHAT_ID:
        await send_telegram_message(TELEGRAM_TOKEN, CHAT_ID, "🤖 Bot iniciado en Render. Escaneando pares...")

    while True:
        try:
            symbols = await list_futures_pairs()
            for sym in symbols:
                # Obtener velas cerradas (placeholders por ahora)
                c15 = {"open": "1", "close": "1"}  # TODO: reemplazar con datos reales
                c5  = {"open": "1", "close": "1"}
                signal = analyze_candle_15m_and_confirm_5m(c15, c5)
                if signal:
                    direction, reason = signal
                    text = f"🔔 Señal {direction} CONFIRMADA\nSímbolo: {sym}\nMarco: {TF_MAIN} (confirmado en {TF_CONFIRM})\nMotivo: {reason}"
                    if TELEGRAM_TOKEN and CHAT_ID:
                        await send_telegram_message(TELEGRAM_TOKEN, CHAT_ID, text)
                    else:
                        print("[WARN] Falta TELEGRAM_TOKEN/CHAT_ID para enviar alerta.")
            await asyncio.sleep(60)  # ejecutar cada minuto
        except Exception as e:
            print(f"[ENGINE][ERROR] {e}")
            await asyncio.sleep(5)

# HTTP minimal para healthcheck
async def health(_):
    return web.json_response({"status": "ok"})

async def on_startup(app):
    app['engine_task'] = asyncio.create_task(engine_loop())

async def on_cleanup(app):
    task = app.get('engine_task')
    if task:
        task.cancel()
        with contextlib.suppress(asyncio.CancelledError):
            await task

def create_app():
    app = web.Application()
    app.router.add_get('/health', health)
    app.on_startup.append(on_startup)
    app.on_cleanup.append(on_cleanup)
    return app

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))
    web.run_app(create_app(), host='0.0.0.0', port=port)
