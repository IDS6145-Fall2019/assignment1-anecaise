## Smart City Escalator Speed and Metro Transit Time Model


As a starting code framework for the Escalator Speed and Metro Transit Time model, several python files have been created that represent each of the classes that will be called in the main simulation program. 

[*View class overview here*](/images/class_diagram.png)

At the highest level, the [*escalator.py class*](/code/escalator.py) will allow us to pass our indepdent variables into the system. This includes the configurations for the simulated escalator (speed: timestep corresponding to speed and height: number of steps), the number of riders that are added with incoming trains, and the frequency of those trains. The escalator class is related to the [*escalator_step class*](/code/escalator_step.py), the [*Lower Plate class*](/code/LowerPlate.py), and the [*Upper Plate Class*](/code/UpperPlate.py)

The [*Escalator Step class*](/code/escalator_step.py) will be generated as a function of the escalator height. This class will update its position everytime step with the current position depending on escalator height. This class will also randomly decide between loading 1-2 passenger when it is at position 1. 

The [*Lower Plate class*](/code/LowerPlate.py) will act as the queue for new subway riders, adding more riders corresponding to the set train frequency. The [*Upper Plate Class*](/code/UpperPlate.py) represents the exit point for subway riders, and will log our output variable.

Finally, the [*Pedestrian class*](/code/pedestrian.py) logs position and running wait time. 
