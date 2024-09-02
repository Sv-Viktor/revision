def send_email(message, recipient, *, sender="university.help@gmail.com"):
    if '@' not in recipient:
        if ".com" not in recipient:
            if ".ru" not in recipient:
                if ".net" not in recipient:
        print("Невозможо отправить письмо с адреса", sender, "на адрес", recipient)
    elif sender == recipient:
        print("Нельзя отправить письмо самому себе!")
    elif sender == "university.help@gmail.com":
        print("Письмо успешно отправлено с адреса", sender, "на адрес", recipient)
    else:
        print("НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса", sender, "на адрес", recipient)
