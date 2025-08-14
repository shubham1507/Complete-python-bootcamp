class AgeError(Exception):
    """Custom exception for invalid age"""
    pass

try:
    # Single specific exception (ValueError)
    age_str = input("Enter age: ")
    age = int(age_str)
    
    # Raise a custom exception
    
    if age < 0:
        raise AgeError("Age can not be negative")
        
    # Multiple specific exceptions
    a = int(input("Eneter the numerator"))
    b = int(input("Eneter the denominator"))
    result = a/b # May raise ZeroDivisionError
    
except ValueError:
    print("Invalid number format, Please enter valid number")
except ZeroDivisionError:
    print(" Can not divided by zero")
except (TypeError, OverflowError) as e:
    # Multiple exceptions in one block
    print("Type or overflow error occurred:", e)
except AgeError as e:
    ## Custom exception handling
    print(f"Custom error occured: {e}")
except Exception as e:
    # Generic exception handling
    print("Unhandeled error occured: ", e)
    
else:
    # Executes only if no exception occurred
    print(f"Division result is {result}")
finally:
     # Always executes
     print("Program execution completed (cleanup if needed).")
