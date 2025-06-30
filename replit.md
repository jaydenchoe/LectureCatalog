# Course Information Platform

## Overview

This is a Flask-based web application that displays technical course information. The platform serves as a simple course catalog, allowing users to browse available courses and view detailed information about each course. It uses a static JSON file for data storage and Bootstrap for responsive UI design.

## System Architecture

The application follows a simple MVC (Model-View-Controller) pattern:

- **Model**: JSON file-based data storage (`static/courses_data.json`)
- **View**: Jinja2 templates with Bootstrap styling
- **Controller**: Flask routes handling HTTP requests

### Technology Stack

- **Backend**: Flask (Python web framework)
- **Frontend**: HTML/CSS with Bootstrap 5.3.0 (dark theme)
- **Icons**: Font Awesome 6.0.0
- **Data Storage**: JSON file
- **Template Engine**: Jinja2 (built into Flask)

## Key Components

### Backend Components

1. **Flask Application** (`app.py`)
   - Main application entry point
   - Route handlers for index and course detail pages
   - JSON data loading functionality
   - Error handling (404 for missing courses)

2. **Application Entry Point** (`main.py`)
   - Simple import of the Flask app for deployment

### Frontend Components

1. **Base Template** (`templates/base.html`)
   - Responsive layout with Bootstrap dark theme
   - Navigation bar with brand logo
   - Footer component
   - Font Awesome icons integration

2. **Index Page** (`templates/index.html`)
   - Hero section with platform introduction
   - Course grid layout displaying course cards
   - Course metadata (duration, category)

3. **Course Detail Page** (`templates/course_detail.html`)
   - Detailed course information display
   - Breadcrumb navigation
   - Structured course content presentation

### Data Layer

1. **Course Data** (`static/courses_data.json`)
   - JSON-based course information storage
   - Course metadata: ID, title, category, description
   - Detailed course information: overview, duration, targets, objectives, curriculum

## Data Flow

1. **Request Processing**:
   - User requests are routed through Flask
   - JSON data is loaded from the static file
   - Templates are rendered with course data

2. **Course Display**:
   - Index page loads all courses and displays them in a grid
   - Course detail page filters by course ID and displays specific course information

3. **Navigation**:
   - Simple URL routing between index and course detail pages
   - Breadcrumb navigation for user orientation

## External Dependencies

### CDN Resources
- **Bootstrap CSS**: `cdn.replit.com/agent/bootstrap-agent-dark-theme.min.css`
- **Bootstrap JS**: `cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js`
- **Font Awesome**: `cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css`

### Python Dependencies
- **Flask**: Web framework for Python
- **Standard Library**: os, json modules

## Deployment Strategy

The application is configured for simple deployment:

- **Host**: `0.0.0.0` (accessible from all network interfaces)
- **Port**: `5000`
- **Debug Mode**: Enabled for development
- **Session Secret**: Environment variable `SESSION_SECRET` with fallback to development key

### Environment Variables
- `SESSION_SECRET`: Flask session secret key (optional, has development fallback)

### Deployment Considerations
- Static file serving through Flask (suitable for development/small-scale deployment)
- JSON file-based storage (no database required)
- Simple file structure for easy deployment

## Changelog

```
Changelog:
- June 30, 2025. Initial setup
```

## User Preferences

```
Preferred communication style: Simple, everyday language.
```

### Architecture Decisions

1. **JSON File Storage**
   - **Problem**: Need simple data storage without database complexity
   - **Solution**: Static JSON file with course information
   - **Pros**: Simple setup, no database required, easy to modify
   - **Cons**: Limited scalability, no concurrent write support

2. **Bootstrap Dark Theme**
   - **Problem**: Need responsive, professional-looking UI
   - **Solution**: Bootstrap with Replit's dark theme variant
   - **Pros**: Consistent styling, responsive design, minimal custom CSS
   - **Cons**: Dependency on external CDN

3. **Template-based Rendering**
   - **Problem**: Need dynamic content generation
   - **Solution**: Jinja2 templates with inheritance
   - **Pros**: Code reusability, separation of concerns
   - **Cons**: Server-side rendering only