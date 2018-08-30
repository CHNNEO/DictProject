import traceback

a =10
try :
    b = a/0
except Exception as e:
    traceback.print_exc()
else:
    print(b)
print("============")