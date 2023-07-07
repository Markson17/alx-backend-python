# Variable Annotations

This repository contains Python scripts that demonstrate variable annotations and type hints. Each script corresponds to a specific task and includes a type-annotated function or variable declarations.

## Files

### 0-add.py
This script defines a function `add` that takes two float arguments, `a` and `b`, and returns their sum as a float.

### 1-concat.py
This script defines a function `concat` that takes two string arguments, `str1` and `str2`, and returns their concatenation as a string.

### 2-floor.py
This script defines a function `floor` that takes a float argument `n` and returns its floor value as an integer.

### 3-to_str.py
This script defines a function `to_str` that takes a float argument `n` and returns its string representation.

### 4-define_variables.py
This script defines and annotates four variables with the following values:
- `a`: an integer with a value of 1
- `pi`: a float with a value of 3.14
- `i_understand_annotations`: a boolean with a value of True
- `school`: a string with a value of "Holberton"

### 5-sum_list.py
This script defines a function `sum_list` that takes a list of floats, `input_list`, as an argument and returns their sum as a float.

### 6-sum_mixed_list.py
This script defines a function `sum_mixed_list` that takes a list of integers and floats, `mxd_lst`, as an argument and returns their sum as a float.

### 7-to_kv.py
This script defines a function `to_kv` that takes a string `k` and an integer or float `v` as arguments and returns a tuple. The first element of the tuple is the string `k`, and the second element is the square of the `v` value, annotated as a float.

### 8-make_multiplier.py
This script defines a function `make_multiplier` that takes a float `multiplier` as an argument and returns a function that multiplies a float by the `multiplier` value.

### 9-element_length.py
This script defines a function `element_length` that takes an iterable object `lst` as an argument and returns a list of tuples. Each tuple contains an element from `lst` and its corresponding length.

## Usage

To test the scripts, you can execute the corresponding main files. For example, to test the first task:

```
$ ./0-main.py
```

This will run the `0-main.py` script, which imports and tests the `add` function from `0-add.py`. It will print whether the function produces the expected result and display the function's type annotations.

Feel free to explore other main files for different tasks and check the results and type annotations.

Note: It's assumed that Python 3 is installed on your system.