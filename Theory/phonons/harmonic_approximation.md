In the harmonic approximation, the potential energy surface is 
$$E = V(R_1, R_2, ..., R_N)$$ 
which can be approximated as  Taylor expansion around a static equilibrium $R_0$.
$$E(R_0 + \Delta R) \approx E (R_0) + \sum_i \frac{\partial E}{\partial R_i} \Delta R_i + \frac{1}{2} \frac{\partial^2E}{\partial R_i \partial R_j} \Delta R_i \Delta R_j $$  
The first term in this equation is the static equilibirum energy (this is the term you would calculate with a "single point/single shot DFT calculation"). The second term (force term, because this is the first derivative of the energy) in this equation goes to zero at static equilibrium (because forces are zero at static equilibrium). The third term is the second derivative of the energy (the Hessian). 

Warning: this approximation is valid only for low temperatures, because at high temperatures the atoms start to move far from the static equlibrium. At high temperatures, the Taylor expansion energies at the hamonic level is not sufficent to describe the real potential energy surface. 

In many cases, this approximation is "good enough" to describe the physics of the system

The Hessian term or the harmonic force constants are generally harder to calculate the forces of the system. This is because the forces of a system are described by the Hellman-Feynman theorem.  It states that within the Born-Oppenheimer approximation, the ground state electrons determine the potential energy, so the potential energy surface is given by the expectation value of the Hamiltionian

$$U(R) = \braket{\psi_R|H_R|\psi_R}$$

So to calculate forces, which is the derivative of the potential energy, 
$$ F_i = -\frac{\partial U(R)}{\partial R_i} = \braket{\psi_R|\frac{\partial H_R}{\partial R_i}|\psi_R} - 2\braket{\psi_R|H_R| \partial \psi_R/\partial R_i}$$ 

The Hellman-Feynman theorem states that the second term in the above equation becomes zero, such that the force is an expectation value of the wavefunction and does not depend on the changes of the wavefunction. However, for the higher order derivative of the forces, such as the Hessian, the response of the wavefunction explicitly depends on the response of the wavefunction to atomic displacement. 

$$ \phi_{ij} = -\frac{\partial F_i}{\partial R_j} = \braket{\psi_R|\frac{\partial^2 H_R}{\partial R_i\partial R_j}|\psi_R} - 2\braket{\psi_R|\frac{\partial H_R}{\partial R_i}| \partial \psi_R/\partial R_i}$$ 

The second term does not vanish, and it needs to be computed explicity. This is also called as the "adiabatic electron phonon coupling" -- how does the wavefunction depend on the displcements of the atoms. 
