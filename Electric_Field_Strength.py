def _electromagnetic_wave_number(self):
    """
    Returns electromagnetic wave number
    -------
    Description:
        calculates the wave number k of the electromagnetic wave

    """
    return (((2)*np.pi)/self.wavelength)
            
def _angular_frequency_(self):
    """
    Returns angular frequency 
    -------
    TYPE
        DESCRIPTION.

    """
    return ((2)*np.pi)*self.frequency
    
def _electric_field(self, xyz,t):
    """
    Parameters
    ----------
    xyz : TYPE
        x,y, or z parameter
    t : TYPE
        time variable

    Returns
    -------
    TYPE
        Gives the electric field strength at any given point in space and 
        time. Taking into account both the amplitude of the wave and its
        phase. The sine function causes the electric field to oscillate
        between positive and negative values as the wave propages through
        space, which is characterisitic of electromagnetic waves.
    """
    # Wavelength of electro-magnetic wave
    k = self._electromagnetic_wave_number()
    ω = self._angular_frequency_()
        
    ε = (8.85e-12-(FARAD*np.random.randint(1,10))) # permittivity of free space
    μ = 1.2566370614359172e-06 # permeability of free space
        
    def generate_photon_magnetic_field_oscillations(n,μ,ε):
        """Generates a list of n random magnetic field oscillations for a photon."""
        electric_field_oscillations = [random.uniform(0, 1) for i in range(n)]
        return [E / (self.c * (μ/ε)**0.5) for E in electric_field_oscillations]
    
    
 
    B0 = random.choice(generate_photon_magnetic_field_oscillations(25,μ,ε))
    E0 = self.c * np.sqrt(μ/ε) * B0

    return (E0 * np.sin(((k*xyz)-(ω*t))))
