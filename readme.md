# Online School Backend

This repository contains the backend implementation of an online school platform using Django and Django REST Framework. The backend handles user registration, authentication, course management, and more, offering separate functionalities for students and teachers.

---

## Getting Started

### 1. Running the Local Server

To run the project locally, follow these steps:

- Ensure all dependencies in the `requirements.txt` file are installed on your machine.
- Run the following command to start the local development server:
    ```bash
    python manage.py runserver
    ```
- Once the server is running, open the `localhost` link in your web browser (e.g., `http://127.0.0.1:8000/`).

### 2. Accessing the Live Server

To explore the project online, simply visit the following link:
- [Live Demo](https://drf-online-school-jsrn-getm.vercel.app/)

---

## API Endpoints

The following API endpoints are available for interacting with the system. These are organized into categories based on user roles (public, teacher, student).

### 1. User Endpoints

- **POST** - Register a new user:  
  `POST /account/registration/`
- **POST** - Login with email and password:  
  `POST /account/login/`
- **GET** - Logout the user:  
  `GET /account/logout/`
- **GET** - Get user details by ID:  
  `GET /account/user_details/<pk>/`
- **POST** - Reset password by email:  
  `POST /account/reset_password/<email>/`

---

### 2. Public Endpoints

- **GET** - Get the top four favorite courses:  
  `GET /course/favorite_course/`
- **GET** - Get four featured courses for the homepage:  
  `GET /course/public_all/home/`
- **GET** - Get all available courses:  
  `GET /course/public_all/all/`
- **GET** - Get all reviews:  
  `GET /course/review/all`
- **GET** - Get reviews for a specific course by course ID:  
  `GET /course/review/<course_id>/`
- **GET** - Get all course categories:  
  `GET /course/category/`
- **GET** - Get courses by department ID:  
  `GET /course/get_by_dep/<dep_id>/`
- **POST** - Submit a contact form:  
  `POST /contact_us/`

---

### 3. Teacher Private Endpoints

- **POST** - Add a new course (authenticated by teacher ID):  
  `POST /course/authentic/<teacher_id>/`
- **PUT** - Edit an existing course (authenticated by teacher ID and course ID):  
  `PUT /course/details/<teacher_id>/<id>/`
- **GET** - Get a list of all students for a specific teacher:  
  `GET /course/my_student/<userId>/`

---

### 4. Student Private Endpoints

- **POST** - Submit a review for a course:  
  `POST /course/review_create/`
- **POST** - Enroll in a course:  
  `POST /course/enrol_create/`
- **GET** - Get a list of all courses the student is enrolled in:  
  `GET /course/enrol/<enrol_by>/`

---

## Technologies Used

- **Python**: Core programming language.
- **Django**: Backend framework for building the web application.
- **Django REST Framework**: For building RESTful APIs.
- **PostgreSQL**: Database used for storing data.
- **Vercel**: Platform for deploying the backend.

---

## Setup and Installation (For Developers)

To get the backend running locally:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-repo/online-school-backend.git
   ```

2. **Navigate to the project directory**:
   ```bash
   cd online-school-backend
   ```

3. **Create a virtual environment** (optional but recommended):
   ```bash
   python -m venv env
   source env/bin/activate  # For Linux/macOS
   env\Scripts\activate  # For Windows
   ```

4. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

5. **Apply migrations** to set up the database:
   ```bash
   python manage.py migrate
   ```

6. **Run the development server**:
   ```bash
   python manage.py runserver
   ```

7. **Access the application** in your browser at `http://127.0.0.1:8000/`.

---

## License

This project is licensed under the **MIT License**. See the `LICENSE` file for more details.

---

## Contact

For any inquiries or issues, feel free to contact me:

- **Md Rakib Bhuiyan**  
- Email: [your-rakib2046.md@gmail.com]  
- GitHub: [https://github.com/46ra20](https://github.com/46ra20)

```

This version organizes the information into sections and provides clear instructions for both users and developers. Let me know if you'd like to adjust anything!