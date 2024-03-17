import requests
import asyncio
from revolt import Client, Message, File

# NewsAPIからニュースのJSONを取得する同期関数
def get_news_json(api_key):
    response = requests.get(
        'https://newsapi.org/v2/top-headlines',
        params={'country': 'jp', 'apiKey': api_key}
    )
    return response.json()

# ニュースをテキストファイルに保存する関数
def save_news_to_txt(news_json, file_path):
    with open(file_path, 'w', encoding='utf-8') as file:
        for article in news_json['articles']:
            title = article['title']
            file.write(f"{title}\n")

# メッセージが送信されたときの処理
async def on_message(client, message, api_key):
    if message.content == "./news":
        loop = asyncio.get_event_loop()
        
        # ニュースを取得し、テキストファイルに保存
        news_json = await loop.run_in_executor(None, get_news_json, api_key)
        file_path = 'news.txt'
        await loop.run_in_executor(None, save_news_to_txt, news_json, file_path)
        
        # テキストファイルをRevoltに送信
        with open(file_path, 'rb') as file:
            await client.send_files(message.channel_id, files=[File("news.txt", file)])

# Botを実行するメイン関数
async def main(token, api_key):
    client = Client(token)

    @client.event
    async def on_message(message: Message):
        await on_message(client, message, api_key)

    await client.start()

if __name__ == '__main__':
    api_key = '8d3db2a0f076426482dfc5b8787bad32'  # NewsAPIのAPIキー
    revolt_token = 'BaL5C9RI1sjs2i0DKd3CUmLRTUedxpaHT7oOz58xKA3ebibeavuQS_I8HL4qUSsU'  # Revoltのトークン
    asyncio.run(main(revolt_token, api_key))  # asyncio.runを使ってメイン関数を実行
