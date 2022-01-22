import random

a = random.randint(1,6)
b = random.random()

lst = ['rock','paper','scissors']
c = random.choice(lst)

cards = [1,2,3,4,5,6,7,8,9,10,'J','Q','K','A']
random.shuffle(cards)

print(a)
print(b)
print(c)
print(cards)