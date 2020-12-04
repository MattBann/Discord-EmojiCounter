""" A little script to help create a list of emoji, for when you want to change the valid emoji list:
-Open discord, open the emoji panel
-Hold shift and click on all the emoji you want, adding spaces inbetween
-Copy the list and paste into the input of this script
-The script will ouput it with string list formatting.
You may not find this helpful, but it works for me.
"""
a = input()

list = a.split(' ')

print(list)