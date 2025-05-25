import requests
import pandas as pd


def get_product_info(article_id):
    url = f"https://card.wb.ru/cards/detail?appType=1&curr=rub&dest=-1257786&nm={article_id}"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        print(f"Ошибка: статус {response.status_code}")
        return None

    data = response.json()
    if not data.get('data') or not data['data'].get('products'):
        print("Товар не найден.")
        return None

    product = data['data']['products'][0]

    return {
        'id': product['id'],
        'Название': product['name'],
        'Бренд': product.get('brand'),
        'Цена': product['priceU'] // 100,
        'Цена со скидкой': product['salePriceU'] // 100,
        'Рейтинг': product.get('rating'),
        'Отзывы': product.get('feedbacks'),
        'link': f"https://www.wildberries.ru/catalog/{product['id']}/detail.aspx"
    }

def main():
    article_id = input("Введите артикул товара Wildberries:\n").strip()
    if not article_id.isdigit():
        print("Ошибка: артикул должен быть числом")
        return

    product = get_product_info(article_id)
    if product:
        print("Информация о товаре:")
        for k, v in product.items():
            print(f"{k}: {v}")

if __name__ == "__main__":
    main()
