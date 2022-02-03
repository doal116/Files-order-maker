import instantiating_files as inst_f
import moving_files as mov_f

files_info = []

'''Instantiation of files: 
file directory, file name, file extension'''
inst_f.file_s.instantiating_from_directory()

'''Storing instantiated elements in list of main py file'''
files_info = inst_f.file_s.list_files

user_input = input('Proceed to the rearrengement [yes/no]?:')

if user_input == 'yes':
    '''Creation of the folders that will 
    hold the files of same extension'''
    mov_f.creating_folders(files_info)

    '''Moving files into their folders'''
    mov_f.moving_files(files_info)

    print("Operation completed.")
else:
    print("Operation canceled.")
