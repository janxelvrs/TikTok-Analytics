#from Crawler import Crawler
from TikTokApi import TikTokApi
import asyncio
import os

crawler = Crawler()

# crawler.getUserPosts("wheel.world")

ms_token = os.environ.get("ms_token", None)

api = TikTokApi()

async def trending_videos():
    async with TikTokApi() as api:
        await api.create_sessions(ms_tokens=[ms_token], num_sessions=1, sleep_after=3)
        async for video in api.trending.videos(count=30):
            print(video.author.username)
            #print(video.as_dict)

async def user_videos():
    async with TikTokApi() as api:
        await api.create_sessions(ms_tokens=[ms_token], num_sessions=1, sleep_after=3)
        async for video in api.user(username="wheel.world").videos():
            # print(api.user(username="emma.davis05").videos(count = 1000))
            #if "contents" in video.as_dict:
            print(video.as_dict)
            # print(video.hashtags[0].name)
            exit()



asyncio.run(user_videos())

