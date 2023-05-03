import asyncio
import time
import os
from typing import Any, Dict
import aiohttp
# Magnus Glantz, sudo@redhat.com, 2023
# Example EDA plugin

# Entrypoint from ansible-rulebook
async def main(queue: asyncio.Queue, args: Dict[str, Any]):

    # Fetch file_name defined in the top of demo-rulebook.yml
    file_name = args.get("file_name", [])
    delay = int(args.get("delay", 1))

    # Infinite loop
    while True:
        # If the file exists, submit a dict which contains name of file and if it exists. We can use any of these things to create rules.
        if os.path.exists(file_name):
            await queue.put(
                dict(
                    demo=dict(
                        file_name=file_name,
                        status="exists"
                    )
                )
            )
        # If the file does not exist, set status to "missing" so users can create a playbook to deal with that scenario
        else:
            await queue.put(
                dict(
                    demo=dict(
                        file_name=file_name,
                        status="missing"
                    )
                )
            )

        # Sleep for delay many seconds
        await asyncio.sleep(delay)

# Main
if __name__ == "__main__":

    class MockQueue:
        async def put(self, event):
            print(event)

    asyncio.run(main(MockQueue(), {"file_name": ["/etc/issue"]}))
