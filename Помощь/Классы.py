class название_класса:
    атрибуты_класса
    методы_класса
    
    
    
class Person:
    pass        #pass. Этот оператор применяется, когда синтаксически необходимо определить некоторый код, однако мы не хотим его,
#и вместо конкретного кода вставляем оператор pass.
    
    


class Person:
    pass
 
tom = Person()      # определение объекта tom
bob = Person()      # определение объекта bob


tom = Person()      # Person() - вызов конструктора, который возвращает объект класса Person



class Person:       # определение класса Person
     def say_hello(self):
        print("Hello")
 
tom = Person()
tom.say_hello()    # Hello
#При определении методов любого класса следует учитывать, что все они должны принимать в качестве первого параметра ссылку на текущий
#объект, который согласно условностям называется self. Через эту ссылку внутри класса мы можем обратиться к функциональности текущего
#объекта. Но при самом вызове метода этот параметр не учитывается.


#Используя имя объекта, мы можем обратиться к его методам. Для обращения к методам применяется нотация точки
#- после имени объекта ставится точка и после нее идет вызов метода:
объект.метод([параметры метода])

tom.say_hello()    # Hello



class Person:       # определение класса Person
    def say(self, message):     # метод 
        print(message)
 
 
tom = Person()
tom.say("Hello METANIT.COM")    # Hello METANIT.COM


#Через ключевое слово self можно обращаться внутри класса к функциональности текущего объекта:
self.атрибут    # обращение к атрибуту
self.метод      # обращение к методу



class Person:
 
    def say(self, message):
        print(message)
 
    def say_hello(self):
        self.say("Hello work")  # обращаемся к выше определенному методу say
 
 
tom = Person()
tom.say_hello()     # Hello work


def say_hello(self):
    say("Hello work")  # ! Ошибка
    
    
#Для создания объекта класса используется конструктор. Так, выше когда мы создавали объекты класса Person,
#мы использовали конструктор по умолчанию, который не принимает параметров и который неявно имеют все классы:
    tom = Person()
#Однако мы можем явным образом определить в классах конструктор с помощью специального метода,
#который называется __init__() (по два прочерка с каждой стороны). К примеру, изменим класс Person, добавив в него конструктор:
    
    class Person:
    # конструктор
    def __init__(self):
        print("Создание объекта Person")
 
    def say_hello(self):
        print("Hello")
         
         
tom = Person()      # Создание объекта Person
tom.say_hello()     # Hello



#Атрибуты хранят состояние объекта. Для определения и установки атрибутов внутри класса можно применять слово self.
#Например, определим следующий класс Person:
class Person:
 
    def __init__(self, name):
        self.name = name    # имя человека
        self.age = 1        # возраст человека
 
 
tom = Person("Tom")
 
# обращение к атрибутам
# получение значений
print(tom.name)     # Tom
print(tom.age)      # 1
# изменение значения
tom.age = 37
print(tom.age)      # 37

print(tom.name)     # получение значения атрибута name
tom.age = 37        # изменение значения атрибута age


class Person:
 
    def __init__(self, name):
        self.name = name    # имя человека
        self.age = 1        # возраст человека
 
 
tom = Person("Tom")
 
tom.company = "Microsoft"
print(tom.company)  # Microsoft


tom = Person("Tom")
print(tom.company)  # ! Ошибка - AttributeError: Person object has no attribute company


class Person:
 
    def __init__(self, name):
        self.name = name    # имя человека
        self.age = 1        # возраст человека
     
    def display_info(self):
        print(f"Name: {self.name}  Age: {self.age}")
 
 
tom = Person("Tom")
tom.display_info()      # Name: Tom  Age: 1



class Person:
 
    def __init__(self, name):
        self.name = name    # имя человека
        self.age = 1        # возраст человека
 
    def display_info(self):
        print(f"Name: {self.name}  Age: {self.age}")
 
 
tom = Person("Tom")
tom.age = 37
tom.display_info()      # Name: Tom  Age: 37
 
bob = Person("Bob")
bob.age = 41
bob.display_info()      # Name: Bob  Age: 41    
    
    