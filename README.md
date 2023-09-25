# Django Web Application

Welcome to our Django web application project! This web application is designed to showcase user authentication, file upload functionality, and creative webpage design.

## Features

1. **User Authentication**
   - Users can register with a username, email, and password.
   - Secure user authentication using Django's built-in authentication system.
   - Passwords are securely hashed and stored.

2. **File Upload Feature**
   - Authenticated users can upload files, such as images and documents, to the server.
   - Only logged-in users can access the file upload functionality.
   - Uploaded files are stored securely on the server.

3. **Creative Webpage Design**
   - We have designed aesthetically pleasing and user-friendly webpages for:
     - User registration
     - User login
     - user logout
     - File upload
   - The layout, color scheme, and styling have been carefully chosen for an appealing interface.

## Getting Started

Follow these steps to set up and run the application locally:

1. **Clone the Repository**
```bash
git clone https://github.com/pranita28Dane/CreatorsLab-Assignment-Task.git
cd CreatorsLab-Assignment-Task
```

2. **Create a Virtual Environment (Optional but recommended)**
```bash
python -m venv env
On Windows, use `env\Scripts\activate`
```
   
3. **Install Dependencies**
```bash
pip install -r requirements.txt
```

4. **Install Pillow for Image Handling**
```bash
pip install pillow
```

5. **Create a Superuser**
Create a superuser account to access the Django admin panel:
```bash
python manage.py createsuperuser
username: admin
password: admin
```

6. **Apply makemigration and Migrate**
```bash
python manage.py makemigrations
python manage.py migrate
```

7. **Run the Application**
```bash
python manage.py runserver
```

8. **Access the Application**
Open your web browser and go to http://localhost:8000 to access the application.


 ## Screenshots
  Here are some screenshots of our webpages:
- HomePage
<img src="https://github.com/pranita28Dane/CreatorsLab-Assignment-Task/blob/dev/img/HomePage.png" width="900" height= "500">

- User Registration
<img src="https://github.com/pranita28Dane/CreatorsLab-Assignment-Task/blob/dev/img/Register.png" width="900" height= "500">
  
- User Login
<img src="https://github.com/pranita28Dane/CreatorsLab-Assignment-Task/blob/dev/img/Login.png" width="900" height= "500">

- File Upload
     1. **Simple Upload**
        <img src="https://github.com/pranita28Dane/CreatorsLab-Assignment-Task/blob/dev/img/Simple_Upload.png" width="900" height= "500">
 
     2. **Model Form Upload**
        <img src="https://github.com/pranita28Dane/CreatorsLab-Assignment-Task/blob/dev/img/Model_Form_Upload.png" width="900" height= "500">


