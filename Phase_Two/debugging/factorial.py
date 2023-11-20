def factorial(n):
    product = 1
    while n > 1:
        
        product *= n        
        n -= 1
    return product

print(f"""
    Running: factorial(5)
  Exptected: 120
     Actual: {factorial(5)}
""")

print(f"""
    Running: factorial(7)
  Exptected: 5040
     Actual: {factorial(7)}
""")

print(f"""
    Running: factorial(10)
  Exptected: 3628800
     Actual: {factorial(10)}
""")