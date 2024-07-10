from openai import OpenAI
import mysql.connector
from mysql.connector import errorcode
import os
client = OpenAI()

USER = os.getenv('MYSQL_USER')
PASSWORD = os.getenv('MYSQL_PASS')
try:
  db = mysql.connector.connect(
      host= "localhost",
      user = USER,
      password = PASSWORD,
      database = "Aleyda_Inc"
  )
  cursor = db.cursor()
except mysql.connector.Error as Err:
  if Err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
    print("Invalid Credientials")
    exit()
  if Err.errno == errorcode.ER_BAD_DB_ERROR:
    print("Database not found")
    exit()
  else:
    print("Cannot connect to the database", Err)
    exit()


# with open("setUp.sql", "r") as file:
#     setup_sql = file.read()
# setup_commands = setup_sql.split(";")
# for command in setup_commands:
#     cursor.execute(command)

# db.commit()

# with open("DataEntry.sql","r") as query:
#    data_entry = query.read()
# query_commands = data_entry.split(";")
# for command in query_commands:
#    cursor.execute(command)
  
# db.commit()

questions =[
   'What is the most popular service in the database?', #Answer is 9012
   'Do most cleaning bookings get completed or canceled?', #Completed
   'What is the most common service description in the service?', #Vacuum and sweep
   'What are the most common type of houses serviced?', #Mansions and Country Clubs
   'When should a booking be made when for Arthur\'s house when Aleyda is available?',
   'Is there a bias towards what kind service is requested relative to the house type?',
   'What is the best type of service?',
   'Is there a trend as to when the booking times are at?',
   'Are most days of the bookings based around the week or weekend?'
]

sqlSystemMessage = {'role': 'system', 'content':'''
Give me ONLY the SQL commands to answer the questions.
If there is an error do not explain it. Do not give any context or additional information.
The data base structure is as follows:
CREATE TABLE IF NOT EXISTS Workers(
    woker_Id INT PRIMARY KEY AUTO_INCREMENT,
    firstName VARCHAR(10),
    lastName VARCHAR(20),
    phone VARCHAR(10),
    address VARCHAR(20)
);

CREATE TABLE IF NOT EXISTS Customer(
    customer_id INT PRIMARY KEY UNIQUE,
    customer_name VARCHAR(20) NOT NULL,
    customer_addr VARCHAR(50) NOT NULL,
    customer_phone VARCHAR(10),
    house_type ENUM('Condo','Apartment','Mansion','Country Club') NOT NULL
);

CREATE TABLE IF NOT EXISTS Service(
    service_Id INT PRIMARY KEY UNIQUE,
    service_description VARCHAR(200) NOT NULL,
    service_price DECIMAL(10,2) NOT NULL
);

CREATE TABLE IF NOT EXISTS Booking(
    booking_id INT PRIMARY KEY UNIQUE,
    booking_date DATE NOT NULL,
    booking_time TIME NOT NULL,
    booking_status ENUM('Pending', 'Confirmed', 'Canceled', 'Completed') NOT NULL,
    customer_id INT NOT NULL,
    worker_id INT NOT NULL,
    service_id INT NOT NULL,
    FOREIGN KEY (customer_id) REFERENCES Customer (customer_id),
    FOREIGN KEY (worker_id) REFERENCES Workers(woker_Id),
    FOREIGN KEY (service_id) REFERENCES Service(service_Id)
);
'''}

friendlySystemMessage = {'role': 'system','content':'''
Regarding the previous question about the database.
Now, please give a user-friendly response about the user's question.
This will be the final message in this conversation.
The structure of the data base is as follows:
CREATE TABLE IF NOT EXISTS Workers(
    woker_Id INT PRIMARY KEY AUTO_INCREMENT,
    firstName VARCHAR(10),
    lastName VARCHAR(20),
    phone VARCHAR(10),
    address VARCHAR(20)
);

CREATE TABLE IF NOT EXISTS Customer(
    customer_id INT PRIMARY KEY UNIQUE,
    customer_name VARCHAR(20) NOT NULL,
    customer_addr VARCHAR(50) NOT NULL,
    customer_phone VARCHAR(10),
    house_type ENUM('Condo','Apartment','Mansion','Country Club') NOT NULL
);

CREATE TABLE IF NOT EXISTS Service(
    service_Id INT PRIMARY KEY UNIQUE,
    service_description VARCHAR(200) NOT NULL,
    service_price DECIMAL(10,2) NOT NULL
);

CREATE TABLE IF NOT EXISTS Booking(
    booking_id INT PRIMARY KEY UNIQUE,
    booking_date DATE NOT NULL,
    booking_time TIME NOT NULL,
    booking_status ENUM('Pending', 'Confirmed', 'Canceled', 'Completed') NOT NULL,
    customer_id INT NOT NULL,
    worker_id INT NOT NULL,
    service_id INT NOT NULL,
    FOREIGN KEY (customer_id) REFERENCES Customer (customer_id),
    FOREIGN KEY (worker_id) REFERENCES Workers(woker_Id),
    FOREIGN KEY (service_id) REFERENCES Service(service_Id)
);
'''}

def getSqlForQuestion(sqlSystemMessage, question):
   response = client.chat.completions.create(
       model = 'gpt-3.5-turbo-1106', 
       messages=[
           sqlSystemMessage,
           {'role': 'user', 'content': question}
       ]
   )
   print("Question: ", question)
   print(response.choices[0].message.content)
   print()
   return response.choices[0].message.content


def getFriendlyResponse(friendlySystemMessage, question, sqlResponse, resultsString):
   promptContent = question + '\nHere is the SQL query I ran:\n' + sqlResponse + '\nAnd here are the query\'s results:\n' + resultsString
   response = client.chat.completions.create(
       model = 'gpt-3.5-turbo-1106', 
       messages=[
           friendlySystemMessage,
           {'role': 'user', 'content': promptContent}
       ]
   )
   print(response.choices[0].message.content)
   print('-'*30)


def answerQuestions(indices):
   for i in indices:
      sqlResponse = getSqlForQuestion(sqlSystemMessage, questions[i])
      cursor.execute(sqlResponse)
      queryResults = cursor.fetchall()
      resultsString = '\n'.join(map(str, queryResults))
      print('Database results:', resultsString, sep='\n')
      print()

      getFriendlyResponse(friendlySystemMessage, questions[i], sqlResponse, resultsString)

indicesOfQuestionsToAnswer = [-1]
answerQuestions(indicesOfQuestionsToAnswer)

cursor.close()
db.close()

