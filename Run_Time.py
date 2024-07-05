import time


def time_function(function, *args, **kwargs):
    start_time = time.time()
    result = function(*args, **kwargs)
    end_time = time.time()
    print(f"Total execution time: {end_time - start_time:.6f} seconds")
    return result
