from scipy import stats

class chi_sq:
    
    def __init__(self, dof):
        self.dof = dof
    
    def left_cdf(self, target):
        print(f"Pr(X <= {target}) = {stats.chi2.cdf(target, self.dof)}")
    
    def pdf(self, target):
        print(f"f({target}) = {stats.chi2.pdf(target, self.dof)}")
    
    def right_cdf(self, target):
        print(f"Pr(X > {target}) = {1 - stats.chi2.cdf(target, self.dof)}")
    
    def ppf(self, target):
        print(f"Pr(X <= {stats.chi2.ppf(target, self.dof)}) = {target}")
        print(f"Pr(X >= {stats.chi2.ppf(1 - target, self.dof)}) = {target}")

    def __str__(self):
        return f"Chi-squared Distribution where degree of freedom  = {self.dof}"
