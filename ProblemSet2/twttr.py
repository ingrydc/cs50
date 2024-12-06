text = input('Input: ').strip()
vowels = 'AEIOUaeiou'
output = ''
for char in text:
    if char not in vowels:
        output += char
print(f'Output: {output}')
