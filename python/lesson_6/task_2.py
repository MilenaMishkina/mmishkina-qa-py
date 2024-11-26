response = {
    "cartButtonEnabled": True,
    "conditions": {
        "campaign": {
            "id": "unlimited_burn_99rub_prd",
            "info": "Доставка в пункт выдачи от",
            "link": "https://support.avito.ru/articles/2369"
        },
        "destination": "по Дзержинску",
        "discount": 900,
        "minDays": 1,
        "price": 99,
        "terms": "От 1 дня, от",
        "trustfactors": [
            {
                "helpIcon": False,
                "icon": "cod",
                "label": "",
                "text": "Можно оплатить при получении"
            }
        ]
    },
    "services": [
        {
            "available": True,
            "enabled": True,
            "type": "delivery"
        },
        {
            "available": True,
            "enabled": True,
            "type": "deliveryCourier"
        },
        {
            "available": False,
            "enabled": False,
            "type": "deliveryCourierD2D"
        },
    ]
}

# Вывести значение ключа icon из списка trustfactors
response_icon = response["conditions"]["trustfactors"][0]["icon"]

# Вывести значение id из campaign
response_id = response["conditions"]["campaign"]["id"]

# Проверить, что helpIcon равен False

# 1) ВАРИАНТ
assert response["conditions"]["trustfactors"][0]["helpIcon"] == False, "helpIcon не равен False"
# 2) ВАРИАНТ
if response["conditions"]["trustfactors"][0]["helpIcon"] == False:
    print("helpIcon равен False")
else:
    print("helpIcon не равен False")

# Получите значение поля type третьего элемента списка services
response_type = response["services"][2]["type"]