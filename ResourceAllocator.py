import os
instances={
    0 : {
        0.12: "large",
        0.23: "xlarge",
        0.45: "2xlarge",
        0.774: "4xlarge",
        1.4: "8xlarge",
        2.82: "10xlarge"
    },
    1 : {
        0.14: "large",
        0.413: "2xlarge",
        0.89: "4xlarge",
        1.30: "8xlarge",
        2.97: "10xlarge"
    }
}
class calc:
    types = {
        0 : {
            1: "large",  
            2: "xlarge",
            4: "2xlarge",
            8: "4xlarge",
            16: "8xlarge",
            32: "10xlarge"
        },
        1 : {
            1: "large",
            4: "2xlarge",
            8: "4xlarge",
            16: "8xlarge",
            32: "10xlarge"
        }
    }

    def getKey(i,val):
        for key, value in instances[i].items():
             if val == value:
                 return key

    #To calculate the requirment of the server by using CPU count/Price
    def bySingleValue(value, hours, types, option): 
        if(option == "cpus"):
            c = [[32, 16, 8, 4, 2, 1], [32, 16, 8, 4, 1]] # 'c' - Used common variable for calculation
        elif(option == "price"):
            c = [[2.82, 1.4, 0.774, 0.45, 0.23, 0.12], [2.97, 1.3, 0.89, 0.413, 0.14]]
        serverType, serverCount = [], []
        for i in range(2):
            s = value
            st = [] # Intermediate state for server type
            sc = [] # Intermediate state for server count
            for j in range(len(c[i])):
                if(s == 0):
                    break
                elif(c[i][j] <= s):
                    if(s//(c[i][j]*hours) >= 1.0):
                        sc.append(int((s//(c[i][j]*hours))))
                        st.append(types[i][c[i][j]])
                        s = s%(c[i][j]*hours)      
            serverType.append(st)
            serverCount.append(sc)
        return serverCount, serverType

    #To calculate the requirment of the server by using both CPU count and Price
    def byCombinationOfBoth(hours, Cpus, Price, types): 
        serverOption = [[32, 16, 8, 4, 2, 1], [32, 16, 8, 4, 1]]
        priceOption = [[2.82, 1.4, 0.774, 0.45, 0.23, 0.12], [2.97, 1.3, 0.89, 0.413, 0.14]]
        c = [[0,0,0,0,0,0],[0,0,0,0,0]] #To store count of servers
        serverType, serverCount = [], []
        for i in range(2):
            cpus = Cpus 
            price = Price
            st = [] # Intermediate state for server type
            sc = [] # Intermediate state for server count
            while(cpus != 0 and price >= 1.0):
                for k in range(len(priceOption[i])):
                    if((price >= priceOption[i][k]*hours) and cpus >= serverOption[i][k]):
                        cpus -= serverOption[i][k]
                        price -= priceOption[i][k]*hours
                        c[i][k] += 1
            for j in range(len(c[i])):
                if(c[i][j] != 0):
                    sc.append(c[i][j])
                    st.append(types[i][serverOption[i][j]])
            serverType.append(st)
            serverCount.append(sc)
        return serverCount, serverType

    #getCost function - This function will seperate and supervise the calculation according to user's wish 
    def getCost(hours, cpus, price):
        serverCount, serverType = [], []
        if(price == 0 and cpus != 0):
            serverCount, serverType = calc.bySingleValue(cpus, 1, calc.types, "cpus")
        elif(cpus == 0 and price != 0):
            serverCount, serverType = calc.bySingleValue(price, hours, instances, "price")
        else: 
            serverCount, serverType = calc.byCombinationOfBoth(hours, cpus, price, calc.types)
        
        cost = []
        server = [[],[]]
        for i in range(2):
            c=0
            for j in range(len(serverCount[i])):
                costPerServer = calc.getKey(i,serverType[i][j])
                c += costPerServer*serverCount[i][j]
                server[i].append((serverType[i][j],serverCount[i][j]))
            cost.append(round(c*hours,2))
        region = ["us-east", "us-west"]
        result = [{},{}]
        for i in range(2):
            result[i].update({"region":region[i]})
            result[i].update({"total-cost":"$"+str(cost[i])})
            result[i].update({"server":server[i]})
        print(result)
        

def start():
    print("Select type")
    print("1. Minimum N CPUs for H hours")
    print("2. Maximum price they are willing to pay for H hours")
    print("3. Combination of both 1 and 2")
    try:
        option = int(input("Enter your Choice: "))

        if(option == 1):
            hours = int(input("Enter hours required: "))
            cpus = int(input("Enter the number of CPU required: "))
            calc.getCost(hours, cpus, 0)
        elif(option == 2):
            hours = int(input("Enter hours required: "))
            price = float(input("Enter how much price willing to pay: "))
            calc.getCost(hours, 0, price)
        elif(option == 3):
            hours = int(input("Enter hours required: "))
            cpus = int(input("Enter the number of CPU required: "))
            price = float(input("Enter how much price willing to pay: "))
            calc.getCost(hours, cpus, price)
        else:
            os.system("cls") # change 'cls' to 'clear' to run in linux
            print("\nPlease select among the given options\n")
            start()
    except ValueError:
        os.system("cls") # change 'cls' to 'clear' to run in linux
        print("\nPlease enter only numeric value...\n")
        start()

os.system("cls") # change 'cls' to 'clear' to run in linux
start()
