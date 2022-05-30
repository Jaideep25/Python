s = "Welcome to scaler docs"
s1 = slice(6) # takes start as 0 automatically
print("s1-obj:", s1)
print("s1-res:", s[s1])
s2 = slice(2,8) # using slice(start, end, step) without step
print("s2-obj:", s2)
print("s2-res:", s[s2])
s3 = slice(1, 20, 2) # using slice(start, end, step) with step
print("s3-obj:", s3)
print("s3-res:", s[s3])
