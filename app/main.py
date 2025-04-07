from typing import Callable, Any
from functools import wraps


def cache(func: Callable) -> Callable:
    results = {}

    @wraps(func)
    def wrapper(*args, **kwargs) -> Any:

        nonlocal results

        if func.__name__ in results:
            if args + tuple(kwargs.items()) in results[func.__name__]:
                print("Getting from cache")
                return results[func.__name__][args + tuple(kwargs.items())]
        else:
            results[func.__name__] = {}

        print("Calculating new result")
        result = func(*args, **kwargs)
        results[func.__name__][args + tuple(kwargs.items())] = result

        return result
    return wrapper
