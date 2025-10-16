
import logging
from telegram import Bot

log = logging.getLogger(__name__)

def send_alert(bot: Bot, chat_id: str, text: str) -> bool:
    try:
        bot.send_message(chat_id=chat_id, text=text, disable_web_page_preview=True)
        return True
    except Exception as e:
        log.error("Error enviando alerta a Telegram: %s", e)
        return False
