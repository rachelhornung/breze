# -*- coding: utf-8 -*-

"""Sparse Filtering.

As introduced in

    Sparse Filtering
    Jiquan Ngiam, Pangwei Koh, Zhenghao Chen, Sonia Bhaskar and Andrew Y. Ng.
    In NIPS*2011.

"""

import numpy as np
import theano

from breze.arch.model.feature import SparseFiltering as _SparseFiltering
from breze.learn.base import (
    UnsupervisedBrezeWrapperBase, TransformBrezeWrapperMixin)


class SparseFiltering(_SparseFiltering, UnsupervisedBrezeWrapperBase,
                      TransformBrezeWrapperMixin):

    def __init__(self, n_inpt, n_feature, feature_transfer='softabs',
                 optimizer='lbfgs', max_iter=1000, verbose=False):
        """Create a SparseFiltering object.

        Parameters
        ----------

        n_inpt : int
            Input dimensionality of the data.
        n_feature : int
            Dimensionality of the hidden feature dimension.
        feature_transfer : string or callable
            Transfer function to use. If a string referring any function found
            in ``breze.arch.component.transfer`` or a function that given an
            (n, d) array returns an (n, d) array as theano expressions.
        max_iter : int
            Maximum number of optimization iterations to perform.
        verbose : bool
            Flag indicating whether to print out information during fitting.
        """
        super(SparseFiltering, self).__init__(
            n_inpt, n_feature, feature_transfer)
        self.f_transform = None
        self.parameters.data[:] = np.random.standard_normal(
            self.parameters.data.shape).astype(theano.config.floatX)
        self.optimizer = optimizer
        self.max_iter = max_iter
        self.verbose = verbose
