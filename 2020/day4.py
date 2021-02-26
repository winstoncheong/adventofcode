import re 
#f = open("testin.txt",'r')
f = open("day4in.txt",'r')
lines = f.readlines()

def verify1(passport):
    # Naive validation for part 1
    keys = passport.keys()

    #print(len(keys))
    if len(keys) == 8:
        return True
    if len (keys) == 7: 
        # the field 'cid' is optional
        if "cid" not in keys: 
            return True

    # assume data isn't terrible
    return False 


def verify2(passport):
    # Verification for part 2

    try:
        byr = int(passport["byr"])
        if not (1920 <= byr <= 2002):
            # print("Bad byr", byr)
            return False

        iyr = int(passport["iyr"])
        if not (2010 <= iyr <= 2020):
            # print("Bad iyr: ", iyr)
            return False

        eyr = int(passport["eyr"])
        if not (2020 <= eyr <= 2030):
            # print ("Bad eyr: ", eyr)
            return False

        hgt = passport["hgt"]
        reg_hgt = r"(\d+)(cm|in)"

        m = re.match(reg_hgt, hgt)    
        if not m: # did not match
            # print("Bad hgt: ", hgt)
            return False 
        num = int(m.group(1))
        unit = m.group(2)
        # print("num: ", num)
        # print("unit: ", unit)

        if (unit == 'cm'):
            if not (150 <= num <= 193): 
                # print("Bad hgt", hgt)
                return False
        elif (unit == 'in'):
            if not (59 <= num <= 76):
                # print("Bad hgt: ", hgt)
                return False
        else:
            # print("Bad hgt: ", hgt)
            return False

        hcl = passport["hcl"]
        if not re.fullmatch("#[0-9a-f]{6}", hcl):
            # print("Bad hcl: ", hcl)
            return False

        eye_colors = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
        ecl = passport["ecl"]
        if ecl not in eye_colors:
            # print("Bad ecl: ", ecl)
            return False

        pid = passport["pid"]
        if not re.fullmatch("[0-9]{9}", pid):
            # print("Bad pid: ", pid)
            return False

        return True

    except KeyError as e:  # some passport field wasn't there
        # print("KeyError ", e)
        return False

    # Shouldn't get here...
    return True
    


count1 = 0
count2 = 0

# store keys
passport = {}

lines.append("\n") # need to process last passport

for line in lines:
    pairs = line.strip().split()

    if len(pairs) == 0: # detect newline
        # found end of passport
        # print('END OF PASSPORT')
        # print(passport)


        # for part 1
        valid = verify1(passport)
        #print("Valid: ", valid)
        if valid:
            count1 += 1

        # for part 2
        valid = verify2(passport)
        # print("Valid: ", valid)
        if valid:
            count2 += 1

        # begin new passport
        passport = {} 
        # print("\n")
        continue

    for pair in pairs:
        key, val = pair.split(':')
        passport[key] = val


print('Ans 1: ', count1)
print('Ans 2: ', count2)