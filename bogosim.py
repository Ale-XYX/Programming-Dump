import random
import time

print('BOGO SORT SIM')

DELAY = input('Seconds of delay: ')
SIZE = input('Amount of entries: ')
ARRAY = []
for i in range(int(SIZE)):
    ARRAY.append(random.randint(0, 100))

IDEAL = sorted(ARRAY)
TIME = 0

print('This process will take anywhere between 0 and ' + str(len(ARRAY) ** len(ARRAY)) + ' seconds.')

while ARRAY != IDEAL:
    random.shuffle(ARRAY)
    print('Trying' + str(ARRAY) + '...', end='', flush=True)

    if ARRAY != IDEAL:
        print('Failed!')
    elif ARRAY == IDEAL:
        print('Success!')

    time.sleep(int(DELAY))
    TIME += int(DELAY)

print('The sort took approxmately ' + str(TIME) + ' seconds.')
