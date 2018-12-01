# After feeling like you've been falling for a few minutes, you look at the
# device's tiny screen. "Error: Device must be calibrated before first use.
# Frequency drift detected. Cannot maintain destination lock." Below the
# message, the device shows a sequence of changes in frequency (your puzzle
# input). A value like +6 means the current frequency increases by 6; a value
# like -3 means the current frequency decreases by 3.
#
# You notice that the device repeats the same frequency change list over and
# over. To calibrate the device, you need to find the first frequency
# it reaches twice.
#
# What is the first frequency your device reaches twice?


input_data = open('input_data.txt', 'r')


def solver(input_data):
    frequencies = input_data.readlines()
    resulting_frequencies = set()
    resulting_frequency = 0

    while True:
        for frequency in frequencies:
            resulting_frequency += int(frequency)

            if resulting_frequency in resulting_frequencies:
                return resulting_frequency

            resulting_frequencies.add(resulting_frequency)


print("First frequency your device reaches twice: {}".format(solver(input_data)))


#       -------Part 2--------
# Day       Time  Rank  Score
#   1   02:11:47  2510      0
