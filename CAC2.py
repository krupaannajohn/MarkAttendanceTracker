from bottle import Bottle, request, response, run, template, redirect
from pymongo import MongoClient

app = Bottle()

# MongoDB setup
client = MongoClient('mongodb://localhost:27017/')
db = client['student_grade_tracker']
collection = db['students']

# Valid usernames and passwords
valid_credentials = {
    "Kavita": "seli2981",
    "Alok": "zeus2345!",
    "Sharmila": "hethy34657",
    "Alia": "samoy23478",
    "Sameer": "liner5678"
}

# Routes
@app.route('/')
def index():
    return '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>Student Grade-Attendance Tracker</title>
      <style>
        body {
          font-family: Arial, sans-serif;
          background-color: #1C2340; 
          display: flex;
          justify-content: center;
          align-items: center;
          height: 100vh;
          margin: 0;
        }
        .container {
          width: 700px;
          height: 1000px;
          padding: 20px;
          background-color: #F0DAC5; 
          border-radius: 10px;
          box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
          text-align: center;
          display: flex;
          flex-direction: column;
          justify-content: center;
          align-items: center;
        }
        h1 {
          color: #50223C; 
        }
        h4 {
          color: #50223C; 
        }
        form {
          margin-top: 20px;
          display: flex;
          flex-direction: column;
          align-items: center;
        }
        input[type="text"], input[type="password"] {
          padding: 10px;
          border-radius: 5px;
          border: 1px solid #cccccc; 
          margin-bottom: 10px;
        }
        button {
          padding: 10px 20px;
          background-color: #50223C; 
          color: #F0DAC5; 
          border: none;
          border-radius: 5px;
          cursor: pointer;
        }
        button:hover {
          background-color: #cccccc; 
          color: black;
        }
      </style>
    </head>
    <body>
      <div class="container">
        <img src=https://spacegeneration.org/wp-content/uploads/2020/08/004_SpaceLawPolicy-200x200.png alt="Your Image">
        <h1>Mark & Attendance Tracker</h1>
        <h4>Please enter login credentials below:</h4>
        <form action="/login" method="post">
          <input type="text" id="username" name="username" placeholder="Username" required>
          <br>
          <input type="password" id="password" name="password" placeholder="Password" required>
          <br>
          <button type="submit">Login</button>
        </form>
      </div>
    </body>
    </html>
    '''

@app.route('/login', method='POST')
def login():
    username = request.forms.get('username')
    password = request.forms.get('password')
    if username in valid_credentials and valid_credentials[username] == password:
        response.set_cookie("username", username, secret="my_secret_key")
        redirect('/home')
    else:
        return "Invalid username or password."

@app.route('/home')
def home():
    username = request.get_cookie("username", secret="my_secret_key")
    if username:
        return template('''
        <!DOCTYPE html>
        <html lang="en">
        <head>
          <meta charset="UTF-8">
          <meta name="viewport" content="width=device-width, initial-scale=1.0">
          <title>Home</title>
          <style>
          body {
          font-family: Arial, sans-serif;
          background-color: #1C2340; 
          display: block;
          justify-content: center;
          align-items: center;
          height: 100vh;
        }
        .container {
          width: 700px;
          height: 1000px;
          padding: 20px;
          background-color: #F0DAC5; 
          border-radius: 10px;
          box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
          text-align: center;
        }
        h1 {
          color: white; 
        }
        p {
          color: white; 
        }
        form {
          margin-top: 20px;
          align-items: center;
        }
        input[type="text"], input[type="password"] {
          padding: 10px;
          border-radius: 5px;
          border: 1px solid #cccccc; 
          margin-bottom: 10px;
        }
        button {
          padding: 10px 20px;
          background-color: #50223C; 
          color: #F0DAC5; 
          border: none;
          border-radius: 5px;
          cursor: pointer;
          margin-bottom: 10px;
        }
        button:hover {
          background-color: #cccccc; 
          color: black
        }
        </style>
        </head>
        <body>
          <h1>Welcome, {{username}}!</h1>
          <br>
          <p>You are now logged in.</p>
          <br>
          <button onclick="location.href='/mark-retrieval';">Retrieve Marks</button>
          <br>
          <button onclick="location.href='/attendance-retrieval';">Retrieve Attendance</button>
        </body>
        </html>
        ''',username=username)
    else:
        return "Access denied. Please login first."

@app.route('/mark-retrieval', method='GET')
def mark_retrieval_form():
    return '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>Mark Retrieval</title>
      <style>
        body {
          font-family: Arial, sans-serif;
          background-color: #1C2340; 
          display: flex;
          justify-content: center;
          align-items: center;
          height: 100vh;
          margin: 0;
        }
        .container {
          width: 700px;
          height: 1000px;
          padding: 20px;
          background-color: #F0DAC5; 
          border-radius: 10px;
          box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
          text-align: center;
          display: flex;
          flex-direction: column;
          justify-content: center;
          align-items: center;
        }
        h1 {
          color: #50223C; 
        }
        h4 {
          color: #50223C; 
        }
        form {
          margin-top: 20px;
          display: flex;
          flex-direction: column;
          align-items: center;
        }
        input[type="text"], input[type="password"] {
          padding: 10px;
          border-radius: 5px;
          border: 1px solid #cccccc; 
          margin-bottom: 10px;
        }
        button {
          padding: 10px 20px;
          background-color: #50223C; 
          color: #F0DAC5; 
          border: none;
          border-radius: 5px;
          cursor: pointer;
        }
        button:hover {
          background-color: #cccccc; 
          color: black
        }
      </style>
    </head>
    <body>
      <div class="container">
        <h1>Mark Retrieval</h1>
        <form action="/mark-retrieval" method="post">
          <label for="reg-no">Registration Number:</label>
          <input type="text" id="reg-no" name="reg-no" required>
          <br>
          <button type="submit">Retrieve Marks</button>
        </form>
        <br>
        <div id="mark-details"></div>
        <button onclick="location.href='/update-marks';">Update Student</button>
        <br>
        <button onclick="location.href='/delete-student';">Delete Student</button>
      </div>
    </body>
    </html>
    '''

