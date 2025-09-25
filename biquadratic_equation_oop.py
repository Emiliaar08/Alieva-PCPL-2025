import sys
import math

class SquareRoots:

    def __init__(self):

        self.coef_A = 0.0
        self.coef_B = 0.0
        self.coef_C = 0.0
        self.num_roots = 0
        self.roots_list = []

    def get_coef(self, index, prompt):
        
        try:
            coef_str = sys.argv[index]
            coef = float(coef_str)
        except:
            while(True):
                print(prompt)
                coef_str = input()
                try:
                    coef = float(coef_str)
                    break
                except:
                    print("Введено некорректное значение, введите действительное число")
                
        return coef

    def get_coefs(self):

        self.coef_A = self.get_coef(1, 'Введите коэффициент А:')
        self.coef_B = self.get_coef(2, 'Введите коэффициент B:')
        self.coef_C = self.get_coef(3, 'Введите коэффициент C:')

    def calculate_roots(self):
      
        self.num_roots = 0
        self.roots_list = []

        if self.coef_A == 0:
            if self.coef_B == 0:
                if self.coef_C == 0:
                    self.roots_list = ["Бесконечное множество корней"]
                    self.num_roots = 0
                else:
                    self.roots_list = ["Нет корней"]
                    self.num_roots = 0
            else:
                if self.coef_C == 0:
                    self.roots_list.append(0)
                    self.num_roots = 1 
                else:
                    x = (- self.coef_C) / self.coef_B
                    if x > 0:
                        self.roots_list.append(math.sqrt(x))
                        self.roots_list.append(- math.sqrt(x))
                        self.num_roots = 2
                    elif x == 0:
                        self.roots_list.append(0)
                        self.num_roots = 1
                    else:
                        self.roots_list = ["Нет корней"]
                        self.num_roots = 0
        else:
            if self.coef_B == 0:
                if self.coef_C == 0: 
                    self.roots_list.append(0)
                    self.num_roots = 1
                else:
                    fourth_degree = (- self.coef_C) / self.coef_A
                    if fourth_degree < 0:                        
                        self.roots_list = ["Нет корней"]
                        self.num_roots = 0
                    else:
                        x = math.sqrt(fourth_degree)
                        if x == 0:                          
                            self.roots_list.append(0)
                            self.num_roots = 1
                        else:                            
                            self.roots_list.append(math.sqrt(x))
                            self.roots_list.append(- math.sqrt(x))
                            self.num_roots = 2
            else:
                if self.coef_C == 0:                   
                    self.roots_list.append(0)
                    self.num_roots = 1
                    x = (- self.coef_B) / self.coef_A
                    if x > 0:                      
                        self.roots_list.append(math.sqrt(x))
                        self.roots_list.append(- math.sqrt(x))
                        self.num_roots = 3
                else:
                    discriminant = self.coef_B ** 2 - 4 * self.coef_A * self.coef_C
                    if discriminant < 0:                       
                        self.roots_list = ["Нет корней"]
                        self.num_roots = 0
                    elif discriminant == 0:
                        t = (- self.coef_B) / (2 * self.coef_A)
                        if t > 0:                           
                            self.roots_list.append(math.sqrt(t))
                            self.roots_list.append(- math.sqrt(t))
                            self.num_roots = 2
                        elif t == 0:                           
                            self.roots_list.append(0)
                            self.num_roots = 1
                        else:                           
                            self.roots_list = ["Нет корней"]
                            self.num_roots = 0
                    else:
                        t1 = (- self.coef_B + math.sqrt(discriminant)) / (2 * self.coef_A)
                        t2 = (- self.coef_B - math.sqrt(discriminant)) / (2 * self.coef_A)
                        self.roots_list = []
                        self.num_roots = 0
                        if t1 > 0:                          
                            self.roots_list.append(math.sqrt(t1))
                            self.roots_list.append(- math.sqrt(t1))
                            self.num_roots += 2
                        elif t1 == 0:                           
                            self.roots_list.append(0)
                            self.num_roots += 1
                        if t2 > 0:                           
                            self.roots_list.append(math.sqrt(t2))
                            self.roots_list.append(- math.sqrt(t2))
                            self.num_roots += 2
                        elif t2 == 0 and t1 != 0:                           
                            self.roots_list.append(0)
                            self.num_roots += 1                      
                        if t1 < 0 and t2 < 0:
                            self.roots_list = ["Нет корней"]
                            self.num_roots = 0

    def print_roots(self):
        if len(self.roots_list) == 1 and isinstance(self.roots_list[0], str):
            if self.num_roots == 0:
                print(self.roots_list[0])
            else:
                print("Произошла ошибка: несоответствие между количеством корней и списком корней")
        else:
            if self.num_roots == len(self.roots_list):
                if self.num_roots == 0:
                    print("Нет корней")
                else:
                    print("Корни:", self.roots_list)
            else:
                print("Произошла ошибка: несоответствие между количеством корней и списком корней")



def main():

    r = SquareRoots()
    r.roots_list = []
    r.get_coefs()
    r.calculate_roots()
    r.print_roots()

if __name__ == "__main__":
    main()
