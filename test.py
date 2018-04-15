import numpy as np
from src.conversions.length.feet_to import centimeters

input = 29998.0
print(centimeters(input))

#from src.nuclear.photon_spec.hermes import discretized_spectrum

#def print_array_to_columns(in_array, num_columns,
#                           total_length, after_decimal):
#    number = '{:' + str(total_length) + '.' + \
#               str(after_decimal) + 'e}'
#    while in_array.any():
#        this_line = in_array[:num_columns]
#        in_array = in_array[num_columns:]
#        line = ["{:6.4e}".format(item) for item in this_line]
#        print(" ".join(line))



#energy, prob = discretized_spectrum('Ballard')
#print_array_to_columns(prob, 5, 6, 4)
