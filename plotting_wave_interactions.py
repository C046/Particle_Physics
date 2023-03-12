import plotly.graph_objs as go
import plotly.offline as pyo
import plotly.io as pio
from WaveFunctions import Wave
import numpy as np
import random


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
    
    
def _electric_field(self, x, y, z, t):
    """
    Parameters
    ----------
    x : float
        x coordinate
    y : float
        y coordinate
    z : float
        z coordinate
    t : float
        time variable

    Returns
        -------
        float
            Gives the electric field strength at any given point in space and 
            time. Taking into account both the amplitude of the wave and its
            phase. The sine function causes the electric field to oscillate
            between positive and negative values as the wave propages through
            space, which is characteristic of electromagnetic waves.
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
    #print(μ/ε)
    E0 = (self.c * (np.sqrt((μ/ε)*-1)*-1)) * B0
    #print(E0)
        
    return (E0 * np.sin(((k*x)+(k*y)+(k*z)-(ω*t))))

Photons = []
y_reals = []
y_imag = []
for i in range(0,4):
    mass, charge, spin = ((np.random.randint(10, 400)*NANOMETER), 0, np.random.RandomState().gamma((0),1))
    Photons.append(_particle(mass, charge, spin, radiation_type))

for i in Photons:
    Electric_Field_Generation = i._electric_field(np.random.RandomState().gamma((0),1),np.random.RandomState().gamma((0),1),np.random.RandomState().gamma((0),1),np.linspace(i.h, i.c*i.hbar, 500))
    y_reals.append(np.real(Electric_Field_Generation))
    y_imag.append(np.real(Electric_Field_Generation))

# Create 3D plot
fig = go.Figure()
for i in range(len(y_reals)):
    fig.add_trace(go.Scatter3d(x=np.linspace(1, 2*np.pi, 100), y=y_reals[i],z=y_imag[i]))


# Set axis labels
fig.update_layout(scene=dict(xaxis_title='t', yaxis_title='Real part', zaxis_title='Imaginary part'))

# Show plot
pyo.iplot(fig)
fig.write_html("Electric_Field(Photon).html")
    
