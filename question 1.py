#Question 1
#define a funtion
#s=str
#i=int
#this function will return the string reversed and concatenated i times
def fun(s,i):
  reversed_s=s[::-1] #to reverse the inputed string
  if i<=0:
    return "" #empty string
  else:
    new_string=reversed_s*i #concatenate i times
    return new_string
s=str(input("Enter your string here: ")) #user's input
i=int(input("Enter how many times repeated: ")) #user's input
result=fun(s,i)
print(result)