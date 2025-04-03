
## 📌 Project Overview
The **Management System** is a Django-based web application that allows users to manage authors, books, and borrowing records efficiently. It provides functionalities to add, list, and export data to an Excel file.

## 🚀 Features
- **Author Management**: Add and list authors.
- **Book Management**: Add and list books with author details.
- **Borrow Record Management**: Track borrowed books with user details.
- **Export Data**: Download authors, books, and borrow records as an Excel file.
- **Pagination**: Easily navigate through lists of authors, books, and borrow records.

## 🛠️ Technologies Used
- **Backend**: Django
- **Frontend**: HTML, CSS, Bootstrap
- **Database**: SQLite (default Django database, but can be changed)
- **Other**: OpenPyXL (for exporting data to Excel)

## 🏗️ Installation Guide
### 1️⃣ Clone the Repository
```bash
git clone https://github.com/devv1310/Hackerkernal_Task/
cd paperstore
```

### 2️⃣ Create a Virtual Environment (Recommended)
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Apply Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5️⃣ Run the Development Server
```bash
python manage.py runserver
```
Visit **http://127.0.0.1:8000/** in your browser.

## 📂 Project Structure
```
library_management/
│── project/     # Main Django project settings
│── paperstore/                # Library app (models, views, forms, etc.)
│   ├── migrations/         # Database migrations
│   ├── templates/library/  # HTML templates
│   ├── static/             # Static files (CSS, JS, images)
│── db.sqlite3              # SQLite database
│── manage.py               # Django project manager
│── requirements.txt        # Project dependencies
│── README.md               # Project documentation
```

## 📜 URL Routes
| URL Path | Functionality |
|----------|--------------|
| `/author/` | List all authors |
| `/book/` | List all books |
| `/borrow-records/` | List all borrow records |
| `/add-author/` | Add a new author |
| `/add-book/` | Add a new book |
| `/add-borrow-record/` | Add a new borrow record |
| `/exportexcel/` | Export data to an Excel file |

## 🎯 Future Enhancements
- User authentication (Admin login, user roles)
- Book availability tracking
- Search and filter options
- API endpoints using Django REST Framework

## 💡 Contributing
Pull requests are welcome! If you'd like to contribute, fork the repo and submit a PR.

## 📄 License
This project is open-source and available under the [MIT License](LICENSE).

---
Happy coding! 🚀


