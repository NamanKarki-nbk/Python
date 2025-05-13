import asyncio


async def set_future_result(future, value):
    await asyncio.sleep(2)
    #Set the result of the future
    future.set_result(value)
    print(f"Set the future's result to: {value} ")
    

async def main():
    #Createa future object
    loop = asyncio.get_running_loop()
    future = loop.create_future()
    
    #Schedule setting the future';s result
    asyncio.create_task(set_future_result(future, "Future result is ready"))
    
    #wait for the futures result
    result = await future 
    print(f"Received the futures result: {result}")
    

asyncio.run(main())