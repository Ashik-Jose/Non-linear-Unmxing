import os
from tkinter import Tk
from tkinter.filedialog import askdirectory
import non_linear_models_calculation

Tk().withdraw()

data_d = askdirectory(initialdir=os.getcwd(), title='Select a folder')
data_files = os.listdir(data_d)
# print(data_d)

lib_d = askdirectory(initialdir=os.getcwd(), title='Select a folder')
lib_files = os.listdir(lib_d)
# print(lib_d)

data_folder_name = os.path.join(data_d, data_files[0])
lib_folder_name = os.path.join(lib_d, lib_files[0])

print(data_folder_name)
print(lib_folder_name)

A=non_linear_models_calculation.non_linear_models_calculate(data_folder_name, lib_folder_name, data_files[0])

# for i in range(0, lib_files_size):
#     for j in range(0, data_files_size):
#         if lib_files[i] == 'micro_plastic_SVC.mat':
#             data_folder_name = os.path.join(data_d, data_files[j])
#             lib_folder_name = os.path.join(lib_d, lib_files[i])
#             print(lib_files[i])
#             print(data_files[j])
#             print(data_files[j] + '_SVC')
#             file_name = data_folder_name + '_SVC'
#             print(file_name)
#             # A, Y = non_linear_models_nasa_new(data_folder_name, lib_folder_name, file_name)
#         else:
#             print('other file')