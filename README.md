# CSC 510: Software Engineering Homework1

![GitHub](https://img.shields.io/badge/Language-Python-blue.svg)
![Linux](https://img.shields.io/badge/Linux-FCC624?style=flat&logo=linux&logoColor=black) 
![MIT License](https://img.shields.io/badge/License-MIT-red.svg) 
![GitHub repo size](https://img.shields.io/github/repo-size/CSC510-SE-HW1/hw1) 
[![Workflow](https://github.com/CSC510-SE-HW1/hw1/actions/workflows/main.yml/badge.svg)](https://github.com/CSC510-SE-HW1/hw1/actions/workflows/main.yml)
![GitHub Pull Requests](https://img.shields.io/github/issues-pr/CSC510-SE-HW1/hw1) 
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/CSC510-SE-HW1/hw1) 
![GitHub contributors](https://img.shields.io/github/contributors/CSC510-SE-HW1/hw1) 
![GitHub forks](https://img.shields.io/github/forks/CSC510-SE-HW1/hw1)
[![codecov](https://codecov.io/gh/CSC510-SE-HW1/hw1/main/graph/badge.svg?token=7c2010bd-8209-40a7-a233-16c2d19990e2)](https://codecov.io/gh/CSC510-SE-HW1/hw1)
![Closed issues](https://img.shields.io/github/issues-closed-raw/CSC510-SE-HW1/hw1?color=bright-green)
![Open issues](https://img.shields.io/github/issues-raw/CSC510-SE-HW1/hw1)
[![Commit Acitivity](https://img.shields.io/github/commit-activity/m/CSC510-SE-HW1/hw1)](https://github.com/CSC510-SE-HW1/hw1)


This repository represents how to have a clean and readable showcase of your work, which is understandable at a glance. All the badges show the essential information about the repository, such as the languages used in it, the code coverage considering the test files, and other info that gives other programmers an idea and understanding of the project by looking through the README!

There is also the workflow, which runs the test files after each commit and checks the code, showing how comprehensive the test cases are and whether they are passing or not after each change, checking the compatibility of the changes with the available code, which helps maintain the repository.


### Files:

1. **`.github/workflows/main.yml`**
   - The `main.yml` file in this repository triggers on push and pull requests, setting up Python 3.x, running tests with `pytest`, generating a coverage report, and uploading it to Codecov for the `hw1` project.

2. **`LICENSE`**
   - This MIT License allows users to freely use, modify, and distribute the `CSC510-SE-HW1` software, provided they include the original copyright notice. 

3. **`README.md`**
   - This file provides an overview of the project. It includes badges that display the build status, license, and code coverage.

4. **`myfileSravya.py`**
   - This Python file defines four basic arithmetic functions: `add` for addition, `subtract` for subtraction, `multiplication` for multiplication, and `divide` for division. Each function takes two arguments and returns the result of the respective operation. 

5. **`myfile_Melika.py`**
   - This Python file defines four functions: `hello(name)` returns a greeting, `age(year, date)` calculates age based on the current year, `count(n)` computes the sum of integers from 1 to n-1, and `square(n)` returns the square of a number.

6. **`test_fileMelika.py`**
   - This test file uses `pytest` to verify the functionality of four functions (`hello`, `age`, `count`, `square`) from `myfile_Melika.py`, with the last two tests currently set up to fail, indicating there may be issues with the `count` and `square` functions.

7. **`test_fileSravya.py`**
   - This test file for `myfileSravya.py` uses `pytest` to verify the correctness of basic arithmetic operations, such as addition and subtraction, while deliberately expecting incorrect results for multiplication and division to demonstrate test failures.