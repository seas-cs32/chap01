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

## ### Part 1

The scripts we built in class and section are all great starting points for this new script. Take a look at them and decide which one will be your starting point. Copy that script into the file named `pset1a.py` in your `pset1` Replit project. Remove the code you don't need and insert some pseudocode for this new problem.

Your **goal** is print a number at the start of each line (including blank lines). Make sure to include a space between the line number and the actual line from the input file. The line numbers should start at 1 and be left-aligned. You can find an example output solution in the `txts` folder.

**Note:** We are not using `main.py` as our main script, and Replit's big green Run button is configured to run that script when you click it. To run the script we're writing (i.e., `pset1a.py`), you can do one of two things:

1.   Run the script directly in the **Shell window**. Click the "Shell" tab in Replit, and type `python3 pset1a.py` at the prompt. This tells Replit computer on which you are running that you'd like to invoke the Python interpreter (i.e., `python3`) with the input script `pset1a.py`. The difference between the Console window and the Shell window is that the Console is running the interactive Python interpreter, and the Shell is just a part of the machine's operating system waiting for you to tell it what you'd like it to do. Ask a member of the teaching staff if you have questions.

2.   **Reconfigure Replit's big green Run button.** Click the three dots in the Replit's file browser (where we went to upload a file) and select "Show hidden files". This will display a bunch of "Config files" in your file browser. We want the `.replit` file so click it to display it in the Replit's editor window. Now make these two fixes: (a) Find the line that says, `run = "python3 main.py"` and change `main.py` to `pset1a.py`. (b) Find the line that says, `entrypoint = "main.py"` and change `main.py` to `pset1a.py`. Yes, the big green button just does what you can do directly in the Shell window! Click `pset1a.py` in the file browser to move away from the config file and back to your script. You can now use the Run button to execute your script. Again, ask if any of this confuses you.

## ### Part 2

Start with your solution to part 1. Copy that script into the file named `pset1b.py`. We won't be removing code as much as adding additional statements to right-align the line numbers that start each line.

You will continue to leave a space between the line number and the actual line from the input file, but now you'll need to insert spaces before the smaller line numbers. You can find an example output solution in the `txts` folder.

We want our script to work with an input file of **any length**. We can't, therefore, pick a particular number of locations at the start of our printed line to reserve for the line number, because some input file might have more digits in the biggest line number than locations we reserved. And we don't know the maximum number of digits that we'll need to print our line numbers until we read the entire file. How will we solve this conundrum? 

Yes! We will look into our **bag of problem-solving templates**. To this point, we have dealt in problems that have only required us to read **once** through our input file. We can solve this problem by reading the input file **twice**: 

1.   On the first pass, we will simply count the number of lines in the input file.
2.   Prior to our second pass, we will use the information from the first pass to determine the maximum number of line-number digits we'll need during the second pass.
3.   On the second pass, we will use computed value as we format our printed lines.

> In general, this is a useful and common problem-solving approach. You can break your problem into multiple phases where the earlier phases compute information that later phases need.

As you solve this part of the pset, you'll not only practice this problem-solving technique, but you'll need to:

(1) Open the input file twice using the with-as statement.

(2) Develop your own while-loop to figure out how to convert the total number of lines in the input file into a maximum number of digits needed for printing the line numbers. Figure out what the logic looks like, and then try writing your while-loop with the looping condition in the while-loop itself, like this:

```python
# initialize a variable v that gets updated in the loop
while condition_using_v_and_info_from_earlier_computations:
    # loop work that eventually updates v
```

If you've done some work in Python previously and know about functions in the `math` library that can help you perform this calculation without a while-loop, please don't. You should use a while-loop and **only use Python's builtin functions and operators** in this part.

(3) Learn about some of the formatting you can do with the `print` statement. In particular, please use Python's **formatted string literal** (or **f-string**). F-strings are string literals prefixed with `f` or `F`. This prefix tells the Python interpreter that you might have embedded a variable in the literal that you'd like it to replace with the value of that variable. You write such a replacement as the variable surrounded by curly braces.

For example, here is how you might print a line in part 1 of this pset, given your line number in the variable `line_num` and the read line in `the_line`:

```python
print(f'{line_num} {the_line}', end='')
```

Notice that there is a literal space character between the two substitutions.

F-strings allow us to specify format information in our variable replacements. In particular, to right-align a value, you follow your variable with a `:`, which says what follows is a format specifier, and then the specifier `>`, which says right-align, and finally a number, which is the number of spaces in the field in which you're right-aligning the value.

For example, if we wanted value of `line_num` right-aligned in a field 5-spaces wide, we would write:

```python
print(f'{line_num:>5} {the_line}', end='')
```

If we want the field width to be a variable itself, instead of a fixed value, we need to wrap this new varaible in curly braces too. Perhaps something like this:

```python
print(f'{line_num:>{max_digits}} {the_line}', end='')
```

Ok, with this information, you're ready to start thinking about how you'll solve the problem. Don't forget to reconfigure the big green Run button if you changed it for part (a)!

## ### Part 3

Start with your solution to part 2. Copy that script into the file named `pset1c.py`. This time we need different functionality out of our last while-loop. We won't be printing every line number, but only every fifth. The line numbers still start at 1, and then we print a line number on the front of line 5, line 10, line 15, etc. Remember that all lines are indented to reserve the space for a line number even if we don't print the line's number. You can find an example output solution in the `txts` folder.

As you solve this part of the pset, you'll learn two new Python operators:

*   The infix modulo operator (`%`) with numbers as its right and left operands. It returns the remainder of dividing the left number by the right.

*   The infix repetition operator (`*`) with a string as its left operand and a number as its right operand. It returns a string that contains the input string repeated the input number of times.

Think about how you might use these operators in solving this part of the problem. Feel free to practice with these operators in the interactive Python interpreter.
