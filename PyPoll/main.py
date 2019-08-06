#Import Modules
import csv

CsvPath = r'C:\Users\wenyu\Desktop\RU-HOU-DATA-PT-07-2019-U-C\03-Python\Homework\PyPoll\Resources\election_data.csv'

#Blank Lists
CsvIds = []
CsvCounties = []
CsvCandidates = []

#Open
with open(CsvPath, newline = '') as CsvContents:
    CsvReader = csv.reader(CsvContents, delimiter= ',') 
    CsvHeader = next(CsvReader)
    CsvIds = [Row[0] for Row in CsvReader]

with open(CsvPath, newline = '') as CsvContents:
    CsvReader = csv.reader(CsvContents, delimiter= ',') 
    CsvHeader = next(CsvReader)
    CsvCounties = [Row[1] for Row in CsvReader]

with open(CsvPath, newline = '') as CsvContents:
    CsvReader = csv.reader(CsvContents, delimiter= ',') 
    CsvHeader = next(CsvReader)
    CsvCandidates = [Row[2] for Row in CsvReader]
    
#Total Votes
TotalVotes = len(CsvIds)

#Unique Values in Candidates
Candidates = []
for Candidate in CsvCandidates:
    if Candidate not in Candidates:
        Candidates.append(Candidate)
print(Candidates)

#Candidate Vote Counts
CandidateVotes = [0]*len(Candidates)
CandidateVoteShares = [0]*len(Candidates)

for Row in CsvCandidates:
    CandidateVotes[Candidates.index(Row)]+=1

RowIndex = 0
for Row in CandidateVotes:
    CandidateVoteShares[RowIndex] = Row/TotalVotes
    RowIndex += 1

Winner = Candidates[CandidateVotes.index(max(CandidateVotes))]

#Print
PrintStr = ['Election Results','----------------------------']
PrintStr.append('Total Votes: ' + str(TotalVotes))
PrintStr.append('----------------------------')
RowIndex = 0
for Row in Candidates:
    PrintStr.append(f'{Row} {CandidateVoteShares[RowIndex]} ({CandidateVotes[RowIndex]})')
    RowIndex += 1
PrintStr.append('----------------------------')
PrintStr.append(f'Winner: {Winner}')
PrintStr.append('----------------------------')
print(PrintStr)

#Write
TextPath = r'C:\Users\wenyu\Documents\BootCamp\HW3\python-challenge\PyPoll\PyPollOutput.txt'
with open(TextPath, mode = 'w') as OutputFile:
    #OutputFile.write('Test')
    OutputFile.writelines('Election Results' + '\n')
    OutputFile.writelines('----------------------------' + '\n')
    OutputFile.writelines('Total Votes: ' + str(TotalVotes) + '\n')
    OutputFile.writelines('----------------------------' + '\n')
    RowIndex = 0
    for Row in Candidates:
        OutputFile.writelines(f'{Row} {CandidateVoteShares[RowIndex]} ({CandidateVotes[RowIndex]})\n')
        RowIndex += 1
    OutputFile.writelines('----------------------------' + '\n')
    OutputFile.writelines(f'Winner: {Winner}\n')
    OutputFile.writelines('----------------------------' + '\n')
