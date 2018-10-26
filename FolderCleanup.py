import os

# FileType Dictionary
def directory_folder(path):
    """
    Returns a dictionary of all the files of the provided path separated by file type
    """
    files = list(os.listdir(path))
    collection = {}
    for file in files:
        typ = file.rfind(".")
        if os.path.isfile(path + '/' + file):
            if file[typ + 1:] not in collection:
                collection[file[typ + 1:]] = []
            collection[file[typ +1 :]].append(file)
    print("Number of file types:",len(collection))
    print('Number of files:', len(files))
    return collection

# Helper Function
    # for moving files into new folders
        # In the programs instance, 
        # checks the existence of file in list and destination, and then moves the file to it
def check_move(file, new, check):
    """
    Helper function to ensure the moved_file and destination exists.
    
    check_move('file.md', 'NewFolder/file.md', 'NewFolder/')
    """
    if os.path.exists(file) and os.path.isdir(check):
        print('yes')
        os.rename(file, new)
    else:
        print("trying to access {} or {}".format(file, check))
        print(os.path.exists(file))
        print(os.path.isdir(check))

#Helper function
# If the directory doesn't exist, create the directory
def check_and_create(path):
    """Helper function to create a new directory provided it doesn't exist"""
    if not os.path.isdir(path):
        os.mkdir(path)
        
# move function
def consolidate(dictionary, search_path, dest):
    """
    Takes the dictionary and path and relocates the files in the directory into a centralized location based on file type
    """
    x = 0
    import datetime
    now = datetime.datetime.now()
    foldname = "CleanUpDate" + \
        str(now.month)+'.'+str(now.day)+'.'+str(now.year)
    nu_path = str(dest) + "/" + foldname
    check_and_create(nu_path)
    for typ in dictionary.keys():
        check_and_create(nu_path + '/' + typ)
        y = 0
        for i in dictionary[typ]:
            check_move(search_path + '/' + i, nu_path + '/'+ str(typ) + '/' + i, nu_path + '/'+ str(typ))
            y += 1
        x += 1

def main(path=None, new_loc = None):
    """Easily executable function for the cleanup"""
    if new_loc == None:
        new_loc = input('Enter Destination Folder Path: ')
    if path == None:
        path = input('Enter CleanUp Path: ')
    dic = directory_folder(path)
    consolidate(dic, path, new_loc)
    
if __name__ == '__main__':
    main()