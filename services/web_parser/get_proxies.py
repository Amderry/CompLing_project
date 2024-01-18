import asyncio
from proxybroker import Broker

async def get_working_proxies(proxies):
    with open("../../proxy_list.txt", "w") as file:
        while True:
            proxy = await proxies.get()
            if proxy is None: break
            print(f'{proxy.host}:{proxy.port}')
            file.write(f'{proxy.host}:{proxy.port}\n')
        file.close()

def get_proxy_list():
    proxies = asyncio.Queue()
    broker = Broker(proxies)
    try:
        tasks = asyncio.gather(
            broker.find(types=['HTTPS'], limit=1, timeout=8, max_tries=3),
            asyncio.wait_for(get_working_proxies(proxies), timeout=5))

        loop = asyncio.get_event_loop()
        loop.run_until_complete(tasks)
    except Exception as e:
        print(e)

