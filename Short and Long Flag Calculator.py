#### ------------------------- ####
#### ---- TOTALS FUNCTION ---- ####
#### ------------------------- ####
def totals(num_list, flag):                                   
    total = 0
    for num in num_list:
        total += num
    avg = total / len(num_list)

    if flag:
        print("FINAL TOTAL: " + str(total))
    print("FINAL AVERAGE: " + str(avg))
    print()

#### ---------------------- ####
#### ---- MAIN PROGRAM ---- ####
#### ---------------------- ####
values = []
new_val = ""

#### ---- INPUT LOOP ---- ####
while new_val != "done":
    new_val = input("Enter a value to add (enter done to finish): ")

    if new_val == "done":
        break
    else:
        values.append(int(new_val))

    print("CURRENT TOTAL: ")
    totals(values)                                      

#### ----- FINAL OUTPUT ---- ####
totals(values)
