### Programming project for Design and Analysis of Algorithms.

## Depenedencies
This project requires the `xlwt` to manipulate .xlsx files. To install, run below command:
`pip install xlwt`

To run the sorting algorithm, simply run `python main.py` from the root directory.

This project implements two way of running the setup -- to check for correctness and do analysis, which can be inputted from the command-line.

For correctness, pre-defined list of integer is consumed as input and two files are created to store the output from the operation -- a .xls which has the runtime of each alogiorthm and a .txt which contains the output of the algorithm. Pre-defined input file for this is another .txt file wtih 50 integers.

For analysis, the idea is to check for various edge-cases for the algorithms implemented in this project. When this option is chosen, the user is provided with choices where he can take decisions on the input characteristic -- like to select sorted or unsorted array with length ranging from 100 to 10,000. The output of this operation is a .xls file which contains the runtime of each algorithm for the consumed input file.
