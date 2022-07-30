# myfile = open('test.txt', 'r')
# print(myfile)
# myfile.close()

# try:
#     somefile = open('test.txt', 'w')
#     try:
#         somefile.write('Hello')
#     except Exception as e:
#         print(e)
#     finally:
#         somefile.close()
#         print('Finally')
# except Exception as ex:
#     print(ex)


# with open('test.txt', 'a') as somefile:
#     # somefile.write('\tHello world')
#     print('Hello world', file=somefile)

# with open('test.txt', 'r', encoding='UTF=8') as file:
#     for line in file:
#         print(line, end="\n")
#     str1 = file.readline()
#     print(str1, end='')
#     str2 = file.readline()
#     print(str2, end='')
#     line = file.readline()
#     while line:
#         print(line, end='')
#         line = file.readline()

    # content = file.read()
    # print(content)

    # content = file.readlines()
    # print(content[3])
    # text = file.read()
    # print(text)


# FILENAME = 'msg.txt'
# msgs = []
#
# for i in range(4):
#     msg = input(f"Введите строку {i}:")
#     msgs.append(msg + "\n")
#
# # print(msgs)
#
#
# with open(FILENAME, 'a') as file:
#     for msg in msgs:
#         file.write(msg)
#
#
#
# with open(FILENAME) as file:
#     for msg in file:
#         print(msg, end="")


import csv


FILENAME = 'users.csv'
users = [
    ['Tom', 28],
    ['Alice', 23],
    ['Bob', 34]

]

with open(FILENAME, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(users)

with open(FILENAME, 'a', newline="") as file:
    user = ['Sam', 31]
    writer = csv.writer(file)
    writer.writerow(user)

with open(FILENAME, 'r', newline='') as file:
    reader = csv.reader(file)
    for row in reader:
        print(f"{row[0]} - {row[1]}")


