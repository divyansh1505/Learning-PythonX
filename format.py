print("Choose words to fill in the given sentence :")
print("{} woke up one day. Ate {} along with {} and went to {} with {}")

a = input("Enter a word : ")
b = input("Enter a word : ")
c = input("Enter a word : ")
d = input("Enter a word : ")
e = input("Enter a word : ")

# print("{} woke up one day. Ate {} along with {} and went to {} with {}".format(f"{a}", f"{b}", f"{c}", f"{d}", f"{e}"))
s = ("{} woke up one day. Ate {} along with {} and went to {} with {}".format(a, b, c, d, e))
print(s)

print("{} is a good {}".format("divyansh", "boy")) #1.
print("{1} is a good {0}".format("divyansh", "boy")) #2.

# output for 1:
# divyansh is a good boy 

# output for 2:
# boy is a good divyansh 