### Solving for adiabatic cylinder, with a stream overdensity

$y_{in} = \lim_{r \to R^-}\rho(r)/\rho(0)$

$y_{out} = \lim_{r \to R^+}\rho(r)/\rho(0)$

$P = K\rho^\gamma, \rho = \rho_c y^n, n=\frac{1}{\gamma-1}$

$\alpha = (\frac{K_{out}}{K_{in}})^{1/\gamma} = \frac{y_{in}}{y_{out}}$

Initially, the solution from the center is the same, until it reaches $\rho(r) \approx y_{in}$. Note: here, $\rho(r)\propto y(r)^n$

Due to the change in constant, which is different across boundary, the normalization factor used for $x=r/r_c$ will change. With $r_c^2 = \frac{K(n+1)}{4\pi G \rho_c^{2-\gamma}}$, $x_{out} = x_{in}\alpha^{-\gamma/2}$

Initial condition for the stream is $\rho(R^+) = \rho(R^-)/\alpha$ and $y(R^+) = y(R^-)/\alpha^{(1/n)}$. 

The second condition is pressure gradient must be continuous, i.e. $\frac{dP_{out}}{dx_{in}}=\frac{dP_{in}}{dx_{in}}$.
Following the conversion to density, $\alpha^{\gamma/2}\frac{d\rho_{out}^\gamma}{dx_{out}}=\frac{d\rho_{in}^\gamma}{dx_{in}}$. Following that $\rho = \rho_c y^n$, $y_{out}' = \alpha^{\gamma/2-1}y_{in}'$
