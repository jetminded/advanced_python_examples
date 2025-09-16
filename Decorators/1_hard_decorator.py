import time
import random
from functools import wraps
from typing import Callable, Type, Tuple

def retry(
    max_attempts: int = 3,
    delay: float = 1,
    backoff: float = 2,
    exceptions: Tuple[Type[Exception]] = (Exception,)
):
    def decorator(func: Callable):
        @wraps(func)
        def wrapper(*args, **kwargs):
            attempts = 0
            current_delay = delay
            
            while attempts < max_attempts:
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    attempts += 1
                    if attempts == max_attempts:
                        print(f"Failed after {max_attempts} attempts: {e}")
                        raise
                    
                    jitter = random.uniform(0, 0.1)
                    sleep_time = current_delay + jitter
                    
                    print(f"Attempt {attempts} failed: {e}. "
                          f"Retrying in {sleep_time:.2f}s...")
                    
                    time.sleep(sleep_time)
                    current_delay *= backoff
        return wrapper
    return decorator


@retry(max_attempts=5, delay=0.5, backoff=2, exceptions=(ValueError,))
def unreliable_function():
    if random.random() < 0.7:
        raise ValueError("Fail!")
    return "Success!"

if __name__ == "__main__":
    print(unreliable_function())
