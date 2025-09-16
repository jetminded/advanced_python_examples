def simple_logger(func):
    """
    A simple decorator that logs when a function is called
    """
    def wrapper():
        print(f"📞 Calling function: {func.__name__}")
        result = func()
        print(f"✅ Function {func.__name__} completed")
        return result
    return wrapper


@simple_logger
def say_hello():
  print("Hello, World!")

@simple_logger  
def say_goodbye():
  print("Goodbye, World!")

if __name__ == "__main__":
  say_hello()
  print()
  say_goodbye()
  print()
  print(say_hello.__name__)
