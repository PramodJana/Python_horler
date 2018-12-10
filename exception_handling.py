try:
    print(x)
except:
    print("an error occured")


print("-----------------------------")
print("trying name error")
try:
    print(x)
except NameError:
    print("Variable x is not defined")
except:
    print("something else went wrong")



print("-----------------------------")
try:
  print("Hello")
except:
  print("Something went wrong")
else:
  print("Nothing went wrong")



print("------------------------------")
print("trying finally")
try:
  print(x)
except:
  print("Something went wrong")
finally:
  print("The 'try except' is finished")



print("-----------------------------------")
print("working with finally")
f = open("demofile.txt")
try:
  f.write("Lorum Ipsum")
except:
  print("Something went wrong when writing to the file")
finally:
  f.close()
