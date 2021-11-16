from scipy import stats

class t:
    
    def __init__(self, dof):
        self.dof = dof

    def left_cdf(self, target):
        print(f"Pr(X <= {target}) = {stats.t.cdf(target, self.dof)}")

    def pdf(self, target):
        print(f"f({target}) = {stats.t.pdf(target, self.dof)}")
    
    def right_cdf(self, target):
        print(f"Pr(X >= {target}) = {1 - stats.t.cdf(target, self.dof)}")
    
    def ppf(self, target):
        print(f"Pr(X <= {stats.t.ppf(target, self.dof)}) = {target}")
        print(f"Pr(X >= {stats.t.ppf(1 - target, self.dof)}) = {target}")

    def __str__(self):
        return f"t-Distribution where degree of freedom  = {self.dof}"
