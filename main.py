import timeit
import xlwt 

import algorithms

# directory name for input and output files
inputDir   = "input/"
outputDir  = "output/"

# only acceptable options for this project that can be inputted from the terminal
optionCorrectness = "correctness"
optionAnalysis    = "analysis"

def timeIt(funcName, param):
  totalTime = 0
  for i in range(5): 
    start = timeit.default_timer()
    if funcName.__name__ == "quickSort":
      result = funcName(param, 0, len(param))
    else:  
      result = funcName(param)
    totalTime += timeit.default_timer() - start

  return ((totalTime/5) * 1000000, result)

def runAlgorithms(option, input):
  outputStream = ""
  if option == optionCorrectness:
    outputStream += f'Input: {str(input)}\n\n'
  workbook = xlwt.Workbook()  
  sheet = workbook.add_sheet("Algorithm Runtime") 
  style = xlwt.easyxf('font: bold 1') 

  sheet.write(0, 0, 'Input Length', style)
  sheet.write(0, 1, len(input))
  sheet.write(2, 0, 'Algorithm Name', style)
  sheet.write(2, 1, 'Runtime (in microsecond)', style)

  timeTaken, result = timeIt(algorithms.bubbleSort, input)
  if option == optionCorrectness:
    outputStream += f'Output of Bubble Sort: \t\t\t\t{str(result)}\n'
  sheet.write(3, 0, 'Bubble Sort')
  sheet.write(3, 1, timeTaken)

  timeTaken, result = timeIt(algorithms.insertionSort, input)
  if option == optionCorrectness:
    outputStream += f'Output of Insertion Sort: \t\t{str(result)}\n'
  sheet.write(4, 0, 'Insertion Sort')
  sheet.write(4, 1, timeTaken)

  timeTaken, result = timeIt(algorithms.mergeSort, input)
  if option == optionCorrectness:
    outputStream += f'Output of Merge Sort: \t\t\t\t{str(result)}\n'
  sheet.write(5, 0, 'Merge Sort')
  sheet.write(5, 1, timeTaken)

  timeTaken, result = timeIt(algorithms.quickSort, input)
  if option == optionCorrectness:
    outputStream += f'Output of Quick Sort: \t\t\t\t{str(result)}\n'
  sheet.write(6, 0, 'Quick Sort')
  sheet.write(6, 1, timeTaken)

  timeTaken, result = timeIt(algorithms.heapSort, input)
  if option == optionCorrectness:
    outputStream += f'Output of Heap Sort: \t\t\t\t\t{str(result)}\n'
  sheet.write(7, 0, 'Heap Sort')
  sheet.write(7, 1, timeTaken)

  if option == optionCorrectness:
    open(f'{outputDir}{option}.txt', "w+").write(outputStream)
    print(f'Output for correctness of the algorithm can be found in {outputDir}{option}.txt')

  workbook.save(f'{outputDir}{option}.xls')
  print(f'Runtime (analysis) of the algorithm can be found in {outputDir}{option}.xls') 

def displayOptions():
  return '''1. Check for correctness.
2. Do analysis.
Enter option >>  '''

def displayAnalysisOption():
  return 'Enter input-data charactersitic [Random (r), Sorted (s)] >> '

def displayDataSetSize():
  return 'Enter dataset size [100, 1000, 5000, 10000] >> '

if __name__ == '__main__' :
  while True:
    option = int(input(displayOptions()))
    if option == 1:
      strList = open(f'{inputDir}correctness.txt', "r").read().split(",")
      data =[int(num) for num in strList]
      runAlgorithms("correctness",  data)
      break
    elif option == 2:
      analysisOpt = str.lower(input(displayAnalysisOption()))
      if analysisOpt != 'r' and analysisOpt != 's' :
        print("Bad input")
        break
      analysisOpt = 'random' if analysisOpt=='r' else 'sorted'
      datasetSize = int(input(displayDataSetSize()))
      strList = open(f'{inputDir}{analysisOpt}_{datasetSize}.txt', "r").read().split(",")
      data = [int(num) for num in strList]
      runAlgorithms("analysis", data)
      break
    else:
      print("Please choose from option #1 or #2\n")
