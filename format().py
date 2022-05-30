# Here we take two variables and do certain operations with it.                                                                                                                        
x = 3
y = 12
mul = x * y
print('The value of x is {} and y is {}'.format(x, y))
# Here we are specifying the order of the variables.
print('{2} is the multiplication of {0} and {1}'.format(x, y, mul))
# We can even use keyword arguments to format strings.
print('Hey! Welcome to {company}. In this article we will learn about {language}'.format(company='Scaler', language='Python'))