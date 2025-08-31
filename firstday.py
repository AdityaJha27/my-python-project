the_world_is_flat = True
if the_world_is_flat:
    print("Be careful not to fall off!")

#3.1. Using Python as a Calculator¶
# 3.1.1. Numbers¶
print(2 + 2)

print(50 - 5*6)

print((50 - 5*6)/ 4)

print(8 / 5)  # division always returns a floating-point number

print(17 / 3)  # classic division returns a float

print(17 // 3)  # floor division discards the fractional part

print(17 % 3)  # the % operator returns the remainder of the division

print(5 * 3 + 2 ) # floored quotient * divisor + remainder

print(5 ** 2)  # 5 squared

print(2 ** 7)  # 2 to the power of 7

width = 20
height = 5 * 9
print(width * height)

print(4 * 3.75 - 1)

tax = 12.5 / 100
price = 100.50
print(price * tax)

a=12.5625 #price*tax
print(price+a)
num=113.0625
rounded_num = round(num, 2)   # 2 matlab 2 decimal places
print(rounded_num)

# 3.1.2. Text
print('spam eggs')  # single quotes

print("Paris rabbit got your back :)! Yay!")  # double quotes

print('1975')  # digits and numerals enclosed in quotes are also strings

print('doesn\'t')  # use \' to escape the single quote...

print("doesn't")  # ...or use double quotes instead

print('"Yes," they said.')

print("\"Yes,\" they said.")

print('"Isn\'t," they said.')

print('C:\some\name')  # here \n means newline!


print(r'C:\some\name')  # note the r before the quote
print('Py' 'thon')

x = ('Put several strings within parentheses '
        'to have them joined together.')
print(x)

# If you want to concatenate variables or a variable and a literal, use +:
print( + 'thon')