import traceback

# Use o modulo traceback para deixar mais claro o erro mostrado
try:
    raise Exception('bad exception with a stupid message')
except:
    print(traceback.print_exc())
