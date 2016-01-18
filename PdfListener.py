import sys
import os
import time

srcpath = "data/"
trash = "trash/"

def spinloop(dstpath):
    while True:
        for f in os.listdir(srcpath): #for each file in folder
            s = os.path.join(srcpath, f)
            if f.endswith(".pdf"): #move to designated folder
                d = os.path.join(dstpath, f)
                os.rename(s, d)
            else:                  #move to trash folder
                d = os.path.join(trash, f)
                os.rename(s, d)
        time.sleep(5)

def setup(dstpath):
    #make sure src exists
    directory = os.path.dirname(srcpath)
    if not os.path.exists(directory):
        os.makedirs(directory)

    #make sure dst exists
    directory = os.path.dirname(dstpath)
    if not os.path.exists(directory):
        os.makedirs(directory)

def main():
    if len(sys.argv) != 2:
        print("Usage: python PdfListener.py <dst path>")
        exit()


    #make sure folder to listen from exists
    dstloc = sys.argv[1]
    if not dstloc.endswith("/"):
        dstloc = dstloc + "/"
    setup(dstloc)

    spinloop(dstloc)


if __name__ == "__main__":
    main()
