def read_puzzel():
    with open("day2_puzzel", "r") as file:
        lines = file.readlines()
    return [line.strip() for line in lines]

def check_id_part1(id_number):
    digits = list(map(int, str(id_number)))
    length = len(digits)
    j = 0
    if length % 2 == 0:
        for i in reversed(range(length//2)): 
            if digits[i] != digits[length - 1 - j]:
                return False
            j += 1
        return True
    
def part1_solver():
    lines = read_puzzel()
    result = 0
    # Find invalid ID numbers
    for line in lines:
        for range in line.split(','):
            begin = range.split('-')[0]
            end = range.split('-')[1]
            current_number = int(begin)
            while current_number <= int(end):
                if check_id_part1(current_number) == True:
                    result += int(current_number)
                current_number = int(current_number) + 1
    print("Result:", result)

def check_id_part2(id_number):
    digits = list(map(int, str(id_number)))
    length = len(digits)

    for pattern_len in range(1, length // 2 + 1):
        if length % pattern_len != 0:
            continue
        pattern = digits[0:pattern_len]
        ok = True
        for i in range(0, length, pattern_len):
            if digits[i:i+pattern_len] != pattern:
                ok = False
                break
        if ok:
            return True
    return False       

def part2_solver():
    lines = read_puzzel()
    result = 0
    # Find invalid ID numbers
    for line in lines:
        for range in line.split(','):
            begin = range.split('-')[0]
            end = range.split('-')[1]
            current_number = int(begin)
            while current_number <= int(end):
                if check_id_part2(current_number) == True:
                    result += int(current_number)
                current_number = int(current_number) + 1
    print("Result:", result)



def main():
    print("Day 2")
    print("Part 1:")
    part1_solver()
    print("Part 2:")
    part2_solver()

if __name__ == "__main__":
    main()
    