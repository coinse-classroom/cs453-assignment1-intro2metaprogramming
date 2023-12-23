## CS453 Assignment 1: Introduction to Metaprogramming

With this assignment, we will learn how to manipulate Python programs programatically (and not by manually editing them). Write a program that accepts another Python program source code, and rewrites it into the same file. The rewriting should include the following:

- Replace all string constants within the given source code with "baba"
- Replace all numeric constants within the given source code with the number 42
- Wrap all Boolean predicates of `if` and `while` statements within the given source code with parentheses and negate them

For example, suppose the following Python code was the input:

```python
if 3 > 5:
  print("Answer to life, universe, and everything is", 0)
```

Then your code should rewrite it as follows:

```python
if not (42 > 42):
	print("baba", 42)
```

Another example. For the following input:

```python
if not len("hello, world!") < 5:
  print("What??")
```

Then after rewriting, it should be:

```python
if not(not len("baba") < 42):
  print("baba")
```

### Skeleton

This repository includes a skeleton code named `rewriter.py` for your rewriting tool. Please keep the existing code and the command line interface provided, so that GitHub Classroom can run the automated grading scripts. The usage is:

```bash
$ python rewriter -t [your target python script file]
```

### Requirements

- Python version >= 3.10

### Reminders

- Make sure your submission is in the main branch.
- Allow enough time to push your changes; do not wait until the last minute.