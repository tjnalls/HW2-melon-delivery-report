filenames = ["um-deliveries-day-1.txt", 
                 "um-deliveries-day-2.txt", 
                 "um-deliveries-day-3.txt"]

def melon_count():
    
    i = 0
    while i < len(filenames):
    '''checks how many delivery days'''

        print(f"Day {i + 1}")
        '''displays referenced day log'''
        the_file = open(filenames[i])
        for line in the_file:
            line = line.rstrip()
            words = line.split('|')
        '''separates out each line of the txt doc file into list items'''

            melon = words[0]
            count = words[1]
            amount = words[2]
        '''assigns variable names for each item of the list'''

            print(f"Delivered {count} {melon}s for total of ${amount}")
        '''displays desired string of each log'''
        the_file.close()
        '''closes out the current doc file'''
        i = i + 1
        '''cycles to next indexed doc in filenames'''
    
melon_count()