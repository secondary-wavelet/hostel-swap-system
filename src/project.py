import queries
import display_strings

from neo4j import GraphDatabase
from dotenv import load_dotenv
import os

def isVerifiedID(stud_id):
    return int(stud_id) in range(1,241)

def connectDB():
    load_dotenv()
    URI = "bolt://localhost:7687"
    USERNAME = "neo4j"
    AUTH = (USERNAME, os.getenv("NEO4J_PASSWORD"))

    try:
        driver = GraphDatabase.driver(URI, auth = AUTH)
        driver.verify_connectivity()
        print("Connected to DB")
        return driver
    except Exception as e:
        print(f"Connection failed: {e}")
        return None
        
def showLoginMsg(driver, stud_id):
    records = driver.execute_query(queries.LOGIN_CONFIRMATION, stud_id = stud_id).records
    deets = records[0]
    print("******************")
    print(f"Logged in as {deets['s']['Name']}\nID {stud_id}.\nHostel Room: {deets['h']['Name']}/{deets['r']['Number']}")

def showMenu():
    print(display_strings.MENU)

def managePreferences(driver, stud_id):
    preferences = driver.execute_query(queries.SHOW_CURRENT_PREFERENCES, stud_id = stud_id).records
    if(not preferences):
        print("You have not currently set any swap preferences.")
    else:
        print("Your current swap preferences are:-")
        for preference in preferences:
            print(preference)

    print(display_strings.PREFERENCE_MENU)
    opt = input("Your choice -> ")
    match(opt):
        case '1':
            createPreference(driver, stud_id)
        case '2':
            editPreference(driver, stud_id)
        case '3':
            deletePreference(driver, stud_id)
        case _:
            pass

def createPreference(driver, stud_id):
    pass

def editPreference(driver, stud_id):
    pass

def deletePreference(driver, stud_id):
    pass

def findSwaps():
    pass

def main():
    driver = connectDB()

    stud_id = input("Enter your ID: ")
    
    if not isVerifiedID(stud_id):
        print("Invalid ID number.")
        print("Exiting.")
        return -1
    
    if(driver):
        showLoginMsg(driver, stud_id)
        isNotExit = True
        retval = -1
        while isNotExit:
            showMenu()
            opt = input("Your choice -> ")

            match(opt):
                case '1':
                    managePreferences(driver, stud_id)
                case '2':
                    findSwaps(driver, stud_id)
                case '3':
                    print("Exiting")
                    print("Closing DB connection")
                    driver.close()
                    retval = 0
                    isNotExit = False
                case _:
                    pass
    return retval
if __name__ == "__main__":
    main()