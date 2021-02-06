import sys
import os

def main():
    print("The system info is given below:")
    print(sys.platform)
    print(os.cpu_count())


if __name__ == '__main__':
    main()
