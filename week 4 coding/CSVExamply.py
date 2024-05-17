import csv

def writingToCSV():
    with open("StudentList.csv", 'w', newline = '') as myCSVFile:
        writeToMyCSV = csv.writer(myCSVFile)
        writeToMyCSV.writerow(['Student Name', 'Student ID', 'Major'])
        writeToMyCSV.writerow(['John Doe', '12341234', 'CS'])
        writeToMyCSV.writerow(['Jane Doe', '43214321', 'CS'])
        writeToMyCSV.writerow(['Jon Doe', '12344321', 'CS'])

def readingFromCSV():
    StudentData = []
    with open('StudentList.csv', 'r', newline = '') as myCSVFile:
        readCSVData = csv.reader(myCSVFile)
        for row in readCSVData:
            StudentData.append(row)

        StudentData.sort()
        return StudentData
        
writingToCSV()
print(readingFromCSV())

