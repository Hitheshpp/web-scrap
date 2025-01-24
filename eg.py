def function_2(var_1):
    var_1.append("D")
    print("second ", var_1)
    return

var_1 = ["E"]
print("first ",var_1)
function_2(var_1)
print("third ",var_1)