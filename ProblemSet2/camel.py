camel = input("camelCase: ")
snake = camel[0].lower()
for char in camel[1:]:
    if char.isupper():
        snake += '_'
        snake += char.lower()
    else:
        snake += char
print(f'snake_case: {snake}')