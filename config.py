valid_email = "vmihailps@gmail.com"
valid_pass = "q1234567V"

invalid_email = 'vmihail@gmail.com'
invalid_pass = 'q54321'

name = 'Михаил'
surname = 'Михайлович'
region = 'Краснодар г'
email = 'vmihailps@gmail.com'
password = 'q1234567V'

false_email = '1234521'
false_mobile_max = '89108228304'
false_mobile_mini = '8910822830'
false_name_mini = 'B'
name_two_letters = "Ок"
thirty_letters = 'ZEFElwfvOSdNq0Gk6zwyJlw2HOJE9H'
thirty_one_letters = 'FJ2gZth1uSBghoMTbuCoK4X0AnvNXXf'

class TestData:
    BASE_URL = 'https://b2c.passport.rt.ru/'

    #Заголовки названий элементов
    FORM_AUTH_MAIL = 'Почта'
    AUTH = 'Авторизация'
    RECOVERY = 'Восстановление пароля'
    CHECK = 'Регистрация'
    VERIFICATION_EMAIL = 'Подтверждение email'
    VERIFICATION_INVALID_EMAIL = 'Введите телефон в формате +7ХХХХХХХХХХ или +375XXXXXXXXX, или email в формате example@email.ru'
    VERIFICATION_INVALID_NAME = 'Необходимо заполнить поле кириллицей. От 2 до 30 символов.'
    ENTRY_VK = 'Войти'
    OK = 'Одноклассники'
    CHOICE_ACCOUNT = 'Вход'
    MM = 'Войти и разрешить'
