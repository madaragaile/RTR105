Python 2.7.12 (default, Dec  4 2017, 14:50:18) 
[GCC 5.4.0 20160609] on linux2
Type "copyright", "credits" or "license()" for more information.
>>> x = 5
>>> if x < 10:
	print('Smaller')

	
Smaller
>>> if x > 20:
	print('Bigger')

	
>>> print('Finis')
Finis
>>> x = 5
>>> if x == 5:
	print('Equals 5')

	
Equals 5
>>> if x > 4:
	print('Greater than 4')

	
Greater than 4
>>> if x > 5:
	print('Greater than or Equals 5')

	
>>> if x < 6:
	print('Less than or equals 5')

	
Less than or equals 5
>>> if x != 6:
	print('Not equal 6')

	
Not equal 6
>>> x = 5
>>> print('Before 5')
Before 5
>>> if x == 5:
	print('Is 5')
	print('Is Still 5')
	print('Third 5')

	
Is 5
Is Still 5
Third 5
>>> print('Afterwards 5')
Afterwards 5
>>> print('Before 6')
Before 6
>>> if x == 6:
	print('Is 6')
	print('Is still 6')
	print('Third 6')

	
>>> print('Afterwards 6')
Afterwards 6
>>> x = 5
>>> if x > 2:
	print('Bigger than 2')
	print('Still bigger')

	
Bigger than 2
Still bigger
>>> print('Done with 2')
Done with 2
>>> 
>>> for i in range(5):
	print(i)
	if i > 2:
		print('Bigger than 2')

		
0
1
2
3
Bigger than 2
4
Bigger than 2
>>> x = 5
>>> if x > 2
SyntaxError: invalid syntax
>>> x = 5
>>> if x > 2:
	print('Bigger than 2')
	print('Still bigger')

	
Bigger than 2
Still bigger
>>> print('Done with 2')
Done with 2
>>> for i in range(5):
	print(i)
	if i > 2:
		print('Bigger than 2')

		
0
1
2
3
Bigger than 2
4
Bigger than 2
>>> print('Done with i', i)
('Done with i', 4)
>>> print('All done')
All done
>>> x = 42
>>> if x > 1:
	print('More tahn one')
	if x < 100:
		print('Less than 100')

		
More tahn one
Less than 100
>>> print('All done')
All done
>>> x = 4
>>> if x > 2:
	print('BIgger')

	
BIgger
>>> else:
	
SyntaxError: invalid syntax
>>> if x > 2:
	print('BIgger')
else:
	print("Smaller")
print("All done")
SyntaxError: invalid syntax
>>> 
============= RESTART: /home/user/RTR105/tests_20181015_1_if.py =============
BIgger
All done
>>> 
============= RESTART: /home/user/RTR105/tests_20181015_1_if.py =============
BIgger
All done
Bigger
All done
>>> 
============= RESTART: /home/user/RTR105/tests_20181015_1_if.py =============
BIgger
All done
Bigger
All done
Medium
All done
small
All done
Medium
All done
LARGE
All done
Medium
Two or more
>>> 
