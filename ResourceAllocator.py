class calc:
    types = {
        1: "large",
        2: "xlarge",
        4: "2xlarge",
        8: "4xlarge",
        16: "8xlarge",
        32: "10xlarge"
    }

    def byCpu(hours, cpus):
        c = [[32, 16, 8, 4, 2, 1], [32, 16, 8, 4, 1]]
        p = [[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
        serverType = []
        serverCount = []
        for i in range(2):
            s = cpus
            for j in range(len(c[i])):
                if(s == 0):
                    break
                elif(c[i][j] <= s):
                    p[i][j] = s//c[i][j]
                    s = s%c[i][j]
            st = []
            sc = []
            for j in range(len(p[i])):
                if(p[i][j] != 0):
                    st.append(calc.types[c[i][j]])
                    sc.append(p[i][j])
            serverType.append(st)
            serverCount.append(sc)
        return serverCount,serverType

    def getCost(instances, hours, cpus, price):
        if(price == 0):
            serverCount,serverType=calc.byCpu(hours, cpus)
            print(serverCount,serverType)


instances={
    "useast" : {
        "large": 0.12,
        "xlarge": 0.23,
        "2xlarge": 0.45,
        "4xlarge": 0.774,
        "8xlarge": 1.4,
        "10xlarge": 2.82
    },
    "uswest" : {
        "large": 0.14,
        "2xlarge": 0.413,
        "4xlarge": 0.89,
        "8xlarge": 1.3,
        "10xlarge":2.97
    }
}

print("Select type")
print("1. Minimum N CPUs for H hours")
print("2. Maximum price they are willing to pay for H hours")
print("3. Combination of both 1 and 2")
option = int(input("Enter your Choice: "))

if(option == 1):
    hours = int(input("Enter hours required: "))
    cpus = int(input("Enter the number of CPU required: "))
    calc.getCost(instances, hours, cpus, 0)
elif(option == 2):
    hours = int(input("Enter hours required: "))
    price = float(input("Enter how much price willing to pay: "))
elif(option == 3):
    hours = int(input("Enter hours required: "))
    cpus = int(input("Enter the number of CPU required: "))
    price = float(input("Enter how much price willing to pay: "))
