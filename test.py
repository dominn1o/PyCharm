mystring = 'digital_girlfriend_2002'
bytes = ' '.join(format(b, '08b') for b in mystring.encode('utf-8'))
print(bytes)