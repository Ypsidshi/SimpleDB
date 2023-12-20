import sqlite3

database = sqlite3.connect("log_and_pass.db")
cursor = database.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS users (
    login TEXT,
    password TEXT
)""")

database.commit()

choice = input("Вход или Регистрация? 1 / 2: ")

if choice == "1":
    login = input('Login: ')

    cursor.execute(f"SELECT login FROM users WHERE login = ?", (login,))
    user = cursor.fetchone()

    if user is not None:
        password = input("Password: ")

        cursor.execute(f"SELECT password FROM users WHERE login = ?", (login,))
        stored_password = cursor.fetchone()[0]

        if stored_password == password:
            print("Вы вошли в систему!")
        else:
            print("Неверный пароль!")
    else:
        print("Пользователя не существует!")
elif choice == "2":
    inp_login = input("Login: ")
    inp_password = input("Password: ")

    cursor.execute("SELECT login FROM users WHERE login = ?", (inp_login,))
    existing_user = cursor.fetchone()

    if existing_user is None:
        cursor.execute("INSERT INTO users VALUES (?, ?)", (inp_login, inp_password))
        database.commit()
        print("Пользователь зарегистрирован!")
    else:
        print("Такой пользователь уже есть!")
