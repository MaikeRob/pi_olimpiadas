#Toda vez que a função print é chamada, imprime quem a chamou 
import builtins
import inspect
from colorama import init, Fore

# Inicializa colorama
init()

original_print = print

def printWithContext(*args, **kwargs):
    caller_frame = inspect.stack()[1] 
    caller_module = inspect.getmodule(caller_frame[0]) 
    caller_function = caller_frame.function 

    original_print(f"{Fore.BLUE}[{caller_module.__name__}]{Fore.RESET}\n{Fore.GREEN}{caller_function}:{Fore.RESET}", *args, **kwargs)

builtins.print = printWithContext
