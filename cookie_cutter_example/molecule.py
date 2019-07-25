"""
molecule.py
A python package for the MolSSI Software Summer School.
Contains a molecule class
"""

import numpy as np
from cookie_cutter_example.measure import *
#UPDATE: I imported this into __init__.py. from .measure import calculate_angle, calculate_distance #we moved these functions to the measure.py in the working directory. Could import all with import *, but it's best practice to import just the functions that you need. Because we had the code written as if the measure functions were in this module and we don't want to modify all the function calls (which we'd have to do if we did import .measure), we use 'from .module import function1, function2'. By doing so, we can just directly call function1 and function2 in this script.
class Molecule:
    def __init__(self, name, symbols, coordinates):
        if isinstance(name, str):
            self.name = name
        else:
            raise TypeError("Name is not a string.")

        self.symbols = symbols
        self._coordinates = coordinates
        self.bonds = self.build_bond_list()

    @property
    def num_atoms(self):
        return len(self.coordinates)

    @property
    def coordinates(self):
        return self._coordinates  #please don't directly change coordinates

    @coordinates.setter  #NOTE: 'coordinates.setter' is a crucial naming. If my function was boop, I'd have to use the boop.setter decorator
    def coordinates(self, new_coordinates):#NOTE: I could use a different name for this function and the code wouldn't break: it doesn't have to be named the same as it is in property. THAT SAID, then I'd have to use the getter molecule.coordinates and the setter molecule.whateverInameit = []. This would be a mess.
        self._coordinates = new_coordinates  #instead, use this to change coordinates.
        self.bonds = self.build_bond_list()  #if coordinates change, recheck bonding

    def build_bond_list(self, max_bond=2.93, min_bond=0):
        """
        Build a list of bonds based on a distance criteria.
        Atoms within a specified distance of one another will be considered bonded.
        Parameters
        ----------
        max_bond : float, optional
        min_bond : float, optional
        Returns
        -------
        bond_list : list
            List of bonded atoms. Returned as list of tuples where the values are the atom indices.
        """

        bonds = {}

        for atom1 in range(self.num_atoms):
            for atom2 in range(atom1, self.num_atoms):
                distance = calculate_distance(self.coordinates[atom1], self.coordinates[atom2])

                if distance > min_bond and distance < max_bond:
                    bonds[(atom1, atom2)] = distance

        return bonds


if __name__ == "__main__":
    # Do something if this file is invoked on its own
    random_coordinates = np.random.random([3, 3])
    name = 'molecule'
    symbols = ['H', 'O', 'H']

    my_molecule = Molecule(name, symbols, random_coordinates)

    print(F'There are {len(my_molecule.bonds)} bonds')
    print(F'The coords are {my_molecule.coordinates}')

    #random_coordinates = np.random.random([3,3])
    random_coordinates[0] += 100
    my_molecule.coordinates = random_coordinates  #what's actually happening is pythonis using the coordinates.setter decorator to change coordinates
    print(
        F'\nThere are {len(my_molecule.bonds)} bonds, and we didnt call updatebondlist, it was in the _coordinates.setter wrapper'
    )
    print(F'The coords are {my_molecule.coordinates}')
    pass
