## Smart City  Escalator Speed and Metro Transit Time Model Model - Behavior Diagram

The activity diagram below is a visualization of the major workflow of the model. A single passenger and a single step of the escalator is represented below. According to this model, a passenger enters the systems on the lower plater. If there is space on the step at position 1, they board that step; otherwise, the passenger waits at the lower plate for the next step. 

![Activity Diagram](/images/Activity_Diagram.png)

The step then goes through a similar process. Every time sequence, the step position is increased by 1. When the step reaches the final position (numbers of steps + 1), the passenger exits the system at the upper plate. Data is logged and the step resets. 

Please see the [*Sequence Diagram*](/model/sequence_diagram.md) for an overview of this system's workflow with multiple passengers in the queue. 
