
with open('fradulent_emails.txt', 'rb')as file:
    data = file.readlines()
    for i in range(len(data)):
        print("urgent", i)
        print(data[i])
