# AI-Driven Agricultural Advisory Platform for Odisha

A Django-based web application that provides AI-powered crop yield predictions and personalized agricultural recommendations for farmers in Odisha.

## Features

- **Yield Prediction**: ML-based crop yield forecasting with confidence intervals
- **Personalized Recommendations**: Top 3 priority actions for irrigation, fertilization, and pest management
- **District-Specific**: Covers all 30 districts of Odisha
- **Multi-Crop Support**: Rice, Maize, Wheat, Groundnut, Mung, Cotton, Sugarcane, Turmeric
- **Seasonal Advisory**: Kharif, Rabi, and Zaid season-specific guidance
- **Responsive Design**: Bootstrap-based UI for mobile and desktop

## Quick Start

1. **Install Dependencies**:
   ```bash
   pip install Django==4.2.7
   ```

2. **Run Migrations**:
   ```bash
   python manage.py migrate
   ```

3. **Start Server**:
   ```bash
   python manage.py runserver
   ```

4. **Access Application**:
   Open http://localhost:8000 in your browser

## Project Structure

```
agri_platform/
├── advisory/                 # Main Django app
│   ├── models.py            # Database models
│   ├── views.py             # View controllers
│   ├── forms.py             # Django forms
│   ├── ml_model.py          # ML prediction logic
│   └── urls.py              # URL routing
├── templates/advisory/       # HTML templates
│   ├── base.html            # Base template
│   ├── home.html            # Landing page
│   ├── farm_input.html      # Input form
│   ├── recommendation.html  # Results page
│   └── about.html           # About page
├── agri_platform/           # Django project settings
├── combined_tables.xlsx     # Training data (to be added)
└── manage.py               # Django management script
```

## Usage

1. **Home Page**: Overview of platform features
2. **Farm Input**: Enter farm details (district, crop, season, etc.)
3. **Get Recommendations**: AI generates yield predictions and actionable advice
4. **Download/Share**: Export or share recommendation reports

## Input Parameters

- **Location**: District selection (30 districts of Odisha)
- **Crop**: Rice, Maize, Wheat, Groundnut, Mung, Cotton, Sugarcane, Turmeric
- **Season**: Kharif, Rabi, Zaid
- **Field Details**: Area, irrigation type, soil type
- **Farming Practices**: Seed variety, soil health card availability
- **Current Status**: Pest/disease presence

## ML Model Features

The prediction model considers:
- Historical yield data
- Rainfall patterns and weather
- Irrigation infrastructure
- Soil characteristics
- Fertilizer usage patterns
- Seed variety and quality
- Seasonal factors
- District-specific conditions

## Technology Stack

- **Backend**: Django 4.2.7, Python
- **Frontend**: HTML5, CSS3, Bootstrap 5
- **Database**: SQLite (development)
- **ML**: Simplified rule-based system (expandable to scikit-learn)

## Future Enhancements

- Integration with real weather APIs
- Advanced ML models (Random Forest, XGBoost)
- Satellite imagery analysis
- Multi-language support (Odia)
- SMS/WhatsApp integration
- Mobile app development

## Data Integration

To use with actual data:
1. Place `combined_tables.xlsx` in the project root
2. Update `ml_model.py` to load and process the Excel data
3. Train ML models with historical yield data
4. Integrate weather APIs for real-time data

## Contributing

1. Fork the repository
2. Create feature branch
3. Make changes
4. Test thoroughly
5. Submit pull request

## License

This project is developed for agricultural development in Odisha.