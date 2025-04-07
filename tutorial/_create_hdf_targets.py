# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 10:02:37 2024

@author: Yannick Zander
"""

from maspim import get_project
from maspim.res.compound_masses import mC37_2, mC37_3, mPyro

import user_params
import logging

# path_folder_real_data = user_params.path_folder_real_data
path_folder_real_data = r'C:\Users\Yannick Zander\Promotion\Cariaco MSI 2024\490-495cm\2018_08_27 Cariaco 490-495 alkenones.i'
project = get_project(is_MSI=True, path_folder=path_folder_real_data)

logging.basicConfig(level=logging.INFO)
# project.set_hdf_file_targets(targets=[mC37_2, mC37_3, mPyro], delta_mz=5e-4, tolerances=3e-3 * 5)
# project.set_hdf_file()
# project.spectra.plot_summed()
project.require_spectra(targets=[mC37_2, mC37_3, mPyro], 
                        tolerances=3e-3, 
                        plts=True, 
                        overwrite=False, 
                        method='height',
                        tag='targeted')

print(project.spectra._line_spectra)
print(project.spectra.feature_table)

logging.basicConfig(level=logging.WARNING)
