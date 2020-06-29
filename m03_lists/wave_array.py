# Given an array of integers, sort the array into a wave like array and return it,
# In other words, arrange the elements into a sequence such that
# a[1] >= a[2] <= a[3] >= a[4] <= a[5]

def wave_array(integers):
    num_integers = len(integers)
    wave_array = []
    while len(integers) > 1:
        wave_array.append(integers.pop((len(wave_array)+1)%2 ))
    wave_array.append(integers.pop())
    integers[:] = wave_array[:]

    return integers

wave_array([1, 2, 3, 4, 5])
# One possible answer : [2, 1, 4, 3]
