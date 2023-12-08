#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    if sys.argv == 1:
        print("0")
    # Excluding the fille name
    args = sys.argv[1:]
    # map iterates over the args and float turning them 
    # into float numbers and then sum adds them
    result = sum(map(float, args))
    # Reternning the numbers to integers
    result = int(result)
    # Final output print
    print("{}".format(result))
