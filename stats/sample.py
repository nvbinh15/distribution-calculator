import statistics

def sample_params(sample_points):
    print(f"Sample points: " + str(sample_points))
    print(f"Number of sample points n = {len(sample_points)}")
    print(f"Sample mean mu = {statistics.mean(sample_points)}")
    print(f"Sample standard deviation s = {statistics.stdev(sample_points)}")
    print(f"Sample variance s^2 = {statistics.variance(sample_points)}")
