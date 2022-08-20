import tkinter.filedialog
from tkinter import *
from tkinter.font import Font
from tkinter import filedialog, ttk, font
import os
import time
##########root block##########
dirpath = "None"
root = Tk()
root.geometry('800x600')
root.title("Files Assistant")
##############var block################
path_fd_chose = False
path_fs_chose = False
var_of_path_downf = StringVar()
var_of_path_sorted = StringVar()
global_font = Font(family='Helvetica', size=15, weight='bold')

####################
start_time = time.time()
path_for_download_folder = "" #####Enter here folder for sorting
path_for_sorted_files = ""  #####Enter here finish folder
all_folders_in_down_folder = None
all_folders_in_sort_folder = None
duplicate = True # if True - copies of files will be added (DUPLICATE),
duplicate_flag = BooleanVar()  # if False, the file will be replaced with the one that is in the "path_for_download_folder"
duplicate_flag.set(True)
check_list_duplicate = []


list_of_files_types = { 'Image': ['jpg', 'png', 'bmp', 'ai', 'psd', 'ico', 'jpeg', 'ps', 'svg', 'tif',
                                    'tiff'],

                        'Video': ['mp4', 'mov', 'avi', 'mkv', 'wmv', '3gp', '3g2', 'mpg', 'mpeg', 'm4v',
                                 'h264', 'flv', 'rm', 'swf', 'vob'],

                        'Audio': ['mp3', 'wav', 'ogg', 'flac', 'aif', 'mid', 'midi', 'mpa', 'wma', 'wpl',
                                    'cda'],


                        'Data': ['sql', 'sqlite', 'sqlite3', 'csv', 'dat', 'db', 'log', 'mdb', 'sav',
                                'tar', 'xml'],


                        'Archive': ['zip', 'rar', '7z', 'z', 'gz', 'rpm', 'arj', 'pkg', 'deb'],

                        'Text': ['pdf', 'txt', 'doc', 'docx', 'rtf', 'tex', 'wpd', 'odt'],

                        '3d': ['stl', 'obj', 'fbx', 'dae', '3ds', 'iges', 'step'],

                        'Presentation': ['pptx', 'ppt', 'pps', 'key', 'odp'],

                        'Spreadsheet': ['xlsx', 'xls', 'xlsm', 'ods'],

                        'Font': ['otf', 'ttf', 'fon', 'fnt'],

                        'Gif': ['gif'],

                        'Installer': ['dmg', 'exe'],

                        'apk': ['apk']

                        }
#############func block################
def browsefunc_dow():
    tempvar = filedialog.askdirectory()
    var_of_path_downf.set(tempvar)
    file_counter(tempvar)
    if len(var_of_path_downf.get()) > 0:
        path_label = Label(root, borderwidth=0, relief="ridge", height=1, width=10,
                           text='Path chosen', anchor=tkinter.W, fg="#228B22")
        path_label.place(x=90, y=200)
    print('THIS',var_of_path_downf.get())

def browsefunc_sort():
    tempvar = filedialog.askdirectory()
    var_of_path_sorted.set(tempvar)
    if len(var_of_path_sorted.get()) > 0:
        path_label = Label(root, borderwidth=0, relief="ridge", height=1, width=10,
                           text='Path chosen', anchor=tkinter.W, fg="#228B22")
        path_label.place(x=512, y=200)

def update_listbox_type():
    type_folders_list.delete(0, END )
    for key in list_of_files_types.keys():
        numb = 0
        type_folders_list.insert(numb, key)
        numb += 1
        print(key)

def file_counter(pathto):
    summ = os.listdir(pathto)
    coun = len(summ)
    print(os.listdir(pathto))
    path_label = Label(root, borderwidth=0, relief="ridge", height=1, width=30,
                            text='・Found files and folders - {}'.format(coun), anchor=tkinter.W, fg="#228B22")
    path_label.place(x=60, y=250)

def minus_from_type_dict():
    target = type_folders_list.get(ANCHOR)
    type_folders_list.delete(ANCHOR)
    list_of_files_types.pop(target)
    update_lisbox_keys()

def plus_to_type_dict():
    target = enter_zone_plus_minus.get()
    list_of_files_types[target] = []
    type_folders_list.update()
    update_listbox_type()

def plus_to_extension():
    target = enter_zone_plus_minus_ext.get()
    if target not in list_of_files_types[type_folders_list.get(ANCHOR)]:
        list_of_files_types[type_folders_list.get(ANCHOR)].append(target)
    print(list_of_files_types[type_folders_list.get(ANCHOR)])
    update_lisbox_keys()
    print(list_of_files_types)
def update_lisbox_keys():
    list_of_files_extension.delete(0,END)
    for i in list_of_files_types.get(type_folders_list.get(ANCHOR)):
        num = 0
        list_of_files_extension.insert(END, i)
        num += 1

def b1(event):
    if event.widget == type_folders_list:
        print('1')
        update_lisbox_keys()

def minus_from_extension():
    list_of_files_types[type_folders_list.get(ANCHOR)].pop\
        (list_of_files_types[type_folders_list.get(ANCHOR)].index(list_of_files_extension.get(ANCHOR)))
    update_lisbox_keys()
    print(list_of_files_types)

def scan_sort_directory():
    os.chdir(var_of_path_sorted.get())
    lst_file = []
    for files in os.walk(var_of_path_sorted.get(), topdown=True):
        if len(files[2]) != 0:
            lst_file.append(files[2])
    for folder in lst_file:
        for file in folder:
            if file != '.DS_Store':
                check_list_duplicate.append(file)

