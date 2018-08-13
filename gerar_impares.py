def impares(min, max):
    result = [];
    for n in range(min, max):
        if n % 2 != 0:
            result.append(n)
    return result

if __name__ == '__main__':
    print(impares(100, 201))
