try:

    with open('numbers.txt','r') as file:
        word = file.read().split(",")
        count = 0
        for i in range(len(word)):
            if i%2==0:
                print(word[i])
            if i%2==1:
                user_answer = input("Otvet = ")
            if user_answer == word[i]:
                print("Vigrish!!!")
                count +=1
            else:print("Proigrish!")
        print(f"Vi pravilno otvichali {count} voprosov")

except:

    print("File ne naiden")