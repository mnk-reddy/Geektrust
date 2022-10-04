from sys import argv

COST={'CAR':100,'TRUCK':200,'BUS':200,'VAN':100,'RICKSHAW':100,'SCOOTER':50,'MOTORBIKE':50}
FASTAG=dict()
ONEWAY=[]
COLLECTION=[0,0]
DISCOUNT=0
TYPE={'BUS':[0,0],'CAR':[0,0],'MOTORBIKE':[0,0],'RICKSHAW':[0,0],'SCOOTER':[0,0],'TRUCK':[0,0],'VAN':[0,0]}
FLAT_FEE=40

# store vehicle details which has fastag
def fastag(number,balance):
    global FASTAG
    FASTAG[number]=int(balance)

# check if its first trip or round trip
def isoneway(number,type):
    global ONEWAY,COST,DISCOUNT
    factor=1
    if number in ONEWAY:        # if its round trip
        ONEWAY.remove(number)
        factor=0.5
        DISCOUNT+=COST[type]*factor
    else:
        ONEWAY.append(number)
    
    return COST[type]*factor

# Collect toll from cash
def collect_cash(type,fee,balance=0):   
    global COLLECTION,FLAT_FEE

    COLLECTION[1]+=FLAT_FEE+fee-balance
    TYPE[type][1]+=FLAT_FEE

#check if sufficient balance in fastag or not
def sufficient_balance(number,fee):
    global FASTAG
    return FASTAG[number]>=fee 

# Collect toll from cash
def collect_fastag(type,number,fee):
    global FASTAG,COLLECTION
    
    if sufficient_balance(number,fee):
        COLLECTION[0]+=fee
        FASTAG[number]-=fee
    else:                                    # if not enough balance in fastag
        collect_cash(type,fee,FASTAG[number])   
        COLLECTION[0]+=FASTAG[number]
        FASTAG[number]=0
# Check for toll collection type 
def toll(type,number):
    global FASTAG,TYPE
    # toll fee based on round trip or not
    fee=isoneway(number,type)

    if number in FASTAG:
        collect_fastag(type,number,fee)
    else:
        collect_cash(type,fee)
    TYPE[type][0]+=1
    TYPE[type][1]+=fee

# print the vehicle summary
def vehicle_summary():
    global TYPE
    min=0
    Sorted=sorted(TYPE.items(), key=lambda x: x[1][1],reverse=True)
    for vehicle in Sorted:
        if vehicle[1][1]>min:
            print(vehicle[0],vehicle[1][0])

# final output
def print_collection():
    global COLLECTION,DISCOUNT
    print('TOTAL_COLLECTION %d %d'%(sum(COLLECTION),DISCOUNT))
    print('PAYMENT_SUMMARY %d %d'%(COLLECTION[0],COLLECTION[1]))
    print('VEHICLE_TYPE_SUMMARY')
    vehicle_summary()

def isfastag(tag):
    return tag=='FASTAG'

def istoll(tool):
    return tool=='COLLECT_TOLL'

# check for the input command 
def checkrule(rule):
    rule=rule.split()
    if(isfastag(rule[0])):
        fastag(rule[1],rule[2])
    elif(istoll(rule[0])):
        toll(rule[1],rule[2])
    else:
        print_collection()

def main():
    # code to read inputs from the file
    if len(argv) != 2:
        raise Exception("File path not entered")
    global TYPE
    file_path = argv[1]
    f = open(file_path, 'r')
    lines = f.readlines()
    for line in lines:
        checkrule(line)
if __name__ == "__main__":
    main()