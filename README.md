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
These files have 2 sections: __Holberton Cases__ and __Test Present Cases__.
* __Holberton Cases__: refers to the inputs that your python function should
handle
```
# <case to check>
```
* __Test Present Cases__: refers to the test that you should have with a line
for the expected output
```
# <a test case to check>
<YOUR_FUNCTION>(arg1, arg2)
```

## Usage
Read your tasks' corresponding file and ensure your code has a test for each
case.

If you need an example of `doctest()` format, please reference the `example.txt`
file at the root of this repository.
```
$ python3 -m doctest -v ./tests/[YOUR-TEST_FILE.txt]
```