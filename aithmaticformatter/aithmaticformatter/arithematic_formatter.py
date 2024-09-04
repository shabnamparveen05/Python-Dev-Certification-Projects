def arithmetic_arranger(problems, show_answers=False):
    # Step 1: Check the number of problems
    if len(problems) > 5:
        return 'Error: Too many problems.'

    # Step 2: Check operators and operands
    operators = []
    numbers = []
    for problem in problems:
        parts = problem.split()
        if parts[1] not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."
        operators.append(parts[1])
        numbers.append(parts[0])
        numbers.append(parts[2])

    # Step 3: Validate numbers (only digits)
    for number in numbers:
        if not number.isdigit():
            return 'Error: Numbers must only contain digits.'

    # Step 4: Validate number length (maximum 4 digits)
    for number in numbers:
        if len(number) > 4:
            return 'Error: Numbers cannot be more than four digits.'

    # Step 5: Calculate answers if requested
    answers = []
    if show_answers:
        for i in range(0, len(numbers), 2):
            num1 = int(numbers[i])
            num2 = int(numbers[i + 1])
            operator = operators[i // 2]
            if operator == '+':
                result = num1 + num2
            else:
                result = num1 - num2
            answers.append(result)

    # Step 6: Format the problems
    top_row = ''
    bottom_row = ''
    dashes = ''
    answer_row = ''
    for i in range(0, len(numbers), 2):
        num1 = numbers[i]
        num2 = numbers[i + 1]
        operator = operators[i // 2]
        space_width = max(len(num1), len(num2)) + 2

        top_row += num1.rjust(space_width)
        bottom_row += operator + num2.rjust(space_width - 1)
        dashes += '-' * space_width
        if show_answers:
            answer_row += str(answers[i // 2]).rjust(space_width)

        if i < len(numbers) - 2:
            top_row += '    '
            bottom_row += '    '
            dashes += '    '
            if show_answers:
                answer_row += '    '

    arranged_problems = top_row + '\n' + bottom_row + '\n' + dashes
    if show_answers:
        arranged_problems += '\n' + answer_row

    return arranged_problems

