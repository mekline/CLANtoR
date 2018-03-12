# CLANtoR

This is a fairly simple R script that just takes a single CHILDES-formatted corpus file and turns it into an R dataframe with all corpus information (e.g. child, age, date) listed on each utterance. From there it can be written out as a CSV or other standard file format.

*Note: this is older code, and a much better solution for converting corpora to tabular data now exists! Go check out [childes-db](http://childes-db.stanford.edu/)*

In addition to copying any tiers that it finds into columns of the dataframe, CLANtoR also creates a gloss of the utterance that removes corpus notation, leaving an unannotated version that is suitable for displaying to experimental participants or conference audiences :) In the example script I've also done some additional processing that deletes ending punctuation and various whitespace anomalies in order to find even more sentences with matched gloss and %mor lines.


Be wary of the output you get with this script, especially if you wish to use tiers other than gloss and mor. If you are not already, become familiar with text encoding, control characters, and csv formats to understand what might be happening if a line looks funny. Especially watch out if there are commas or quotation marks anywhere in your corpus file.


In the Brown (1973) corpus this finds matching lengths for approximately 97% of adult sentences and 95% of child sentences- most of the exceptions are repairs (He has, she has a doll) and sentence fragments. The script is pretty slow (10 minutes or so to read the entire Eve corpus on my machine) but you should only need to run it once per corpus.

I also include two additional Python files that may make the above more useful. They were written for the Brown (1973) corpus as well.  and the second simply 

ClantoR.R - The main script

example.R Example script for the Brown corpus

fixer.py - Corrects for some of the text encoding anomalies

splitter.py - Gives you a set of smaller csv slices that are somewhat less likely to crash your spreadsheet program.

