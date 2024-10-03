def cinema_ticket_buy(age: int, adult: False, full_name=None):
    """
    Функция для покупки билета в кинотеатр,
    которая  проверяет возраст и наличие взрослого сопровождающего, если человеку меньше 18
    """
    if age < 18 and adult == True:
        print("Билет продан под присмотром взрослого")
    elif age < 18:
        print("Нельзя продать билет")
    else:
        print("Покупка совершена! Возьмите Ваш билет.")

cinema_ticket_buy(age = 17, adult=True)