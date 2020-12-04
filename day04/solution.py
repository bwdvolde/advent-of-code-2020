import re

from read_file.read_file import read_file

mandatory_fields = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}
optional_fields = {"cid"}


def has_valid_fields(passport):
    all_mandatory_fields_present = all(field in passport for field in mandatory_fields)
    no_other_fields_present = all(field in mandatory_fields or field in optional_fields for field in passport)
    return all_mandatory_fields_present and no_other_fields_present


def has_valid_values(passport):
    if not 1920 <= int(passport["byr"]) <= 2002:
        return False
    if not 2010 <= int(passport["iyr"]) <= 2020:
        return False
    if not 2020 <= int(passport["eyr"]) <= 2030:
        return False
    hgt = passport["hgt"]
    hgt_value = int(hgt[:-2])
    if not ("cm" in hgt or "in" in hgt):
        return False
    if "cm" in hgt:
        if not 150 <= hgt_value <= 193:
            return False
    else:
        if not 59 <= hgt_value <= 76:
            return False
    if not re.match("#[0-9a-f]{6}", passport["hcl"]):
        return False
    if not passport["ecl"] in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
        return False
    if not re.match("^[0-9]{9}$", passport["pid"]):
        return False

    return True


if __name__ == '__main__':
    lines = read_file("input.txt")
    passports = []
    current_passport = {}
    for line in lines:
        if not line:
            passports.append(current_passport)
            current_passport = {}
        else:
            fields_with_values = [pair.split(":") for pair in line.split(" ")]
            for (field, value) in fields_with_values:
                current_passport[field] = value

    # Part 1
    count = 0
    for passport in passports:
        count += has_valid_fields(passport)

    count = 0
    for passport in passports:
        count += has_valid_fields(passport) and has_valid_values(passport)
    print(count)
