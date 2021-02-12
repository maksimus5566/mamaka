#index = место или расположение (нумеровние) чего либо, может быть и положительным или отрицательным, начинается с 0

string_sample = "Hello world world!"
string_sample2 = "I want coffee"
string_sample3 = " I want coffee "
print(string_sample[1]) #квадратные скобки за место курглых около 1

print(string_sample[0:5])
print(string_sample[0:5], string_sample[8:15])
print(string_sample[7:])
print(string_sample[:7])
print(string_sample[:]) # тоже самое как print(string_sample)
print(string_sample[-6:])
print(string_sample[0:14:2]) #3 число, которое является шагом, то етсь через каоето число
print(string_sample[::-1])

print(len(string_sample))#длинна строки -1 это колличесво знаков
print(string_sample.upper())
print(string_sample2.lower()) #оставляет спец символы
print(string_sample.casefold()) #изменяет размер спецсивол
print(string_sample.capitalize()) #Первая заглавная буква, остальное уменьшеное (он не видет где заканчивается строка)

print("world" in string_sample)
print(string_sample.find("world")) #нахождение позицию слова в строке (назодит только первую позицию)
print(string_sample[6:]) #наxождение слова
print(string_sample.count("world")) #находит общее колличество нужной инфо
print(string_sample3.strip()) #убирает все ненужные пробелы по краям

print("Hello \nworld") #перенос на вторую строку
print("Hello\tworld")

variable = 1000
variable = float(variable)
print (type(variable))
print("Hello" + string_sample + str(1000))
print(type(variable))

worker1 = "Roman"
salary1 = 1000
print("Hello" + worker1 + ". " + "Your salary is ", salary1)
print("Hello {}. Your salary is {}".format(worker1, salary1))
print("Hello {}. Your salary is {}".format(salary1, worker1))
print("Hello {0}. Your salary is {1}".format(worker1, salary1))



price_string = "This is {product:}, it cost {price:.2f} euro."
print(price_string.format(price=350, product="computer"))



number = 50003040266

if len(str(number)) == 11:
    print("ID code is correct")
else:
    print("ERROR")



id_code = input("Please enter your national ID code:")

if len(id_code) == 11:
    print("Your ID code is correct")
if id_code[0] == 3:
       print("Your are male")
    elif    len(id_code) > 11:
        print("Code you entered is longer that 11 digits")
    else:
    print("Code you entered is shorter that 11 digits")

# string_sample = "Hello world world"
#
# print(string_sample.count("hello" or "hy"))