def main():
    list_of_item_prices = [10, 4, 20]
    discount(list_of_item_prices)  # Expect this to print 4
    # what other lists might this function be called with?
    

def discount(item_prices):
    """ Complete this function that returns the discount earned for a list of item prices
    If a customer has ordered more than three items, the cheapest item is free.
    Example: if this function is called with a list of [10, 4, 20] then return 4.

    if no discount will be taken, return 0
    What appropriate if function is called with weird/invalid data?
    """
    # numberofitems = len(item_prices)

    # cheapest_item = min(item_prices)
    #print(sorted(item_prices))
    if len(item_prices) > 3:
        for i in item_prices:
            i = min(item_prices)
            return i

    elif len(item_prices) < 3:
        return 0
    
    if item_prices == None:
        raise ValueError('Need list')
    # elif len(item_prices) == 0:
    #     raise ValueError('No items in cart.')
    
    else:
        return None
    
    
    
    # pass  # todo replace this line with your code 


if __name__ == '__main__':
    main()