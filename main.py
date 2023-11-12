def calculate_simple_interest(principal, rate, time):
    # Simple Interest formula: SI = P * R * T / 100
    simple_interest = (principal * rate * time) / 100
    return simple_interest

def calculate_compound_interest(principal, rate, time):
    # Compound Interest formula: CI = P * (1 + R/100)^T - P
    compound_interest = principal * (pow((1 + rate / 100), time)) - principal
    return compound_interest

# Input values
principal_amount = float(input("Enter principal amount: "))
interest_rate = float(input("Enter annual interest rate: "))
time_period = float(input("Enter time period (in years): "))

# Calculate and display simple interest
simple_interest_result = calculate_simple_interest(principal_amount, interest_rate, time_period)
print(f"\nSimple Interest: {simple_interest_result:.2f}")

# Calculate and display compound interest
compound_interest_result = calculate_compound_interest(principal_amount, interest_rate, time_period)
print(f"Compound Interest: {compound_interest_result:.2f}")
