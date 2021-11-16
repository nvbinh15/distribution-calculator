from scipy import stats

class poisson:
    
    def __init__(self, xlambda):
        self.xlambda = xlambda

    def left_cdf(self, target):
        print(f"Pr(X <= {target}) = {stats.poisson.cdf(target, self.xlambda)}")
    
    def pmf(self, target):
        print(f"Pr(X = {target}) = {stats.poisson.pmf(target, self.xlambda)}")
    
    def right_cdf(self, target):
        print(f"Pr(X > {target}) = {1 - stats.poisson.cdf(target, self.xlambda)}")

    def ppf(self, target):
        print(f"Pr(X <= {stats.poisson.ppf(target, self.xlambda)}) >= {target}")

    def __str__(self):
        return f"Poisson Distribution\nX: number of successes in a Poisson experiment." \
            + f"\nE(X) = V(X) = lambda = {self.xlambda}"
