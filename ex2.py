my_name = 'Matt E. Leggett'
my_age = 44 # not a lie
my_height = 71 # inches
my_weight = 238 # lbs
my_eyes = 'Blue'
my_teeth = 'White'
my_hair = 'Dirty Blonde'

print "Let's talk about %s." % my_name
print "He's %d inches tall." % my_height
print "He's %d pounds heavy." % my_weight
print "Actually that's a little too heavy."
print "He's got %s eyes and %s hair." % (my_eyes, my_hair)
print "His teeth are usually %s depending on what he's been eating." % my_teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (
    my_age, my_height, my_weight, my_age + my_height + my_weight)
