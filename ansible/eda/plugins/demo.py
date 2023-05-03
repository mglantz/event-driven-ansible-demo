import asyncio
import time
import os
from typing import Any, Dict
import aiohttp

# Entrypoint from ansible-rulebook
async def main(queue: asyncio.Queue, args: Dict[str, Any]):

    file_name = args.get("file_name", [])
    delay = int(args.get("delay", 1))

    while True:
        if os.path.exists(file_name):
            await queue.put(
                dict(
                    demo=dict(
                        file_name=file_name,
                        status="exists"
                    )
                )
            )
        else:
            await queue.put(
                dict(
                    demo=dict(
                        file_name=file_name,
                        status="missing"
                    )
                )
            )


        await asyncio.sleep(delay)

if __name__ == "__main__":

    class MockQueue:
        async def put(self, event):
            print(event)

    asyncio.run(main(MockQueue(), {"file_name": ["/etc/issue"]}))
