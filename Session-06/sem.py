import asyncio


async def access_resource(semaphore, resource_id):
    async with semaphore:
        #Simulate accesing alimited resource
        print(f"Acessing recource {resource_id}")
        await asyncio.sleep(1)
        print(f"Releasing resoruce {resource_id}")
        

async def main():
    semaphore = asyncio.Semaphore(2) #'Allow 2 concurrent accesses'
    await asyncio.gather(*(access_resource(semaphore, i) for i in range(5))) #* is unpack operator,, Think of * like opening a packed bag of items.
    
asyncio.run(main())