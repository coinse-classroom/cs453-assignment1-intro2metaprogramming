import ast
import sys
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Rewrites programs.')
    parser.add_argument('-t', '--target', required=True)
    parser.add_argument("remaining", nargs="*")
    args = parser.parse_args()

    target = args.target
    sys.argv[1:] = args.remaining

    code = "".join(open(target, "r").readlines())
    root = ast.parse(code)

    # implement rewriting routines here
    # make modifications to the AST

    modified = ast.unparse(root)
    with open(target, "w") as f:
        f.write(modified)
        f.close()