import sys

def print_contributors():
    contributors = ["Sebastien"]
    print("This is a Yale SOM class of 2025 project maintained by:")
    for cont in contributors:
        print("   " + cont)
    
    return

def addition(num_1, num_2):
    return num_1 + num_2

#main process
result = 0
if(len(sys.argv) < 4):
    print("Usage: arg1 operation arg2")
    print("    supported operations:")
    print("       + : addition")

else:
    num_1 = int(sys.argv[1])
    operation = sys.argv[2]
    num_2 = int(sys.argv[3])

    if(operation == '+'):
        result = addition(num_1, num_2)

    print("Result = " + str(result))

print_contributors()
