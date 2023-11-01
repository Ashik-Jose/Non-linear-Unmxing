import numpy as np
import scipy.io
import scipy.ndimage
import scipy.optimize
import non_linear_models
import pandas as pd
import rasterio

def non_linear_models_calculate(data_file, library_file, raw_file_name):
    # input image
    # y = scipy.ndimage.imread(data_file)
    # r, c, b = y.shape
    # t = r * c  # total number of pixels
    # y = np.transpose(y, (2, 0, 1))
    # y = y.reshape(b, t)
    # y = y.astype(float)

    # input image
    dataset = rasterio.open(data_file)
    cols = dataset.width
    rows = dataset.height
    bands = dataset.count
    with rasterio.open(data_file) as r:
        raster_matrix= r.read()
    y=raster_matrix.reshape(bands,(rows*cols))

    
    # input library
    excel_spectral = pd.read_excel(library_file)
    # print(excel_spectral)
    spectral_sig_names = excel_spectral.columns
    spectral_sig_names = np.asarray(spectral_sig_names)
    # print(spectral_sig_names)
    # print(excel_spectral.values)
    A=excel_spectral.values

    
    # processing all non linear models
    print('calculating unmixing of non linear models')
    # a_LMM, x_LMM, a_FM, x_FM, a_GBM, x_GBM, a_PPNM, x_PPNM, a_MLM, x_MLM, a_HAPKE, x_HAPKE = non_linear_models.nl_models_new(y, A)

    return A
    
    # # FAN_BL
    # print('FAN_BL')
    # abundance_size = a_FM.shape
    # s = abundance_size[0]
    # file_name = raw_file_name + '_FAN_BL'
    # # band_abundance, y, new_y = stats_unmixing(y, a_FM, x_FM, A, r, c, b, s, wavelengths, file_name)
    # # totat_stats = rmse_corl_covr_sre(y, new_y, file_name)
    # print('END of FAN_BL')
    
    # # GBM
    # print('GBM')
    # abundance_size = a_GBM.shape
    # s = abundance_size[0]
    # file_name = raw_file_name + '_GBM'
    # # band_abundance, y, new_y = stats_unmixing(y, a_GBM, x_GBM, A, r, c, b, s, wavelengths, file_name)
    # # totat_stats = rmse_corl_covr_sre(y, new_y, file_name)
    # print('END of GBM')
    
    # # HAPKE
    # print('HAPKE')
    # abundance_size = a_HAPKE.shape
    # s = abundance_size[0]
    # file_name = raw_file_name + '_HAPKE'
    # # band_abundance, y, new_y = stats_unmixing(y, a_HAPKE, x_HAPKE, A, r, c, b, s, wavelengths, file_name)
    # # totat_stats = rmse_corl_covr_sre(y, new_y, file_name)
    # print('END of HAPKE')
    
    # # MLMM
    # print('MLMM')
    # abundance_size = a_MLM.shape
    # s = abundance_size[0]
    # file_name = raw_file_name + '_MLMM'
    # # band_abundance, y, new_y = stats_unmixing(y, a_MLM, x_MLM, A, r, c, b, s, wavelengths, file_name)
    # # totat_stats = rmse_corl_covr_sre(y, new_y, file_name)
    # print('END of MLMM')
    
    # # PPNM
    # print('PPNM')
    # abundance_size = a_PPNM.shape
    # s = abundance_size[0]
    # file_name = raw_file_name + '_PPNM'
    # # band_abundance, y, new_y = stats_unmixing(y, a_PPNM, x_PPNM, A, r, c, b, s, wavelengths, file_name)
    # # totat_stats = rmse_corl_covr_sre(y, new_y, file_name)
    # print('END of PPNM')
