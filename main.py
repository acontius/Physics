# 1 force (نیرو)
def calculate_force(mass, acceleration):
    force = mass * acceleration
    return force

# Input values for mass and acceleration
mass = 5  # in kilograms
acceleration = 10  # in meters per second squared

# Calculate the force using the function
resultant_force = calculate_force(mass, acceleration)
print(f"The resultant force is {resultant_force} Newtons.")


#2 kenetic energy or (انرژی جنبشی)
def calculate_kinetic_energy(mass, velocity):
    kinetic_energy = 0.5 * mass * velocity**2
    return kinetic_energy

# Input values for mass and velocity
mass = 2  # in kilograms
velocity = 10  # in meters per second

# Calculate the kinetic energy using the function
kinetic_energy = calculate_kinetic_energy(mass, velocity)
print(f"The kinetic energy of the object is {kinetic_energy} Joules.")


#3 hoock or (کمان)
def calculate_hook_constant(force, displacement):
    hook_constant = force / displacement
    return hook_constant

# ورودی‌ها برای نیرو و جابه‌جای
force = 50  # به نیوتن
displacement = 5  # به متر

# محاسبه‌ی ثابت هوک با استفاده از تابع
hook_const = calculate_hook_constant(force, displacement)
print(f"ثابت هوک یا ضریب کمانش برابر است با {hook_const} نیوتن بر متر.")
