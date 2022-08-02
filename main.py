from classes import Shop, Store, Request
print("Привет!")

storage_1 = Store(items={"Телефоны": 10, "Компьютеры": 10, "Телевизоры": 10})
storage_2 = Store(items={"Телефоны": 10, "Компьютеры": 10, "Приставка": 10})
shop_1 = Shop(items={"Телефоны": 3, "Компьютеры": 3, "Телевизоры": 3})

while True:
    print("Остатки товара")
    print(f"storage_1 : {storage_1}")
    print(f"storage_2 : {storage_2}")
    print(f"shop_1 : {shop_1}")
    user_text = input("Введите команду:\n")

    if user_text == "стоп":
        break
    else:
        req = Request(user_text)
        req.move()
