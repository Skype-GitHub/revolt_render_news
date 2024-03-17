import requests
import revolt
import asyncio
import always_on
class RevoltBot(revolt.Client):
    async def on_ready(self):
        print(f"Logged in as {self.user.name}")
# NewsAPIからニュースのJSONを取得する同期関数
def get_news_json(api_key):
    response = requests.get(
        'https://newsapi.org/v2/top-headlines',
        params={'country': 'jp', 'apiKey': api_key}
    )
    return response.json()

class RevoltBot(revolt.Client):
  async def on_ready(self):
      print(f"Logged in as {self.user.name}")

  async def on_message(self, message: revolt.Message):
   if message.content == "./news":
        loop = asyncio.get_event_loop()
        news_json = await loop.run_in_executor(None, get_news_json, api_key)
        await client.send_message(message.channel_id, str(news_json))
   await client.start()

async def main():
    async with revolt.utils.client_session() as session:
        client = RevoltBot(session = session, token = "BaL5C9RI1sjs2i0DKd3CUmLRTUedxpaHT7oOz58xKA3ebibeavuQS_I8HL4qUSsU")
        

if __name__ == '__main__':
  api_key = '8d3db2a0f076426482dfc5b8787bad32'  # NewsAPIのAPIキー   # Revoltのトークン
  asyncio.run(main()) # asyncio.runを使ってメイン関数を実行
  always_on.activate()
