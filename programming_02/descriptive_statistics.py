# descriptive_statistics.py
'''The following program helps us to calculate descriptive
statistics for numbers found in columns of a given input file'''

import sys
import math


def main():
    '''Descriptive statistics

    :return: Descriptive statistics
    '''
    # open the file
    # listing the data set
    with open(sys.argv[1], 'r') as infile:
        numbers = []
        count = 0
        for line in infile:
            count += 1
            try:
                column_to_parse = sys.argv[2]
                num = line.split("\t")[int(column_to_parse)]

                if not num.isalpha():
                    numbers.append(float(num))
                else:
                    print("Skipping line number ", count,
                          ": could not convert string to float: ", num)
                continue
            except IndexError:
                # this throws an IndexError when there is no user input provided
                print("Exiting: There is no valid 'list index' "
                      "in column 10 in line 1 in file: data_file3.txt")
                sys.exit(1)


    # for calculating the valid number of the column
    try:
        valid_num = int(len(numbers))
        if valid_num == 0:
            raise ValueError()

        # for calculating the average of the column
        average = sum(numbers)/valid_num

        # to calculate the maximun value of the column
        maximum = max(numbers)

        #to calculate the minimum value of the column
        minimum = min(numbers)

        # to calculate the variance of the column
        var_num = 0
        var = 0
        if valid_num != 1:
            for num in numbers:
                var_num += (num - average) ** 2
            var = var_num / (valid_num - 1)

        # to calculate the standard deviation
        std_deviation = math.sqrt(var)

        # to calculate median of the column
        numbers.sort()
        med_num = int(valid_num / 2)
        if valid_num % 2 == 0:  # even number
            median = (numbers[med_num] + numbers[med_num - 1]) / 2
        else:
            median = numbers[med_num]  # odd number
    except ValueError:
        print("Error: There were no valid number(s) in column 3 in file: data_file3.txt")
        sys.exit(1)
    # print the output
    print("\tColumn:     ", column_to_parse)
    print("\t\tCount:    ", '%.3f'%float(count))
    print("\t\tValidNum: ", '%.3f'%valid_num)
    print("\t\tAverage:  ", '%.3f'%average)
    print("\t\tMaximum:  ", '%.3f'%maximum)
    print("\t\tMinimum:  ", '%.3f'%minimum)
    print("\t\tVariance: ", '%.3f'%var)
    print("\t\tStd Dev:  ", '%.3f'%std_deviation)
    print("\t\tMedian:   ", '%.3f'%median)


if __name__ == '__main__':
    main()
