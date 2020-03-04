#Shiuli Ganguly
#PyPoll
#CSV file given election_data.csv
#Voter ID, County, Candidate
#Objective: Count Votes and Calculate Percentage
import os 
import csv
thisfile_location = os.path.dirname(os.path.realpath(__file__))                 #This File
datafile_location = os.path.join(thisfile_location, 'election_data.csv')        #Given File
outputfile_location = os.path.join(thisfile_location, 'election_results.csv')   #The results Candidate, Percent

total_votes=0


with open(datafile_location) as election_data:
            election_reader = csv.DictReader(election_data)
            Candidate_list = []
            County_list = []
            total_votes=0
            votes = 0
            Candidate_Count = []
                     
            #Required: For every Candidate, Count the Number of Votes   

            for vote in election_reader:
                total_votes = total_votes+1
                read_candidate = vote['Candidate']
                vote_alive = 1
                
                if not(read_candidate in Candidate_list):
                    Candidate_list.append(read_candidate)
                    get_index = Candidate_list.index(read_candidate)
                    Candidate_Count.insert(get_index, 0)

                if (read_candidate in Candidate_list):
                    get_index = Candidate_list.index(read_candidate)
                    Candidate_Count[get_index]=Candidate_Count[get_index] +1

#Sort           
#Zip the two lists.
#Create a new, sorted list based on the zip using sorted().

            election_counted = zip(Candidate_Count, Candidate_list)
            election_results = sorted(election_counted, reverse = True)

#Print 
#Print The Header

            for i in range(20):
                print("* ", end='')

            print(" ")
            print("Election Results")
            for i in range(20):
                print("* ", end='')

            print(" ")

            for entry in election_results:
                vote_percent = entry[0]/total_votes *100
                display_percent = str(round(entry[0]/total_votes *100))
                print(" ")
                print("Candidate : " + entry[1]+" ; " + " Votes : "+ display_percent + "%")
                print(" ")

#Print Winner

            for i in range(20):
                print("* ", end='')

            print(" ")
            entry = election_results[0]
            print('\033[1m'+"The Winner is Candidate "+ entry[1])


            for i in range(20):
                print("* ", end='')

#Writing to the Output File
#outputfile_location = os.path.join(thisfile_location, 'election_results.csv')   
#election_results.csv
#Candidate, Percent
            with open('election_results.csv', mode='w') as output_file:
                results_writer = csv.writer(output_file, delimiter=',')
                results_writer.writerow(['Candidate', 'Percent'])
                for entry in election_results:
                    results_writer.writerow([entry[0], entry[1]])

                print(" ")

                print(" ")
                print('\033[94m' + "The Election Results are available:")
                print("filename: <election_results.csv>, Rows: Candidate, Percent")
                #try blinking
                #\33[5m and \33[6m
                print('\033[92m' "QED")

#End of File
#QED