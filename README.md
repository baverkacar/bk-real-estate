# BK Real Estate

This project is a django based website application. The project is an application made to improve my django skills.

## Table of Contents

- [Tech Stack](#tools)
- [Installation](#installation)
- [Structure](#structure)
- [Screenshots](#screenshots)

## Tech Stack

**Frontend:** Django Template HTML, CSS, Bootstrap4 (Frontend part is taken ready except django template)

**Backend:** Django, PostreSQL



## Installation

### Create venv and Activate It:
```
    git clone https://github.com/baverkacar/bk-real-estate.git
    cd bk-real-estate
```

#### On windows
```
    python -m venv venv
    venv\Scripts\activate
```

#### On Lınux and MacOS

```
    Python3 -m vena ./venv
    Source ./venv/bin/activate
```

### Install Django:
```
    pip install django
```

### Run app:
```
    python manage.py runserver
```

## Structure


```
├── README.md
├── bkemlak
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── static
│   │   ├── css
│   │   │   ├── all.css
│   │   │   ├── bootstrap.css
│   │   │   ├── lightbox.min.css
│   │   │   └── style.css
│   │   ├── img
│   │   │   ├── about.jpg
│   │   │   ├── building.jpg
│   │   │   ├── close.png
│   │   │   ├── loading.gif
│   │   │   ├── logo.png
│   │   │   ├── next.png
│   │   │   ├── prev.png
│   │   │   └── showcase.jpg
│   │   ├── js
│   │   │   ├── bootstrap.bundle.min.js
│   │   │   ├── jquery-3.3.1.min.js
│   │   │   ├── lightbox.min.js
│   │   │   └── main.js
│   │   └── webfonts
│   │       ├── fa-brands-400.eot
│   │       ├── fa-brands-400.svg
│   │       ├── fa-brands-400.ttf
│   │       ├── fa-brands-400.woff
│   │       ├── fa-brands-400.woff2
│   │       ├── fa-regular-400.eot
│   │       ├── fa-regular-400.svg
│   │       ├── fa-regular-400.ttf
│   │       ├── fa-regular-400.woff
│   │       ├── fa-regular-400.woff2
│   │       ├── fa-solid-900.eot
│   │       ├── fa-solid-900.svg
│   │       ├── fa-solid-900.ttf
│   │       ├── fa-solid-900.woff
│   │       └── fa-solid-900.woff2
│   ├── urls.py
│   └── wsgi.py
├── bkemlak-about.gif
├── bkemlak-links.gif
├── bkemlak-listings1.gif
├── bkemlak-listings2.gif
├── bkemlak-search.gif
├── db-schema
├── listings
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── choices.py
│   ├── migrations
│   │   ├── 0001_initial.py
│   │   └── __init__.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── manage.py
├── pages
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations
│   │   └── __init__.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── realtors
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations
│   │   ├── 0001_initial.py
│   │   └── __init__.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
├── requirements.txt
└── templates
    ├── includes
    │   ├── _footer.html
    │   ├── _navbar.html
    │   └── _topbar.html
    ├── lay.html
    ├── listings
    │   ├── listing.html
    │   ├── listings.html
    │   └── search.html
    └── pages
        ├── about.html
        └── index.html
```

## Screenshots

### About Page
![about](https://github.com/baverkacar/bk-real-estate/blob/main/bkemlak-about.gif?raw=true)

### Listings Page 

![listings-1](https://github.com/baverkacar/bk-real-estate/blob/main/bkemlak-listings1.gif?raw=true)

![listings-2](https://github.com/baverkacar/bk-real-estate/blob/main/bkemlak-listings2.gif?raw=true)

### Search Page
![search](https://github.com/baverkacar/bk-real-estate/blob/main/bkemlak-search.gif?raw=true)

### Links

![links](https://github.com/baverkacar/bk-real-estate/blob/main/bkemlak-links.gif?raw=true)