def crete_folders():
    os.chdir(var_of_path_sorted.get())
    for newfolder in list_of_files_types:
        if os.path.isdir(newfolder) == True:
            pass
        else:
            os.mkdir(newfolder)

def sorting_fun():
    global all_folders_in_down_folder
    global all_folders_in_sort_folder
    global duplicate
    all_folders_in_down_folder = os.listdir(var_of_path_downf.get())
    all_folders_in_sort_folder = os.listdir(var_of_path_sorted.get())
    print(all_folders_in_sort_folder, '!!!!!!!')
    os.chdir(var_of_path_downf.get())
    for file in all_folders_in_down_folder:
        if os.path.isdir(file) == False and os.path.exists(file) == True:
            if file != '.DS_Store':
                print(file)
            if file in check_list_duplicate:
                if var_of_path_downf.get() != var_of_path_sorted.get() and file in check_list_duplicate and duplicate == True:
                    for typeof in list(list_of_files_types.items()):
                        for typeoftype in typeof:
                            if file.split('.')[-1] in typeoftype:
                                os.rename(os.path.abspath(file),
                                          var_of_path_sorted.get() + '/' + typeof[0] + '/' + file.split('.')[
                                              0] + "(DUPLICATE)." + file.split('.')[1])
                                print('1')

                elif var_of_path_downf.get() != var_of_path_sorted.get() and file in check_list_duplicate and duplicate == False:
                    for typeof in list(list_of_files_types.items()):
                        for typeoftype in typeof:
                            if file.split('.')[-1] in typeoftype:
                                os.rename(os.path.abspath(file), var_of_path_sorted.get() + '/' + typeof[0] + '/' + file)
                                print('2')

                elif var_of_path_downf.get() == var_of_path_sorted.get() and file in check_list_duplicate and duplicate == True:
                    for typeof in list(list_of_files_types.items()):
                        for typeoftype in typeof:
                            if file.split('.')[-1] in typeoftype:
                                os.rename(os.path.abspath(file),
                                          var_of_path_sorted.get() + '/' + typeof[0] + '/' + file.split('.')[
                                              0] + "(DUPLICATE)." + file.split('.')[1])
                                print('3')

                elif var_of_path_downf.get() == var_of_path_sorted.get() and file in check_list_duplicate and duplicate == False:
                    for typeof in list(list_of_files_types.items()):
                        for typeoftype in typeof:
                            if file.split('.')[-1] in typeoftype:
                                os.rename(os.path.abspath(file), var_of_path_sorted.get() + '/' + typeof[0] + '/' + file)
                                print('4')
            elif file not in check_list_duplicate:
                for typeof in list(list_of_files_types.items()):
                    for typeoftype in typeof:
                        if file.split('.')[-1] in typeoftype:
                            os.rename(os.path.abspath(file), var_of_path_sorted.get() + '/' + typeof[0] + '/' + file)
                            print('5')

def start():
    scan_sort_directory()
    crete_folders()
    os.chdir(var_of_path_downf.get())
    sorting_fun()

def check_flaag():
    global duplicate
    duplicate = not duplicate
    if duplicate == True:
        duplicate_flag.set(True)
    elif duplicate == False:
        duplicate_flag.set(False)
    print(duplicate_flag.get(), 'dupl_var',duplicate )
##############widget block###################
browsebutton_dow_fol = Button(root, text="Choose Folder", command=browsefunc_dow)
browsebutton_dow_fol.place(x = 225, y=170)

browsebutton_sort_fol = Button(root, text="Choose Folder", command=browsefunc_sort)
browsebutton_sort_fol.place(x = 650, y=170)

button_plus = Button(root, text="+", command=plus_to_type_dict)
button_plus.place(x=30, y=270)

button_minus = Button(root, text="-", command=minus_from_type_dict)
button_minus.place(x=250, y=270)

enter_zone_plus_minus = ttk.Entry(root)
enter_zone_plus_minus.place(x=72, y=272, width=180)

button_plus_ext = Button(root, text="+", command=plus_to_extension)
button_plus_ext.place(x=430, y=270)

button_minus_ext = Button(root, text="-", command=minus_from_extension)
button_minus_ext.place(x=650, y=270)

enter_zone_plus_minus_ext = ttk.Entry(root)
enter_zone_plus_minus_ext.place(x=472, y=272, width=180)

teststring = str()
label_download_folder = ttk.Entry(root, textvariable=var_of_path_downf)
label_download_folder.place(x = 30, y=172)

label_sorted_folder = ttk.Entry(root, textvariable=var_of_path_sorted)
label_sorted_folder.place(x = 455, y=172)

type_folders_list = Listbox(root, selectmode=SINGLE, font=global_font)
type_folders_list.place(x = 70, y= 300)

list_of_files_extension = Listbox(root, font=global_font)
list_of_files_extension.place(x = 470, y= 300)

button_start_sort = Button(root, text="Sort Files", command=start)
button_start_sort.place(x=700, y=500)

report_line = ttk.Entry(root)
report_line.place(x=100, y=500, width=600)

flag_duplicate = Checkbutton(root, variable=duplicate_flag, command=check_flaag, text='Duplicate (WARNING: if uncheck - duplicate files\n in target folder'
                                                                                      ' will be replaced)')
flag_duplicate.place(x=30, y=220)

###############sorted func block###############

###############udner block#####################
# pathlabel = Label(root)
# pathlabel.pack()
################other block######################
update_listbox_type()

root.bind("<Button-1>" , b1)
root.iconbitmap("/Users/consul/PycharmProjects/Files Assistant/ico/main_ico.ico")
root.mainloop()