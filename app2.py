# HOW TO BREAK PASSWORD WITH PYTHON BRUTE FORCE ATTACK?
# 2 - READING FROM TEXT DOCUMENT

passwd = "P%kek]+Mx%"
passwd_list = []
with open("passwd.txt", "r", encoding="utf-8") as pwd:
    passwords = pwd.readlines()
    for password in passwords:
        passwd_list.append(password.replace("\n", ""))

# print(passwd_list)

value = 0
for passwd in passwd_list:
    print(passwd)
    value += 15
    if passwd == passwd:
        print("Password : " + str(passwd) + " found in the result attempt #" + str(value))
        break
