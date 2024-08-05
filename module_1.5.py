immutable_val = 1, 2, "True", False, "my string" # val чтобы подчеркнуть неизменяемость
print(immutable_val)
"""
immutable_val[0] = True # краш потому что объект кортеж не поддерживает назначение элементов
"""
mutable_var = [1,2,"True",False,"my string"]
print(f"Mutable obj:\n{mutable_var}")
if("True" in mutable_var):
    mutable_var.remove("True")
mutable_var[0] = True
mutable_var.reverse()
print(f"changed list\n{mutable_var}")