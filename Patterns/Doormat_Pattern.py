# CODE: Mr.Vincent works in a door mat manufacturing company.One day, he designed a new door mat with the following
# specifications:
# - Mat size must be X.( is an odd natural number, and is times.)
# - The design should have 'WELCOME' written in the center.
# - The design pattern should only use |., and - characters.
# Sample Designs
# Size: 7 x 21
# ---------.|.---------
# ------.|..|..|.------
# ---.|..|..|..|..|.---
# -------WELCOME-------
# ---.|..|..|..|..|.---
# ------.|..|..|.------
# ---------.|.---------

# Size: 11 x 33
# ---------------.|.---------------
# ------------.|..|..|.------------
# ---------.|..|..|..|..|.---------
# ------.|..|..|..|..|..|..|.------
# ---.|..|..|..|..|..|..|..|..|.---
# -------------WELCOME-------------
# ---.|..|..|..|..|..|..|..|..|.---
# ------.|..|..|..|..|..|..|.------
# ---------.|..|..|..|..|.---------
# ------------.|..|..|.------------
# ---------------.|.---------------

def pattern(row, column):
    for i in [*range(1, row // 2 + 1), 0, *range(row // 2, 0, -1)]:
        print(f"{(2 * i - 1) * '.|.' if i else 'WELCOME'}".center(column, '-'))


pattern(7, 21)
print()
pattern(9, 27)
print()
pattern(11, 33)
