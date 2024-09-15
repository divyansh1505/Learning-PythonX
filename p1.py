try:
    with open ("1.txt", "r") as f:
       print(f.read())

except Exception as e:
    print(e)

try:
    with open ("2.txt", "r") as f:
       print(f.read())

except Exception as e:
    print(e)

try:
    with open ("3.txt", "r") as f:
       print(f.read())

except Exception as e:
    print(e)


print("Thank you")
# This statement is outside the try-except blocks and will 
# always be executed, regardless of whether any exceptions occur 
# during the file-reading operations.