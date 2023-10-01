#What is the expected outcome of the following code?
def fun(x):
    return 1 / x

def mid_level(x):
    try:
        fun(x)
    except:
        raise AssertionError
    else:
        return 0
    

try:
    x = mid_level(0)
except Exception:
    x = -1 
except:
    x = -2
print(x)

#-1

"""
1. The fun(0) invocation raises the ZeroDivisionError exception;
2. The exception is caught by the except: branch, and the AssertionError is raised;
3. As the AssertError is a sub-class of Error, it is handled by the except Exception: branch;
4. In effect the x variable is set to -1, and this is the value that will be printed.

"""