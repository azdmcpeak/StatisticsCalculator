import math
import statistics


def ClassBoundaries():
    # set number
    floor = 50000
    # set number
    ceiling = 290000
    # set number
    number_of_classes = 6
    width = math.trunc((ceiling - floor) / number_of_classes)

    print("width:", width)
    print("")
    # do not change
    Counter = 0

    class_floor = floor
    class_ceiling = class_floor + width

    while Counter < number_of_classes:
        print(class_floor, " but less than ", class_ceiling)
        print("class midpoint: ", (class_floor + class_ceiling) / 2)
        class_floor = class_ceiling
        class_ceiling = class_ceiling + width
        Counter += 1
        print("")

    # for readability
    print(" ")

    # resetting counter back to zero
    Counter = 0


# Provide a range of numbers
def counter():
    # add commas to list
    # https://delim.co/#

    # x values
    # add x values
    values = []
    # The_range is used to calculate the range of numbers that fall between the Range Min and Range Max
    # LEAVE EMPTY
    The_range = []
    # Floor
    # Set floor
    Range_min = 0
    # Ceiling
    # Set ceiling
    Range_max = 0
    # frequency percent

    for i in range(len(values)):
        if values[i] >= Range_min and values[i] <= Range_max:
            The_range.append(values[i])

    percent = round(len(The_range) / len(values) * 100, 2)

    print("Frequency: ", len(The_range))
    print("Percentage Distribution: ", percent)


# added for readability
print(" ")


def MainCalculation():
    def CalculateZScores(Value, Mean, StandDeviation):
        the_value = ((Value - Mean) / StandDeviation)
        return round(the_value, 2)

    # list of x values
    # add list of x values
    listOfValues = []
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


ClassBoundaries()
# counter()
# MainCalculation()
