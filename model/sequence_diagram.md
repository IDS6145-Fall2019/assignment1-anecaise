
## Smart City Escalator Speed Model - Sequence Diagram


While the [*Activity Diagram*](/model/behavior_diagram.md) provided the basic flow of events for a single subway passenger who entered the system, the sequence diagram below provides the general sequence of events for all components of the system. 

![Sequence Diagram](/images/Sequence_diagram.png)

This diagram helps to visualize how the model will scale depending on the number of subway riders and the height of the escalator. The queue of riders at the lower plate will decrease as new steps arrive and transition through the system. 

