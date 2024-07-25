from termcolor import colored
import time

def ftest(function):
    
    def wrapper(*args, **kwargs):
        functionName = colored(function.__name__, "light_magenta")
        functionArgs = colored(str(args).replace("(","").replace(")","").removesuffix(","), "light_magenta")
        functionKwargs = colored(str(kwargs).replace("{","").replace("}","").replace(": ","="), "light_magenta")
        
        try:
            start = time.time()
            returnValue = function(*args, **kwargs)
            end = time.time()
            success = colored(text="SUCCESS", color="green", attrs=["bold"])
            executionTime = colored(f"{(end-start)*10**3:.03f}ms", "light_yellow")

            print(f"\nINSTANCE: {functionName}({functionArgs + functionKwargs}) : {success}")
            print(f"TIME: {executionTime}")

            return returnValue
        
        except Exception as functionError:
            failed = colored(text="FAILED", color="red", attrs=["bold"])
            functionError = colored(functionError, "light_yellow")

            print(f"\nINSTANCE: {functionName}({functionArgs + functionKwargs}) : {failed}")
            print(f"ERROR: {functionError}")
   
    return wrapper