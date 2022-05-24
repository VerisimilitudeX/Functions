"""
LESSON: 6.1 - Functions
TECHNIQUE 2: Flags
PRACTICE 1
"""
#
#### ------------------------- ####
#### ---- TOTALS FUNCTION ---- ####
#### ------------------------- ####

# Add flag to function header
def totals(num_list, flag):                                   
#
    # Calculate total & average             
    total = 0
    for num in num_list:
        total += num
#
    avg = total / len(num_list)
#
    # Output values
    if flag:
        print("FINAL TOTAL: " + str(total))
    print("FINAL AVERAGE: " + str(avg))
#
    print()
#
#
#### ---------------------- ####
#### ---- MAIN PROGRAM ---- ####
#### ---------------------- ####
values = []
new_val = ""
#
#### ---- INPUT LOOP ---- ####
while new_val != "done":
    new_val = input("Enter a value to add (enter done to finish): ")

    if new_val == "done":
        break
    else:
        values.append(int(new_val))

    # Print partial total
    print("CURRENT TOTAL: ")
    totals(values)                                      
#
#
#### ----- FINAL OUTPUT ---- ####

# Print full total
totals(values)
#
#
# Turn in your Coding Exercise.
#
#
#
######################
##
#
#
#
##
#
##################
#
#
#
#
#
####################
#