#!/usr/bin/env python3

import numpy as np
from FADiff import FADiff


class Vect:
    def __init__(self, vect, der=None, parents=[], name=None, new_input=False):
        self._val = np.array(vect)
        if new_input:
            self._der = {}
            for vec_var in FADiff.vectors_list:
                self._der[vec_var] = 0
                vec_var._der[self] = 0
            self._der[self] = der * np.identity(len(vect))
            FADiff.vectors_list.append(self)
        else:
            self._der = der
        self.name = name  # TODO: Utilize somewhere?
        self.parents = parents

    # TODO
    def __sub__(self, other):
        try:
            derivs = {}
            for var, part_der in self._der.items():
                derivs[var] = part_der - other._der.get(var)
            # parents = self.set_parents(self, other)
            return Vect(self._val - other._val, derivs)#, parents)
        except AttributeError:
            # parents = self.set_parents(self)
            return Vect(self._val - other, self._der)#, parents)

    def __rsub__(self, other):
        return self.__sub__(other)

    def compute_jacobian(self):
        pass
