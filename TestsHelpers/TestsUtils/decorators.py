import functools
import nose

def expectedFailure(reason):
    def wrapper(test):
        @functools.wraps(test)
        def decoratedTest(*args, **kwargs):
            try:
                test(*args, **kwargs)
            except Exception:
                raise nose.SkipTest(f"Unresolved issue {reason}")
            else:
                raise AssertionError(f"Failure expected according to {reason}")
        return decoratedTest
    return wrapper

def errorExplanation(why):
    def _errorExplanation(func):
        def test_wrapper(*args, **kwargs):
            classData = func.__qualname__.split(".")
            errorPrintLen = 25 if not func.__doc__ else len(func.__doc__) + 25
            print("#"*errorPrintLen)
            print(f"# Class: {classData[0]}, Test: {classData[1]}")
            print(f"# Description: {func.__doc__}")
            print(f"# FAILED because: {why}")
            print("#"*errorPrintLen)
            
            return func(*args, **kwargs)
        return test_wrapper
    return _errorExplanation