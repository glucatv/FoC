# Fundamentals of Computing

## Syllabus

Introduction to computational method. Von Neumann architecture. Programming languages: assembler, compiled, and interpreted languages. Basic concepts of programming languages: variables; data types and assignment; control structures (loops, conditional selection); basic data structures; input and output. Functions and recursion. Searching and sorting algorithms. Computational complexity. Dynamic data structures: array; linked lists; trees; hash tables. Object oriented programming.

The programming languages taught are Python and C.

## Reference Texts

- Downey, A. B. (2015). Think Python: How to Think Like a Computer Scientist. O'Reilly Media
- Guttag, J. V. (2013). Introduction to Computation and Programming Using Python: With Application to Understanding Data. MIT Press.
- Kernighan, B. W., & Ritchie, D. M. (1988). The C Programming Language (2nd ed.). Prentice Hall.

## Class schedule

Wednesday and Friday from 4:00 PM to 6:15 PM on the [Teams platform](https://teams.microsoft.com/l/team/19%3AYcNOCv_8DjwXCYEoufVGMeB4wf_3kBHSLpGidR3SD_E1%40thread.tacv2/conversations?groupId=09b56678-d778-4096-85ac-0bf85c46cad9&tenantId=24c5be2a-d764-40c5-9975-82d08ae47d0e).

## Exam format

- Written part
  - Multiple choice text (T) on MS Forms platform
    - Success 6-10
  - Coding part (C) on your own PC
    - Only for those that have passed the test
    - In the same day of the test
    - Success 12-20  
  - Written grade = (T)+(C)
- Oral part
  - Optional
  - Only for those that have passed the written part (grade >= 18)
  - In the same session of the written part
  - The final grade can be modified both positively and negatively

## Office hours

 On Microsoft Teams, email me to arrange one.

## Next exams: autumn session
- 1st session
    - Written: 02/09/2024 at 14:00, classroom B3
    - Oral:  06/09/2024 at 9:00, on Teams
- 2nd session
    - Written: 16/09/2024 at 14:00, classroom B3
    - Oral: 20/09/2024 at 15:00, on Teams

Registration on Delphi will open one week before the written test.

## Class diary

### Week 1 (mar/13 and mar/15)

- Introduction to the course.
- The computational method: problem, model, algorithm, program. Examples: Guarini puzzle.
- The computational method applied to the square root problem.
- What is an algorithm.
- Algorithms and programs
- Von Neuman architecture
- Binary encoding of data and computer instruction
- High level programming languages.
- The limits of computational method: efficiency and incompleteness
- From algorithm to programs.
- Using the [Python](https://www.python.org) programming language tools: [Anaconda](https://www.anaconda.com/) and  [Spyder](https://www.spyder-ide.org/).
- Design the first program by using Spyder, the square root of a positive number  and the conversion between decimal to binary sistem.

#### Course material
- [about.pdf](00-about.pdf)
- [intro.pdf](01-intro.pdf)
- [week_01.py](week_01.py)

### Week 2 (mar/20 and mar/22)

- A first look to the components of a programming language: data (floating point, integer and boolean); variables; the assignment operator; arithmetic, relational and logical operators; output; control of flow with while; blocks of code; comments.
- The string data type: assignment, relational operators, concatenation, repetition, indexing. The `len()` function.
- the `for` statement;
- The `if`...`elif`...`else`  statement and other  variants;  the `for` statements and the `range` function;
- The `enumerate` function
- The `in` statement;
- Type conversion: the functions `int()` and `float()`
- The function `input()`
- The `break` statement
- The `ord()` and `chr()` funcionts
- The slicing operator over strings

#### Course material
- [week_02](week_02.ipynb)

### Week 3 (mar/27)

- Functions: optional arguments and parameters with default values; passing arguments by position or by name.
- Stack frames, function environment, local variables and formal parameters, global variables.
- The `None` type and value.
- Functions that return more values: introduction to the tuple data type.

#### Course material
- [week_03](week_03.ipynb)

### Week 4 (apr/03 lab and apr/05)

- The tuple data type and its properties: indexing, slicing, concatenation, repetition, the len function, the  `in` statement, functions that return tuples.
- The  max and min functions; customizing the objective function with the  key  parameter.
- Functions as parameter of functions.

#### Course material
- [week_04](week_04.ipynb)

### Week 5 (apr/10 and apr/12 lab)

- Negative indexes and slicing with steps: reversig a string
- Packing and unpacking
- The `str` function
- The list data structure: indexing, slicing, concatenation, repetition, packing and unpacking operations, the len() function and mutable operations like item assignment, insertion and deletion; the `append` method.
- Aliasing and clonig

#### Course material
- [week_05](week_05.ipynb)

### Week 6 (apr/17 and apr/19)

- Aliasing and cloning of lists; lists as input of functions
- Recursive functions
- Deep cloning
- List comprehension
- Recursive generation of all binary strings of a given length
- Local functions (a function defined in the block of another function)
- Bubble-sort algorithm

#### Course material
- [week_06](week_06.ipynb)

### Week 7 (apr/24 and apr/26)

- Customizing sorting criteria
- Comparing and sorting non-scalar types
- Sorting according multiple criteria
- `lambda` functions
- Introduction to computational complexity: time complexity; worst case complexity and big-O notation
- Time complexity of the bubble-sort algorithm
- Time complexity of Python operators on non-scalar types
- Introduction to the binary search algorithm

#### Course material
- [week_07](week_07.ipynb)

### Week 8 (may/3 lab)

### Week 9 (may/08 lab and may/10)

- Time complexity of the binary search algorithm
- Space complexity
- Computing the intersection with and without sorting
- The `sort` method and the `sorted()` function

#### Course material
- [week_09](week_09.ipynb)

### Week 10 (may/15 and may 17)

- The dictionary data structure: definitions; operations; methods and computational complexity.
- Using dictionaries to improve the time complexity  of the operations on sets.
- The `extend` methods for lists
- The merge-sort algorithm: description; implementation, analysis and computational complexity.

#### Course material
- [week_10](week_10.ipynb)

### Week 11 (may/28, may/29 and may/30 lab)

- Interpreted and compiled languages. Introduction to the C language. Differences with Python.
- The Linux command line interface and how to install Linux using the Windows Subsystem for Linux
- Some usefull Linux Command
- How to use the `gcc` compiler: the first `C` program
- Variables, types and assignment

#### Course material
- [week_11](https://github.com/glucatv/FoC/blob/main/C/01-first_program.c)

### Week 12 (june/4, june/5 and june/7)

- Arrays and pointers
- Dynamic arrays: how to implement in C the Python list
- Characters and strings

### Curse material
 - [week_12](week_12.md)
