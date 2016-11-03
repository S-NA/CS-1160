'''
Information about different string methods can be found at:
https://docs.python.org/2/library/stdtypes.html#string-methods
'''

## Prompt the user for input and set equal to the variable str_a
str_a = raw_input("Enter your input: ")

## Test to make sure the user inputted an alpha-numeric string, quit() if they did not
if (str_a.isalnum()):
  print "Alpha-numeric input."
else:
  print "Non-alpha-numeric input."

## Find out how many characters are in the string (its count) and print it to console
numberOfElems = len(str_a)
print numberOfElems

## Print whether or not the string contains the character 'y'
# for elem in str_a:
#   if elem == 'y':
#     print "Your string contains a y."
#     break

## Alternative mehod:
if 'y' in str_a:
    print "Your string contains a y."

## Find and print to console the 6th character in the string (try...except with quit())
try:
  print str_a[5]
except:
  quit()

## Print the string back to the user, but in all uppercase
print str_a.upper()

####################################################################################################
## Methods on hard coded strings:
####################################################################################################

####
str_b = '    Python     '
## *Strip* all the whitespace in str_b, print to console with a '.' at the end
print str_b.strip() + '.'
####
str_c = 'Hakuna Matata, 1, 2, 3           '
## *Strip* the whitespace to the right of the '3' in str_c, print to console
print str_c.rstrip()

## *Split* str_c (without trailing whitespace) based on commas, print the list of strings to console
print str_c.rstrip().split(",")

####
str_d = 'LOWERCASE uppercase'
## Print a copy of str_d with 'lowercase' in lowercase and uppercase in uppercase (*swap* the cases)
print str_d.swapcase()

####
str_e = 'Halalaoa, Waoaralada!'
## Print str_e to console without the 'a' characters
print str_e.replace('a', '')

###
str_f = 'The dog is a puppy'
## Replace 'is' with 'was' and print to console.
print str_f.replace("is", "was")
