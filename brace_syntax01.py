'''
'''

def check_braces(expressions):
    # Write your code here
    # To print results to the standard output you can use print
    # Example print "Hello world!"
    for brace in expressions:
        if len(brace) % 2 == 0:
            # figure out if properly closing
            ''' 
            basically, brace is improper if it has an 'improper' distnce to each other
            so, compute that distance for each type of brace
            unless, that brace doesn't exist
            '''
            rd = brace.find(")") - brace.find("(")
            square = brace.find("]") - brace.find("[")
            curly = brace.find("}") - brace.find("{")
            multiple = 1
            '''
            insight is if item is not 0, then multiples of odd numbers 
            remain an odd number
            '''
            if rd == 0:
                multiple = square * curly
            elif square == 0:
                multiple = rd * curly
            elif curly == 0:
                multiple = rd * square
            else:
                multiple = rd * square * curly
            if multiple % 2 == 1:
                print 1
            else:
                print 0
        else:
            # no need to further review
            print 0
