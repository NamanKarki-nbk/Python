import asyncio

#Define a coroutine that simulates a time-consuming task


async def fetch_data(delay):
    print("Fetching data...")
    await asyncio.sleep(delay)  #  Simulate an I/O operation wiith a sleep
    print("Data fetched")
    return {"data": "Some Data"} # Return soime data


async def main():
    print("Start of main coroutine")
    task = fetch_data(2) # ==> coroutine object
    print("End of main coroutine")
    
    result = await task
    print(f"Received result: {result}")
# Run the main coroutine
asyncio.run(main())
# thi s main()==> is a coroutine function which will return coroutine object
