import os

with open("output.log", "w") as f:
    pass


def run_return_py(cmd):
    os.system(f"python -u {cmd} > output.log")
    with open("output.log", "r") as f:
        out = f.read()
    return out

def run_return_node(cmd):
    os.system(f"node {cmd} > output.log")
    with open("output.log", "r") as f:
        out = f.read()
    return out