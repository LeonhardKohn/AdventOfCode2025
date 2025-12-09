from functools import cache
from operator import index
def read_input(file_path):
    with open(file_path, 'r') as file:
        data = file.readlines()
    return [line.strip() for line in data]

def part1(data):
    max_jolts = 0
    for line in data:
        digits = [int(d) for d in line if d.isdigit()]
        d1 = max(digits[:-1])
        max_pos = digits.index(d1)
        rest = digits[max_pos+1:]
        d2 = max(rest) if rest else 0
        max_jolts += d1*10 + d2

    print("Part 1 Result:", max_jolts)
    return max_jolts

def part2(data):
  max_jolts = 0

  for line in data:
    digits = [int(d) for d in line if d.isdigit()]
    rest = digits.copy()
    twelve_jolts = 0
    for i in range(12):        
        max_digit = max(rest[:-11+i] if i != 11 else rest)
        rest = rest[rest.index(max_digit)+1:] 
        twelve_jolts = twelve_jolts + max_digit * (10 ** (12-i-1))
    print(twelve_jolts)
    max_jolts += twelve_jolts  
  print("Part 2 Result:", max_jolts)
  return max_jolts



def main():
    data = read_input("day3_puzzel")
    part1(data)
    part2(data)

    
if __name__ == "__main__":
    main()