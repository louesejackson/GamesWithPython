Python 3.8.1 (v3.8.1:1b293b6006, Dec 18 2019, 14:08:53) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> spam = 'hello'
>>> spam
'hello'
>>> 'Hello' + 'World'
'HelloWorld'
>>> 'Hello ' + 'World'
'Hello World'
>>> 
===== RESTART: /Users/mary/Desktop/GamesWithPython/GamesWithPython/hello.py ====
Hello world!
What is your name?
Mary
It is good to meet you, Mary
>>> 
===== RESTART: /Users/mary/Desktop/GamesWithPython/GamesWithPython/hello.py ====
Hello world!
What is your name?
Sean
It is good to meet you, Sean
>>> 
>>> 
===== RESTART: /Users/mary/Desktop/GamesWithPython/GamesWithPython/hello.py ====
Hello world!
What is your name?
Mindy
It is good to meet you, Mindy
>>> 
===== RESTART: /Users/mary/Desktop/GamesWithPython/GamesWithPython/hello.py ====
Hello world!
What is your name?
bob qwerty 554
It is good to meet you, bob qwerty 554
>>> 
===== RESTART: /Users/mary/Desktop/GamesWithPython/GamesWithPython/guess.py ====
Hello! What is your name?
Mary
Well, Mary, I am thinking of a number between 1 and 20.
Take a guess.
5
Your guess is too low.
Take a guess.
15
Your guess is too high.
Take a guess.
7
Take a guess.
8
Your guess is too high.
Take a guess.
7
Take a guess.
6
Your guess is too low.
Nope. The umber I was thinking of was 7
>>> 
===== RESTART: /Users/mary/Desktop/GamesWithPython/GamesWithPython/guess.py ====
Hello! What is your name?
Mary
Well, Mary, I am thinking of a number between 1 and 20.
Take a guess.
15
Your guess is too high.
Take a guess.
8
Your guess is too low.
Take a guess.
10
Your guess is too low.
Take a guess.
12
Your guess is too low.
Take a guess.
14
Good job, Mary! You guessed my number in 5guesses!
>>> 
===== RESTART: /Users/mary/Desktop/GamesWithPython/GamesWithPython/guess.py ====
Hello! What is your name?
Mary
Well, Mary, I am thinking of a number between 1 and 20.
Take a guess.
12
Your guess is too low.
Take a guess.
18
Your guess is too high.
Take a guess.
16
Your guess is too high.
Take a guess.
14
Your guess is too low.
Take a guess.
15
Good job, Mary! You guessed my number in 5 guesses!
>>> 
>>> import random
>>> random.randint(1,20)
1
>>> random.randint(1,20)
13
>>> random.randint(1,20)
19
>>> random.randint(1,20)
11
>>> random.randint(1,20)
15
>>> random.randint(1,20)
8
>>> random.randint(1,20)
18
>>> random.randint(1,4)
3
>>> random.randint(1000,2000)
1068
>>> 
===== RESTART: /Users/mary/Desktop/GamesWithPython/GamesWithPython/guess.py ====
Hello! What is your name?
Mary
Well, Mary, I am thinking of a number between 1 and 100.
Take a guess.
50
Your guess is too low.
Take a guess.
80
Your guess is too low.
Take a guess.
90
Your guess is too high.
Take a guess.
85
Your guess is too low.
Take a guess.
87
Your guess is too low.
Take a guess.
89
Good job, Mary! You guessed my number in 6 guesses!
>>> 
>>> 
>>> spam = True
>>> eggs = False
>>> spam
True
>>> eggs
False
>>> 
>>> 0 <6
True
>>> 6<0
False
>>> 50 < 10
False
>>> 50 > 10
True
>>> 10<10
False
>>> 
>>> 10 == 10
True
>>> 10 == 11
False
>>> 11==10
False
>>> 10 != 10
False
>>> 10 != 11
True
>>> 'Hello' == 'Hello'
True
>>> 'Hello' == 'Goodbye'
False
>>> 'Hello' == 'HELLO'
False
>>> 'Goodbye' != 'Hello'
True
>>> 
>>> 42 == 'Hello'
False
>>> 42 != '42'
True
>>> 
>>> 
>>> int('42')
42
>>> 3 + int('2')
5
>>> int('fourty-two')
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    int('fourty-two')
ValueError: invalid literal for int() with base 10: 'fourty-two'
>>> 
>>> 
>>> float('42')
42.0
>>> float (42)
42.0
>>> str(42)
'42'
>>> str(42.0)
'42.0'
>>> str(False)
'False'
>>> bool('')
False
>>> bool('any nonempty string')
True
>>> 