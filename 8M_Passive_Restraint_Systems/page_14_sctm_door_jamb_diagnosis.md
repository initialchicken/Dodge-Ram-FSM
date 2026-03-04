# DESCRIPTION AND OPERATION (Continued)

responds to the horizontal attitude of the vehicle. If the G-sensor monitors a gravity force of greater than about 0.7G in any horizontal direction, or that the vehicle is tilted in any direction at an angle of greater than about 45 degrees, the SCTM will sense the input from the G-sensor and de-energize the seat belt retractor latch solenoids, which will cause the retractors to latch.

The SCTM electronic timer circuit provides the vehicle occupants with the ability to extract the seat belt webbing from the retractor spool for a time period of about 30 minutes after the ignition switch is turned to the Off position. The electronic timer circuit also monitors the state of the door jamb switches, and unlatches the seat belt retractors after either door jamb switch cycles from open to closed or from closed to open. Each time the SCTM receives an input indicating a change in the state of a monitored switch has occurred, the 30 minute timer starts again. The timer also is used to de-energize the retractor latch solenoids after about 30 minutes, and prevent the battery from being drained while the vehicle is not being driven.

The hard wired SCTM output to the ACM is used to indicate whether a fault condition is present in the structural seat belt control system. The ACM monitors the input from the SCTM and sends the proper messages to the instrument cluster on the Chrysler Collision Detection (CCD) data bus to turn the seat belt reminder lamp on or off. If the ACM receives a fault input or does not detect any input from the SCTM, it sets a fault code and sends messages to the instrument cluster to turn the lamp on. See Seat Belt Reminder Lamp in the Description and Operation section of Group 8E - Instrument Panel Systems for more information.

See Airbag Systems in this group for more information about the ACM. For diagnosis of the CCD data bus, the ACM or the ACM input from the SCTM, the use of a DRB scan tool and the proper Diagnostic Procedures manual are recommended. The SCTM cannot be repaired. If faulty or damaged, it must be replaced.

### SEAT BELT RETRACTOR LATCH SOLENOID

A seat belt retractor latch solenoid is integral to each of the two outboard front seat belt retractors. The solenoid is grounded at all times through its wire harness connector and circuit. The solenoid receives battery current, which is switched by the Seatbelt Control Timer Module (SCTM), through a fuse in the junction block.

When the seat belt retractor latch solenoids are energized the retractor spools are unlatched, and the seat belt webbing can be withdrawn from the retractor. When the solenoids are de-energized the retractor spools latch, preventing the seat belt webbing from being withdrawn any further from the retractor.

The seat belt retractor latch solenoids cannot be repaired. If the solenoid is faulty or damaged, the entire seat belt retractor unit must be replaced. Refer to Group 23 - Body for the seat belt retractor service procedures.

### DOOR JAMB SWITCH

The door jamb switches are mounted to the door hinge pillars. The switches close a path to ground for the Seatbelt Control Timer Module (SCTM) when a door is opened, and open the ground path when a door is closed.

The door jamb switches cannot be repaired and, if faulty or damaged, they must be replaced. Refer to Door Jamb Switch in the Removal and Installation section of Group 8Q - Vehicle Theft Security Systems for the service procedures.

# DIAGNOSIS AND TESTING

## SEAT BELT CONTROL SYSTEM TEST MODE

The structural seat belt control system has a test mode feature. This feature allows the seat belt control system to be tested for proper operation while the vehicle is stationary by overriding the normal Seatbelt Control Timer Module (SCTM) control functions. The seat belt control system and the airbag system must be tested for proper operation following the service of any seat belt control system or airbag system component. See Airbag Systems in this group for more information on testing of the airbag system.

This test mode will confirm the following:

- Both door jamb switches and their input circuits to the SCTM are functional.
- The fused B(+), fused ignition switch output (run/acc), and ground circuits to the SCTM are functional.
- The SCTM fault circuit to the Airbag Control Module (ACM), the ACM, the Chrysler Collision Detection (CCD) data bus, and the seat belt reminder lamp in the instrument cluster are functional.
- Both seat belt retractor latch solenoids and their circuits are functional and can be activated by the SCTM.

To initiate the seat belt control system test mode, proceed as follows:

(1) If the seat belt control system test mode has not been performed previously within the past 72 hours, reset the SCTM by removing the Ignition-Off Draw (IOD) fuse from the junction block, then reinstalling it.

(2) Sit in the driver side front seat of the vehicle and close all doors.

(3) Push in the cigar lighter.

---
*8M Passive Restraint Systems - Page 14*
