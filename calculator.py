import sys

def print_contributors():
    contributors = ['Tungalag']
    print("This is a Yale SOM class of 2025 project maintained by:")
    for cont in contributors:
        print("   " + cont)
    
    return


#main process
if(len(sys.argv) == 1):
    print("Usage: operation arg1 arg2")
    print("    supported operations:")

print_contributors()