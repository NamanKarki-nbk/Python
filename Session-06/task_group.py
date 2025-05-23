import asyncio


async def fetch_data(id, sleep_time):
    print(f"Coroutine {id} staring to fetch data.")
    await asyncio.sleep(sleep_time)
    return{"id": id, "data": f"Sample data from coroutine {id}"}


async def main():
    tasks = []
    async with asyncio.TaskGroup() as tg:
        for i, sleep_time in enumerate( [2, 1, 4], start=1):
            task = tg.create_task(fetch_data(i, sleep_time))
            tasks.append(task)
    
    #After the Task Group block, all tasks have completed
    results = [task.result() for task in tasks] #example of list comprehension
    
    for result in results:
        print(f"Received result: {result}")
        

asyncio.run(main()) 