@app.route('/mark-retrieval', method='POST')
def retrieve_marks():
    reg_no = request.forms.get('reg-no')
    student = collection.find_one({'reg_no': reg_no})
    if student:
        name = student.get('name', 'N/A')
        mark_details = student.get('marks', {})
        return template('''
        <!DOCTYPE html>
        <html lang="en">
        <head>
          <meta charset="UTF-8">
          <meta name="viewport" content="width=device-width, initial-scale=1.0">
          <title>Mark Details</title>
          <style>
            body {
              background-color: #1C2340;
              color: #F0DAC5;
              font-family: Arial, sans-serif;
            }
            table {
              border-collapse: collapse;
              width: 100%;
            }
            th, td {
              border: 1px solid #F0DAC5;
              text-align: left;
              padding: 8px;
            }
            th {
              background-color: #1C2340;
              color:#F0DAC5
            }
            .low-marks {
              color: red;
            }
            button {
              padding: 10px 20px;
              background-color: #50223C; 
              color: #F0DAC5; 
              border: none;
              border-radius: 5px;
              cursor: pointer;
              margin-bottom: 10px;
        }
        button:hover {
          background-color: #cccccc; 
          color: black
        }
          </style>
        </head>
        <body>
        <h2>Mark Details</h2>
        <p>Name: {{ name }}</p>
        <p>Registration Number: {{ reg_no }}</p>
        <table>
          <tr>
            <th>Subject</th>
            <th>Mark</th>
          </tr>
          % for subject, mark in mark_details.items():
            <tr>
              <td>{{ subject }}</td>
              % if mark < 40:
                <td class="low-marks">{{ mark }}</td>
              % else:
                <td>{{ mark }}</td>
              % end
            </tr>
          % end
        </table>
        <br>
        <button onclick="location.href='/update-marks';">Update Student</button>
        <button onclick="location.href='/delete-student';">Delete Student</button>
      </body>
      </html>
        ''', name=name, reg_no=reg_no, mark_details=mark_details)
    else:
        return "Student not found"

