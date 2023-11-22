testResult = int(input("Enter your test result: "))
maxResult = testResult
minResult = testResult

while testResult != -1:
    if testResult > maxResult:
        maxResult = testResult
    if testResult < minResult:
        minResult = testResult
    testResult = int(input("Please enter test result (-1 to finish): "))
    print("\nMaximum test result =", maxResult)
    print("Minimum test result =", minResult)