def send_mail(message, recipient,  sender="university.help@gmail.com"):
    if '@' not in recipient:
        print(f"Невозможно отправить письмо с адреса {sender}, на адрес {recipient}")
    elif '@' not in sender:
        print(f"Невозможно отправить письмо с адреса {sender}, на адрес {recipient}")
    if recipient[-4:] != '.com':
        if recipient[-4:] != '.net':
            if recipient[-3:] != '.ru':
                print(f"Невозможно отправить письмо с адреса {sender}, на адрес {recipient}")
    if sender[-4:] != '.com':
       if sender[-4:] != '.net':
            if sender[-3:] != '.ru':
                print(f"Невозможно отправить письмо с адреса {sender}, на адрес {recipient}")
            if sender == recipient:
                print('Нельзя отправить письмо самому себе!')
    elif sender != "university.help@gmail.com":
            print("НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса ", sender, "на адрес ", recipient, ".")
    elif sender == "university.help@gmail.com":
        print(f"Письмо успешно отправлено с адреса {sender}, на адрес {recipient}")

send_mail("Это сообщение для проверки связи", "vasyok1337@gmail.com")
send_mail('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_mail('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_mail('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')