from __init__ import *
from l_size import *

def l_export(widget, filename, width, height):
    
    if width is None:
        width = list(l_size(width))[1]
    if height is None:
        height = list(l_size(width))[2]

    valid_extensions = l_export_valid_formats() 
    
    #file_extension = tools::file_ext(filename)
    if file_extension in valid_extensions:
        fname = tcl("::loon::export", widget, filename, width, height))
    else:
        str2 = ", ".join(valid_extensions)
        str1 = "The file fomat '" + file_extension + "' is not supported on your system.\nSupported formats are: " + str2 + '.'
        sys.exit(str1)
    

    return fname




def l_export_valid_formats():
    valid_extensions = ["ps", "eps"]
    
    if isexist('epstopdf') != "":
        valid_extensions = [valid_extensions, "pdf"]


    if _withTclImg:
        valid_extensions = [valid_extensions,'jpg','jpeg','png','bmp','tiff','gif']
    
    return valid_extensions





png="Portable Network Graphics",
jpg="JPEG",
ps="Postscript",
eps="Encapsulated Postscript",
pdf="Portable Document Graphics",
tiff="Tagged Image File Format",
bmp="Bitmap",
gif="Graphics Interchange Format"                

filetypes = [png, jpg, ps, eps, pdf, tiff, bmp, gif]

def exportImageDialog(widget) :

    fm = l_export_valid_formats()
    formats = fm.remove('jpeg')
    fnames = formats, function(x)filetypes[[x]], character(1))

    types <- ""
    for (i in seq_along(formats)) {
        types <- paste(types, '{',
                       paste0('{', fnames[i], '}'),
                       paste0('{','.', formats[i], '}'),
                       '}')        
    }
    
    fileName <- as.character(
        tcl('tk_getSaveFile',
            initialdir=getwd(),
            initialfile='loon_plot',
            title="Export Plot As Image",
            parent=tkwinfo('toplevel', widget),
            filetypes=types))
    
    if (length(fileName) == 1) {
        l_export(widget, fileName)
    }
    return(fileName)
