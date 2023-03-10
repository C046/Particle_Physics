class _particle(Wave):
    def __init__(self, Mass, Charge, Spin, Radiation_type):
        """
        Description:
            This class represents the particle as a particle and a wave.
            It expresses and describes the particle-wave duality.

        Properties:
            [
                Photons are massless particles that require the wavelength
                to caclulate its energy. Since we have neither the frequency
                or wavelength, we need to define the type of radiation the
                photon belongs to. We have three kinds of radiation for
                particles. Alpha,Beta, and Gamma.

                - Alpha Particles/Alpha Radaition: Alpha particles are made of
                two neutrons, and are emitted from the nucleus of an atom but
                this is during radio-active decay. They have a positive charge
                and are relatively heavy, These particles are stopped by a
                piece of paper or even skin such as a hand, also dangerous
                if injested. ~I am serious, I laughed too.~

                - Beta Particles/ Beta Radiation: Beta particles are HIGH SPEED
                ELECTRONS OR even POSITRONS emitted from the nucleus of an atom
                during radio-active decay. They HAVE A NEGATIVE CHARGE and are
                LIGHTER than ALPHA particles, so they can penetrate deeper into
                matter. You can stop these particles by a few millimeters of
                aluminum or a thin sheet of plastic.

                _______________________________________________________________
                ##### -WARNING -#####
                  ~ Pay attention to this detail below, it is about photons. ~
                _______________________________________________________________
                ##### -WARNING -####

                - Gamma Rays: GAMMA RAYS are HIGH ENERGY PHOTONS emitted from
                the nucleus of an tom during radio-active decay. These are NOT
                PARTICLES, but rather ELECTRO-MAGNETIC RADIATION. They have NO
                CHARGE, these gamma rays are HIGHLY PENETRATING, meaning they
                CAN TRAVEL THROUGH thick layers of LEAD OR CONCRETE.

            ]
        """
        super().__init__()
        # Define the mass of particle
        self.mass = Mass
        # Define the charge of the partcle
        self.charge = Charge
        # Define the spin of the particle
        # This may change
        self.spin = Spin
        # Define a size ranges
        self.nanometer = 1e-09
        self.milimeter = 1e-3
        # Define Rydbergs constant in J
        self.R_H = 2.1798741e-18

        # self.RADIO_WAVE_VALUE_RANGE = np.random.randint(0,1000000)*self.milimeter
        # self.INFARED_LIGHT_VALUE_RANGE = np.random.randint(700,1000000)*self.nanometer
        # self.VISIBLE_LIGHT_VALUE_RANGE = np.random.randint(400,699)*self.nanometer
        # self.ULTRA_VIOLET_VALUE_RANGE = np.random.randint(10,399)*self.nanometer
        # self.X_RAY_VALUE_RANGE = np.random.randint(0.01,9)*self.nanometer
        # self.GAMMA_RAY_VALUE_RANGE = 0.1-(np.random.randint(1,1000000)*self.nanometer)

        # Define radiation types allowed.
        self.radiation_type = {
            "Gamma_Rays": 0,
            "Beta_Particles": 0,
            "Alpha_Particles": 0,
            "Radio_Waves": 0,
            "Microwaves": 0,
            "Infared": 0,
            "VisibleLight": [
                "Violet",
                "Blue",
                "Green",
                "Yellow",
                "Orange",
                "Red",
            ],
            "Ultraviolet": 0,
            "X_Ray": 0,
        }
        # Wrap entire script a try, exception. At failure default to Gamma.
        try:
            # Set the capital for var radiation_type
            capital = Radiation_type.capitalize()[0]
            # If the capital is == V
            # Set the radiation type and randomize the visible light selection.
            if capital == "V":
                radiation_type = "VisibleLight"
                self.radiation_type = (
                    radiation_type, random.choice(
                        self.radiation_type[radiation_type]
                    )
                )
            try:
                # If the radiation type is still visible light, create a dict
                # from the radiation type.
                if Radiation_type in self.radiation_type["VisibleLight"]:
                    self.radiation_type = ("VisibleLight", Radiation_type)
                else:
                    # Else iterate through all types of radiation
                    # checking for matches.
                    for rads in self.radiation_type:
                        if rads[0] == "V":
                            pass
                        else:
                            if rads[0] == capital:
                                self.radiation_type = (rads, 1)
            except Exception:
                pass

        except Exception:
            # Defaults to gamma
            self.radiation_type = {"Gamma_Rays": 1}

        # Define the wavelength of the particle using its mass
        self.wavelength = self.Photon_wavelength(self.mass)
        # Define a frequency of the particle using its wavelength
        self.frequency = self.Photon_frequency(self.wavelength)
        # Define the mass again as energy.
        self.energy = self.Photon_energy(self.frequency)
        # Define principle quantum number
        self.PQN = self._principle_quantum_number(self.energy)

    def _interaction(self, Particle):
        pass

    ##### WARNING #####
    # Functions for an electron are within this section
    def _principle_quantum_number(self, energy):
        """
        Parameters
        ----------
        energy : FLOAT -2.1798741e-18 < (energy)
            The qunatum number of an energy level in an atom.
            This describes the energy, orbital shape, and orientation of an
            electron in that level.

        Returns
        -------
        TYPE
            INT32

        """
        return np.round((-energy/self.R_H)**0.5).real
    "_________________________________________________________________________"

    
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
