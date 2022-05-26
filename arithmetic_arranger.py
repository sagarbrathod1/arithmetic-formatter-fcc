import re

def arithmetic_arranger(problems, solve = False):

  # error handling
  if(len(problems) > 5):
    return "Error: Too many problems."
  
  first_line = ""
  second_line = ""
  vinculum = ""
  sum_line = ""
  string = ""

  for prob in problems:

    # error handling
    if re.search("[^\s0-9+-]", prob):
      if re.search("[/]", prob) or re.search("[*]", prob):
        return "Error: Operator must be '+' or '-'."
      return "Error: Numbers must only contain digits."

    first_num = prob.split(" ")[0]
    oper = prob.split(" ")[1]
    second_num = prob.split(" ")[2]

    # error handling
    if len(first_num) >= 5 or len(second_num) >= 5:
      return "Error: Numbers cannot be more than four digits."

    sum = ""
    
    if oper == "+":
      sum = str(int(first_num) + int(second_num))
    elif oper == "-":
      sum = str(int(first_num) - int(second_num))

    length = max(len(first_num), len(second_num)) + 2
    top = str(first_num).rjust(length)
    bottom = oper + str(second_num).rjust(length - 1)
    dashes = ""
    solution = str(sum).rjust(length)
    
    for i in range(length):
      dashes += "-"

    if prob != problems[-1]:
      first_line += top + '    '
      second_line += bottom + '    ' 
      vinculum += dashes + '    '
      sum_line += solution + '    '
    else:
      first_line += top
      second_line += bottom
      vinculum += dashes
      sum_line += solution

  if solve:
    arranged_prob = first_line + "\n" + second_line + "\n" + vinculum + "\n" + sum_line
  else: 
    arranged_prob = first_line + "\n" + second_line + "\n" + vinculum

  return arranged_prob