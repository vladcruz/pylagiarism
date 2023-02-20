import argparse
import rapidfuzz as rf

def compare_texts(file1, file2, threshold):
    first_file = open(file1, mode='r', encoding='utf8')
    second_file = open(file2, mode='r', encoding='utf8')
    results_file = open('results.txt', mode='w', encoding='utf8')

    file1 = first_file.readlines()
    file2 = second_file.readlines()
    counterf1 = 1
    result = ''

    for line_1 in file1:
        counterf2 = 1
        for line_2 in file2:
            if(rf.distance.JaroWinkler.similarity(line_1, line_2) > float(threshold)):
                result =  result + 'File 1 - Line ' + str(counterf1) + ' | File 2 - Line ' + str(counterf2) + ' -> ' + str(rf.distance.JaroWinkler.similarity(line_1, line_2)) + '\n'
            counterf2 = counterf2 + 1
        counterf1 = counterf1 + 1
        
    results_file.write(result)
    first_file.close
    second_file.close
    results_file.close

if(__name__ == "__main__"):
    # creating the parser for the parameters
    parser = argparse.ArgumentParser(description='Compare two text files for similarities.')
    parser.add_argument('--files', dest='files', help='File being compared.', nargs=2)
    parser.add_argument('--threshold', dest='threshold', help='Threshold of similarity', nargs=1)
    args = parser.parse_args()
    
    # calling the comparison function
    compare_texts(args.files[0], args.files[1], args.threshold[0])