def priceCheck(products, productPrices, productSold, soldPrice):
    # Map product to its actual price
    price_map = {}
    for i in range(len(products)):
        price_map[products[i]] = productPrices[i]

    errors = 0

    # Compare sold price with actual price
    for i in range(len(productSold)):
        product = productSold[i]
        if soldPrice[i] != price_map[product]:
            errors += 1

    return errors
