import asyncio

#A shared variable

shared_resoiurce = 0

# An asyncio lock
lock = asyncio.Lock()


async def modify_shared_resource():
    global shared_resoiurce
    async with lock:
        #Critical section starts
        print(f"Resource before modification: {shared_resoiurce}")
        shared_resoiurce +=1 
        await asyncio.sleep(1)
        print(f"Resource after modification: {shared_resoiurce}")
        #Critrical section ends
        
        
async def main():
    await asyncio.gather(*(modify_shared_resource() for _ in range(5)))
    

asyncio.run(main())