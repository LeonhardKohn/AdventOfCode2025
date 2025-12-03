def rotaion_Left(current_value,value):
    zero_counter = 0
    new_value = (current_value - value)%100
    zero_counter = abs((current_value-value) // 100)
    if new_value == 0 and value !=0:
        zero_counter +=1
    if current_value ==0:
        zero_counter -= 1
    return new_value, zero_counter
    
def rotaion_Right(current_value,value):
    zero_counter = 0
    new_value = (current_value + value)%100
    zero_counter = abs((current_value + value) // 100)
    return new_value, zero_counter

def read_input():
    with open("day1_list", "r") as file:
        lines = file.readlines()
    return [line.strip() for line in lines]
    
# part 1
def simple_solver():
    lines = read_input()
    value = 50
    zero_count = 0
    for line in lines:
        rotaion, number = line[0], line[1:].lstrip()
        if rotaion == "L":
            value,_ = rotaion_Left(value, int(number))
        elif rotaion == "R":
            value,_ = rotaion_Right(value, int(number))
        else:
            print("Invalid rotation command:", rotaion)
            continue

        if value == 0:
            zero_count += 1

        #print(rotaion, number, "=>", value, "Zero Count:", zero_count)

    return zero_count

# part 2
def click_solver():
    lines = read_input()
    value = 50
    zero_count = 0
    tmp = 0
    for line in lines:
        rotaion, number = line[0], line[1:].lstrip()
        if rotaion == "L":
            value,tmp = rotaion_Left(value, int(number))
        elif rotaion == "R":
            value,tmp = rotaion_Right(value, int(number))
        else:
            print("Invalid rotation command:", rotaion)
            continue
        zero_count += tmp
        #print(rotaion, number, "=>", value, "Zero Count:", zero_count)

    return zero_count

def main():
    password = click_solver()
    print("Password:", password)


if __name__ == "__main__":
    main()

