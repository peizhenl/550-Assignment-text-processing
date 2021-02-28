with open('fradulent_emails.txt', 'rb')as file:
    data = file.readlines()
    for o in range(len(data)):
        print("Word Strength", o)
        print(data[o])