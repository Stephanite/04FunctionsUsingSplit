print("enter a mathmatical expression: ")
def operation(mathExpression):
  integer1,operator,integer2 = mathExpression.split( )

  integer1=int(integer1)
  integer2=int(integer2)

  if operator=="+":
    return integer1+integer2
  if operator=="-":
    return integer1-integer2
  if operator=="*":
    return integer1*integer2
  if operator=="/":
    return integer1/integer2
  
print("=",operation(input()))