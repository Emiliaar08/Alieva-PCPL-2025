from operator import itemgetter

class Part:
    def __init__(self, id, name, weight, manufacturer_id):
        self.id = id
        self.name = name
        self.weight = weight
        self.manufacturer_id = manufacturer_id

class Manufacturer:
    def __init__(self, id, name):
        self.id = id
        self.name = name

class PartManufacturer:
    def __init__(self, manufacturer_id, part_id):
        self.manufacturer_id = manufacturer_id
        self.part_id = part_id

manufacturers = [
    Manufacturer(1, 'Завод А'),
    Manufacturer(2, 'Завод Б'),
    Manufacturer(3, 'Завод В'),
    Manufacturer(4, 'Завод Г'),
]

parts = [
    Part(1, 'Болт', 0.5, 1),
    Part(2, 'Гайка', 0.2, 1),
    Part(3, 'Винт', 0.3, 2),
    Part(4, 'Шуруп', 0.4, 2),
    Part(5, 'Гвоздь', 0.1, 3),
]

parts_manufacturers = [
    PartManufacturer(1, 1),
    PartManufacturer(4, 2),
    PartManufacturer(2, 3),
    PartManufacturer(3, 4),
    PartManufacturer(3, 5),
    PartManufacturer(1, 3),
    PartManufacturer(2, 5),
]

def main():
    one_to_many = [(p.name, p.weight, m.name) 
                   for m in manufacturers 
                   for p in parts 
                   if p.manufacturer_id == m.id]
    
    many_to_many_temp = [(m.name, pm.part_id) 
                         for m in manufacturers 
                         for pm in parts_manufacturers 
                         if m.id == pm.manufacturer_id]
    
    many_to_many = [(p.name, p.weight, man_name) 
                    for man_name, part_id in many_to_many_temp
                    for p in parts if p.id == part_id]
    
    print('Задание 1')
    res_1 = sorted(one_to_many, key=itemgetter(0))
    for item in res_1:
        print(f"{item[0]} - {item[2]}")

    print('\nЗадание 2')
    res_2_unsorted = []
    for m in manufacturers:
        m_parts = list(filter(lambda i: i[2] == m.name, one_to_many))
        if len(m_parts) > 0:
            res_2_unsorted.append((m.name, len(m_parts)))

    res_2 = sorted(res_2_unsorted, key=itemgetter(1))
    for item in res_2:
        print(f"{item[0]}: {item[1]} деталей")

    print('\nЗадание 3')
    res_3 = {}
    for p in parts:
        if p.name.endswith('т'):
            p_manufacturers = list(filter(lambda i: i[0] == p.name, many_to_many))
            manufacturers_names = [man_name for _, _, man_name in p_manufacturers]
            res_3[p.name] = manufacturers_names
    
    if res_3:
        for part_name, manufacturers_list in res_3.items():
            print(f"{part_name}: {', '.join(manufacturers_list)}")
    else:
        print("Деталей, оканчивающихся на 'т', не найдено")

if __name__ == '__main__':
    main()