# Functions
  # What is a function?
    * Code written somewhere other than where it is used
    * Can be in a library
    * Can also be at the top of a program
    * Performs some action
  # Why do we use functions?
    * Can be called many times without re-writing code
    * Makes the main program smaller and easier to read
    * Helps us focus on implementing one task at a time
  # What is the syntax for a function definition?
    * Starts with header:
      * def function_name(parameters):
    * Parameters are separated by commas
    * Function and parameter names are made up when creating function
    * Lines of code inside the function are indented under the header
    * Function must contain at least one line of code
    * Functions are defined at the top of the program
  # How is a function called?
    * Syntax:
    * function_name(arguments)
    * Can be called anywhere in the main program
    * Can be called from inside other functions
    * Number of arguments (given information) must match the number of parameters (asked-for information)
  # What is scope?
    * Area in which a variable can be used
    * Variables created inside a function (including parameters), should not be used in the main program, and vice-versa
    * Variables in a function may have the same name as those in the main program, but they are unrelated
  # How does a function definition end?
    * By default, it ends when the indented code ends
    * Can be ended early with a return statement
    * Syntax:
      * return
    * Works like break for loops
