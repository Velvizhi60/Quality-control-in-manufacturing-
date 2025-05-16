# Quality Control in Management - Basic Example

# Minimum quality score required to pass inspection
quality_threshold = 90

# List of products with their inspection scores
products = [
    {"name": "Widget A", "score": 95},
    {"name": "Widget B", "score": 88},
    {"name": "Widget C", "score": 91},
    {"name": "Widget D", "score": 85},
    {"name": "Widget E", "score": 93}
]

# Check each product against the threshold
for product in products:
    name = product["name"]
    score = product["score"]
    
    if score >= quality_threshold:
        result = "PASS"
    else:
        result = "FAIL"
    
    print(f"{name}: Score = {score} --> {result}")