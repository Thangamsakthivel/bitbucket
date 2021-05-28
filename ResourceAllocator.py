class calc:
    types = {
        1: "large",
        2: "xlarge",
        4: "2xlarge",
        8: "4xlarge",
        16: "8xlarge",
        32: "10xlarge"
    }
    print(types[1])
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
    def getCost(instances, hours, cpus, price):
        print(calc.uswest["large"])

    def byCpu(hours,cpus):
        binary = []
        while cpus != 0:
            binary.append(cpus%2)
            cpus = cpus/2

print("Enter your Choice")
print("1. Minimum N CPUs for H hours")
print("2. Maximum price they are willing to pay for H hours")
print("3. Combination of both")

option = int(input(">>>"))

if(option == 1):
    hours = int(input("Enter hours required: "))
    cpus = int(input("Enter the number of CPU required: "))
elif(option == 2):
    hours = int(input("Enter hours required: "))
    price = float(input("Enter how much price willing to pay: "))
elif(option == 3):
    hours = int(input("Enter hours required: "))
    cpus = int(input("Enter the number of CPU required: "))
    price = float(input("Enter how much price willing to pay: "))

c = calc
