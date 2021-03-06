# Contains constants to configure bot game-play behaviour

# Game settings ---------------------------------------------------------------


# Maximum time in seconds until game result is Tie
max_gametime = 2612 # 900 = 15 min, 1200 = 20 min , 1800 = 30 min, 2612s = 43 min 12s = max duration in data-set

# Minimum amount of units to attack
min_units_attack = 12 # i.e. same amount as commandcenter https://github.com/davechurchill/commandcenter

# Increment factor for more units in next wave
min_units_attack_increment = 6

# retreat if less than (min_units_attack * retreating_level) units left
retreating_level = 0.5

# maximum border of min_units_attack
always_units_attack = 36

# Minimum amount of units to defend
min_units_defend = 3
# Maximum military units when giving up
max_units_giveup = min_units_defend
# Maximum distance to defend against enemy units, distance from own base
distance_defend = 30
# First distance to attack, distance from enemy base
distance_attack = 120
# Value to decrease distance_attack
distance_attack_speed = 4

# 16 iterations == 1 second
gameloops_check_frequency = 16

# Amount of new workers per expansion
worker_expand_increase = 16

# Amount of new workers per new gas resource
worker_gas_increase = 3

# Supply of a single worker
worker_supply = 1

# Initial supply
init_supply = 12



# if more less auto_build_idle_limit idle buildings, build new ones
auto_build_idle_limit = 3

# 16 only mineral, will be increased automatically for gas
init_worker_count = 16

# Check for isclose if build is completed
build_progress_completed = 1



# Auto build ------------------------------------------------------------------

# Minimum number of resources to perform an upgrade
# Maximum costs for Terran upgrades are 300 i.e. ShipPlatingLevel3
min_resource_upgrades = 300 

# Minimum number of resources to autobuild units
sufficently_enough_minerals = 400 # for comparison: Battlecruiser or commandcenter == 400 
sufficently_enough_vespene = 300 # for comparison: Battlecruiser == 300  

# Minimum number of resources to autobuild buildings
sufficently_much_minerals = sufficently_enough_minerals + 200 
sufficently_much_vespene = sufficently_enough_vespene + 150 

# Minimum number of resources to auto expand
sufficently_gigantic_minerals = sufficently_much_minerals + 100

# increase cum supply in case of auto build builgings
supply_increase_autobuild_buildings = 0.5