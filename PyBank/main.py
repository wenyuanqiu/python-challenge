#Import Modules
import csv

CsvPath = r'C:\Users\wenyu\Desktop\RU-HOU-DATA-PT-07-2019-U-C\03-Python\Homework\PyBank\Resources\budget_data.csv'

#Blank Lists
CsvMonths = []
CsvPnl = []

#Open and Append to Blank Lists
with open(CsvPath, newline = '') as CsvContents:
    CsvReader = csv.reader(CsvContents, delimiter= ',') 
    CsvHeader = next(CsvReader)
    for Row in CsvReader:
        CsvMonths.append(Row[0])
        CsvPnl.append(int(Row[1]))

#Calculate 
MonthCount = 0
TotalPnl = 0
ListIndex = 0
PnlChanges = []

for Row in CsvMonths:
    MonthCount += 1 
    TotalPnl += CsvPnl[ListIndex]
    #If Not First Row, Calculate Change From Prior
    if ListIndex > 0:
        PnlChanges.append(CsvPnl[ListIndex]-CsvPnl[ListIndex-1])
    ListIndex += 1

AveragePnlChange = sum(PnlChanges)/len(PnlChanges)
BestPnlChange = max(PnlChanges)
WorstPnlChange = min(PnlChanges)
BestPnlChangeMonth = CsvMonths[PnlChanges.index(BestPnlChange)+1]
WorstPnlChangeMonth = CsvMonths[PnlChanges.index(WorstPnlChange)+1]

#Print
PrintStr = ['Financial Analysis','----------------------------']
PrintStr.append('Total Months: ' + str(MonthCount))
PrintStr.append('Total: ' + str(TotalPnl))
PrintStr.append('Average Change: ' + str(AveragePnlChange))
PrintStr.append('Greatest Increase in Profits: ' + str(BestPnlChangeMonth) + ' (' + str(BestPnlChange) + ')')
PrintStr.append('Greatest Decrease in Profits: ' + str(WorstPnlChangeMonth) + ' (' + str(WorstPnlChange) + ')')
print(PrintStr)

#Write
TextPath = r'C:\Users\wenyu\Documents\BootCamp\HW3\python-challenge\PyBank\PyBankOutput.txt'

with open(TextPath, mode = 'w') as OutputFile:
    OutputFile.writelines('Financial Analysis' + '\n')
    OutputFile.writelines('----------------------------' + '\n')
    OutputFile.writelines('Total Months: ' + str(MonthCount) + '\n')
    OutputFile.writelines('Total: ' + str(TotalPnl) + '\n')
    OutputFile.writelines('Average Change: ' + str(AveragePnlChange) + '\n')
    OutputFile.writelines('Greatest Increase in Profits: ' + str(BestPnlChangeMonth) + ' (' + str(BestPnlChange) + ')' + '\n')
    OutputFile.writelines('Greatest Decrease in Profits: ' + str(WorstPnlChangeMonth) + ' (' + str(WorstPnlChange) + ')')