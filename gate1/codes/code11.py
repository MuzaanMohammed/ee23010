def is_true(e_x, var_x):
    np = e_x
    np_1_minus_p = var_x

    if np_1_minus_p <= np:
        return "True case."
    else:
        return "False case1."

if __name__ == "__main__":
    e_x = float(input("Enter the value of E(X): "))
    var_x = float(input("Enter the value of Var(X): "))

    result = is_true(e_x, var_x)
    print(result)
