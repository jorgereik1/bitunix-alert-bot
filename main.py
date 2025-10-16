
import os
import asyncio
import logging
from datetime import datetime

from telegram.ext import Application, CommandHandler

import bitunix_api as api
import strategy
from telegram_alerts import send_alert

logging.basicConfig(
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
    level=logging.INFO,
)
log = logging.getLogger("bitunix-bot")

TELEGRAM_TOKEN = os.environ.get("TELEGRAM_TOKEN", "")
CHAT_ID = os.environ.get("CHAT_ID", "")
SYMBOLS = [s.strip().upper() for s in os.environ.get("SYMBOLS", "BTCUSDT,ETHUSDT").split(",") if s.strip()]
TF_MAIN = int(os.environ.get("TF_MAIN", "15"))
TF_CONFIRM = int(os.environ.get("TF_CONFIRM", "5"))

async def cmd_ping(update, context):
    await update.message.reply_text("🏓 Pong! Bot activo.")

async def scan_once(app):
    bot = app.bot
    for symbol in SYMBOLS:
        main_ohlc = api.fetch_klines(symbol, TF_MAIN, limit=60)
        conf_ohlc = api.fetch_klines(symbol, TF_CONFIRM, limit=60)
        if not main_ohlc or not conf_ohlc:
            log.info("Datos insuficientes para %s (demo).", symbol)
            continue
        sig = strategy.evaluate(symbol, main_ohlc, conf_ohlc)
        if sig:
            msg = f"📣 Señal {sig} | {symbol}\nTF {TF_MAIN} confirmada por {TF_CONFIRM} | {datetime.utcnow().isoformat()}Z"
            if TELEGRAM_TOKEN and CHAT_ID:
                send_alert(bot, CHAT_ID, msg)
            log.info("ALERTA: %s", msg)
        else:
            log.info("Sin señal para %s.", symbol)

async def job_loop(app):
    while True:
        try:
            await scan_once(app)
        except Exception as e:
            log.exception("Error en ciclo: %s", e)
        await asyncio.sleep(60)

async def main():
    if not TELEGRAM_TOKEN:
        log.warning("TELEGRAM_TOKEN vacío; agrega variables de entorno.")
    app = Application.builder().token(TELEGRAM_TOKEN).build()
    app.add_handler(CommandHandler("ping", cmd_ping))
    app.create_task(job_loop(app))
    log.info("Bot iniciado. Timeframes: main=%s confirm=%s | symbols=%s", TF_MAIN, TF_CONFIRM, SYMBOLS)
    await app.run_polling(close_loop=False)

if __name__ == "__main__":
    asyncio.run(main())
