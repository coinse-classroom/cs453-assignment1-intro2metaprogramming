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

def test_types():
    run_rewriter("examples/types.py")
    output = run_target("examples/types.py")
    assert output == "84 baba 42 3.141592653589793 -42 -43\n"