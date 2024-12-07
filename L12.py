import pyfiglet
banner=pyfiglet.figlet_format("Calculator")
print(banner)
print ("           Cretor By Ashik_Raj\n")

print(" The Calculator You Need\n")  #\n ata holo new line er jonno.
print(" Enter + to do  addition\n")
print(" Enter * to do Multiplicatipn\n")
print(" Enter - to do  subraction\n")
print(" Enter / to do Division\n")

user=input(" Enter a Choice : ")

if user=="+":
  num1=float(input("Enter your 1st number : "))
  num2=float(input("Enter your 2nd number : "))
  sol=(num1+num2)
  result=str(sol)
  print(" Your Result :"+result)

elif user=="-":
  num1=float(input("Enter your 1st number : "))
  num2=float(input("Enter your 2nd number : "))
  sol=(num1-num2)
  res=str(sol)
  print(" Your Result :" +res)

elif user=="*":
  num1=float(input(" Enter your 1st number : "))
  num2=float(input(" Enter your 2nd number : "))
  sol=(num1*num2)
  res=str(sol)
  print(" Your Result :" + res)

elif user=="/":
  num1=float(input(" Enter your 1st number : "))
  num2=float(input(" Enter your 2nd number : "))
  sol=(num1/num2)
  res=str(sol)
  print(" Your Result :" + res)
else :
  print (" Plz Enter Right Selection ")
