# TODO Your solution(s)
def change(amount):
    # Calculate the number of quarters (25c)
    quarters = amount // 25
    # Calculate the remaining amount after using quarters
    amount %= 25

    # Calculate the number of dimes (10c)
    dimes = amount // 10
    # Calculate the remaining amount after using dimes
    amount %= 10

    # Calculate the number of nickels (5c)
    nickels = amount // 5

    # The remaining amount is in cents
    cents = amount % 5

    return (quarters, dimes, nickels, cents)









