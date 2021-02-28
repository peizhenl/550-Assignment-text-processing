with open('fradulent_emails.txt', 'rb')as file:
    data = file.readlines()
    for p in range(len(data)):
        print("now", p)
        print(data[p])