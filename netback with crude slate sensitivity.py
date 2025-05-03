# -*- coding: utf-8 -*-
"""


@author: cgarn
"""

import pandas as pd

# Scenario parameters: price differentials, costs, and taxes for multiple crudes
scenarios = {
    'WTI': {'base_price': 75, 'blending': 2, 'treating': 3, 'conversion': 4, 'distillation': 2, 'taxes': 3},
    'Mars (USA Light)': {'base_price': 80, 'blending': 3, 'treating': 4, 'conversion': 5, 'distillation': 3, 'taxes': 2},
    'Brent': {'base_price': 85, 'blending': 3, 'treating': 3, 'conversion': 4, 'distillation': 2, 'taxes': 3},
    'Dubai': {'base_price': 70, 'blending': 2, 'treating': 3, 'conversion': 4, 'distillation': 2, 'taxes': 4}
}

# Function to calculate netback for a given crude
def calculate_netback(crude_type, scenario):
    price = scenario['base_price']
    total_costs = scenario['blending'] + scenario['treating'] + scenario['conversion'] + scenario['distillation'] + scenario['taxes']
    netback = price - total_costs
    return netback

# Simulate crude slate sensitivity
def crude_slate_sensitivity(slate, price_changes):
    results = []
    
    for price_change in price_changes:
        slate_netback = 0
        for crude, scenario in slate.items():
            scenario['base_price'] += price_change  # Apply price change to each crude in slate
            netback = calculate_netback(crude, scenario)
            slate_netback += netback * slate[crude]  # Weighted netback based on slate mix
        
        results.append({'Price Change': price_change, 'Slate Netback': slate_netback})
    
    return pd.DataFrame(results)

# Crude slate example with weighting (e.g., 50% WTI, 30% Mars, 20% Brent)
crude_slate = {
    'WTI': 0.5,  # 50% WTI in the slate
    'Mars (USA Light)': 0.3,  # 30% Mars in the slate
    'Brent': 0.2  # 20% Brent in the slate
}

# Sensitivity analysis over a range of price changes (-5 to +5)
price_changes = range(-5, 6, 1)  # Price changes from -5 to +5 USD
df_sensitivity = crude_slate_sensitivity(crude_slate, price_changes)

# Display the results
print(df_sensitivity)