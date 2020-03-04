""" If no argument's are passed onto who the default value is taken here as harry."""

def greet(who = "harry"):
    print("hello,", who)

greet()
greet(who = "tom")
greet(who = "world")
