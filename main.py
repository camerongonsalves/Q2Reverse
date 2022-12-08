userinput=input("What is your word?")
n=0
num=""
for i in range (0,len(userinput)):
  n=n-1
  num=num+userinput[n]
print()
print("The reverse of your input is",num)