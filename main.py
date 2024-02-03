from art import logo

def add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2

operations = {
  '+' : add,
  '-' : subtract,
  '*' : multiply,
  '/' : divide
}

def calculator():
  print(logo)
  num1 = float(input("What's the first number?: "))
  for j in operations:
    print(j)
  operator = input("Pick and operation from the lines above: ")
  num2 = float(input("What's the second number?: "))
  
  def calculation(num_1, num_2):
    for i in operations:
      if operator == i:
        function = operations[i]
        return function(num_1, num_2)
  
  first_answer = calculation(num1, num2)
  
  print(f"{num1} {operator} {num2} = {first_answer}")
  
  calc_continue = True
  
  while calc_continue == True:
    proceed = input(f"Type 'y' to continue with {first_answer}, or type 'n' to start a new calculation, or type 'x' to exit: ").lower()
    if proceed == 'y':
      calc_continue = True
  
      operator = input("Pick another operation: ")
      num3 = float(input("What's the next number?: "))
      second_answer = calculation(first_answer, num3)    
      print(f"{first_answer} {operator} {num3} = {second_answer}")
      first_answer = second_answer
    elif proceed == 'n':
      calc_continue = False
      calculator()
    elif proceed == 'x':
      print("Have a nice day!")
      calc_continue = False      
    else:
      print("Wrong input. Start again!")
      calc_continue = False

calculator()