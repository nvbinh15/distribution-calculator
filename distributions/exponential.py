from scipy import stats

class exponential:
    
    def __init__(self, alpha):
        self.xlambda = 1 / alpha

    def left_cdf(self, target):
        print(f"Pr(X <= {target}) = {stats.expon.cdf(target, 0, self.xlambda)}")
    
    def pdf(self, target):
        print(f"f({target}) = {stats.expon.pdf(target, 0, self.xlambda)}")

    def right_cdf(self, target):
        print(f"Pr(X > {target}) = {1 - stats.expon.cdf(target, 0, self.xlambda)}")

    def ppf(self, target):
        print(f"Pr(X <= {stats.expon.ppf(target, 0, self.xlambda)}) = {target}")

    def __str__(self):
        return f"Exponential Distribution\n" \
            + f"E(X) = lambda = 1 / alpha = {self.xlambda}; V(X) = lambda^2 = 1 / (alpha ^2) = {self.xlambda * self.xlambda}"
