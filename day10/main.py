#Calculator

def add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}

def calculator():
  num1 = float(input("What's the first number? "))
  print("Which operation would you like to do:")
  for operation in operations:
    print(operation)
  operation = input()
  num2 = float(input("What's the second number? "))

  calculation_function = operations[operation]
  answer = calculation_function(num1, num2)

  print(f"Answer: {answer}")

  no_more_operations = False
  while not no_more_operations:
    ui = input(f"Would you like to perform another operation on {answer}? (y/n) ")
    if ui == "n": calculator()

    print("Which operation would you like to do:")
    for operation in operations:
      print(operation)
    operation = input()

    num2 = float(input("What's the second number? "))

    calculation_function = operations[operation]
    answer = calculation_function(answer, num2)
    
    print(f"Answer: {answer}")


calculator()