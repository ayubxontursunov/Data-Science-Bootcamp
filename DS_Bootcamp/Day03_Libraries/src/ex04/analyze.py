import pstats

# Load the profiling data
p = pstats.Stats('profiling-http.prof')

# 1. Sorted by total time spent in the function
print("Sorted by total time spent in the function:")
p.sort_stats('tottime').print_stats()

# Save the result to profiling-tottime.txt
with open('profiling-tottime.txt', 'w') as f:
    p.sort_stats('tottime').stream = f
    p.print_stats()

# 2. Sorted by the number of calls
print("Sorted by number of calls:")
with open('profiling-ncalls.txt', 'w') as f:  # Make sure the file is open here
    p.sort_stats('ncalls').stream = f
    p.print_stats()  # Now it will write to the file

# 3. Sorted by cumulative time spent in the function
print("Sorted by cumulative time spent in the function:")
with open('profiling-cumulative.txt', 'w') as f:  # Make sure the file is open here
    p.sort_stats('cumtime').stream = f
    p.print_stats(5)  # Get the top 5 functions
