def add(a, b): #remove : from here to check the pre-commit and pre-push hooks pre-commit will run first 
    return a + b

def divide(a, b):
    return a / b


def main():
    result = add(2, 3)
    #print("Result is:", result)  # ❌ will fail your print check


if __name__ == "__main__":
    main()
