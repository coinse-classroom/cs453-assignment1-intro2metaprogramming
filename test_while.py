import os.path
import subprocess

def run_rewriter(target):
    cmd = ["python3", "rewriter.py", "-t", target]
    ret = subprocess.run(cmd, stdout=subprocess.PIPE, encoding='UTF-8')
    return ret.stdout

def run_target(target):
    cmd = ["python3", target]
    ret = subprocess.run(cmd, stdout=subprocess.PIPE, encoding='UTF-8')
    return ret.stdout

def test_if():
    run_rewriter("examples/while.py")
    output = run_target("examples/while.py")
    assert output == "baba\n"