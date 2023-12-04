try:
    # Some code that might raise an exception
    result = int("abc")
except Exception as e:
    # Handling the exception and using the exception object (e)
    print(f"Caught an exception: {type(e).__name__}")
    # You can also access additional information from the exception object
    print(f"Exception details: {e}")
