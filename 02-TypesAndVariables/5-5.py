price = float(input('Enter price: '))
discount = float(input('Enter discount %: '))
reduction = price * discount / 100
new_price = price - reduction
print(f'Price: {price:.2f}')
print(f'Discount: {discount}%')
print(f'Price with discount: {new_price:.2f}')
print(f'Reduction: {reduction:.2f}')