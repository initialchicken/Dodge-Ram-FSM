# DESCRIPTION AND OPERATION (Continued)

While the combination flasher has a International Standards Organization (ISO)-type relay terminal configuration or footprint, the internal circuitry is much different. The combination flasher does not use standard ISO-relay inputs or provide ISO-relay type outputs or functions. The combination flasher should never be substituted for an ISO-relay or replaced with an ISO-relay, or else component and vehicle damage may occur.

The combination flasher has five blade-type terminals intended for the following inputs and outputs: Battery B+, Ignition B+, Ground, Turn Signal circuit, and Hazard Warning circuit. Constant battery voltage and ground are supplied to the flasher so that it can perform the hazard warning function, and ignition switched battery voltage is supplied for the turn signal function. Refer to 8W-52 - Turn Signals in Group 8W - Wiring Diagrams for complete circuit descriptions, diagrams and terminal function identification.

The IC within the combination flasher (Fig. 1) contains the logic that controls the flasher operation and the flash rate. Pin 6 of the IC receives a sense voltage from the hazard warning portion of the multi-function switch. When the hazard switch is turned on, the "hazard on sense" voltage will become low due to the circuit being grounded through the turn signal bulbs. This low voltage sense signals the IC to energize the flash control Positive-Negative-Positive (PNP) transistor at a pre-calibrated flash rate or frequency. Each time the PNP transistor energizes the hazard warning circuit, the pin 6 "hazard on sense" voltage will become high and the IC signals the PNP transistor to de-energize the circuit. This cycling will continue until the hazard warning switch is turned off.

[Figure]

*Fig. 1 Combination Flasher - Typical*

Likewise, pin 8 of the IC receives a sense voltage from the turn signal portion of the multi-function switch. When the left or right turn signal is turned on, the "turn signal on sense" voltage will become low due to the circuit being grounded through the turn signal bulbs. This low voltage sense signals the IC to energize the flash control PNP transistor at a pre-calibrated flash rate or frequency. Each time the PNP transistor energizes the turn signal circuit, the pin 8 "turn signal on sense" voltage will become high and the IC signals the PNP transistor to de-energize the circuit. This cycling will continue until the right or left turn signal is turned off.

A special design feature of the combination flasher allows it to "sense" that a turn signal circuit or bulb is not operating, and provide the driver an indication of the condition by flashing the remaining bulbs in the affected circuit at a higher rate (120 flashes-per-minute or higher). Conventional flashers either continue flashing at their typical rate (heavy-duty type), or discontinue flashing the affected circuit entirely (standard-duty type). During turn signal operation, the combination flasher IC compares normal battery voltage input on pin 2 with the shunt resistor voltage input on pin 7. If the IC "senses" that the voltage difference between pin 2 and pin 7 is different than the pre-calibrated value of the IC, it will increase the rate at which it signals the PNP transistor to energize the pin 1 output. Thus, the inoperative half (left or right side) of the turn signal circuit will flash faster.

Because of the active electronic elements within the combination flasher, it cannot be tested with conventional automotive electrical test equipment. If the combination flasher is believed to be faulty, test the turn signal and hazard warning system circuits as described in this group. Then replace the combination flasher with a known good unit to confirm system operation.

The combination flasher cannot be repaired and, if faulty or damaged, it must be replaced.

### TURN SIGNAL SWITCH AND HAZARD WARNING SWITCH

The turn signal and hazard warning switches are contained in the multi-function switch assembly (Fig. 2). The multi-function switch assembly is secured to the left side of the steering column. A switch stalk that extends from the left side of the steering column is moved up or down to activate the right or left turn signals, respectively. A latching push-button that extends upward from the multi-function switch and through the top of the upper steering column shroud is used to control the hazard warning system.

The multi-function switch contains circuitry for the following functions:

---
*8J - Turn Signal and Hazard Warning Systems - Page 2*
