from time import time
from multiprocessing import Pool, cpu_count

def factorize(*number):
    result = []
    for num in number:
        factors = []
        for i in range(1, num + 1):
            if num % i == 0:
                factors.append(i)
        result.append(factors)
    return result

if __name__ == '__main__':

    timer = time()
    a, b, c, d  = factorize(128, 255, 99999, 10651060)

    print(f'Done by 1 process: {round(time() - timer, 4)}')

    timer = time()
    with Pool(cpu_count()) as pool:
        a, b, c, d = pool.map(factorize, [128, 255, 99999, 10651060])

    print(f'Done by multiprocessing: {round(time() - timer, 4)}')