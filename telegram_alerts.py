import aiohttp
import asyncio
import os

TELEGRAM_API = "https://api.telegram.org"

async def send_telegram_message(token: str, chat_id: str, text: str) -> bool:
    url = f"{TELEGRAM_API}/bot{token}/sendMessage"
    payload = {"chat_id": chat_id, "text": text, "disable_web_page_preview": True}
    timeout = aiohttp.ClientTimeout(total=15)
    async with aiohttp.ClientSession(timeout=timeout) as session:
        async with session.post(url, json=payload) as resp:
            ok = resp.status == 200
            if not ok:
                body = await resp.text()
                print(f"[TELEGRAM][ERROR] {resp.status} {body}")
            return ok
