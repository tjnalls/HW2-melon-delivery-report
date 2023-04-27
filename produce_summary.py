filenames = ["um-deliveries-day-1.txt", 
                 "um-deliveries-day-2.txt", 
                 "um-deliveries-day-3.txt"]

def melon_count():
    
    i = 0
    while i < len(filenames):
        print(f"Day {i + 1}")
        the_file = open(filenames[i])
        for line in the_file:
            line = line.rstrip()
            words = line.split('|')

            melon = words[0]
            count = words[1]
            amount = words[2]

            print(f"Delivered {count} {melon}s for total of ${amount}")
        the_file.close()
        i = i + 1
    
melon_count()