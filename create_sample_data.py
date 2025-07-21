import pandas as pd

# Sample data
sample_data = {
    'title': [
        'MED - REELS - INHOUSE - MC 2025 05 29 - Cortisol Belly Campaign',
        'MED - REELS - INHOUSE - MC 2025 05 30 - Weight Loss Challenge',
        'MED - REELS - INHOUSE - MC 2025 05 31 - Fitness Motivation'
    ],
    'ad_account': ['AA1', 'AA2', 'AA3'],
    'spend': [348.91, 250.00, 420.50],
    'cac_scientific': [58.15, 45.20, 62.30],
    'cac_last_click': [43.61, 38.50, 48.75],
    'cac_clicks_only': [57.58, 52.30, 65.20],
    'cac_last_non_direct': [43.61, 40.10, 50.15],
    'new_visits_pct': [51.23, 48.75, 55.80],
    'ecr_pct': [3.74, 4.20, 3.95],
    'date_created': ['Jul 2, 2025', 'Jul 3, 2025', 'Jul 4, 2025'],
    'fb_link_text': ['FB Link', 'FB Link', 'FB Link'],
    'fb_link_url': [
        'https://facebook.com/cortisol-belly-campaign',
        'https://facebook.com/weight-loss-challenge',
        'https://facebook.com/fitness-motivation'
    ],
    'ig_link_text': ['IG Link', 'IG Link', 'IG Link'],
    'ig_link_url': [
        'https://instagram.com/cortisol-belly-campaign',
        'https://instagram.com/weight-loss-challenge',
        'https://instagram.com/fitness-motivation'
    ]
}

# Create DataFrame
df = pd.DataFrame(sample_data)

# Save to Excel
df.to_excel('sample_data.xlsx', index=False)

print("Sample data Excel file created: sample_data.xlsx")
print(f"Created {len(df)} sample rows with all required columns") 