@app.route('/attendance-retrieval', method='GET')
def attendance_retrieval_form():
    return '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>Attendance Retrieval</title>
      <style>
        body {
          font-family: Arial, sans-serif;
          background-color: #1C2340; 
          display: flex;
          justify-content: center;
          align-items: center;
          height: 100vh;
          margin: 0;
        }
        .container {
          width: 700px;
          height: 1000px;
          padding: 20px;
          background-color: #F0DAC5; 
          border-radius: 10px;
          box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
          text-align: center;
          display: flex;
          flex-direction: column;
          justify-content: center;
          align-items: center;
        }
        h1 {
          color: #50223C; 
        }
        h4 {
          color: #50223C; 
        }
        form {
          margin-top: 20px;
          display: flex;
          flex-direction: column;
          align-items: center;
        }
        input[type="text"], input[type="password"] {
          padding: 10px;
          border-radius: 5px;
          border: 1px solid #cccccc; 
          margin-bottom: 10px;
        }
        button {
          padding: 10px 20px;
          background-color: #50223C; 
          color: #F0DAC5; 
          border: none;
          border-radius: 5px;
          cursor: pointer;
        }
        button:hover {
          background-color: #cccccc; 
          color: black
        }
      </style>
    </head>
    <body>
      <div class="container">
        <h1>Attendance Retrieval</h1>
        <form action="/attendance-retrieval" method="post">
          <label for="reg-no">Registration Number:</label>
          <input type="text" id="reg-no" name="reg-no" required>
          <br>
          <button type="submit">Retrieve Attendance</button>
        </form>
        <br>
        <div id="attendance-details"></div>
        <button onclick="location.href='/update-attendance';">Update Student</button>
        <br>
        <button onclick="location.href='/delete-student';">Delete Student</button>
      </div>
    </body>
    </html>
    '''

@app.route('/attendance-retrieval', method='POST')
def retrieve_attendance():
    reg_no = request.forms.get('reg-no')
    student = collection.find_one({'reg_no': reg_no})
    if student:
        name = student.get('name', 'N/A')
        attendance_details = student.get('attendance', {})
        return template('''
        <!DOCTYPE html>
        <html lang="en">
        <head>
          <meta charset="UTF-8">
          <meta name="viewport" content="width=device-width, initial-scale=1.0">
          <title>Attendance Details</title>
          <style>
            body {
              background-color: #1C2340;
              color: #F0DAC5;
              font-family: Arial, sans-serif;
            }
            table {
              border-collapse: collapse;
              width: 100%;
            }
            th, td {
              border: 1px solid #F0DAC5;
              text-align: left;
              padding: 8px;
            }
            th {
              background-color: #1C2340;
              color: #F0DAC5;
            }
            .low-attendance {
              color: red;
            }
            button {
              padding: 10px 20px;
              background-color: #50223C;
              color: #F0DAC5;
              border: none;
              border-radius: 5px;
              cursor: pointer;
              margin-bottom: 10px;
            }
            button:hover {
              background-color: #cccccc;
              color: black;
            }
          </style>
        </head>
        <body>
          <h2>Attendance Details</h2>
          <p>Name: {{ name }}</p>
          <p>Registration Number: {{ reg_no }}</p>
          <table>
            <tr>
              <th>Subject</th>
              <th>Attendance</th>
            </tr>
            % for subject, attendance in attendance_details.items():
              <tr>
                <td>{{ subject }}</td>
                <td class="{{ 'low-attendance' if attendance < 80 else '' }}">{{ attendance }}</td>
              </tr>
            % end
          </table>
          <br>
          <button onclick="location.href='/update-attendance';">Update Student</button>
          <button onclick="location.href='/delete-student';">Delete Student</button>
        </body>
        </html>

        ''',name=name, reg_no=reg_no, attendance_details=attendance_details)
    else:
        return "Student not found"


@app.route('/delete-student', method='GET')
def delete_student_form():
    return '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>Delete Student</title>
      <style>
        
            body {
              background-color: #1C2340;
              color: #F0DAC5;
              font-family: Arial, sans-serif;
            }
            button {
              padding: 10px 20px;
              background-color: #50223C; 
              color: #F0DAC5; 
              border: none;
              border-radius: 5px;
              cursor: pointer;
              margin-bottom: 10px;
        }
        button:hover {
          background-color: #cccccc; 
          color: black
        }
          
      </style>
    </head>
    <body>
      <h1>Delete Student</h1>
      <form action="/delete-student" method="post">
        <label for="reg-no">Registration Number:</label>
        <input type="text" id="reg-no" name="reg-no" required>
        <button type="submit">Delete</button>
      </form>
    </body>
    </html>
    '''


@app.route('/delete-student', method='POST')
def delete_student():
    reg_no = request.forms.get('reg-no')
    result = collection.delete_one({'reg_no': reg_no})
    if result.deleted_count > 0:
        return '''
        <html>
        <head>
            <title>Delete Student</title>
            <style>
                body {
                    background-color: #F0DAC5; 
                    color: #1C2340; 
                    font-family: Arial, sans-serif; 
                }
            </style>
        </head>
        <body>
            <h1 style="color: #50223C;">Student deleted successfully.</h1> 
        </body>
        </html>
        '''
    else:
        return '''
        <html>
        <head>
            <title>Delete Student</title>
            <style>
                body {
                    background-color: #F0DAC5; 
                    color: #1C2340; 
                    font-family: Arial, sans-serif; 
                }
            </style>
        </head>
        <body>
            <h1 style="color: #50223C;">No student found with given registration number.</h1> 
        </body>
        </html>
        '''

