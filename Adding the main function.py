
def searchName():
    user_input = input(">>").title()
    
    my_file = open("names.txt" , "r")
    
    for s in my_file:
        if s.startswith(user_input):
            print(s)

def searchAge():
    inline = open("names.txt", "r")
    user_input=str(input("Enter a number: "))
    
    for s in inline:
        if user_input in s:
            print(s)

            
if __name__=='__main__':
    
    pick = int(input("enter 1 to search for name or enter 2 to search for age: "))
    
    if pick == 1 :
        searchName()
    elif pick == 2:
        searchAge()
    else:
        print("Invalid Choice ")
