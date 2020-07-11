from stack import Stack

PARENTHESES = {")": "(", "]": "[", "}": "{"}


def validate_parentheses(expression):
    opening_parens = Stack()
    for char in expression:
        if char in PARENTHESES.values():
            opening_parens.push(char)
        elif char in PARENTHESES:
            if len(opening_parens) == 0 or not PARENTHESES[char] == opening_parens.pop():
                return False

    return len(opening_parens) == 0


if __name__ == "__main__":
    print(validate_parentheses("}[()]{()}[]"))
