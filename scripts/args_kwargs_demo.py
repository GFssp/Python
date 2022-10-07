def print_name(name):
    print(name)

print_name('Alex')


def function(a, b, *args, **kwars):
    print(a, b)
    for arg in args:
        print(arg)
    for key in kwars:
        print(key, kwarg[key])

function(1, 2, 3, 4, 5, six=6, seven=7)