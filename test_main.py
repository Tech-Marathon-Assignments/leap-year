from main import main

# def isLapYear(year):
# 	if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
# 		print("It's a lap year", year)
# 	else:
# 		print("It's not a leap year", year)
#

# Test Case 1:
# Input: year = 2000
# Output: "2000 is a lap year"
def test_leap_year_true(capfd):
    main(2000)
    out, err = capfd.readouterr()
    assert out == "2000 is a lap year\n"

# Test Case 2:
# Input: year = 2001
# Output: "2001 is a lap year"
def test_leap_year_false(capfd):
    main(2001)
    out, err = capfd.readouterr()
    assert out == "2001 is not a lap year\n"
