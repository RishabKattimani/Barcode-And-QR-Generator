from barcode import EAN13

number = '5901234123457'

my_code = EAN13(number)

my_code.save("new_code")
