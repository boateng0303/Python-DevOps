import sys
import os
import time

# stop, stop, restart


# args = sys.argv
# print(args)

time.sleep(4)
def validity_check():
    if len(sys.argv) < 2 or sys.argv[1] not in ('stop', 'start', 'restart'):
        print("Please provide a valid choice: ('stop, start, restart)")


def start_d():
    os.system('systemctl start httpd')

def stop_d():
    os.system('systemctl stop httpd')

def restart_d():
    os.system('systemctl restart httpd')

# def main():
#     validity_check()
#     if sys.argv[1] == 'stop':
#         stop_d()
#     elif sys.argv[1] == 'start':      You can do this but after using the main function you have to call main() after the contructor or use the the alternative after the constructor
#         start_d()
#     else:
#         restart_d()


if __name__== '__main__':
    validity_check()
    if sys.argv[1] == 'stop':
        stop_d()
    elif sys.argv[1] == 'start':
        start_d()
    else:
        restart_d()


