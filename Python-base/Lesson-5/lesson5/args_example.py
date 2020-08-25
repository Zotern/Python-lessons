import sys


def ping():
    print("pong")


def sum_int(*args):
    print(sum(map(int, args)))


commands = {
    "ping": ping,
    "sum": sum_int,
}


if __name__ == '__main__':
    if len(sys.argv) < 2 or sys.argv[1] not in commands:
        print("usage: {} - {} [args]".format(
            sys.argv[0], '|'.join(commands)))
        exit(1)

    commands[sys.argv[1]](*sys.argv[2:])

# argparse

# import traceback
# import inspect
