import timeit
from dynamic_programming import get_combination_counts
from greedy_algorithm import find_coins_greedy

amount = 123123
number = 1

def measure_time(func, number, *args):
    return timeit.timeit(lambda: func(*args), number=number) / number

time_greedy = measure_time(find_coins_greedy, number, amount)
time_dp = measure_time(get_combination_counts, number, amount)

print(f"Greedy time (avg of {number} runs): {time_greedy:.6f} sec")
print(f"DP time (avg of {number} runs): {time_dp:.6f} sec")
