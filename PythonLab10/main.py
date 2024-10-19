#Функція, що відкриває файл і одразу перевіряє чи він відкрився
#Останнім аргументом  можна передати кодування(за замовчуванням utf-8)
def fopen(name, mode, enc = "utf-8"):
    try:
        file = open(name, mode, encoding = enc)
    except:
        print("File not found")
        return None
    else:
        return file


text = ("Never gonna give you up\n"
        "Never gonna let you down\n"
        "Never gonna run around and desert you\n"
        "Never gonna make you cry\n"
        "Never gonna say goodbye\n"
        "Never gonna tell a lie and hurt you\n")


file1_name = "cool_file.txt"

file1 = fopen(file1_name, "w")

file1.write(text)
file1.write("Андрій Чемарьов\n")
file1.write("\nДля наступного члену команди: Запиши до файлу кількі строк якої-небудь пісні.")

file1.close()
