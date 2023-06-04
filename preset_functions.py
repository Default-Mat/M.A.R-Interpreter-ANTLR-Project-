def square(x):
    return x * x


def cube(x):
    return x * x * x


def mult(x, y):
    return x * y


def show(string):
    if type(string) == str:
        for i in string:
            if i == '"':
                indexOfCharacter = string.index(i)
                s1 = string[:indexOfCharacter]
                s2 = string[indexOfCharacter+1:]
                string = s1 + s2

    print(string)


def to_string(nonstring):
    return str(nonstring)

