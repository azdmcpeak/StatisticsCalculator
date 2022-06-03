# mid point calculator
import statistics


# Provide a range of numbers
def counter():
    # add commas to list
    # https://delim.co/#

    # x values
    values = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    # The_range is used to calculate the range of numbers that fall between the Range Min and Range Max
    The_range = []
    # Floor
    Range_min = 10
    # Ceiling
    Range_max = 14
    # frequency percent

    for i in range(len(values)):
        if values[i] >= Range_min and values[i] <= Range_max:
            The_range.append(values[i])

    percent = round(len(The_range) / len(values) * 100, 2)

    print("Frequency: ", len(The_range))
    print("Percentage Distribution: ", percent)


counter()
# added for readability
print(" ")


def MainCalculation():
    def CalculateZScores(Value, Mean, StandDeviation):
        the_value = ((Value - Mean) / StandDeviation)
        return round(the_value, 2)

    listOfValues = [1, 2, 3, 4, 5, 4, 6, 7, 8, 9]
    # sorted list that is only used to determine range
    sortedList = listOfValues.copy()
    sortedList.sort()

    mean = (statistics.fmean(listOfValues))
    median = statistics.median(listOfValues)
    mode = statistics.multimode(listOfValues)
    Range = sortedList[-1] - sortedList[0]
    variance = (statistics.variance(listOfValues, mean))
    standard_Deviation = (statistics.stdev(listOfValues))
    coefficient_Of_Variation = (standard_Deviation / mean * 100)

    print("ZScores")
    for i in listOfValues:
        print(i, " ", CalculateZScores(i, mean, standard_Deviation))

    # for readability
    print(" ")

    return print("Mean: ", round(mean, 2), "\n",
                 "Median: ", median, "\n",
                 "Mode: ", mode, "\n",
                 "range: ", Range, "\n",
                 "Variance: ", round(variance, 2), "\n",
                 "Standard Deviation: ", round(standard_Deviation, 2), "\n",
                 "CoEfficient of Variation: ", round(coefficient_Of_Variation, 2))


MainCalculation()
