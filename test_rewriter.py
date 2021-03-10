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

def test_baba():
    run_rewriter("examples/baba.py")
    output = run_target("examples/baba.py")
    assert output == "baba 42\n"

def test_addition():
    run_rewriter("examples/addition.py")
    output = run_target("examples/addition.py")
    assert int(output) == 84

def test_strings():
    run_rewriter("examples/strings.py")
    output = run_target("examples/strings.py")
    assert output == "babababababababababa\n"