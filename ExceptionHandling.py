try:
    # a = 10
    # # b = 0
    # b = 2
    # c = a / b
    # print(c)
    age = 10
    if age<18:
        raise ValueError("not eligible for vote")
    else:
        print("eligible for vote")
except ZeroDivisionError as e:
    print("Exception occured => " +str(e))
except ValueError as e:
    print("Exception => " + str(e))

except:
    print("Exception occured")
else:
    print("Program Executed")
finally:
    print("Harman")

