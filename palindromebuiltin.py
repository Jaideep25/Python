# Taking the number 12345 as n to check palindrome
n = 12345

# Converting the input number n to a sequence (string).
seq = str(n)

# Checking whether the reversed sequence and the original sequence are equal or not.
if (seq == "".join(reversed(seq))):
    print("Palindrome")
else:
    print("Not a Palindrome")
