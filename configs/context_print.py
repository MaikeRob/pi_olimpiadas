#Toda vez que a função print é chamada, imprime quem a chamou 
import builtins
import inspect

original_print = print

def printWithContext(*args, **kwargs):
  caller_frame = inspect.stack()[1] #Ultima função? da pilha - função atual
  caller_module = inspect.getmodule(caller_frame[0]) 
  caller_function = caller_frame.function 
  #caller_filename = caller_module.__file__ 

  original_print(f"\033[34m[\033[0m{caller_module}\033[34m]\033[0m\n\033[1;32m{caller_function}\033[0m:",*args,**kwargs)

builtins.print = printWithContext



