def main():
    #prob1()
    #prob2()
    #challenge1()
    challenge2()



def prob1():
    userInput= ""
    while True:
        if userInput=="Q":
            break
        if userInput=="q":
            break
        userInput= input("Enter somthing that makes you happy")
        print(userInput)

def prob2():
    prob2_helper(4,9,10,'prod')

def prob2_helper(num1,num2,num3, operation):
    if operation == 'sum':
        print("The sum is",int(num1+num2+num3))
    elif operation == 'prod':
        print("The product is",int(num1*num2*num3))
    elif operation == 'avg':
        print('The average it',int(num1+num2+num3/3))
    else:
        print("error")



def challenge1():
    userInput = input("How many starts do you want to print? ")
    count= 1
    for x in range(0,int(userInput)):
        print("*"*int(count))
        count += 1


def challenge2():
    userinput= input("Enter your speed")
    points= 0
    if int(userinput)<=70:
        print("ok")
    elif int(userinput)>70:
        for x in range(70,int(userinput),5):
            points= x
        if points>12:
            print("license suspended")
        else:
            print("Points: ",points)















if __name__ == '__main__':
    main()
