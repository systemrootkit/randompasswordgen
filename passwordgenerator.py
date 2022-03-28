import random
pl=int(input("enter the length of your password"))
s='asdfghjklpoiuytrewqzxcvbnmASDFGHJKLPOIUYTREWQZXCVBNM0987654321!@#$%^&*()_-+=<>?/'
p="".join(random.sample(s,pl))
print(p)