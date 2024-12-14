def read_cookbook(recipes_dic):
    cookbook = {}
    current_dish = None

    with open(recipes_dic, 'r', encoding='utf-8') as file:
        for line in file:
            line = line.strip()
            if not line:  # Если строка пустая, пропускаем её
                continue

            if line.endswith(':'):  # Если строка заканчивается на двоеточие
                current_dish = line[:-1]  # Убираем двоеточие
                cookbook[current_dish] = []  # Создаём пустой список для ингредиентов
            else:
                if current_dish:  # Если текущее блюдо уже задано
                    try:
                        ingredient, quantity, measure = line.split('|')  # Разделяем строку по |
                        quantity = int(quantity) if quantity.isdigit() else quantity  # Преобразуем количество
                        measure = measure.strip()  # Убираем лишние пробелы
                        cookbook[current_dish].append({
                            'ingredient_name': ingredient.strip(),
                            'quantity': quantity,
                            'measure': measure
                        })
                    except ValueError:
                        print(f"Ошибка в строке: {line}")
                        continue  # Пропускаем некорректную строку
    print(cookbook)

    return cookbook