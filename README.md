# Pytest Suite
This repository is a use case of the pytest testing module. This allows a user to carry out tests on functions before publication, similar to that used by Codewars - creating mock examples to provide a wide range of potential inputs, allowing the user to find and correct issues with specific inputs.
## Description
This is a demonstration of how pytest can be used to pre-empt potential formatting issues with input data, or checking the output of a function against what is expected. In this instance, it is used on scripts from earlier projects, which then allowed the functions to be modified with additional scenarios in mind.

## Technologies used
* Python - Pytest is a python module, and is used on Python scripts. For convenience, I would suggest using this in a virtual environment, as you need to be in the directory of the file you want to test. Using a venv makes this part of the process easier.
## How to use

### Audiobook.py and Weather_noSQL.py
The two files used for testing. Compared to the original files, changes have been made to allow for testing, as pytest requires functions for targeting and testing. In addition, the functions have been edited in response to testing.

### Test_files.py
The file used to test the functions from the audiobook script. It contains the testing operations, as well as the test cases to check against. For instance, the first test checks the function by inputting the sample time (in hours and minutes), then comparing it against what the time should be in the output (in minutes). The first 

### Test_weather.py
The file for testing functions from the weather project, covered in greater detail in that repository. Here, the SQL function has been removed, as it creates an extra layer of bloat that is not needed here. In this file, more advanced utilities for testing are used - the suite is able to generate mock API responses. In this case, it is used to check the original script's ability to deal with a 400 error, meaning the API is not responding. In this case, a function has been added to carry out an initial check of the API, with a provision that if it does not recieve a positive response, it will raise an error. Of note is that while the script will raise the error and halt the runtime, the test will run completely and report a success. The test is not meant to produce a full output, it is there to see how the script handles given inputs. Here, the function accounts for a failed API call, so it is successful.

Using Pytest is odd compared to typical uses of modules, as it is done from the command line. Once downloaded, it is run using the command
```
pytest {filename}.py
```
It will then run the test by carrying out the function with the given sample input. In cases where an input is required from the user during the run, you will need to use
```
pytest -s {filename}.py
```
Thsi will deliver the output of all print statements, as well as allow you to provide inputs mid test, such as using the input() function. Otherwise, the test will fail, as it cannot run without this input.