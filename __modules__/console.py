import os

with open("output.txt", "w") as f:
    pass


def run_return(cmd):
    os.system(f"python -u {cmd} > output.txt")
    with open("output.txt", "r") as f:
        out = f.read()
    return out