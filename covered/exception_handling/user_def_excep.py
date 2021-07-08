# define Python user-defined exceptions
class Error(Exception):
    """Base class for other exceptions"""
    pass


class ValueTooSmallError(Error):
    """Raised when the input value is too small"""
    pass


class ValueTooLargeError(Error):
    """Raised when the input value is too large"""
    pass


number = 10
while True:
    try:
        # 1/0
        num = int(input("Enter a number: "))
        if num < number:
            raise ValueTooSmallError
        elif num > number:
            raise ValueTooLargeError("value larger than given number")
        break
    except ValueTooSmallError:
        print("This value is too small, try again!")
    except ValueTooLargeError as e:
        print(e)
    # except Exception as e:
    #     print("Something went wrong : ", e)
    #     break
