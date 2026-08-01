def count_lower_upper(text):
    result = {"Uppercase": 0, "Lowercase": 0}

    for ch in text:
        if ch.isupper():
            result["Uppercase"] += 1
        elif ch.islower():
            result["Lowercase"] += 1

    return result
 
print(count_lower_upper("Hello World"))
print(count_lower_upper("PYTHON PROgramming"))