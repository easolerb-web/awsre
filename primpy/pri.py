# Function to check if a number is prime
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# List to store prime numbers
primes = []

# Find primes between 1 and 250
for num in range(1, 251):
    if is_prime(num):
        primes.append(num)

# Display the prime numbers
print("Prime numbers between 1 and 250:")
for p in primes:
    print(p)

# Save results to a file
with open("results.txt", "w") as file:
    file.write("Prime numbers between 1 and 250:\n")
    for p in primes:
        file.write(str(p) + "\n")

print("\nResults have been saved to results.txt")