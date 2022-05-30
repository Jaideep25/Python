# Case fold
myText = "Interview Bit Problem Solving"
x = myText.casefold()
print(x)

# Center aligned
txt = "interviewBit"
# [Mandatory] length is the first parameter
x = txt.center(20)
print(x)
# [Optional] 2nd parameter is character
# to fill the missing space on each side
x = txt.center(20, '|')
print(x)