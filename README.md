# Agriculture Management System

## Overview
This Django-based Agriculture Management System provides farmers with a comprehensive tool to track and manage their agricultural operations. The system currently focuses on field management with a modern, user-friendly interface that allows for detailed tracking of farming activities, costs, and yields.

## Features

### Field Management (Implemented)
- **Field Registration**
  - Add and manage multiple fields with unique names
  - Track field locations (Currently supports Rowena and Bridgewater locations)
  - Edit and delete field information
  - View comprehensive field listings with search and filter capabilities

- **Yearly Data Tracking**
  - Record and maintain yearly data for each field including:
    - Crop type selection (Corn, Soybeans, Wheat, Oats, Alfalfa, Grass, or custom crops)
    - Acreage tracking
    - Yield amounts in bushels
    - Cost tracking:
      - Seed costs
      - Fertilizer costs
      - Chemical costs
      - Crop insurance
    - Automatic calculation of total costs and yield per dollar metrics
  - Historical data viewing and management
  - Year-over-year comparison capabilities

### Equipment Management (Partially Implemented)
- Basic equipment tracking functionality
- Equipment maintenance records
- Cost tracking for equipment

### Future Implementations

#### Livestock Management (Planned)
- Cattle tracking and management
- Health records
- Feed consumption tracking
- Breeding records
- Production metrics

## Technical Details

### Frontend
- Responsive design using Bootstrap 5
- Custom CSS with modern design elements
- Interactive forms with dynamic features
- Mobile-friendly interface
- Print functionality for reports
- Modern UI components including:
  - Searchable dropdown menus
  - Dynamic form fields
  - Responsive tables
  - Confirmation dialogs for critical actions

### Backend
- Django framework with robust model relationships
- Efficient data management system
- Form validation and error handling
- Search and filter capabilities
- Data integrity protection

### Security Features
- CSRF protection
- Secure form handling
- Data validation
- Protected routes

## Project Structure
```
agriculture_management/
├── fields/
│   ├── models.py          # Data models for fields and yearly data
│   ├── views.py           # View logic for field management
│   ├── forms.py           # Form definitions
│   ├── urls.py           # URL routing
│   └── templates/        # HTML templates
├── static/
│   └── fields/
│       ├── styles.css    # Custom styling
│       └── images/       # Static images
└── templates/            # Global templates
```

## Current Limitations
- Limited to two locations (Rowena and Bridgewater)
- Basic reporting capabilities
- Equipment management features are limited
- Livestock management not yet implemented

## Future Enhancements
1. Enhanced reporting and analytics
2. Weather data integration
3. Complete equipment management system
4. Full livestock management implementation
5. Mobile app development
6. Export capabilities for data
7. Integration with external agriculture APIs
8. Advanced cost analysis tools

## Project Status
This is currently a personal project designed for individual farm management needs. It is not actively seeking contributors or distributed under any specific license at this time. Feel free to use it as inspiration or reference for similar personal agriculture management solutions.
