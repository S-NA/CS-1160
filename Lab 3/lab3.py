# CS 1160 Week 5 Lab Challenge
# @author: Dr. Adam Bryant
# @date: 9-26-2016

import random

print '\n**** CS 1160 Week 5 Lab ****\n'

###################################################
# Run the program and follow the instructions to complete 
#   each of the challenges.
# Change the problem = 0 statement below to move on to the next 
#   problem. 
# Good luck!
###################################################


def start():
    problem = 8
    print_instructions(problem)

###################################################


def problem_0():

    # Change this
    print range(10, 21)

###################################################


def problem_1():

    # change this
    for x in range(10, 52, 2):
        print pow(2, x)

######################################################


def problem_2():

    # change this
    friends = ['Luigi', 'Michael']
    for person in friends:
        print 'My best friend is ' + person + '.'
        print '... wait, no ...'
    print 'I\'m all out of friends. :( '

####################################################


def problem_3():

    friends = ['Luigi', 'Michael']
    for person in friends:
        print pig_latin(person)


# NOTE: don't change this
def pig_latin(text_string):
    '''
  Changes a name into pig-latin.
  '''
    text_string = text_string.lower()
    vowels = ['a', 'e', 'i', 'o', 'u']
    consonant_blends = ['bl', 'br', 'ch', 'ck', 'cl', 'cr', 'dr', 'fl', 'fr',
                        'gh', 'gl', 'gr', 'ng', 'ph', 'pl', 'pr', 'qu', 'sc',
                        'sh', 'sk', 'sl', 'sm', 'sn', 'sp', 'st', 'sw', 'th',
                        'tr', 'tw', 'wh', 'wr']
    if text_string[0] in vowels:
        new_string = text_string + 'ay'  # moves the first vowel
    elif text_string[0] + text_string[1] in consonant_blends:
        new_string = text_string[2:] + text_string[:2] + 'ay'  # moves first two letters
    else:
        new_string = text_string[1:] + text_string[0] + 'ay'  # just add ay if it starts with a vowel
    new_string = new_string.capitalize()  # capitalizes it
    return new_string

####################################################


def problem_4():
    friends = ['Luigi', 'Michael']
    for person in friends:
        print 'My friend ' + person + ' has ' + str(
            random.randint(1, 100)) + ' dollars.'

####################################################


def problem_5():
    # change this
    for i in range(15):
        var = ''
        if i % 2 == 0:
            var = "fizz"
        if i % 5 == 0:
            var += "buzz"
        print str(i) + ' ' + var

####################################################


def problem_6():

    # change this
    x = 0
    y = 10
    while x < 10:
        while y > -1:
            print 'x is ' + str(x) + ";" + 'y is ' + str(y)
            x += 1
            y -= 1

####################################################


def problem_7():
    raw_input("Press any key...")
    # change this
    x = 0

    while x < 100:
        print 'x = ' + str(x) + '. It shouldn\'t still be the same number.'
        x += 1
    while x < 150:
        print 'This is always an infinte loop'
        print 'That is a lie.'
        x += 1
    while x != 100:
        print 'This is too.'
        x -= 1

####################################################


def problem_8():

    # change this
    for x in range(2):
        for y in range(2):
            for z in range(2):
                for o in range(2):
                    print str(x) + ' ' + str(y) + ' ' + str(z) + ' ' + str(o)

####################################################


def problem_9():

    # change this
    variables = [12, 32.475, True, "Words", 'c', pig_latin]
    i = 0
    for item in variables:
        print str(i) + ': '
        print 'name: ' + str(item)
        print 'type: ' + str(type(item))
        print dir(item)
        print 'Methods:'
        for entry in dir(item):
            print '    ' + entry
        print '\n\n'
        i += 1

##############################################################
##############################################################

