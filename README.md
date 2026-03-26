# URBAN CRUISE - Travel Website

A full-stack travel website built with Django that allows users to explore destinations, book tours, and manage their travel experiences.

## Features

- **Destination Management**: Browse and search through various travel destinations
- **Tour Booking**: Browse detailed tour information and make bookings
- **User Authentication**: Secure user registration, login, and profile management
- **Review System**: Users can rate and review tours they've experienced
- **Admin Panel**: Comprehensive admin interface for content management
- **Responsive Design**: Modern, mobile-friendly UI built with Bootstrap 5
- **Search & Filtering**: Advanced search and filtering for tours and destinations
- **Booking Management**: Track and manage user bookings

## Technology Stack

- **Backend**: Django 4.2.7
- **Frontend**: HTML5, CSS3, JavaScript, Bootstrap 5
- **Database**: SQLite (development), PostgreSQL (production ready)
- **Image Processing**: Pillow
- **Forms**: Django Crispy Forms with Bootstrap 5

## Installation

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Virtual environment (recommended)

### Setup

1. **Clone the repository:**
   ```bash
   git clone <your-repository-url>
   cd urban
   ```

2. **Create virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run migrations:**
   ```bash
   python manage.py migrate
   ```

5. **Create superuser:**
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the server:**
   ```bash
   python manage.py runserver
   ```

Visit `http://127.0.0.1:8000/` to see the application.

## Project Structure

```
urban/
├── travel/                 # Main Django app
│   ├── models.py          # Database models
│   ├── views.py           # View functions
│   ├── urls.py            # URL patterns
│   └── templates/         # HTML templates
├── urban_cruise/          # Django project settings
│   ├── settings.py        # Project configuration
│   └── urls.py            # Main URL configuration
├── static/                # CSS, JavaScript, images
├── templates/             # Base templates
├── media/                 # User uploaded files
└── requirements.txt      # Python dependencies
```

## Key Features

### User Features
- **Browse Destinations**: Explore various travel destinations with detailed information
- **Tour Booking**: Book tours with secure payment integration
- **User Profiles**: Manage personal information and booking history
- **Reviews**: Rate and review tours based on personal experience
- **Search**: Advanced search and filtering options

### Admin Features
- **Content Management**: Manage destinations, tours, and bookings
- **User Management**: View and manage user accounts
- **Analytics**: Track booking statistics and user engagement
- **Review Moderation**: Approve or moderate user reviews

### Design Features
- **Professional Logo System**: Custom SVG logos with hover effects
- **Branded Loading Screen**: Professional loading experience
- **Responsive Design**: Mobile-first approach with Bootstrap 5
- **Modern UI**: Clean, intuitive interface with smooth animations

## Security Features

- **Secure Authentication**: Django's built-in authentication system
- **CSRF Protection**: Cross-site request forgery protection
- **SQL Injection Prevention**: Django ORM protection
- **XSS Protection**: Cross-site scripting protection
- **Secure Headers**: Security headers for production

## Performance Optimization

- **Database Optimization**: Optimized queries and indexing
- **Caching**: Built-in caching framework ready
- **Static File Optimization**: Compressed static files
- **CDN Ready**: Configured for CDN integration

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

