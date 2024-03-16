from revolt import Client, Message
from newsapi import NewsApiClient

# NewsAPIとRevoltの設定
newsapi = Client(session, os.environ['api-key'])
client = Client(session, os.environ['Revolt-TOKEN'])

# Revoltに接続
@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

    # ニュースを取得
    top_headlines = newsapi.get_top_headlines(language='ja')

    # Revoltチャンネルにニュースを送信
    channel_id = '01HPENF32VKTWPD2VFW0EH0GYK'  # 送信するチャンネルのIDを指定
    for article in top_headlines['articles']:
        content = f"{article['title']}\n{article['description']}\n{article['url']}"
        await client.send_message(channel_id, content)

# ボットを起動
client.run()
