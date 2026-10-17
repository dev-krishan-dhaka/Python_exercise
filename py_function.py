# Python fundamentals practice
def greet(name):
    return f"Hello, {name}!"

# 1. Dictionary and loop practice
scores = {"Math": 85, "Python": 90, "English": 78}

print(greet("Dev"))
print("\nScores:")
for subject, score in scores.items():
    print(f"{subject}: {score}")

# 2. List comprehension
passed = [sub for sub, score in scores.items() if score > 80]
print(f"\nPassed subjects: {passed}")