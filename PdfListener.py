import sys
import os
import time

srcpath = "data/"
trash = "trash/"

def spinloop(dstpath):
    while True:
        for f in os.listdir(srcpath):
            print(f)
        time.sleep(5)

def setup():
    directory = os.path.dirname(srcpath)
    if not os.path.exists(directory):
        os.makedirs(directory)

def main():
    if len(sys.argv) != 2:
        print("Usage: python PdfListener.py <dst path>")
        exit()

    setup()

    #make sure folder to listen from exists
    dstloc = sys.argv[1]
    print(dstloc)

    spinloop(dstloc)


if __name__ == "__main__":
    main()
