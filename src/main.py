"""
===========================================================
Graph-Theoretic Algorithmic Inspection (GTA)

Reference implementation accompanying the work:

Application of Graph Theory in Detection of Illegal Weapons
or Drugs at Port

Author: Himanshu Kumar

Originally developed during Master's research
Department of Mathematics
National Institute of Technology Durgapur
===========================================================
"""

# ==========================================================
# Configuration Data
# ==========================================================

DESTINATIONS = ["China", "Singapore", "Sri Lanka", "Malaysia", "Bangladesh"]

DESTINATION_WEIGHTS = [0.073, 0.020, 0.075, 0.073, 0.0695]

GOODS = ["fertilizer", "coal", "rice", "iron", "sand"]

CONTAINER_CAPACITY = {
    "20": 21727,
    "40": 26780,
    "45": 29050,
    "48": 32650,
}

GOODS_WEIGHTS = {
    "China": [0.461, 0.532, 0.383, 0.635, 0.421],
    "Singapore": [0.030, 0.050, 0.010, 0.050, 0.010],
    "Sri Lanka": [0.106, 0.039, 0.507, 0.093, 0.077],
    "Malaysia": [0.209, 0.305, 0.358, 0.461, 0.342],
    "Bangladesh": [0.066, 0.177, 0.285, 0.033, 0.335],
}

COMPANY_WEIGHTS = {
    "Roy Shipping Agency": 0.079,
    "Star Container Services": 0.065,
    "Res Trans-Logis": 0.042,
}

# ==========================================================
# Risk Model Parameters
# ==========================================================

lambda1 = 0.4321   # Weight change
lambda2 = 0.3210   # Destination
lambda3 = 0.1542   # Goods
lambda4 = 0.0927   # Shipping company

# ==========================================================
# User Input
# ==========================================================

destination = input("Enter the destination: ")
goods = input("Enter the goods: ")
container_length = input("Enter the length of container (in ft): ")
container_weight = int(input("Enter the weight of container (kg): "))
company = input("Enter the name of shipping company: ")

# ==========================================================
# Weight Change Analysis
# ==========================================================

weight_change = abs(container_weight - CONTAINER_CAPACITY[container_length])

if weight_change <= 50:
    weight_factor = 0.01
elif weight_change <= 100:
    weight_factor = 0.07
elif weight_change <= 200:
    weight_factor = 0.40
elif weight_change <= 300:
    weight_factor = 0.60
else:
    weight_factor = 0.80

destination_factor = DESTINATION_WEIGHTS[
    DESTINATIONS.index(destination)
]

goods_factor = GOODS_WEIGHTS[destination][GOODS.index(goods)]

company_factor = COMPANY_WEIGHTS[company]

# ==========================================================
# Risk Score Computation
# ==========================================================

R = (
    lambda1 * weight_factor
    + lambda2 * destination_factor
    + lambda3 * goods_factor
    + lambda4 * company_factor
)

# ==========================================================
# Final Decision
# ==========================================================

print("\n------------------------------------------")
print("Graph-Theoretic Algorithmic Inspection")
print("------------------------------------------")
print(f"Weight Difference : {weight_change} kg")
print(f"Risk Score (R)    : {R:.2f}")

if R <= 0.30:
    print("Decision          : Store to ship.")
else:
    print("Decision          : Proceed to further check.")
