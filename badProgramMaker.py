
file = open(r"path", 'w')


# header
file.write("print('Welcome to my calculator! It can add (+), subtract(-), multiply(*), divide(/), raise to a power(^), and take the nth root of (root) whole numbers from -50 to 50')\n")
file.write("num1 = int(input('First number: '))\n")
file.write("sign = input('Operator: ')\n")
file.write("num2 = int(input('Second number: '))\n")

operators = ["+", "-", "*", "/", "^", "root"]

minNum = -50
maxNum = 50

for op in operators:
    for i in range(minNum, maxNum + 1):
        if i%100 == 0: print(op, i)
        for j in range(minNum, maxNum + 1):
            file.write("if num1 == " + str(i) + " and sign == \"" + op + "\" and num2 == " + str(j) + ":" + "\n")
            if op == "+": file.write("\tprint(\"" + str(i) + " + " + str(j) + " = " + str(i+j) + "\")\n")
            elif op == "-": file.write("\tprint('" + str(i) + " - " + str(j) + " = " + str(i-j) + "')\n")
            elif op == "*": file.write("\tprint('" + str(i) + " * " + str(j) + " = " + str(i*j) + "')\n")
            elif op == "/" and j != 0: file.write("\tprint('" + str(i) + " / " + str(j) + " = " + str(i/j) + "')\n")
            elif op == "^" and not (i == 0 and j < 0): file.write("\tprint('" + str(i) + " ^ " + str(j) + " = " + str(i**j) + "')\n")
            elif op == "root" and i != 0 and not (j == 0 and i < 0): file.write("\tprint('" + str(i) + "th root of " + str(j) + " = " + str(j**(1/i)) + "')\n")
            else: file.write("\tprint(\"error\")\n")
file.write("input()")