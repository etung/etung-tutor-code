import math

def convert_language_to_base10 (source_dictionary, value) :
        ret_val = 0
        index = 0
        for character in reversed(value):
                ret_val += pow(len(source_dictionary),index) * source_dictionary[character]
                index += 1

        return ret_val

def convert_base10_to_language (target_dictionary, value) :
        base = len(target_dictionary)

        raw_val = ""
        while value != 0 :
                raw_val += str(value%base)
                value = value / base

        translated_val = ""

        for digit in raw_val :
                translated_val += target_dictionary[int(digit)]

        ret_val = translated_val[::-1]

        return ret_val


count = int(input())
for x in xrange(count) :

        args = str(raw_input())

        values = args.split(' ')

        source = values[0]
        source_language = values[1]
        target_language = values[2]

        source_dictionary = {}
        for digit in xrange(len(source_language)):
                source_dictionary[source_language[digit]] = digit


        real_val = convert_language_to_base10(source_dictionary, source)

        target_dictionary = {}
        for digit in xrange(len(target_language)):
                target_dictionary[digit] = target_language[digit]


        print "Case #{0}: {1}".format(x+1,
                convert_base10_to_language(target_dictionary, real_val))

