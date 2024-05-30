## CS32 PSet #1

*NOTE: The ["PSet #1" assignment page on the CS32 Canvas course site](https://canvas.harvard.edu/courses/112459/assignments/638980) states when this assignment is due, what materials you should submit, and how to submit them.*

## ### Big Picture

This assignment has three parts, and you should do all of these parts in Replit. Please use the project titled `pset1` in the CS32 Team under the unit titled "Week 1".

a.   In part (a), you'll print the story we've been reading so that **each line starts with a line number**. It should look as if you read the file into Replit's editor pane. This part builds on the work you did in Chapter 1's exercises.

```
$ python3 pset1a.py
What book would you like to print with line numbers? CatInTheHat.txt
1 The sun did not shine.
2 It was too wet to play.
3 So we sat in the house
4 All that cold, cold wet day.
5 
6 I sat there with Sally.
7 We sat there, we two.
8 And I said, "How I wish
9 We had something to do!"
10 
11 Too wet to go out
```

b.   In part (b), you'll make part (a) look better by **right aligning the printing of the line numbers**. It will now really look as if you read the file into Replit's editor pane.

```
$ python3 pset1b.py
What book would you like to print with line numbers? CatInTheHat.txt
  1 The sun did not shine.
  2 It was too wet to play.
  3 So we sat in the house
  4 All that cold, cold wet day.
  5 
  6 I sat there with Sally.
  7 We sat there, we two.
  8 And I said, "How I wish
  9 We had something to do!"
 10 
 11 Too wet to go out
```

c.   In part (c), you'll build off part (b) to print the story as if it were a deposition, where you count each line but **print the line number on only every fifth line**.

```
$ python3 pset1c.py
What book would you like to print as a deposition? CatInTheHat.txt
    The sun did not shine.
    It was too wet to play.
    So we sat in the house
    All that cold, cold wet day.
  5 
    I sat there with Sally.
    We sat there, we two.
    And I said, "How I wish
    We had something to do!"
 10 
    Too wet to go out
```

As you have undoubtedly noticed, each part of this programming problem set builds on code we wrote earlier. This is not only a step in our problem-solving process, but something that experts do regularly. As you start a problem, look for pieces of code that you've already wrote and which already do a lot of what you need. This will make it easier to start problem solving and provide you with a foundation that you're confident does what you want it to do. Then you can tailor and extend this code so that it solves your new problem. In class, I will often build a new script by starting with an existing script.

## ### Part a

The scripts from class are all great starting points. Take a look at them and decide which will be your starting point. Copy that script into the file named `pset1a.py` in your `pset1` Replit project. Remove the code you don't need and insert some pseudocode for this new problem.

Your **goal** is print a number at the start of each line (including blank lines). Make sure to include a space between the line number and the actual line from the input file. The line numbers should start at 1 and be left-aligned. You can find an example output solution in the `txts` folder.

**Note:** We are not using `main.py` as our main script, and Replit's big green Run button is configured to run that script when you click it. To run the script we're writing (i.e., `pset1a.py`), you can do one of two things:

1.   Run the script directly in the **Shell window**. Click the "Shell" tab in Replit, and type `python3 pset1a.py` at the prompt. This tells the Replit computer on which you are running that you'd like to invoke the Python interpreter (i.e., `python3`) with the input script `pset1a.py`. The difference between the Console window and the Shell window is that the Console is running the interactive Python interpreter, and the Shell is just a part of the machine's operating system waiting for you to tell it what you'd like it to do. Ask a member of the teaching staff if you have questions.

2.   **Reconfigure Replit's big green Run button.** Click the three dots in the Replit's file browser (where we went to upload a file) and select "Show hidden files". This will display a bunch of "Config files" in your file browser. We want the `.replit` file so click it to display it in the Replit's editor window. Now make these two fixes: (a) Find the line that says, `run = "python3 main.py"` and change `main.py` to `pset1a.py`. (b) Find the line that says, `entrypoint = "main.py"` and change `main.py` to `pset1a.py`. Yes, the big green button just does what you can do directly in the Shell window! Click `pset1a.py` in the file browser to move away from the config file and back to your script. You can now use the Run button to execute your script. Again, ask if any of this confuses you.

## ### Part b

Copy your solution to part (a) into the file named `pset1b.py`. We won't be removing code as much as adding additional statements to right-align the line numbers that start each line.

You will continue to leave a space between the line number and the actual line from the input file, but now you'll need to insert spaces before the smaller line numbers. You can find an example output solution in the `txts` folder.

We want our script to work with an input file of **any length**. We can't, therefore, pick a particular number of locations at the start of our printed line to reserve for the line number, because some input file might have more digits in the biggest line number than locations we reserved. And we don't know the maximum number of digits that we'll need until we read the entire file. How will we solve this conundrum? 

Yes! We will look into our **bag of problem-solving templates**. To this point, we have dealt in problems that have required us only to read **once** through our input file. We can solve this problem by reading the input file **twice**: 

1.   On the first pass, we will simply count the number of lines in the input file.
2.   Prior to our second pass, we will use the count from the first pass to compute the maximum number of prepended columns we'll need during the second pass.
3.   On the second pass, we will use this computed value as we format our printed lines.

> In general, this is a useful and common problem-solving approach. You break your problem into multiple phases where the earlier phases compute information that later phases need.

As you solve this part of the pset, you'll not only practice this problem-solving technique, but you should:

*   Open (and close) the input file **twice** using the with-as statement.

*   Figure out how to **compute the number of columns to reserve** at the start of a file line from a count of the total number of lines in the input file. There are many ways to do this, and some are easier than others. We'll accept any method that works.

*   Learn how to format your output using **formatted string literal** (or **f-string**).

**Using Python's f-string**. F-strings are string literals prefixed with `f` or `F`. One of the very useful things you can do with a f-string is have the Python interpreter replace any variable names you have embedded in the string literal with the value of that variable. You do this by surrounding the variable name with curly braces.

For example, here is how you might print a line in part 1 of this pset, given your line number in the variable `line_num` and the read line in `the_line`:

```python
print(f'{line_num} {the_line}', end='')
```

Notice that there is a literal space character between the two substitutions.

F-strings also allow us to specify format information in each variable replacement. To right-align a value, you follow your variable with a `:`, which says what follows is a format specifier, and then the specifier `>`, which says right-align, and finally a number, which is the number of spaces in the field in which you're right-aligning the value.

For example, if we wanted value of `line_num` right-aligned in a field 5-spaces wide, we would write:

```python
print(f'{line_num:>5} {the_line}', end='')
```

If we want the field width to be a variable rather than a constant, we need to wrap this new varaible in curly braces. Perhaps something like this:

```python
print(f'{line_num:>{max_digits}} {the_line}', end='')
```

Ok, you're now ready to solve the problem. Don't forget to reconfigure the big green Run button if you changed it for part (a)!

## ### Part c

Copy your solution to part (b) into the file named `pset1c.py`.

This time we won't be printing every line number, but only every fifth. The line numbers still start at 1, and then we print a line number on the front of line 5, line 10, line 15, etc. Remember that all lines are indented to reserve the space for a line number even if we don't print the line's number. You can find an example output solution in the `txts` folder.

As you solve this part of the pset, you'll learn two new Python operators:

*   The infix modulo operator (`%`) with numbers as its right and left operands. It returns the remainder of dividing the left number by the right.

*   The infix repetition operator (`*`) with a string as its left operand and a number as its right operand. It returns a string that contains the input string repeated the input number of times.

In thinking about how you might use these operators in your solution, first spend some time practicing with them in the interactive Python interpreter.
