# After feeling like you've been falling for a few minutes, you look at the
# device's tiny screen. "Error: Device must be calibrated before first use.
# Frequency drift detected. Cannot maintain destination lock." Below the
# message, the device shows a sequence of changes in frequency (your puzzle
# input). A value like +6 means the current frequency increases by 6; a value
# like -3 means the current frequency decreases by 3.
#
# Starting with a frequency of zero, what is the resulting frequency after
# all of the changes in frequency have been applied?


input_data = open('input_data.txt', 'r')


def solver(input_data):
    frequencies = input_data.readlines()
    resulting_frequency = 0

    for frequency in frequencies:
        resulting_frequency += int(frequency)

    return resulting_frequency


print("Resulting frequency: {}".format(solver(input_data)))


#       -------Part 1--------
# Day       Time  Rank  Score
#   1   01:45:29  3024      0
