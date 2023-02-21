## CS453 Assignment 1: Introduction to Metaprogramming

With this assignment, we will learn how to manipulate Python programs programatically (and not by manually editing them). Write a program that accepts another Python program source code, and modifies it. The rewriting should include the following:

- Replace all string constants within the given source code with "baba"
- Replace all numeric constants within the given source code with the number 42
- Negate all Boolean predicates of `if` and `while` statements within the given source code

For example, suppose the following Python code was the input:

```python
if 3 > 5:
  print("Answer to life, universe, and everything is", 0)
```

Then your code should rewrite it as follows:

```python
if not 42 > 42:
	print("baba", 42)
```

### Skeleton

This repository includes a skeleton code named `rewriter.py` for your rewriting tool. Please keep the existing code and the command line interface provided, so that GitHub Classroom can run the automated grading scripts. The usage is:

```bash
$ python rewriter -t [your target python script file]
```

### Libraries

The default Python library contains `ast` module that allows you to manipulate the Abstract Syntax Tree. Since the assignment requires you to write the modified program back to the original file, you will want to dump the modified AST back into Python code. For this, [`astor`](https://pypi.org/project/astor/) can be useful.

### Submission Deadline

You need to submit this assignment before **18:00 on 15 of March, 2023.**

