Author:'TalithaDunn'
DateCreated:'30/4/2022'
Course:'ITT103'
Purpose:'this is a python program from the pervieous pseudocode'

terminate=True
while terminate==True:
 sales = int(input('enter sales: '))
 rate = int(input('enter rate: '))
 Class = int(input('enter class: '))
 print("sales: ")
 print("rate: ")
 print("class: ")
 if Class == 1:
    if sales <= 1000:
        print(0.06 * sales)
    elif 1000 < sales <= 2000:
        print(0.07 * sales)
    else:
        print(0.1 * sales)
 elif Class == 2:
    if sales <= 1000:
        print(0.04 * sales)
    else:
        print(0.06 * sales)
 elif Class == 3:
    print(0.045 * sales)
    break 
else:
    print('invaild class')
    
end=input('enter 0 to end the program')
if end ==0:
      terminate==False 
    
