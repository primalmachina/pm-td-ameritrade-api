import asyncio

from td.client import TdAmeritradeClient
from td.enums.enums import QOSLevel
from td.config import TdConfiguration

# from samples.stream_client.example_handlers import news_handler


async def callback_func(msg):
    # pass
    print(msg)


config = TdConfiguration()
td_client = TdAmeritradeClient()
stream_client = td_client.streaming_api_client(on_message_received=callback_func)
stream_services = stream_client.services


async def run_td_stream_client():
    stream_client.open_stream(asyncio.get_running_loop())
    stream_services.quality_of_service(qos_level=QOSLevel.EXPRESS)


async def add_account_activity_handler():
    pass
    # TODO: Implement Handlers for ACCT_ACTIVITY
    # stream_services.add_handler("data", "NEWS_HEADLINE", news_handler.data_message_handler)


async def main():
    await run_td_stream_client()
    await add_account_activity_handler()

    stream_services.account_activity()

    await asyncio.sleep(30)


if __name__ == "__main__":
    asyncio.run(main())
