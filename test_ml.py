#!/usr/bin/env python
import os
import sys
import django

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'agri_platform.settings')
django.setup()

from advisory.models import FarmInput
from advisory.ml_model import yield_predictor
from datetime import date

# Create a test farm input
test_input = FarmInput(
    district='cuttack',
    crop='rice',
    season='kharif',
    sowing_date=date(2024, 6, 15),
    field_area=2.5,
    irrigation='tubewell',
    soil_type='alluvial',
    soil_health_card=True,
    seed_variety='hybrid',
    pest_presence=False
)

print("Testing ML Model...")
print(f"Test Input: {test_input.crop} in {test_input.district} district")

try:
    # Test yield prediction
    predicted_yield, confidence = yield_predictor.predict_yield(test_input)
    print(f"Predicted Yield: {predicted_yield:.0f} kg/ha {confidence}")
    
    # Test recommendations
    recommendations = yield_predictor.generate_recommendations(test_input, predicted_yield)
    print(f"Estimated Gain: {recommendations['estimated_gain']:.1f}%")
    print(f"Action 1: {recommendations['action_1']}")
    print(f"Action 2: {recommendations['action_2']}")
    print(f"Action 3: {recommendations['action_3']}")
    print(f"Reasoning: {recommendations['reasoning']}")
    
    # Test district average
    district_avg = yield_predictor.get_district_average(test_input.district, test_input.crop, test_input.season)
    print(f"District Average: {district_avg:.0f} kg/ha")
    
    print("\n✅ ML Model is working correctly!")
    
except Exception as e:
    print(f"❌ Error: {e}")
    import traceback
    traceback.print_exc()