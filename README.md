<<<<<<< HEAD
# Calorie Tracker

![Calorie Tracker](https://img.shields.io/badge/Calorie%20Tracker-v1.0.0-brightgreen)
![Django](https://img.shields.io/badge/Django-3.2-blue)
![License](https://img.shields.io/badge/License-MIT-green)

A comprehensive web application built with Django that enables users to track daily calorie intake with precision and visual insight.

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Technical Stack](#technical-stack)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage Guide](#usage-guide)
- [Project Structure](#project-structure)
- [Customization](#customization)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)
- [License](#license)

## 🔭 Overview

Calorie Tracker is a feature-rich web application designed to help users monitor and manage their daily caloric intake. With an intuitive interface and comprehensive reporting capabilities, it provides valuable insights into dietary patterns, helping users make informed decisions about their nutrition.

The application offers a complete suite of CRUD operations for food entries, along with data visualization tools to track progress toward caloric goals. Whether you're aiming to lose weight, maintain your current weight, or gain weight, Calorie Tracker provides the tools needed to achieve your nutritional objectives.

## ✨ Features

### Core Functionality

- **Complete Food Entry Management**
  - Create, view, update, and delete food entries
  - Record food name, calorie count, and consumption date
  - Optional categorization of food items

- **Advanced Filtering**
  - Filter entries by date with an intuitive calendar widget
  - Search functionality for finding specific food items
  - Sort entries by various criteria

- **Visual Data Representation**
  - Interactive charts showing calorie trends over time
  - Progress bars for daily goal tracking
  - Visual breakdown of nutritional information

### User Experience

- **Intuitive User Interface**
  - Modern, responsive design works across all devices
  - Clean, distraction-free layout emphasizes important data
  - Smooth animations and transitions enhance usability

- **Personalization**
  - Customizable daily calorie goals
  - Light and dark mode themes
  - Goal tracking with personalized feedback

- **Health Insights**
  - Smart nutritional suggestions based on intake
  - Daily, weekly, and monthly consumption summaries
  - Automated alerts for goal progress

## 🛠️ Technical Stack

### Backend
- **Django 3.2+**: Robust Python web framework
- **SQLite** (default database, configurable for other databases)

### Frontend
- **HTML5 / CSS3**: Modern web standards
- **Bootstrap 4**: Responsive design framework
- **JavaScript / jQuery**: Dynamic user interactions
- **Chart.js**: Interactive data visualization
- **Font Awesome**: Icon library
- **Custom CSS Variables**: Theme control

### Additional Libraries
- **django-bootstrap4**: Bootstrap integration
- **Pillow**: Image processing (for future features)
- **django-crispy-forms**: Enhanced form rendering
- **whitenoise**: Efficient static file serving
- **AOS**: Animate On Scroll library

## 📦 Installation

### Prerequisites

- Python 3.6 or higher
- pip (Python package installer)
- Git (optional, for cloning the repository)

### Step-by-Step Installation

1. **Create a Project Directory**
   ```bash
   mkdir -p d:\Calorie-Tracker
   cd d:\Calorie-Tracker
   ```

2. **Set Up a Virtual Environment**
   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Clone or Download the Repository**
   ```bash
   git clone https://github.com/yourusername/calorie-tracker.git .
   
   # If you don't have Git, download and extract the ZIP file
   ```

4. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

5. **Initialize the Database**
   ```bash
   cd calorie_tracker
   python manage.py makemigrations tracker
   python manage.py migrate
   ```

6. **Create an Administrator Account**
   ```bash
   python manage.py createsuperuser
   ```
   Follow the prompts to set up your username, email, and password.

## ⚙️ Configuration

### Environment Settings

The application is configured with sensible defaults, but you may wish to adjust:

1. **Database Configuration**
   - The default SQLite database works for most users
   - For production, consider PostgreSQL or MySQL
   - Edit `settings.py` to configure alternative databases

2. **Static Files**
   - Static files are served from the `static` directory
   - Run `python manage.py collectstatic` before deployment

3. **Time Zone**
   - Default: UTC
   - Modify `TIME_ZONE` in `settings.py` to match your location

## 🚀 Usage Guide

### Running the Development Server

```bash
python manage.py runserver
```

The application will be available at [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

### Accessing the Admin Interface

Navigate to [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/) and log in with your superuser credentials.

### Using the Application

1. **Setting Calorie Goals**
   - Click the "Set Goals" button in the navigation menu
   - Enter your daily calorie target
   - Select your weight goal (lose, maintain, or gain)
   - Choose your activity level

2. **Adding Food Entries**
   - Navigate to "Add Entry" in the menu or click "Add New Entry" on the home page
   - Enter the food name, calorie content, and date consumed
   - Click "Save" to record the entry

3. **Viewing and Filtering Entries**
   - Go to "All Entries" to see your complete food log
   - Use the date picker to filter entries by specific dates
   - View daily totals and progress toward your goals

4. **Tracking Progress**
   - The home page displays your current day's consumption
   - Review the calorie history chart to analyze trends
   - Check your goal progress bar at the top of each page

5. **Managing Entries**
   - Edit entries by clicking the pencil icon
   - Delete entries with the trash icon
   - View detailed information by selecting an entry

## 📁 Project Structure

```
d:\Calorie-Tracker\
├── calorie_tracker\            # Django project directory
│   ├── calorie_tracker\        # Project settings package
│   │   ├── __init__.py
│   │   ├── asgi.py
│   │   ├── settings.py         # Main settings file
│   │   ├── urls.py             # Project URL routing
│   │   └── wsgi.py
│   │
│   ├── tracker\                # Main application
│   │   ├── migrations\         # Database migration files
│   │   ├── __init__.py
│   │   ├── admin.py            # Admin interface config
│   │   ├── apps.py             # App configuration
│   │   ├── forms.py            # Form definitions
│   │   ├── models.py           # Data models
│   │   ├── urls.py             # App-specific URLs
│   │   └── views.py            # View controllers
│   │
│   ├── templates\              # HTML templates
│   │   ├── base.html           # Base template
│   │   └── tracker\            # App-specific templates
│   │
│   ├── static\                 # Static assets (CSS, JS, images)
│   │   ├── css\                # Stylesheets
│   │   ├── js\                 # JavaScript files
│   │   └── img\                # Images
│   │
│   └── manage.py               # Django management script
│
├── venv\                       # Virtual environment (not in repo)
├── requirements.txt            # Project dependencies
├── README.md                   # Project documentation
└── LICENSE                     # License information
```

## ✏️ Customization

### Extending the Application

1. **Adding New Features**
   - Define new models in `models.py`
   - Create corresponding views in `views.py`
   - Add URL patterns in `urls.py`
   - Create templates in the `templates` directory

2. **Customizing the User Interface**
   - Modify CSS variables in the `<style>` block of `base.html`
   - Add custom JavaScript in `static/js/main.js`
   - Adjust templates to change layout and components

3. **Adding User Authentication**
   - Django's built-in authentication can be integrated
   - Update views to include `@login_required` decorators
   - Create user profile functionality

## 🔧 Troubleshooting

### Common Issues

1. **Database Errors**
   - **Issue**: "No such table" errors
   - **Solution**: Run migrations with `python manage.py migrate`

2. **Static Files Not Loading**
   - **Issue**: CSS or JavaScript not applied
   - **Solution**: Check `STATIC_URL` in settings and run `collectstatic`

3. **Dark Mode Issues**
   - **Issue**: Inconsistent appearance in dark mode
   - **Solution**: Ensure all components use CSS variables for colors

4. **JavaScript Errors**
   - **Issue**: Features like charts or goal tracking not working
   - **Solution**: Check browser console for errors and ensure all scripts are loaded

### Getting Help

If you encounter persistent issues:

1. Check the Django documentation: [https://docs.djangoproject.com/](https://docs.djangoproject.com/)
2. Search Stack Overflow for similar issues
3. Open an issue on the project repository

## 👥 Contributing

Contributions to the Calorie Tracker project are welcome! To contribute:

1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Commit your changes: `git commit -m 'Add some feature'`
4. Push to the branch: `git push origin feature-name`
5. Submit a pull request

Please ensure your code follows the project's style guidelines and includes appropriate tests.

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

---

**Developed by Sohaib**

*Last updated: 5 May 2025*
=======
# Calorie Tracker

![Calorie Tracker](https://img.shields.io/badge/Calorie%20Tracker-v1.0.0-brightgreen)
![Django](https://img.shields.io/badge/Django-3.2-blue)
![License](https://img.shields.io/badge/License-MIT-green)

A comprehensive web application built with Django that enables users to track daily calorie intake with precision and visual insight.

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Technical Stack](#technical-stack)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage Guide](#usage-guide)
- [Project Structure](#project-structure)
- [Customization](#customization)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)
- [License](#license)

## 🔭 Overview

Calorie Tracker is a feature-rich web application designed to help users monitor and manage their daily caloric intake. With an intuitive interface and comprehensive reporting capabilities, it provides valuable insights into dietary patterns, helping users make informed decisions about their nutrition.

The application offers a complete suite of CRUD operations for food entries, along with data visualization tools to track progress toward caloric goals. Whether you're aiming to lose weight, maintain your current weight, or gain weight, Calorie Tracker provides the tools needed to achieve your nutritional objectives.

## ✨ Features

### Core Functionality

- **Complete Food Entry Management**
  - Create, view, update, and delete food entries
  - Record food name, calorie count, and consumption date
  - Optional categorization of food items

- **Advanced Filtering**
  - Filter entries by date with an intuitive calendar widget
  - Search functionality for finding specific food items
  - Sort entries by various criteria

- **Visual Data Representation**
  - Interactive charts showing calorie trends over time
  - Progress bars for daily goal tracking
  - Visual breakdown of nutritional information

### User Experience

- **Intuitive User Interface**
  - Modern, responsive design works across all devices
  - Clean, distraction-free layout emphasizes important data
  - Smooth animations and transitions enhance usability

- **Personalization**
  - Customizable daily calorie goals
  - Light and dark mode themes
  - Goal tracking with personalized feedback

- **Health Insights**
  - Smart nutritional suggestions based on intake
  - Daily, weekly, and monthly consumption summaries
  - Automated alerts for goal progress

## 🛠️ Technical Stack

### Backend
- **Django 3.2+**: Robust Python web framework
- **SQLite** (default database, configurable for other databases)

### Frontend
- **HTML5 / CSS3**: Modern web standards
- **Bootstrap 4**: Responsive design framework
- **JavaScript / jQuery**: Dynamic user interactions
- **Chart.js**: Interactive data visualization
- **Font Awesome**: Icon library
- **Custom CSS Variables**: Theme control

### Additional Libraries
- **django-bootstrap4**: Bootstrap integration
- **Pillow**: Image processing (for future features)
- **django-crispy-forms**: Enhanced form rendering
- **whitenoise**: Efficient static file serving
- **AOS**: Animate On Scroll library

## 📦 Installation

### Prerequisites

- Python 3.6 or higher
- pip (Python package installer)
- Git (optional, for cloning the repository)

### Step-by-Step Installation

1. **Create a Project Directory**
   ```bash
   mkdir -p d:\Calorie-Tracker
   cd d:\Calorie-Tracker
   ```

2. **Set Up a Virtual Environment**
   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Clone or Download the Repository**
   ```bash
   git clone https://github.com/yourusername/calorie-tracker.git .
   
   # If you don't have Git, download and extract the ZIP file
   ```

4. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

5. **Initialize the Database**
   ```bash
   cd calorie_tracker
   python manage.py makemigrations tracker
   python manage.py migrate
   ```

6. **Create an Administrator Account**
   ```bash
   python manage.py createsuperuser
   ```
   Follow the prompts to set up your username, email, and password.

## ⚙️ Configuration

### Environment Settings

The application is configured with sensible defaults, but you may wish to adjust:

1. **Database Configuration**
   - The default SQLite database works for most users
   - For production, consider PostgreSQL or MySQL
   - Edit `settings.py` to configure alternative databases

2. **Static Files**
   - Static files are served from the `static` directory
   - Run `python manage.py collectstatic` before deployment

3. **Time Zone**
   - Default: UTC
   - Modify `TIME_ZONE` in `settings.py` to match your location

## 🚀 Usage Guide

### Running the Development Server

```bash
python manage.py runserver
```

The application will be available at [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

### Accessing the Admin Interface

Navigate to [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/) and log in with your superuser credentials.

### Using the Application

1. **Setting Calorie Goals**
   - Click the "Set Goals" button in the navigation menu
   - Enter your daily calorie target
   - Select your weight goal (lose, maintain, or gain)
   - Choose your activity level

2. **Adding Food Entries**
   - Navigate to "Add Entry" in the menu or click "Add New Entry" on the home page
   - Enter the food name, calorie content, and date consumed
   - Click "Save" to record the entry

3. **Viewing and Filtering Entries**
   - Go to "All Entries" to see your complete food log
   - Use the date picker to filter entries by specific dates
   - View daily totals and progress toward your goals

4. **Tracking Progress**
   - The home page displays your current day's consumption
   - Review the calorie history chart to analyze trends
   - Check your goal progress bar at the top of each page

5. **Managing Entries**
   - Edit entries by clicking the pencil icon
   - Delete entries with the trash icon
   - View detailed information by selecting an entry

## 📁 Project Structure

```
d:\Calorie-Tracker\
├── calorie_tracker\            # Django project directory
│   ├── calorie_tracker\        # Project settings package
│   │   ├── __init__.py
│   │   ├── asgi.py
│   │   ├── settings.py         # Main settings file
│   │   ├── urls.py             # Project URL routing
│   │   └── wsgi.py
│   │
│   ├── tracker\                # Main application
│   │   ├── migrations\         # Database migration files
│   │   ├── __init__.py
│   │   ├── admin.py            # Admin interface config
│   │   ├── apps.py             # App configuration
│   │   ├── forms.py            # Form definitions
│   │   ├── models.py           # Data models
│   │   ├── urls.py             # App-specific URLs
│   │   └── views.py            # View controllers
│   │
│   ├── templates\              # HTML templates
│   │   ├── base.html           # Base template
│   │   └── tracker\            # App-specific templates
│   │
│   ├── static\                 # Static assets (CSS, JS, images)
│   │   ├── css\                # Stylesheets
│   │   ├── js\                 # JavaScript files
│   │   └── img\                # Images
│   │
│   └── manage.py               # Django management script
│
├── venv\                       # Virtual environment (not in repo)
├── requirements.txt            # Project dependencies
├── README.md                   # Project documentation
└── LICENSE                     # License information
```

## ✏️ Customization

### Extending the Application

1. **Adding New Features**
   - Define new models in `models.py`
   - Create corresponding views in `views.py`
   - Add URL patterns in `urls.py`
   - Create templates in the `templates` directory

2. **Customizing the User Interface**
   - Modify CSS variables in the `<style>` block of `base.html`
   - Add custom JavaScript in `static/js/main.js`
   - Adjust templates to change layout and components

3. **Adding User Authentication**
   - Django's built-in authentication can be integrated
   - Update views to include `@login_required` decorators
   - Create user profile functionality

## 🔧 Troubleshooting

### Common Issues

1. **Database Errors**
   - **Issue**: "No such table" errors
   - **Solution**: Run migrations with `python manage.py migrate`

2. **Static Files Not Loading**
   - **Issue**: CSS or JavaScript not applied
   - **Solution**: Check `STATIC_URL` in settings and run `collectstatic`

3. **Dark Mode Issues**
   - **Issue**: Inconsistent appearance in dark mode
   - **Solution**: Ensure all components use CSS variables for colors

4. **JavaScript Errors**
   - **Issue**: Features like charts or goal tracking not working
   - **Solution**: Check browser console for errors and ensure all scripts are loaded

### Getting Help

If you encounter persistent issues:

1. Check the Django documentation: [https://docs.djangoproject.com/](https://docs.djangoproject.com/)
2. Search Stack Overflow for similar issues
3. Open an issue on the project repository

## 👥 Contributing

Contributions to the Calorie Tracker project are welcome! To contribute:

1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Commit your changes: `git commit -m 'Add some feature'`
4. Push to the branch: `git push origin feature-name`
5. Submit a pull request

Please ensure your code follows the project's style guidelines and includes appropriate tests.

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

---

**Developed by Sohaib**

*Last updated: 5 May 2025*
>>>>>>> 8127e94 (Initial commit with Docker support)
