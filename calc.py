principal = input("Please input principal: ")
rate = input("Please input rate: ")
time = input("Please input time in months: ")

d = int(time)/12

PRT = int(principal) * int(rate) * int(d)
result = int(PRT) /100

total_fee = int(result) + int(principal)

def output():
    print("Your Simple Interest is: "+ str(result) + " total fee payable is " + str(total_fee))


output()
