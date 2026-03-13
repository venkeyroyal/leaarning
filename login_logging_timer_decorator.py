import time

# Login decorator
def login_required(func):
    def inner(user):
        if user == "admin":
            print("Login successful")
            func(user)
        else:
            print("Access denied")
    return inner


# Logging decorator
def logger(func):
    def inner(user):
        print("Function started")
        func(user)
        print("Function finished")
    return inner


# Timer decorator
def timer(func):
    def inner(user):
        start = time.time()
        func(user)
        end = time.time()
        print("Execution time:", end-start)
    return inner


@timer
@logger
@login_required
def dashboard(user):
    print("Welcome to dashboard", user)


user = input("Enter username: ")
dashboard(user)