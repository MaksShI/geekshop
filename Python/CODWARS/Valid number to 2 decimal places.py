def valid_number(n):
    try:
        print(n)
        n = float(n)
        n = int(n)
        return True
    except:
        return False


print(valid_number(".00-"))
