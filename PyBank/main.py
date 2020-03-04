#Shiuli Ganguly
#Read the csv file as a Dictionary and Input into a List
#Use the List to analyze the data
import os
import csv
thisfile_location = os.path.dirname(os.path.realpath(__file__))             #This File
datafile_location = os.path.join(thisfile_location, 'budget_data.csv')      #Given File
outputfile_location = os.path.join(thisfile_location, 'fin_data.csv')
outputfile_location1 = os.path.join(thisfile_location, 'fin_report.txt')

with open(datafile_location) as budget:
        cheque_list = []
        change_list = []
        count = 0
        average_change = 0
        total_change = 0
        Net_total = 0
        Net_Profit = 0
        Net_Loss = 0
        Net_value = 0
        Max_Profit = 0
        Most_Loss = 0
        Catch_index_Max = 0
        Catch_index_Min = 0
        
   
        budget_row = csv.DictReader(budget)

        for row in budget_row:
            cheque_list.append(row)
            count = count +1
        
        #number_of_entries = count
        # Caution cheque_list has data starting at 0 
        # Caution cheque_list starts at 0 and ends at (count-1)
  

        for i in range(count):
            Net_amount = cheque_list[i]['Profit/Losses']
            #print(Net_amount)
            Net_value = int(Net_amount)
            Net_total = Net_total + Net_value
            if(Net_value>0):
                Net_Profit = Net_Profit + Net_value

            if(Net_value<0):
                Net_Loss = Net_Loss + Net_value


        if count>1:
            for i in range(count-1):
                Net_amount = cheque_list[i]['Profit/Losses']
                Net_value = int(Net_amount) 
                Net_amount_next = cheque_list[i+1]['Profit/Losses']
                Net_value_next = int(Net_amount_next) 
                change = Net_value_next - Net_value
                total_change = total_change + change
                change_list.append(change)
                if change > Max_Profit :
                    Max_Profit = change
                    Catch_index_Max =i+1
                if change < Most_Loss:
                    Most_Loss = change
                    Catch_index_Min = i+1

        if(count>1):
            average_change = total_change/(count-1)
            average_change = round(average_change, 2)

        with open('fin_datat.csv', mode='w') as output_file:
                results_writer = csv.writer(output_file, delimiter=',')
                results_writer.writerow(['Key Month', 'Most Profit/Loss'])
                d = cheque_list[Catch_index_Max]['Date']
                p = cheque_list[Catch_index_Max]['Profit/Losses']
                results_writer.writerow([d, p])
                d = cheque_list[Catch_index_Min]['Date']
                p = cheque_list[Catch_index_Min]['Profit/Losses']
                results_writer.writerow([d, p])

        
        with open('fin_report.txt', mode='w') as output_file:
                #results_writer = csv.writer(output_file)
                output_file.writelines("* Financial Analysis /n")
                output_file.writelines("* Total Months : " + str(count)+ " months /n")
                output_file.writelines("* Total : $ " + str(Net_total) + "/n")
                output_file.writelines("* Average Change : $ " + str(average_change)+"/n")
                output_file.writelines("* Maximum Profit : $ " + str(Max_Profit)+"/n")
                d = cheque_list[Catch_index_Max]['Date']
                output_file.writelines("* Greatest increase in "+ d + "/n")
                output_file.writelines("* Most Loss : $ " + str(Most_Loss)+"/n")
                d = cheque_list[Catch_index_Min]['Date']
                output_file.writelines("* Greatest Loss in "+ d + "/n")

                
bold = '\033[1m'
reset='\033[0m'
blue='\033[94m'
grey ='\33[90m'

print(grey)
for _ in range(20):
    print("* ", end='')
print(reset)



print(bold)
print(blue + "Financial Analysis")
#print(reset)


print(grey)
for _ in range(20):
    print("* ", end='')
#print(" ")
print(reset)




print("Total Months : " + str(count)+ " months")
print("Total : $ " + str(Net_total))
print("Average Change : $ " + str(average_change))
print(blue)
print("Maximum Profit : $ " + str(Max_Profit))
d = cheque_list[Catch_index_Max]['Date']
p = cheque_list[Catch_index_Max]['Profit/Losses']
print("Greatest increase in "+ d)
#print(cheque_list[Catch_index_Max])
print(reset)
#print(grey + "Previous Month")
#print(cheque_list[Catch_index_Max-1])
print("Most Loss : $ " + str(Most_Loss))
d = cheque_list[Catch_index_Min]['Date']
p = cheque_list[Catch_index_Min]['Profit/Losses']
print("Greatest Loss in  "+ d)
#print(grey + "Previous Month")
#print(cheque_list[Catch_index_Min-1])
print(reset)

print(grey)
for _ in range(20):
    print("* ", end='')
print(" ")
print(reset)

             

           