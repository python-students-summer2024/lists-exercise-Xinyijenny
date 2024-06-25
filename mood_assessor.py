import datetime
import os

def ask_mood():
    invalid = True #flag
    while invalid:
        response = input("Enter your current mood here(happy, relaxed, apathetic, sad, or angry): ").lower().strip()
        if response in ["happy","relaxed","apathetic","sad","angry"]:
            if response == "happy":
                return 2
            elif response == "relaxed":
                return 1
            elif response == "apathetic":
                return 0
            elif response == "sad":
                return -1
            else:
                return -2
        else:
            print("Opps, invalid response, please do it again!\n")

def create_data():
    if not os.path.exists('data'):#check if there is a directory named 'data'
        os.makedirs('data') # if not, create directory

    file_path = os.path.join('data', 'mood_diary.txt')
    if not os.path.exists(file_path): # check if the text file in the directory
        with open(file_path, 'w', encoding='utf-8') as file:
            pass  



def store_mood_date():

    mood_value = ask_mood()
    date_today = get_date()

    with open('data/mood_diary.txt', 'a', encoding='utf-8') as file:
        
        file.write(f"{date_today},{mood_value}\n") 



def get_date():
    date_today = datetime.date.today() # get the date today as a date object
    date_today = str(date_today) # convert it to a string
    return date_today

def has_entered():
    date_today = get_date()
    with open('data/mood_diary.txt', 'r', encoding='utf-8') as file:
        file_lines = file.readlines()
        for line in file_lines:
            if date_today in line:# if input already today
                return True
            
    return False # return false after checking all lines
            
        
def diagnose():
    with open('data/mood_diary.txt', 'r', encoding='utf-8') as file:
        file_lines = file.readlines()[-7:]#read the last 7 lines
        if len(file_lines)<7:
            return
        
        moodlist = []#create an empty list for storing the mood value number
        for line in file_lines:
            mood = int(line.split(',')[1])#spereate the list strings and look for the second component
            moodlist.append(mood)#put the value into the new list
        avg_mood = round(sum(moodlist) / 7) # calculate average mood value

        #to find out the the amount user input happy,sad, and apathetic
        happy_count = moodlist.count(2)
        sad_count = moodlist.count(-1)
        apathetic_count = moodlist.count(0)

        #check number of happy, sad, or apathetic
        if happy_count >= 5:
            diagnosis = "manic"
        elif sad_count >= 4:
            diagnosis = "depressive"
        elif apathetic_count >= 6:
            diagnosis = "schizoid"
        #other diagnosis we can look for the average mood 
        else:
            if avg_mood == 2:
                diagnosis = "happy"
            elif avg_mood == 1:
                diagnosis = "relaxed"
            elif avg_mood == 0:
                diagnosis = "apathetic"
            elif avg_mood == -1:
                diagnosis = "sad"
            elif avg_mood == -2:
                diagnosis = "angry"

        print(f"Your diagnosis: {diagnosis}!")




    
    



     
def assess_mood():

    create_data() # create a text file in the subdirectory

    # when there is input already for today
    if has_entered():
        print("Sorry, you have already entered your mood today.")
        return
   
    store_mood_date() # store in the file

    diagnose()


    

    


    