- **Project Link**: [https://github.com/anujv3130-spec/urban](https://github.com/anujv3130-spec/Urban-Cruise-Travel-Agent-in-Lucknow)
- **WhatsApp**: +91 9260994765
- **Email**: info@urbancruise.com

## Acknowledgments

- Django Framework
- Bootstrap 5
- Font Awesome Icons
- Unsplash for beautiful images
- **Image Processing**: Pillow
- **Forms**: Django Crispy Forms with Bootstrap 5

## Installation

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Virtual environment (recommended)

### Setup Instructions

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd urban
   ```

2. **Create and activate virtual environment**
   ```bash
   # Windows
   python -m venv venv
   venv\Scripts\activate

   # macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables** (optional)
   Create a `.env` file in the root directory:
   ```
   DEBUG=True
   SECRET_KEY=your-secret-key-here
   ALLOWED_HOSTS=localhost,127.0.0.1
   ```

5. **Run database migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Create a superuser account**
   ```bash
   python manage.py createsuperuser
   ```

7. **Collect static files**
   ```bash
   python manage.py collectstatic
   ```

8. **Start the development server**
   ```bash
   python manage.py runserver
   ```

9. **Access the application**
   - Main website: http://127.0.0.1:8000/
   - Admin panel: http://127.0.0.1:8000/admin/

## Project Structure

```
urban/
├── manage.py                 # Django management script
├── requirements.txt          # Python dependencies
├── README.md                # Project documentation
├── urban_cruise/           # Main project directory
│   ├── __init__.py
│   ├── settings.py         # Django settings
│   ├── urls.py            # Main URL configuration
│   ├── wsgi.py            # WSGI configuration
│   └── asgi.py            # ASGI configuration
├── travel/                # Main travel app
│   ├── __init__.py
│   ├── admin.py           # Admin interface configuration
│   ├── apps.py            # App configuration
│   ├── forms.py           # Django forms
│   ├── models.py          # Database models
│   ├── urls.py            # App URL configuration
│   └── views.py           # View functions
├── templates/             # HTML templates
│   ├── base.html          # Base template
│   ├── registration/      # Authentication templates
│   └── travel/            # Travel app templates
├── static/               # Static files
│   ├── css/
│   │   └── style.css     # Custom styles
│   └── js/
│       └── script.js     # Custom JavaScript
└── media/                # User uploaded files
    ├── destinations/
    ├── tours/
    └── testimonials/
```

## Models Overview

### Destination
- Represents travel destinations
- Fields: name, country, description, image, featured flag

### Tour
- Represents individual tours/experiences
- Fields: title, destination, description, type, duration, price, max travelers
- Relationships: Many-to-one with Destination

### Booking
- Represents user bookings for tours
- Fields: user, tour, travelers count, total price, status, contact info
- Relationships: Foreign keys to User and Tour

### Review
- User reviews for tours
- Fields: user, tour, rating (1-5), comment
- Relationships: Foreign keys to User and Tour

### Testimonial
- Customer testimonials for display
- Fields: name, email, message, image, featured flag

## Available URLs

### Public Pages
- `/` - Home page
- `/destinations/` - Browse destinations
- `/tours/` - Browse tours
- `/tour/<id>/` - Tour details page
- `/about/` - About us page
- `/contact/` - Contact page

### User Authentication
- `/accounts/login/` - User login
- `/accounts/logout/` - User logout
- `/signup/` - User registration
- `/accounts/password_reset/` - Password reset

### User Dashboard
- `/profile/` - User profile
- `/my-bookings/` - User's booking history

### Admin
- `/admin/` - Django admin panel

## Customization

### Adding New Tour Types
Edit `travel/models.py` and add new choices to the `TOUR_TYPES` tuple in the `Tour` model.

### Customizing Styles
Modify `static/css/style.css` to customize the appearance.

### Adding New Pages
1. Create view functions in `travel/views.py`
2. Add URL patterns in `travel/urls.py`
3. Create corresponding templates in `templates/travel/`

## Deployment

### Production Settings

1. **Set environment variables**:
   ```
   DEBUG=False
   SECRET_KEY=your-production-secret-key
   ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com
   ```

2. **Database configuration**:
   Update `DATABASES` settings in `urban_cruise/settings.py` for PostgreSQL or MySQL.

3. **Static files**:
   Configure your web server to serve static files from `STATIC_ROOT`.

4. **Security**:
   - Use HTTPS
   - Set up proper CORS policies
   - Configure security headers

### Example Production Server Setup (Gunicorn + Nginx)

```bash
# Install Gunicorn
pip install gunicorn

# Run the application
gunicorn urban_cruise.wsgi:application --bind 0.0.0.0:8000

# Nginx configuration example:
server {
    listen 80;
    server_name yourdomain.com;

    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }

    location /static/ {
        alias /path/to/your/project/staticfiles/;
    }

    location /media/ {
        alias /path/to/your/project/media/;
    }
}
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

For support and questions:
- Email: support@urbancruise.com
- Create an issue in the repository

## Future Enhancements

- Payment gateway integration (Stripe, PayPal)
- Email notifications
- Multi-language support
- Advanced search with maps
- Mobile app development
- Social media integration
- Advanced analytics dashboard

---

**URBAN CRUISE** - Your gateway to amazing travel experiences!
