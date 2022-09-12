def arithmetic_arranger(problems, show_result=False):
    if len(problems) > 5:
        return "Error: Too many problems."
    # arranged_problems = ""
    line1 = ''
    line2 = ''
    dash_lines = ''
    results = ''
    for prob in problems:
        splitted_problems = prob.split()
        is_only_digit = splitted_problems[0].isnumeric() and splitted_problems[2].isnumeric()
        if not is_only_digit:
            return "Error: Numbers must only contain digits."
            # quit()
        num1 = int(splitted_problems[0])
        operator = splitted_problems[1]
        num2 = int(splitted_problems[2])
        if (len(str(num1)) > 4) or (len(str(num2)) > 4):
            return "Error: Numbers cannot be more than four digits."
            quit()
        if operator == "+":
            result = num1 + num2
        elif operator == "-":
            result = num1 - num2
        else:
            return "Error: Operator must be '+' or '-'."
            quit()
        distance = max(len(str(num1)), len(str(num2))) + 2
        row1 = str(splitted_problems[0].rjust(distance)) + "        "
        row2 = operator + str(splitted_problems[2].rjust(distance - 1)) + "        "
        lines = ''
        resultss = str(str(result).rjust(distance)) + "        "
        for line in range(distance):
            lines += "-" 
            if len(lines) == distance:
              lines += ' '
        line1 = line1 + row1
        line2 = line2 + row2
        dash_lines = dash_lines + lines
        results = results +resultss
        # arranged_problems = arranged_problems + row1 + "\n" + row2 + "\n" + lines + "\n" + results
    if show_result:
        return print(''.join(line1) + '\n' + ''.join(
            line2) + '\n' + ' '.join(dash_lines) + ' ' + '\n' + ''.join(results))
    else:
        return print(''.join(line1) + '\n' + ''.join(
            line2) + '\n' + ' '.join(dash_lines) + '\n')