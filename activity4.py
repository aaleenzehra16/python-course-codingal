# Farm Harvest Calculator
# harvest and earning calculators
harvest1=120
harvest2=150
harvest3=200
harvest4=300
harvest5=400

total_harvest=harvest1+harvest2+harvest3+harvest4+harvest5
average_harvest=total_harvest/5
percrop_cost=5
total_earnings=percrop_cost*total_harvest
percrop_weight=0.5

print("total harvest is",total_harvest*percrop_weight,"kg")
print("average harvest per feild is",average_harvest)
print("total earnings are Rs",total_earnings)

number_of_bags=(total_harvest*percrop_weight)//25
leftover_grain=(total_harvest*percrop_weight) % 25
print(f"number of full bags are {number_of_bags}\nleftover_grain is {leftover_grain}")

last_harvest=1500
print(total_harvest > last_harvest)
print(total_harvest == last_harvest)
print(total_harvest >= last_harvest)

bonus_crop=35
total_harvest +=bonus_crop
print("total harvest after adding bonus crop",total_harvest)
grain_seeds=10
total_harvest-=grain_seeds
print("total harvest after removing grain seeds",total_harvest)

after_adjustments=(total_harvest*percrop_weight)//25
print("final number of bags packed are",after_adjustments)