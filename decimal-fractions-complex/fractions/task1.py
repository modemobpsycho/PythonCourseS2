from fractions import Fraction

numbers = [
    '6.34', '4.08', '3.04', '7.49', '4.45', '5.39', '7.82', '2.76', '0.71',
    '1.97', '2.54', '3.67', '0.14', '4.29', '1.84', '4.07', '7.26', '9.37',
    '8.11', '4.30', '7.16', '2.46', '1.27', '0.29', '5.12', '4.02', '6.95',
    '1.62', '2.26', '0.45', '6.91', '7.39', '0.52', '1.88', '8.38', '0.75',
    '0.32', '4.81', '3.31', '4.63', '7.84', '2.25', '1.10', '3.35', '2.05',
    '7.87', '2.40', '1.20', '2.58', '2.46'
]

for i in numbers:
    print(f"{i} = {Fraction(i)}")
