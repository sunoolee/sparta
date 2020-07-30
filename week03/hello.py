fruits = ['사과', '배', '배', '감', '수박', '귤', '딸기', '사과', '배', '수박']

def count_fruits(name):
    apple = 0
    for fruit in fruits:
        if fruit is name:
            apple += 1
    return apple

print(count_fruits('수박'))