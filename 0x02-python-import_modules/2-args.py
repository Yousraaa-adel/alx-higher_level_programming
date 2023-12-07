#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    # Getting the number of the argv
    arg_len = len(sys.argv) - 1

    # arguments if plural and argument when more than 1 args
    arg = "argument" if arg_len == 0 or arg_len == 1 else "arguments"

    pun = "." if arg_len == 1 else ":"

    line = "\n" if arg_len >= 1 else ""
        
    # Output for the number of args + argument
    output = "{} {}{}{}".format(arg_len, arg, pun, line)

    # Looping over the list of args to print each arg on a separate line
    for i, argument in enumerate(sys.argv[1:], start=1):
        output += "{}: {}".format(i, argument)
        if i < arg_len:
            output += "\n"

    # Print the final output
    print(output)
