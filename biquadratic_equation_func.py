import sys
import math

def get_coef(index, prompt):
        
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

def get_coefs(coefficients):

    coefficients[0] = get_coef(1, 'Введите коэффициент А:')
    coefficients[1] = get_coef(2, 'Введите коэффициент B:')
    coefficients[2] = get_coef(3, 'Введите коэффициент C:')
        
    return coefficients

def calculate_roots(coefficients, result):
      
    num_roots = 0
    roots_list = []

    if coefficients[0] == 0:
        if coefficients[1] == 0:
            if coefficients[2] == 0:
                roots_list = ["Бесконечное множество корней"]
                num_roots = 0
            else:
                roots_list = ["Нет корней"]
                num_roots = 0
        else:
            if coefficients[2] == 0:
                roots_list.append(0)
                num_roots = 1 
            else:
                x = (- coefficients[2]) / coefficients[1]
                if x > 0:
                    roots_list.append(math.sqrt(x))
                    roots_list.append(- math.sqrt(x))
                    num_roots = 2
                elif x == 0:
                    roots_list.append(0)
                    num_roots = 1
                else:
                    roots_list = ["Нет корней"]
                    num_roots = 0
    else:
        if coefficients[1] == 0:
            if coefficients[2] == 0: 
                roots_list.append(0)
                num_roots = 1
            else:
                fourth_degree = (- coefficients[2]) / coefficients[0]
                if fourth_degree < 0:                        
                    roots_list = ["Нет корней"]
                    num_roots = 0
                else:
                    x = math.sqrt(fourth_degree)
                    if x == 0:                          
                        roots_list.append(0)
                        num_roots = 1
                    else:                            
                        roots_list.append(math.sqrt(x))
                        roots_list.append(- math.sqrt(x))
                        num_roots = 2
        else:
            if coefficients[2] == 0:                   
                roots_list.append(0)
                num_roots = 1
                x = (- coefficients[1]) / coefficients[0]
                if x > 0:                      
                    roots_list.append(math.sqrt(x))
                    roots_list.append(- math.sqrt(x))
                    num_roots = 3
            else:
                discriminant = coefficients[1] ** 2 - 4 * coefficients[0] * coefficients[2]
                if discriminant < 0:                       
                    roots_list = ["Нет корней"]
                    num_roots = 0
                elif discriminant == 0:
                    t = (- coefficients[1]) / (2 * coefficients[0])
                    if t > 0:                           
                        roots_list.append(math.sqrt(t))
                        roots_list.append(- math.sqrt(t))
                        num_roots = 2
                    elif t == 0:                           
                        roots_list.append(0)
                        num_roots = 1
                    else:                           
                        roots_list = ["Нет корней"]
                        num_roots = 0
                else:
                    t1 = (- coefficients[1] + math.sqrt(discriminant)) / (2 * coefficients[0])
                    t2 = (- coefficients[1] - math.sqrt(discriminant)) / (2 * coefficients[0])
                    roots_list = []
                    num_roots = 0
                    if t1 > 0:                          
                        roots_list.append(math.sqrt(t1))
                        roots_list.append(- math.sqrt(t1))
                        num_roots += 2
                    elif t1 == 0:                           
                        roots_list.append(0)
                        num_roots += 1
                    if t2 > 0:                           
                        roots_list.append(math.sqrt(t2))
                        roots_list.append(- math.sqrt(t2))
                        num_roots += 2
                    elif t2 == 0 and t1 != 0:                           
                        roots_list.append(0)
                        num_roots += 1                      
                    if t1 < 0 and t2 < 0:
                        roots_list = ["Нет корней"]
                        num_roots = 0
        
    result = [num_roots, coefficients, roots_list]
    return result

def print_roots(result):
        if len(result[2]) == 1 and isinstance(result[2][0], str):
            if result[0] == 0:
                print(result[2][0])
            else:
                print("Произошла ошибка: несоответствие между количеством корней и списком корней")
        else:
            if result[0] == len(result[2]):
                if result[0] == 0:
                    print("Нет корней")
                else:
                    print("Корни:", result[2])
            else:
                print("Произошла ошибка: несоответствие между количеством корней и списком корней")



def main():
    result = [0, [0.0, 0.0, 0.0], []]
    coefficients = [0.0, 0.0, 0.0]
    coefficients = get_coefs(coefficients)
    result = calculate_roots(coefficients, result)
    print_roots(result)

if __name__ == "__main__":
    main()
