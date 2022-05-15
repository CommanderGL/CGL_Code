import os

with open("output.txt", "w") as f:
    pass


def run_return_py(cmd):
    os.system(f"python -u {cmd} > output.txt")
    with open("output.txt", "r") as f:
        out = f.read()
    return out

def run_return_node(cmd):
    os.system(f"node {cmd} > output.txt")
    with open("output.txt", "r") as f:
        out = f.read()
    return out