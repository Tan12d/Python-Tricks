import asyncio
from gofile2 import Gofile

async def main():
    g_a = await Gofile.initialize(token="TPi1fX1TRV3cSkyFqEhODi8aio23Dqr7")

    # Get current server
    await g_a.get_server()

    # Upload a file
    await g_a.upload(file="Anti.pdf")

    # After everything, close Gofile client
    await g_a.done()

# Call first within an async context
asyncio.run(main())

