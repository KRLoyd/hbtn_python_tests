# hbtn_python_tests
Test-driven development (TDD)

## Description
This repository is for sf-jan17 Holberton Students to collaborate on what Tests
Cases must be tested for our python codes.

* Each directory name matches a Holberton project name.
* Each directory holds files that match file names for the particular project.
* Each file lists tests to pass for the task.

### Please Note
This repository is not for code, it is for listing test cases and their
parameters only.

## Style

### doctest

These files have 2 sections: __Holberton Cases__ and __Test Present Cases__.

* __Holberton Cases__: refers to the inputs that your python function, in your
python `.py` file, should handle as input arguments.

```
# <case to check> (i.e. arg1 arg2)
```

* __Test Present Cases__: refers to the test that you should have, in your
testing file `.txt`, that includes a line for the expected output.  __NOTE:__
all of the above Holberton Cases should be tested plus additional cases to check
how your code handles errors.

```
# <a test case to check>
<YOUR_FUNCTION>(arg1, arg2)
```

### unittest

* __Test Present Cases__: refers to the test that you should have, in your test
`.py`, file that includes a line for the expected output

```
# <case to check>
<YOUR_FUNCTION>(arg1, arg2)
```

## Usage
Read your tasks' corresponding file and ensure your code has a test for each
case.

If you need an example of `doctest()` format, please reference the `example.txt`
file at the root of this repository.
```
#doctest
$ python3 -m doctest -v ./tests/[YOUR-TEST_FILE.txt]

#unittest
$ python3 -m unittest -v ./tests/[YOUR-TEST_FILE.py]
```