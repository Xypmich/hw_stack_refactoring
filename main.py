class Stack:
    def __init__(self):
        self.some_list = []

    def isEmpty(self):
        if self.some_list:
            return False
        else:
            return True

    def push(self, element):
        if not self.some_list:
            self.some_list.append(element)
        else:
            new_list = [element]
            for value in self.some_list:
                new_list.append(value)
            self.some_list = new_list

    def pop(self):
        self.some_list.pop(0)
        if self.size() > 0:
            return self.some_list[0]

    def peek(self):
        return self.some_list[0]

    def size(self):
        return len(self.some_list)


def bracket_balance(bracket_str: str):
    open_brackets = ['(', '{', '[']
    close_brackets = [')', '}', ']']
    if not bracket_str:
        result = 'Несбалансировано'
        return result
    elif len(bracket_str) % 2 != 0:
        result = 'Несбалансировано'
        return result
    stack = Stack()
    for value in bracket_str:
        if value in open_brackets:
            stack.push(value)
        elif value in close_brackets and stack.size() > 0:
            stack.pop()
    if stack.size() == 0:
        result = 'Cбалансировано'
        return result
    else:
        result = 'Несбалансировано'
        return result


if __name__ == '__main__':
    brackets = '[[{())}]'

    print(bracket_balance(brackets))
