
# Getting started

Download [`python 3.5+`](https://www.activestate.com/activepython) package from ActivePython where embeded Tcl/Tk package [`tkinter`] for us to use.


The [`tkinter`](https://docs.python.org/3/library/tkinter.html)
package provides an interface between `Python` and `Tcl/Tk`. In the
following code I assume that the Python version 3+ is used. (For
Python 2.x the package is called
[`Tkinter`](https://docs.python.org/2/library/tkinter.html)).

First
Download [`loon`](https://github.com/waddella/loon/tree/dev-python/Tcl) and [   `Img`](http://www.posoft.de/html/extTkImg.html) packages and put it into your local path of python directory [`yourpath/python/tcl/`]

First the tkinter package needs to be loaded

```
import tkinter
```

Then load the tk library which creates the toplevel window `.`. The
toplevel window needs to be hidden because all other `Tk` windows will
be children of it, and if the toplevel window gets destoyed (closed)
then all its children get destroyed too.

```
toplevel = tkinter.Tk()
toplevel.withdraw() 
```

Now load the loon and Img libraries (needs to be done once, replace the path
accordingly)

```
toplevel.eval('lappend auto_path yourpath/python/tcl//loon')
toplevel.eval('lappend auto_path1 yourpath/python/tcl//Img')
toplevel.eval('package require loon')
toplevel.eval('pacakge require Img')
```

The `toplevel.eval` method provides access to the `Tcl` interpreter

Now you can create the first `loon` plot.

```
toplevel.eval('set p [loon::plot -x {1 2 3} -y {1 2 3}]')
```

Alternatively you can also import the loon namespace in `Tcl`

```
root.eval('namespace import loon::*')
root.eval('set p [plot -x {1 2 3} -y {1 2 3}]')
```

# Roadmap

Look at the Python Tix package.







