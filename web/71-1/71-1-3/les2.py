



class Car:

    def __init__(self,karkas, name, style) -> None: # конструктор для начальных парметров машины
        print('Создание АВТО\n')
        self.karkas={}
        self.karkas[karkas]=None
        self.name=name
        self.style=style
        self.price=0
        self.wheel=dict()

        
    def wheel_type(self,season):# создание колес
        #print('созадние колес')
        #season= #input('Введите время года: \n>>> ')
        if season=='Зима':
            self.wheel['Шипованные']=250
            self.price+=250
        else:
            self.wheel['Обычные']=200
            self.price+=200

        
    def frame_type(self):#рама или же каркас 
        if 'спортивный' in self.karkas.keys():
            self.karkas['спортивный']=900
            self.price+=900
        else:
            self.karkas['обычный']=600
            self.price+=600 # если обычный каркас
        

    def __del__(self): # магический метод вызываемый при удалении экземпляра класса 

        #print('\n',self.__dict__,'\n') # вывод всех параметров экземпляра класса 
        print()
        print(f'Навазние машины      >>>{self.name}')
        print(f'Общая цена машины    >>>{self.price}')
        print(f'Каркас машины        >>>{list(self.karkas.keys())[0]} >>> Цена >>>{list(self.karkas.values())[0]}')
        print(f'Колеса машины        >>>{list(self.wheel.keys())[0]}  >>> Цена >>>{list(self.wheel.values())[0]} ')
        

# Наследование от класса Car(родитлеьский класс)
# создадим дочерний класс 
class Bus(Car): # так указывается наследование от родительского класса 

    def __init__(self, karkas, name, style) -> None:
        super().__init__(karkas, name, style) # дает экземпляру класса параметры Родительского класса 
        
    def type_engine(self,engine): # тип двигателя
        self.engine=engine

    def __del__(self):
        super().__del__()
        print(f'Тип двигателя        >>>{self.engine}')
        return 

mazda=Car('спортивный', 'mazda','sport') # экзмеляр класса машины
mazda.wheel_type('Зима') # вызываемый метод класса 
mazda.frame_type()# вызываемый метод класса 

mersedes_bus=Bus('обычный', 'mers', 'normal')
mersedes_bus.wheel_type('Зима')
mersedes_bus.type_engine('электрический')




