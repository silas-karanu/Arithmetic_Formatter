def arithmetic_arranger(problems, show_answers=False):
    
    #Validation
    if len(problems) > 5:
        return "Error: Too many problems."

    top_row = []
    bottom_row = []
    dashes = []
    answers = []

    for problem in problems:
        parts = problem.split()
        if len(parts) != 3:
            return "Error: Invalid problem format"

        first, op, second = parts

        if op not in ["+","-"]:
            return "Error: Operator must be '+' or '-'."

        if not first.isdigit() or not second.isdigit():
            return "Error: Numbers must only contain digits."

        if len(first) > 4 or len(second) > 4:
            return "Error: Numbers cannot be more than four digits."

        #Finds the maximum width between the two numbers.
        #Adds 2 extra characters
        width = max(len(first), len(second)) + 2


        #right-aligns first in a field of width characters
        top_row.append(first.rjust(width))

        # right-align second in width - 1 characters.
        bottom_row.append(op + second.rjust(width - 1))

        #Creates a line of - characters as long as the total width.
        dashes.append("-" * width)



        #checks if caller asked to show answers
        #calculates the result of the problem string
        #converts the number into a string so we can align it
        if show_answers:
            result = str(eval(problem))
            answers.append(result.rjust(width))

    # assemble the individual formatted parts
    #with four spaces between them
    arranged = "    ".join(top_row) + "\n" + \
               "    ".join(bottom_row) + "\n" + \
               "    ".join(dashes)
    
    
    if show_answers:
        arranged += "\n" + "    ".join(answers)

    return arranged
     

print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])}')
print(f'\n{arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True)}')