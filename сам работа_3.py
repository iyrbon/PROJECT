import requests

def get_categories():
    url = "https://fakestoreapi.com/products/categories"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print("Ошибка при получении категорий товаров.")
        return []

def get_products_by_category(category):
    url = f"https://fakestoreapi.com/products/category/{category}"
    response = requests.get(url)
    if response.status_code == 200:
        products = response.json()
        for product in products:
            print(f"Название: {product['title']}")
            print(f"Цена: ${product['price']:.2f}")
            print(f"Описание: {product['description']}\n")
    else:
        print(f"Ошибка при получении товаров из категории {category}.")

def main():
    categories = get_categories() 
    if not categories:
        print("Не удалось получить список категорий.")
        return

    print("Доступные категории:")
    for i, category in enumerate(categories, start=1):
        print(f"{i}. {category}")

    try:
        category_index = int(input("Введите номер категории: ")) - 1
        selected_category = categories[category_index]
        get_products_by_category(selected_category)
    except (ValueError, IndexError):
        print("Некорректный ввод. Пожалуйста, выберите номер категории из списка.")

if __name__ == "__main__":
    main()