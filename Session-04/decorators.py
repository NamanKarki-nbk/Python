# A decorator is a function that:

# Takes another function

# Adds something extra

# Returns a new function

import time
def time_decorator(func):
    def wrapper():
        start_time =time.time()
        func()
        end_time=time.time()
        print(f"⏱️ Took {end_time - start_time:.4f} seconds")
    return wrapper


@time_decorator
def slow_function():
    time.sleep(2)  # Pretend it's doing something slow
    print("Finished working!")
slow_function()