text = [['The range() Function',
         'Uses the range(end) function to get a list of numbers.',
         ['Go to the function called problem_0()',
          'Change the code to print out a list of numbers between 10 and 20',
          'Make the list include both 10 and 20',
          'When you are done, change line 20 to problem = 1 ']],
        ['For Loop With the range() Function',
         'Creating a for loop from 0 to n using range(n)',
         ['Go to the function called problem_1()',
          'Make the for loop iterate through all the even numbers between\n'
          '    10 and 50 (including both numbers) \n'
          '    **** HINT **** : Use range(start, stop, step)',
          'Change the code so it prints the number that is 2 to the \n'
          '    power of x (instead of just x)',
          'When you are done, change line 20 to problem = 2 ']],
        ['For Loop Over a List',
         'Making a for loop over a list that prints the elements. \n'
         '    NOTE: The variable named person after for can be named\n'
         '    whatever you want.',
         ['Go to the function called problem_2()',
          'Change the entries in the list called "friends" so it has\n'
          '    the names of the people sitting at your table.',
          'Change the variable "yoyo" to be named "person"',
          'When you are done, change line 20 to problem = 3 ']
 ], ['For Loop with Functions', 'Making a for loop that calls a function',
     ['Go to the function called problem_3()', 'Copy the list from problem 2 '
      'Make a for loop that calls the pig_latin() function for each\n'
      '    of the people in the list you defined before.\n'
      '    NOTE: there should only be one call made to the \n'
      '    pig_latin() function.',
      'When you are done, change line 20 to problem = 4']
 ], ['For Loops with Counters',
     'Setting a counter (or index) variable before the loop and use\n'
     '   it to number the items in the list',
     ['Go to the function called problem_4()',
      'Import the "random" module and call random.randint(start, end)',
      'Change the code so it prints a random number for each person',
      'When you are done, change line 20 to problem = 5  ']],
        ['Loop Conditions (Fizz Buzz)',
         'Using a condition in a loop (fizz buzz)',
         ['Go to the function called problem_5()',
          'Change the code so it prints the number of i, \n'
          '    then fizz if the number is even, buzz if the number is a\n'
          '    multiple of 5, and fizzbuzz if it is both.\n'
          '    NOTE: Some hiring managers find this to be an effective job\n'
          '    interview question because a lot of candidates who claim \n'
          '    programming skills cannot do this. I have seen this myself!',
          'When you are done, change line 20 to problem = 6  ']],
        ['"While" Loops and Increment / Decrement Operators',
         'Using x = x + 1 to increment a variable (adds 1) and y -= 1 \n'
         '    to decrement it (subtracts 1)',
         ['Go to the function called problem_6()',
          'Change x = x + 1 to x += 1 to increment the x variable',
          'Change y = y - 1 to y -= 1 to decrement the y variable',
          'Put both print statements on the same line like: x is 3; y is 7',
          'When you are done, change line 20 to problem = 7 ']
 ], ['Avoiding Infinite Loops',
     '*** WARNING *** : When you run the following code\n'
     'it will continue forever, since it has an infinite \n'
     'loop built into it. Press ctrl+C to stop the program.',
     ['Go to the function called problem_7()',
      'Change the conditions in each while loop (like adding an increment or \n'
      '    decrement statement or changing a variable) to make the loop\n'
      '    so it does not just continue indefinitely (i.e., terminate the loop)',
      'When you are done, change line 20 to problem = 8  ']
 ], ['Debugging with Print Statements',
     'Using print statements with variable numbers in them to debug a while loop',
     ['Go to the function called problem_8()',
      '  Change the code so it counts out all combinations of a four-digit binary number:\n'
      '    (i.e., 0000, 0001, 0010, 0011, ... all the way to 1111).',
      'When you are done, show the results to your TA. Congratulations! ']]]


def print_instructions(num):
    print str.format('\nProblem {}: {}\n* {}', num, text[num][0], text[num][1])
    print '\n\nTasks:'
    for i, item in enumerate(text[num][2]):
        print 2 * ' ' + str(i) + ': ' + item
    print '\nOutput:\n'
    problems = [problem_0, problem_1, problem_2, problem_3, problem_4,
                problem_5, problem_6, problem_7, problem_8]
    problems[num]()


def merp():
    while True:
        choice = raw_input("Which problem?")
        if choice is 'q' or choice is 'Q':
            quit()
        try:
            print_instructions(int(choice))
        except:
            pass


if __name__ == '__main__':
    import sys
    if sys.argv[1] is 'merp':
        merp()
    else:
        start()
