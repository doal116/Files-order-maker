import os
import shutil


def creating_folders(file_list):
    already_created_fold = []
    for file in file_list:
        if file.extension in already_created_fold:
            pass
        else:
            try:
                path_of_folder = os.path.join(
                    file.directory, file.extension[1:])
                os.mkdir(path_of_folder)
                already_created_fold.append(file.extension)
            except(FileExistsError):
                pass


def moving_files(lt):
    for file in lt:
        ext = os.path.splitext(file.directory + '/' + file.name)
        folder = ext[1]
        original_path = os.path.join(file.directory, file.name)
        new_path = os.path.join(file.directory, folder[1:])
        shutil.move(original_path, new_path)
