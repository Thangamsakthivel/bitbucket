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

    def by(value, option, types):  #To calculate the requirment of the server by using CPU count 
        if(option == "cpus"):
            c = [[32, 16, 8, 4, 2, 1], [32, 16, 8, 4, 1]]
        elif(option == "price"):
            c = [[2.82, 1.4, 0.774, 0.45, 0.23, 0.12], [2.97, 1.3, 0.89, 0.413, 0.14]]
        serverType, serverCount = [], []
        for i in range(2):
            s = value
            st = []
            sc = []
            for j in range(len(c[i])):
                if(s == 0):
                    break
                elif(c[i][j] <= s):
                    st.append(types[i][c[i][j]])
                    sc.append(s//c[i][j])
                    s = s%c[i][j]      
            serverType.append(st)
            serverCount.append(sc)
        return serverCount, serverType

    def getCost(hours, cpus, price):
        serverCount, serverType = [], []
        if(price == 0 and cpus != 0):
            serverCount, serverType=calc.by(cpus, "cpus", calc.types)
            print(serverCount, serverType)
        elif(cpus == 0 and price != 0):
            serverCount, serverType=calc.by(price/hours, "price", instances)
            print(serverCount, serverType)
        else:
            pass           

print("Select type")
print("1. Minimum N CPUs for H hours")
print("2. Maximum price they are willing to pay for H hours")
print("3. Combination of both 1 and 2")
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