@app.route('/update-marks', method='GET')
def update_marks_form():
    return '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>Update Marks</title>
      <style>
        body {
          font-family: Arial, sans-serif;
          background-color: #1C2340; 
          display: flex;
          justify-content: center;
          align-items: center;
          height: 100vh;
          margin: 0;
        }
        .container {
          width: 700px;
          height: 1000px;
          padding: 20px;
          background-color: #F0DAC5; 
          border-radius: 10px;
          box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
          text-align: center;
          display: flex;
          flex-direction: column;
          justify-content: center;
          align-items: center;
        }
        h1 {
          color: #50223C; 
        }
        h4 {
          color: #50223C; 
        }
        form {
          margin-top: 20px;
          display: flex;
          flex-direction: column;
          align-items: center;
        }
        input[type="text"], input[type="password"] {
          padding: 10px;
          border-radius: 5px;
          border: 1px solid #cccccc; 
          margin-bottom: 10px;
        }
        button {
          padding: 10px 20px;
          background-color: #50223C; 
          color: #F0DAC5; 
          border: none;
          border-radius: 5px;
          cursor: pointer;
        }
        button:hover {
          background-color: #cccccc; 
          color: black
        }
      </style>
    </head>
    <body>
      <div class="container">
        <h1>Update Marks</h1>
        <form action="/update-marks" method="post">
          <label for="reg-no">Registration Number:</label>
          <input type="text" id="reg-no" name="reg-no" required>
          <br>
          <label for="subject">Subject:</label>
          <input type="text" id="subject" name="subject" required>
          <br>
          <label for="mark">Mark:</label>
          <input type="text" id="mark" name="mark" required>
          <br>
          <button type="submit">Update Mark</button>
        </form>
      </div>
    </body>
    </html>
    '''

@app.route('/update-marks', method='POST')
def update_marks():
    reg_no = request.forms.get('reg-no')
    subject = request.forms.get('subject')
    mark = int(request.forms.get('mark'))  

    student = collection.find_one({'reg_no': reg_no})
    if student:
        mark_data = student.get('marks', {})
        mark_data[subject] = mark
        collection.update_one({'reg_no': reg_no}, {'$set': {'marks': mark_data}})
        return "Mark updated successfully."
    else:
        return "Student not found."

@app.route('/update-attendance', method='GET')
def update_attendance_form():
    return '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>Update Attendance</title>
      <style>
        body {
          font-family: Arial, sans-serif;
          background-color: #1C2340; 
          display: flex;
          justify-content: center;
          align-items: center;
          height: 100vh;
          margin: 0;
        }
        .container {
          width: 700px;
          height: 1000px;
          padding: 20px;
          background-color: #F0DAC5; 
          border-radius: 10px;
          box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
          text-align: center;
          display: flex;
          flex-direction: column;
          justify-content: center;
          align-items: center;
        }
        h1 {
          color: #50223C; 
        }
        h4 {
          color: #50223C; 
        }
        form {
          margin-top: 20px;
          display: flex;
          flex-direction: column;
          align-items: center;
        }
        input[type="text"], input[type="password"] {
          padding: 10px;
          border-radius: 5px;
          border: 1px solid #cccccc; 
          margin-bottom: 10px;
        }
        button {
          padding: 10px 20px;
          background-color: #50223C; 
          color: #F0DAC5; 
          border: none;
          border-radius: 5px;
          cursor: pointer;
        }
        button:hover {
          background-color: #cccccc; 
          color: black
        }
      </style>
    </head>
    <body>
      <div class="container">
        <h1>Update Attendance</h1>
        <form action="/update-attendance" method="post">
          <label for="reg-no">Registration Number:</label>
          <input type="text" id="reg-no" name="reg-no" required>
          <br>
          <label for="subject">Subject:</label>
          <input type="text" id="subject" name="subject" required>
          <br>
          <label for="attendance">Attendance:</label>
          <input type="text" id="attendance" name="attendance" required>
          <br>
          <button type="submit">Update Attendance</button>
        </form>
      </div>
    </body>
    </html>
    '''

@app.route('/update-attendance', method='POST')
def update_attendance():
    reg_no = request.forms.get('reg-no')
    subject = request.forms.get('subject')
    attendance = int(request.forms.get('attendance'))  

    student = collection.find_one({'reg_no': reg_no})
    if student:
        attendance_data = student.get('attendance', {})
        attendance_data[subject] = attendance
        collection.update_one({'reg_no': reg_no}, {'$set': {'attendance': attendance_data}})
        return "Attendance updated successfully."
    else:
        return "Student not found."
    
if __name__ == '__main__':
    run(app, host='localhost', port=3000, debug=True)