#!/usr/bin/python3
def main():
    char = input("Character: ")
    result = islower(char)
    print(result)

def islower(c):
    for i in range(ord("a"), ord("z") + 1):
        if c == chr(i):
            return True
    return False

main()