# Unique Words Counter by Binary Search Tree
Counting Unique Words in the given txt files by using Binary Search Tree

### Content
* [Description](#description)
* [How to use](#how-to-use)
* [Results](#results)

<br/>

### <a id="description">Description</a>
The **main aim** of the program is to count certain keys in the given *txt* files. These keys are:
* Lines
* Symbols
* Words
* Unique Words

Program reads all *txt* files in the given directory. *Symbols* are considered as *all characters including punctuations*, spaces are not counted. *Unique words* are not case sensitive.

Collecting *Unique words* are implemented by *Binary Search Tree*, where also *frequencies* of *Unique words* are counted.

<br/>

### <a id="how-to-use">How to use</a>
It is possible to run the file in *Terminal Window* or *Anaconda Prompt* and use argument *-p* specifying path to the directory where txt files will be read by program. Run follwing:

`python words_count_Python.py -p /home/my_name/Downloads/txt_files`

By default program reads directory *tests* that is next to the main Python file.

One more way is to *import* program as *utility* for instance in *Jyputer notebook*.

And of course, any Python IDE is as standard option.

<br/>

### <a id="results">Results</a>
As a result, program prints following (example):
<br/>`Total lines = 4`
<br/>`Total symbols = 111`
<br/>`Total words = 22`
<br/>`Total unique words = 19`

Also, *Bar Charts* are plotted as shown below.
<br/>Pay attention! If there are a lot of *Unique words* they will not be visible on the plot.

<br/>Final results, are written into the file *results.txt* next to the main Python file.

![Plotting results](https://github.com/sichkar-valentyn/Unique-Words-Count/plot.png)

<br/>

### MIT License
### Copyright (c) 2019 Valentyn N Sichkar
### github.com/sichkar-valentyn
