# Строки

x = 'Aleks'
print(x)
y = "Some text 123"
print(y)
z = "Some 'long' text"  # При необходимости использования кавычек в тексте
print(z)
x = 'Some \'long\', and \'answer\' text'  # При необходимости использования однотипных кавычек начало и конец можно обозначить обратным слешом
print(y)
y = r'C:\Users\dell\Desktop'  # При необходимости использования обратных слешей внутри кавычек
x = 'some long text \nand new string'  # При необходимости вывода с переносом строки
print(x)

# Срезы строки
text = str('hello world')
print(text)
print(text[0])  # обращаемся к символу в строке по индексу
print(text[0] + text[1])  # конкатенация символов в строке
print(text[-1] + text[1]) # обращение к последнему символу
print(text[6:] + ' ' + text[:6]) # срез от конкретного символа и до конца строки и наоборот
print(text[6:8]) # срез от символа к символу
print(text[::1]) # срез с шагом 1
print(text[::2]) # срез с шагом 2
