# Make an empty list for storing aliens.
aliens = []

# Make 30 green aliens.
for alien_number in range(30):
    new_alien = {'colour': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

for alien in aliens[:3]:
    if alien['colour'] == 'green':
        alien['colour'] = 'yellow'
        

# Show the first 5 aliens.
for alien in aliens[:5]:
    print(alien)
print("...")

# Show how many aliens have been created.
print(f"Total number of aliens: {len(aliens)}")

# Move the alien to the right.
# Determine how far to move the alien based on its current speed.
if aliens['speed'] == 'slow':
    x_increment = 1
elif aliens['speed'] == 'medium':
    x_increment = 2
else:
    # This must be a fast alien
    x_increment = 3

new_alien['speed'] = new_alien['speed'] + x_increment