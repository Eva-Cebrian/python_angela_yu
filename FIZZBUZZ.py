# dibisible entre 3 FIZZ
# divisible entre 5 BUZZ
# dibisible entre 3 y 5 FIZZBUZZ

for i in range(1,101):
    if i % 3 == 0 and i % 5 == 0:
        print("FIZZBUZZ")
    elif i % 3 == 0:
        print("FIZZ")
    elif i % 5 == 0:
        print("BUZZ")
    else: print(i)