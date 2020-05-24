n=int(input("enter an integer: "))
mod=n%2
if mod!=0:
 print("Weird")
if mod==0 and n>1 and n<=5:
 print("Not Weird")
if mod==0 and n>5 and n<=20:
 print("Weird")
if mod==0 and n>20:
 print("Not Weird")