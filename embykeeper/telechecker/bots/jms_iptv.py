from pyrogram.types import Message

from .base import AnswerBotCheckin


class JMSIPTVCheckin(AnswerBotCheckin):
    name = "卷毛鼠IPTV"
    bot_username = "JMSIPTV_bot"
    bot_captcha_len = [5]

    async def on_captcha(self, message: Message, captcha: str):
        await super().on_captcha(message, captcha.upper())
