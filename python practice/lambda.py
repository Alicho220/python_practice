# functional programming
# simple one line function..

# lambda is usually expressed as
# lambda parameter(s): return or expression/statement

# instead of using def use the lambda keyword and assign it to a variable

multiply = lambda x:2*x
print(multiply(4))

multiply2 = lambda x,y :x * y
print(multiply2(4,4))

if_else = lambda x,y:x if x > y or x == y else y
print(if_else(2,8))