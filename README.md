Django Expense Tracker
A simple yet powerful Expense Tracker web application built using Django. This app allows users to register, log in, add and categorize their expenses, and view insightful summaries including total yearly spending and category-wise breakdowns with visual charts.
Key Features
•	User authentication: login & logout
•	Add, view, and categorize expenses
•	Yearly total expense summary
•	Pie chart visualization by category
•	Filter expenses by month and year
Technologies Used
•	Backend: Django 
•	Frontend: HTML,  JavaScript
•	Database: SQLite (default, easy to set up for development)
•	Charting: Chart.js for category-wise visualization
Setup Instructions
1.	Clone the Repository
git clone https://github.com/your-username/expense-tracker.git
cd expense-tracker  
2.	Create and Activate Virtual Environment
python -m venv venv
venv\Scripts\activate
3.	Install Dependencies
pip install -r requirements.txt
4.	Set Up the Database
python manage.py migrate
5.	Create Superuser (Admin Login)
python manage.py createsuperuse
6.	 Run the Development Server
python manage.py runserver
Visit http://127.0.0.1:8000/login/ in your browser to log in and start using the app.
