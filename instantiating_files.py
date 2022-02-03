import os


def arranging_path(path):
    pattern = r"\\"
    new_path = ''

    for i in range(len(path)):
        if path[i] == pattern[0]:
            new_path += '/'
        else:
            new_path += path[i]

    return new_path


class file_s():
    list_files = []

    def __init__(self, directory, name, extension):

        self.__directory = directory
        self.__name = name
        self.__extension = extension

        file_s.list_files.append(self)

    @property
    def directory(self):
        return self.__directory

    @property
    def name(self):
        return self.__name

    @property
    def extension(self):
        return self.__extension

    @classmethod
    def instantiating_from_directory(cls):

        path_directory = input(
            "Input the path of the directory you want to arrange: ")
        arranging_path(path_directory)

        for dir, fold, files in os.walk(path_directory):
            if dir == path_directory:
                for file in files:
                    file_extension = os.path.splitext(dir + file)
                    file_s(dir, file, file_extension[1])

    def __repr__(self):
        return f"dir: {self.directory} | name: {self.name} | extension: {self.extension}"
