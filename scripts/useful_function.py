import time


def useful_function():
    for i in range(5):
        print(f'I am a useful function I swear {i}')
        time.sleep(1)

# What NOT to do
# useful_function()


# What TO DO
if __name__ == '__main__':
    useful_function()
