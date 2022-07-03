while True:
  print("Select operation.")
  print("1.Add      : + ")
  print("2.Subtract : - ")
  print("3.Multiply : * ")
  print("4.Divide   : / ")
  print("5.Power    : ^ ")
  print("6.Remainder: % ")
  print("7.Terminate: # ")
  print("8.Reset    : $ ")


  # take input from the user
  choice = input("Enter choice(+,-,*,/,^,%,#,$): ")
  print(choice)
  
  def terminate1():
    if((choice) == "#"):
      print("Done. Terminating")
      exit()
    elif ("#" in str(firstNumber)):
      print("Done. Terminating")
      exit()
    else:
      return
  
  def terminate2():
    if ("#" in str(secondNumber)):
      print("Done. Terminating")
      exit()
    else:
      return
  
  if((choice) == "#"):
    terminate1()
    
  if ((choice) == "$"):
    True
    
  if(choice) == "+":
    firstNumber = input ("Enter first number: ")
    print(firstNumber)
    terminate1()
    if ("$" in str(firstNumber)):
      True
    else:
      secondNumber = input ("Enter second number: ")
      print(secondNumber)
      terminate2()
      if ("$" in str(secondNumber)):
        True
      else:
        sum = float(firstNumber) + float(secondNumber)
        print (float(firstNumber),"+",float(secondNumber),"=",float(sum))

  if(choice) == "-":
    firstNumber = input ("Enter first number: ")
    print(firstNumber)
    terminate1()
    if ("$" in str(firstNumber)):
      True
    else:
      secondNumber = input ("Enter second number: ")
      print(secondNumber)
      terminate2()
      if ("$" in str(secondNumber)):
        True
      else:
        difference = float(firstNumber) - float(secondNumber)
        print (float(firstNumber),"-",float(secondNumber),"=",float(difference))   
  
  if(choice) == "*":
    firstNumber = input ("Enter first number: ")
    print(firstNumber)
    terminate1()
    if ("$" in str(firstNumber)):
      True
    else:
      secondNumber = input ("Enter second number: ")
      print(secondNumber)
      terminate2()
      if ("$" in str(secondNumber)):
        True
      else:
        product = float(firstNumber) * float(secondNumber)
        print (float(firstNumber),"*",float(secondNumber),"=",float(product))   
   
  if (choice) == "/":
    firstNumber = input ("Enter first number: ")
    print(firstNumber)
    terminate1()
    if ("$" in str(firstNumber)):
      True
    else:
      secondNumber = input ("Enter second number: ")
      print(secondNumber)
      terminate2()
      if ("$" in str(secondNumber)):
        True
      elif (secondNumber) == "0":
        print("float division by zero")
        print (float(firstNumber),"/",float(secondNumber),"= None ")
      else:
        division = float(firstNumber) / float(secondNumber)
        print (float(firstNumber),"/",float(secondNumber),"=",float(division))
        
  if (choice) == "^":
    firstNumber = input ("Enter first number: ")
    print(firstNumber)
    terminate1()
    if ("$" in str(firstNumber)):
      True
    else:
      secondNumber = input ("Enter second number: ")
      print(secondNumber)
      terminate2()
      if ("$" in str(secondNumber)):
        True
      else:
        answer = float(firstNumber) ** float(secondNumber)
        print (float(firstNumber),"^",float(secondNumber),"=",float(answer))
        
  if (choice) == "%":
    firstNumber = input ("Enter first number: ")
    print(firstNumber)
    terminate1()
    if ("$" in str(firstNumber)):
      True
    else:
      secondNumber = input ("Enter second number: ")
      print(secondNumber)
      terminate2()
      if ("$" in str(secondNumber)):
        True
      else:
        remainder = float(firstNumber) % float(secondNumber)
        print (float(firstNumber),"%",float(secondNumber),"=",float(remainder))
