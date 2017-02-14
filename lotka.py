"""
Work on these problems with your group.
You will submit one solution for the entire group.

You should write the Python using only your group's knowledge and
the Python documentation (the "Docs" link on the CodeSkulptor page).

  Kutub Gandhi
"""


#################################################################
# Predator-prey problem

# 1:
# Define the functions change_prey(birth, predation, prey, pred)
# and change_pred(growth, death, prey, pred), as described in the
# Lotka-Volterra Model video.
def change_prey(birth, predation, prey, pred):
    """Returns the change in prey population based on certain variables"""
    change_in_prey = (birth)*prey - predation*prey*pred
    return change_in_prey
def change_pred(growth, death, prey, pred):
    """Returns the change in predator population based on certain variables"""
    change_in_pred = (growth)*prey*pred - death*pred
    return change_in_pred
def pred_prey_timesteps(birth, predation, growth, death, prey, pred, years, num_timesteps_per_year):
    """Returns a list of time elapsed, prey pop. pred pop. Takes in smaller increments than a year"""
    preylist=[prey]
    predlist=[pred]
    store=[(prey, pred)]
    for _hello_its_me in range(years*num_timesteps_per_year):
        preylist.append(prey+change_prey(birth/num_timesteps_per_year, predation/num_timesteps_per_year, prey, pred))
        predlist.append(pred+change_pred(growth/num_timesteps_per_year, death/num_timesteps_per_year, prey, pred))
        prey = preylist[-1]
        pred = predlist[-1]
        store.append((prey,pred))
    time_stop=0.0
    index=0
    return_list = []
    while(time_stop <= years):
        temp_tuple = (time_stop, store[index][0], store[index][1])
        return_list.append(temp_tuple)
        time_stop+=1.0/num_timesteps_per_year
        index+=1
    return return_list
#                                 b   p   g  d  pr   pr y   n
populations = pred_prey_timesteps(0.5, 0, 0, 0, 100, 5, 40, 100)
# 2:
# Define the function
# pred_prey(birth, predation, growth, death, prey, pred, num_timesteps)
# that computes the populations as described in the Lotka-Volterra
# Model video.  It returns a list of pairs of (prey, pred) populations.
#
# The input "num_timesteps" tells how many time periods that the simulation
# will run.  For example, each time step could be a year, and we could
# run the simulation for 20 years.  The various input rates are assumed
# to be rates per each time step.  The output list is of length
# "num_timesteps"+1 -- it has the populations at the beginning of the
# simulation, plus after each time step.

def pred_prey(birth, predation, growth, death, prey, pred, num_timesteps):
    """Returns data indicating changes in predator and prey population pver time"""
    preylist=[prey]
    predlist=[pred]
    store=[(prey, pred)]
    for _hello_its_me in range(num_timesteps):
        preylist.append(prey+change_prey(birth, predation, prey, pred))
        predlist.append(pred+change_pred(growth, death, prey, pred))
        prey = preylist[-1]
        pred = predlist[-1]
        store.append((prey,pred))
    return store


def pred_prey_carrying(birth, predation, growth, death, carry_cap, prey, pred, years, num_timesteps_per_year):
    """Acts like pred_prey_timesteps, however this caps the prey population at a carrying cap"""
    preylist=[prey]
    predlist=[pred]
    store=[(prey, pred)]
    for _hello_its_me in range(years*num_timesteps_per_year):
        temp_new_prey = prey+change_prey(birth/num_timesteps_per_year, predation/num_timesteps_per_year, prey, pred)
        preylist.append(min(carry_cap, temp_new_prey))
        predlist.append(pred+change_pred(growth/num_timesteps_per_year, death/num_timesteps_per_year, prey, pred))
        prey = preylist[-1]
        pred = predlist[-1]
        store.append((prey,pred))
    time_stop=0.0
    index=0
    return_list = []
    while(time_stop <= years):
        temp_tuple = (time_stop, store[index][0], store[index][1])
        return_list.append(temp_tuple)
        time_stop+=1.0/num_timesteps_per_year
        index+=1
    return return_list

#populations = pred_prey_timesteps(0.0, 0.0, 0.0, 0.0025000000000000001, 0, 100, 10, 2)
##################################################################
# Plotting results


#print(populations)

def plot_pred_prey(populations, pred_name, prey_name):
    """plots prey pop. vs predator pop."""
    import simpleplot

    _time, prey, pred = zip(*populations)
    prey_pred = zip(prey, pred)

    simpleplot.plot_lines("Plot of predator and prey populations",
                         600, 300,
                         pred_name, prey_name,
                         [prey_pred], True)

#plot_pred_prey(populations, "Foxes", "Rabbits")


def plot_time_populations(populations, pred_name, prey_name):
    """Plots populations of prey and pred vs years elapsed"""
    prey_e=[]
    pred_e=[]
    print(pred_name)
    print(prey_name)
    time, prey, pred = zip(*populations)
    for prey_index in range(len(prey)):
        prey_e.append((2000 + time[prey_index], prey[prey_index]))
    for pred_index in range(len(pred)):
        pred_e.append((2000 + time[pred_index], pred[pred_index]))
    import simpleplot
    simpleplot.plot_lines("Plot of years and populations",
                          600, 300, "Year", "Populations",
                          [prey_e, pred_e], True)

plot_time_populations(populations, "Pred", "Prey")


#print(pred_prey_timesteps(0.0, 0.0, 0.0, 0.0025, 0, 100, 3 ,2))
