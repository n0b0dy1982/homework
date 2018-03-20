def have_trains_crashed(v1, v2):
    if v2 >= v1 * 1.5:
        return True
    else:
        return False
print(have_trains_crashed(12, 16))