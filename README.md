# Assignment 6: GUI Calculator Using Tkinter
Develop a Python application that:

1. Presents a graphical interface for input and output.

2. Allows users to perform:

   Addition

   Subtraction

   Multiplication

   Division

3. Accepts input via clickable buttons (no keyboard input required).

4. Displays real-time results and clears input when requested.



Solution 
1. Entry Widget

   Displays numbers and results.

   Acts as the calculator’s screen.

2. Buttons

   Digits (0–9): Used for numeric input.

   Operators (+, −, ×, ÷): Trigger arithmetic operations.
 
   Equal (=): Executes the operation and displays the result.

   Clear (C): Clears the screen for a new calculation.

# Functional Workflow

1. Number Input

   Each digit button appends its value to the screen.

2. Operation Selection

   When an operator button is clicked:

   The current number is stored as the first operand.

   The selected operation is remembered.

   The input field is cleared for the next number.

3. Execution

   On pressing =, the program:

   Retrieves the second operand.

   Performs the stored operation.

   Displays the result in the input field.

4. Reset

   Clicking  clears the display and resets stored values.



