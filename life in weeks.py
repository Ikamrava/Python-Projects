age = input("Please input your age: ")

remainigAge = 90 - int(age)
remainingWeeks = remainigAge * 52
remainingDays = remainigAge * 365
remainingMonths = remainigAge * 12

print(f"If you live 90 years , You have {remainingDays} days, {remainingWeeks} weeks, and {remainingMonths} months left")