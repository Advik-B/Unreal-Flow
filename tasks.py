from invoke import task
import os

def is_windows():
    return os.name == 'nt'

PYTHON = 'python'
PIP = 'pip'
PYTHON += '.exe' if is_windows() else '3'
PIP += '.exe' if is_windows() else PYTHON+' -m pip'


@task
def check_compiler(c):
    PATH = os.environ['PATH']
    PROTOC = 'protoc'
    if is_windows():
        PROTOC += '.exe'
    for path in PATH.split(os.pathsep):
        if os.path.exists(os.path.join(path, PROTOC)):
            return
    raise RuntimeError("protoc not found")


@task
def proto(c):
    check_compiler(c)
    c.run("protoc proto/*.proto --python_out=src/")

@task
def requirements(c):
    c.run(PIP + " install -r requirements.txt")
