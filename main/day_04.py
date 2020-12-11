from main.file_reader import read


def validate_passports(lines: list, validate_value: bool) -> int:
    byr = iyr = eyr = hgt = hcl = ecl = pid = False

    num_valid_passports = 0

    for line in lines:
        if not line:
            if byr and iyr and eyr and hgt and hcl and ecl and pid:
                num_valid_passports += 1

            byr = iyr = eyr = hgt = hcl = ecl = pid = False
        else:
            splits = line.split(" ")
            for split in splits:
                code, value = split.split(":")
                if code == "byr":
                    byr = not validate_value or 1920 <= int(value) <= 2002
                if code == "iyr":
                    iyr = not validate_value or 2010 <= int(value) <= 2020
                if code == "eyr":
                    eyr = not validate_value or 2020 <= int(value) <= 2030
                if code == "hgt":
                    if not validate_value:
                        hgt = True
                    elif not (value.endswith("cm") or value.endswith("in")):
                        hgt = False
                    else:
                        height, units = int(value[:-2]), value[-2:]
                        if units == "cm":
                            hgt = 150 <= height <= 193
                        else:
                            hgt = 59 <= height <= 76

                if code == "hcl":
                    hcl = not validate_value or (
                        len(value) == 7
                        and value[0] == "#"
                        and contains_only_digits_or_letters_to_f(value[1:])
                    )
                if code == "ecl":
                    ecl = not validate_value or value in {
                        "amb",
                        "blu",
                        "brn",
                        "gry",
                        "grn",
                        "hzl",
                        "oth",
                    }
                if code == "pid":
                    pid = not validate_value or (len(value) == 9 and value.isdigit())

    if byr and iyr and eyr and hgt and hcl and ecl and pid:
        num_valid_passports += 1

    return num_valid_passports


def contains_only_digits_or_letters_to_f(str):
    for c in str:
        if not (c.isdigit() or ("a" <= c <= "f")):
            return False
    return True


if __name__ == "__main__":
    input = read("day04-01.txt")
    print(validate_passports(input, validate_value=False))  # 235
    print(validate_passports(input, validate_value=True))  # 194
