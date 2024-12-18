def fopen(name, mode, enc="utf-8"):
    try:
        file = open(name, mode, encoding=enc)
    except FileNotFoundError:
        print("Файл не знайдено")
        return None
    else:
        return file

text = ("Never gonna give you up\n"
        "Never gonna let you down\n"
        "Never gonna run around and desert you\n"
        "Never gonna make you cry\n"
        "Never gonna say goodbye\n"
        "Never gonna tell a lie and hurt you\n")

text2 = ("Не шукай вечорами\n"
        "Ти у мене єдина\n"
        "Тільки ти, повір\n"
        "Бо твоя врода\n"
        "То є чиста вода\n"
        "То є бистрая вода\n"
        "З синіх гір\n")

file1_name = "cool_file.txt"

file1 = fopen(file1_name, "w")
file1.write(text)
file1.write("Андрій Чемарьов\n")
file1.write("\nДля наступного члену команди: Запиши до файлу кількі строк якої-небудь пісні і підрахуй кількість слів.\n")
file1.write(text2)
file1.write("Майборода Єгор\n")
file1.write("\nДля наступного члену команди: введи обмеження файлу до 200 символів.\n")
file1.close()

# Перечитуємо файл для підрахунку слів
file2 = fopen(file1_name, "r")
count = 0
if file2:
    for line in file2:
        words = line.split()
        count += len(words)
    file2.close()

# Дописуємо кількість слів
file1 = fopen(file1_name, "a")
file1.write(f"\nКількість слів: {count}\n")
file1.close()
file1 = fopen(file1_name, "r+")
file1.seek(0)  # Повертаємося на початок файлу, щоб перевірити вміст
content = file1.read()
    
    # Якщо довжина вмісту перевищує 200 символів, скорочуємо його
if len(content) > 200:
        file1.seek(0)
        file1.write(content[:200])
        file1.truncate()  # Обрізаємо будь-які символи після 200-го
file1.close()