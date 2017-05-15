# hbtn_python_tests

## Description
This repository is for sf-jan17 Holberton Students to collaborate on what Tests Cases must be tested for our python codes. 

* Each directory name matches a Holberton project name. 
* Each directory holds files that match file names for the particular project. 
* Each file lists tests to pass for the task. 

### Please Note
This repository is not for code, it is for listing test cases and their parameters only. 

## Style
Each case will have the following format:
```
# <case to check>
<function>(agr1, arg2)
```

## Usage
Read your tasks' corresponding file and ensure your code has a test for each case. 

If you need an example of `doctest()` format, please reference the `example.txt` file at the root of this repository.
```
$ python3 -m doctest -v ./tests/[YOUR-TEST_FILE.txt]
```