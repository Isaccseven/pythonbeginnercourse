try:
    x = 5
except:
    print('Error')
finally:
    print('The "try" is finished')




x = -1

if x < 0:
    raise Exception("Sorry, no numbers below zero")



try:
    f = open("demofile.txt")
    try:
        f.write("Lorum Ipsum")
    except:
        print("Something went wrong when writing to the file")
    finally:
        f.close()
except:
    print("Something went wrong when opening the file")
