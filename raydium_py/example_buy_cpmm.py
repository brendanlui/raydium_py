from raydium.cpmm import buy

if __name__ == "__main__":
    pair_address = "2KUEBor9P8e2YVGCUnD9ipmhGM9nL4pG11zeEoQVQZWg"
    sol_in = .1
    slippage = 5
    buy(pair_address, sol_in, slippage)
