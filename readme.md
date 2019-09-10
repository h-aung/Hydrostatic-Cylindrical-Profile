# README

Requirement: python, numpy, scipy

Run by ./gen_profile.py

The parameters can be changed in line 95-97 of `gen_profile.py`. `gamma` is adiabatic index, `mu` is normalized mass per unit length, `delta` is density ratio of central axis to stream edge ($\delta_c$ in Aung+ 19), and `box_res` is the unit length of box in units of radius of stream ($1/R_s$ where $R_s$ is the value in namelist file as Rstream, the default in Aung+ 19 for `box_res` is 32). To save time, you may comment out line 105 of  `gen_profile.py` after you have runned the script at least once with the same gamma. The profile is generated as `profile_gamma*_mu*_delta*.txt`



Some related equations for applying boundary condition at stream radius and pressure normalization below. Open in markdown editors or copy and paste to latex to see equations.

### Solving for adiabatic cylinder, with a stream overdensity 

$y_{in} = \lim_{r \to R^-}\rho(r)/\rho(0)$

$y_{out} = \lim_{r \to R^+}\rho(r)/\rho(0)$

$P = K\rho^\gamma, \rho = \rho_c y^n, n=\frac{1}{\gamma-1}$

$\alpha = (\frac{K_{out}}{K_{in}})^{1/\gamma} = \frac{y_{in}}{y_{out}}$

Initially, the solution from the center is the same, until it reaches $\rho(r) \approx y_{in}$. Note: here, $\rho(r)\propto y(r)^n$

Due to the change in entropy, which is different across boundary, the normalization factor used for $x=r/r_c$ will change. With $r_c^2 = \frac{K(n+1)}{4\pi G \rho_c^{2-\gamma}}$, $x_{out} = x_{in}\alpha^{-\gamma/2}$

Initial condition for the stream is $\rho(R^+) = \rho(R^-)/\alpha$ and $y(R^+) = y(R^-)/\alpha^{(1/n)}$. 

$\frac{\partial P}{\partial r} = -\rho\frac{\partial \phi}{\partial r}$

The second condition is pressure gradient has same factor as density from first thermo equation and gradient of potential is continuous, i.e. $\alpha\frac{dP_{out}}{dx_{in}}=\frac{dP_{in}}{dx_{in}}$.
Following the conversion to density, $\alpha^{1+\gamma/2}\frac{d\rho_{out}^\gamma}{dx_{out}}=\frac{d\rho_{in}^\gamma}{dx_{in}}$. Following that $\rho = \rho_c y^n$, $y_{out}' = \alpha^{-\gamma/2}y_{in}'$

### Pressure Normalization

The code unit of pressure in RAMSES needs to be normalized by $\frac{k_b}{m_p}(\frac{t_0}{L_0})^2\frac{T}{\mu}$ where $t_0 = 1/\sqrt{G\rho_c}$ and $L_0 = xR_s$ is unit length of box, $x$ is `box_res` in parameter list.

Using $\rho_c = c_s^2/4\pi Gr_c^2 (\gamma-1)$ and $L_0 = xr_c(R_s/r_c)$, the pressure normalization can be written as $\frac{4\pi (\gamma-1)}{\gamma x^2 (R_s/r_c)^2}$.