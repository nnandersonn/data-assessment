# opens specified file and stores contents in variable log_file
log_file = open("um-server-01.txt")

# creates a function called  sales_reports that takes in log_file as a parameter
def sales_reports(log_file):
    # for loop that will go through row by row of the contents of log_file, calling each line in the file 'line'
    for line in log_file:
        # set line equal to line minus trailing characters (like white space in this case and by default)
        line = line.rstrip()
        # sets day = to the first 3 characters in a string 
        day = line[0:3]
        # simple if statement checking if the 3 characters sliced above are equal to Tue
        if day == "Tue":
            # prints the whole line that starts with Tue. The for loop will continue after this and move to the next row if there is one
            print(line)

# runs the above function passing in our created log_file variable as the param
sales_reports(log_file)
