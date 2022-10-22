

count = 0
b = 0
StringB = ""
String = ""


String = input()
StringLower = String.lower()
i = len(String)
while b != i:
    count = StringLower.count(StringLower[b])
    if count > 1:
        StringB = StringB + ")"
    else:
        StringB = StringB + "("
    b += 1
  
print(StringB)

