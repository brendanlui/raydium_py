from raydium.cpmm import sell

if __name__ == "__main__":
    pair_address = "2KUEBor9P8e2YVGCUnD9ipmhGM9nL4pG11zeEoQVQZWg"
    percentage = 100
    slippage = 5
    sell(pair_address, percentage, slippage)
