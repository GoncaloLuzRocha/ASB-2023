# ASB-2023-assignment_01
The scripts were made in python, and tested in linux shell.
I tested them using: python3 script.py (substitute script.py witht the name of the script)
I did not test them using only: python script.py because there was some error, either with the way i installed my dependencies in my VM or with how the VM was setup, idk.

Before trying any of the scripts, make sure to have installed:
pip;
python;
Bio python package;
mafft;
raxml or another phylogenetic tree builder;

The order to run the scrips is:
1: getFastas.py;
2: concat.py;
3: mafftAlign.py;
4: renamer.py;

and then run the file that is the output from rename.py, with raxml, i ran it with raxmlHPC-PTHREADS-SSE3, but be my guess and try the other raxml versions.


update, the way i made this, is wrong, i should align before concatenating the sequences.
in this im concatenating before the alignemnt.
