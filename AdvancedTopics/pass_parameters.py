import sys

sys.stdout.write("Welcome!")

try:
    if len(sys.argv) > 1:
        sys.argv.remove("pass_parameters.py")
        for arg in sys.argv:
            arg = int(arg)
    else:
        sys.stdout.write("Vazio.")


except Exception as e:
    print(e)

            
