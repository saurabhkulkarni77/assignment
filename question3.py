import sys
import re
import os
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--folder_name", help="folder name", required=True)
parser.add_argument("--filename", nargs="?", required=False)
parser.add_argument("--behaviour", nargs="?", required=False)
parser.add_argument("--Outfile", nargs="?", required=False)

value = parser.parse_args()
folder_name = value.folder_name
filename = value.filename
behaviour = value.behaviour
outfile = value.Outfile
kwargs = {"foldername": folder_name,"filename": filename, "behaviour": behaviour,"Outfile":outfile}
def sorted_alphanumeric(data,**kwargs):
    args = kwargs['behaviour']
    convert = lambda text: int(text) if text.isdigit() else text.lower()
    alphanum_key = lambda key: [ convert(c) for c in re.split('([0-9]+)', key) ] 
    if args == None:
        return sorted(data, key=alphanum_key)
    elif args == 'descending':
        return sorted(data, key=alphanum_key, reverse=True)
    elif args == 'ascending':
        return sorted(data,key=alphanum_key, reverse=False)
    

def data_processing(**kargs):
    folder_name =kwargs['foldername']
    filename = kwargs['filename']
    outfile = kwargs['Outfile']
    if filename == None:
        dirlist = sorted_alphanumeric(os.listdir(folder_name),**kwargs)
        print("All files in folder",dirlist)
    elif filename != None:
        dirlist = sorted_alphanumeric(os.listdir(folder_name),**kwargs)
        for i in dirlist:
            if i == filename:
                print("Filename detected",i)
    if outfile != None and filename != None:
       with open(folder_name+"/"+filename) as f:
           with open(outfile, "w") as f1:
               for line in f:
                   f1.write(line)
    elif outfile == None and filename != None:
         with open(folder_name+"/"+filename,'r') as viewFileOpen:
             data = viewFileOpen.read()
             print("Outfile content:",data)
            
if __name__ == "__main__":
    data_processing()
