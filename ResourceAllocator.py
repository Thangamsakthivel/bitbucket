region = ["uswest","useast"]
r = int(input("Select region\n1.uswest\n2.useast\nEnter your choice: "))-1

class calc:
    types = {
        1: "large",
        2: "xlarge",
        4: "2xlarge",
        8: "4xlarge",
        16: "8xlarge",
        32: "10xlarge"
    }
    useast = {
        "large": 0.12,
        "xlarge": 0.23,
        "2xlarge": 0.45,
        "4xlarge": 0.774,
        "8xlarge": 1.4,
        "10xlarge": 2.82
    }
    uswest = {
        "large": 0.14,
        "2xlarge": 0.413,
        "4xlarge": 0.89,
        "8xlarge": 1.3,
        "10xlarge":2.97
    }

    def getCost(hours, serverCount, serverType):
        

    def byCpu(hours,cpus):
        if(region[r] == "useast"):
            c = [32, 16, 8, 4, 2, 1]
            p = [0, 0, 0, 0, 0, 0]
        elif(region[r] == "uswest"):
            c = [32, 16, 8, 4, 1]
            p = [0, 0, 0, 0, 0]
        s = cpus
        for i in range(len(c)):
            if(s == 0):
                break
            elif(c[i] <= s):
                p[i] = s//c[i]
                s = s%c[i]
        serverType = []
        serverCount = []
        for i in range(len(p)):
            if(p[i] != 0):
                serverType.append(calc.types[c[i]])
                serverCount.append(p[i])
        calc.getCost(hours, serverCount, serverType)


print("Select type")
print("1. Minimum N CPUs for H hours")
print("2. Maximum price they are willing to pay for H hours")
print("3. Combination of both 1 and 2")
option = int(input("Enter your Choice: "))

if(option == 1):
    hours = int(input("Enter hours required: "))
    cpus = int(input("Enter the number of CPU required: "))
    calc.byCpu(hours,cpus)
elif(option == 2):
    hours = int(input("Enter hours required: "))
    price = float(input("Enter how much price willing to pay: "))
elif(option == 3):
    hours = int(input("Enter hours required: "))
    cpus = int(input("Enter the number of CPU required: "))
    price = float(input("Enter how much price willing to pay: "))
    
    
