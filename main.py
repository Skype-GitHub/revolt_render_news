import requests
from revolt import Client, TextChannel
import always_on
import time

async def on_ready(self):
        print(f"Logged in as {self.user.username}")
        # ここでニュースを送信したいチャンネルのIDを指定してください
        channel_id = '01HPENF32VKTWPD2VFW0EH0GYK'
        channel = await self.fetch_channel(channel_id)
        if isinstance(channel, TextChannel):
            news_articles = get_news(api_key, 'jp')
            if news_articles:
                for article in news_articles[:5]:  # トップ5記事のみ送信
                    await channel.send(f"Title: {article['title']}\nURL: {article['url']}")
            else:
                await channel.send("今日はニュースがありません。")
        else:
            print("指定されたチャンネルはテキストチャンネルではありません。")

# ここにRevoltボットのトークンを入力してください
revolt_bot_token = 'BaL5C9RI1sjs2i0DKd3CUmLRTUedxpaHT7oOz58xKA3ebibeavuQS_I8HL4qUSsU'

# NewsAPIのAPIキーを入力してください
api_key = '8d3db2a0f076426482dfc5b8787bad32'

# 既存のget_newsとdisplay_news関数はここに含める

# ボットの実行
bot = NewsBot(revolt_bot_token)
always_on.activate()
bot.run()
