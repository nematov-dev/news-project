# 📰 S-News.uz Website - Overview

## About the Website

The S-News.uz website is a dynamic platform where users can read the latest news and blogs, as well as engage with content by commenting on posts.  
It provides a rich, interactive experience for visitors, allowing them to sign up, create accounts, and manage their profiles.

---

## Features

### User Registration and Account Creation
- Users can sign up to create an account by providing basic information such as name, email, and password.
- After registration, users can log in to access personalized content and manage their profiles.

### Login
- Registered users can log in to their accounts using their credentials (email and password).

### Profile Management
- Users can edit their profile details after logging in, including name, email, and password.

### News and Blog Reading
- The website provides a variety of news articles and blog posts in different categories for users to read.

### Commenting on Posts
- Registered users can leave comments on both news articles and blogs, fostering interaction with the community.

---

## How to Use

1. **Sign Up / Register**  
   Fill out the registration form to create a new account.

2. **Login**  
   Log in with your registered email and password.

3. **Edit Profile**  
   After logging in, navigate to your profile section to update your details.

4. **Comment on Blogs**  
   Browse news and blog posts and leave your thoughts in the comment section.

---

## Technologies Used

- **Frontend:** HTML, CSS, JavaScript  
- **Backend:** Python, Django framework  
- **Database:** PostgreSQL  

---

## Installation

To run this project locally:

1. **Clone the repository:**

```bash
git clone https://github.com/nematov-dev/news-project.git
```

2. **Move to the project directory:**

```bash
cd news-project
```

3. **Install required libraries:**

```bash
pip install -r requirements.txt
```

4. **Update the database:**

```bash
python manage.py migrate
```

5. **Start the local server:**

```bash
python manage.py runserver
```

Once the server is running, open your browser and navigate to `http://127.0.0.1:8000` to access the website.

---

## Project Structure

```
app_blogs/          # Blog management app
app_common/         # Common utilities and templates
app_news/           # News management app
app_pages/          # Static pages (about, contact, etc.)
app_users/          # User registration, authentication, and profile management
assets/assets/      # Frontend assets (CSS, JS, images)
media/profile_pics/ # User profile pictures
templates/          # HTML templates
manage.py           # Django management script
requirements.txt    # Python dependencies
README.md           # Project overview
```

---

## Author

👤 [Saidakbar Nematov](https://nematov.uz)  

---

## License

This project is intended for **educational and demonstration purposes**.
