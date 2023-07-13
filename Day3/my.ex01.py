def ending_balance(principal, apr, years, interest_frequency):
    return principal * pow(1+apr/interest_frequency, years * interest_frequency)


principal = 40000
apr = 0.06
years = 3
frequency = 12

print(ending_balance(principal, apr, years, frequency))

