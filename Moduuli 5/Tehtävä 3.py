def is_prime(n):
    if n<2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
user_input = int(input("Syötä kokonaisluku:"))
if is_prime(user_input):
    print(str(user_input) + "on alkuluku")
else:
    print(str(user_input) + "ei ole alkuluku.")