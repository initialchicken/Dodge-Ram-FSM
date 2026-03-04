# DIAGNOSIS AND TESTING (Continued)

(4) Within five seconds the ignition switch must be cycled On, Off, On, Off, On, Off, and then finally back to On. Leave the ignition switch in the On position for the remainder of this procedure. This action enters the seat belt control system into its test mode for a maximum of five minutes. After five minutes, the seat belt control system will automatically return to its normal operating mode.

(5) The seat belt reminder lamp should light shortly after entering the test mode to confirm that the seat belt control system is in the test mode, and that the seat belt control system fault circuit is functional. If the lamp fails to light, use a DRB scan tool and the proper Diagnostic Procedures manual to diagnose the SCTM fault circuit to the ACM, the ACM, and the CCD data bus.

(6) Open the driver side front door. Check that both the passenger and driver side outboard front seat belt retractors are unlatched by slowly pulling the seat belt webbing out of the retractor. If only one retractor is unlatched, the latched retractor and circuit must be diagnosed. See Seat Belt Retractor Latch Solenoid in the Diagnosis and Testing section of this group. If both retractors are latched, see Seatbelt Control Timer Module in the Diagnosis and Testing section of this group.

(7) Close the driver side front door. Check that both the passenger and driver side outboard front seat belt retractors are latched by slowly pulling the seat belt webbing out of the retractor. If only one retractor is latched, the unlatched retractor and circuit must be diagnosed. See Seat Belt Retractor Latch Solenoid in the Diagnosis and Testing section of this group. If both retractors are unlatched, see Seatbelt Control Timer Module in the Diagnosis and Testing section of this group.

(8) Repeat Step 6 and Step 7, but open and close the passenger side front door instead of the driver side.

(9) Turn the ignition switch to the Off position. This will cause the seat belt control system to exit its test mode and return to normal operation.

(10) Turn the ignition switch back to the On position. The seat belt reminder and airbag indicator lamps should turn off shortly after their normal display functions (about six and seven seconds, respectively). If either lamp remains lighted, use a DRB scan tool and the proper Diagnostic Procedures manual to diagnose the SCTM fault circuit to the ACM, the airbag system, the ACM, and the CCD data bus.

(11) If the seat belt control system test mode has timed out prior to completion of the tests (about five minutes after the test was initiated), go back to Step 2.

The SCTM is programmed to consider certain parameters as an indication of a faulty Gravity (G)-sensor. In some peculiar vehicle use situations these parameters may be exceeded, causing the seat belt reminder lamp to illuminate indicating an SCTM fault, and then extinguish for no apparent reason. The following parameters should be considered if an intermittent seat belt reminder lamp illumination complaint is being diagnosed, and the test mode reveals no problems with the structural seat belt control system operation.

- If the SCTM monitors ten ignition cycles without an input from the G-sensor indicating that the vehicle has accelerated or decelerated sufficiently to require the seat belts to be latched. An ignition cycle is defined as: The ignition switch turned to the On position for at least thirty minutes, followed by the ignition switch being turned to the Off position. The SCTM considers this a G-sensor fault because it would normally be expected that the seat belts would require latching at some point within ten ignition cycles of driving. The SCTM will discontinue the fault signal and reset the ignition cycle counter to zero as soon as it sees a "normal" G-sensor input.

- If the SCTM monitors that the G-sensor input has required the seat belts to remain latched for more than about four seconds. This condition could occur if the vehicle is parked on a steep grade with the ignition switch in the On position, and is considered a G-sensor fault by the SCTM because the duration of the G-sensor input requiring the seat belts to be latched should not normally exceed four seconds. The SCTM will discontinue the fault signal as soon as it sees a "normal" G-sensor input.

## SEATBELT CONTROL TIMER MODULE

For circuit descriptions and diagrams, refer to 8W-67 - Restraint System in Group 8W - Wiring Diagrams.

(1) Check the fused B(+) fuse in the junction block. If OK, go to Step 2. If not OK, repair the shorted circuit or component as required and replace the faulty fuse.

(2) Check for battery voltage at the fused B(+) fuse in the junction block. If OK, go to Step 3. If not OK, repair the open circuit as required.

(3) Check the fused ignition switch output (run/acc) fuse in the junction block. If OK, go to Step 4. If not OK, repair the shorted circuit or component as required and replace the faulty fuse.

(4) Turn the ignition switch to the On position. Check for battery voltage at the fused ignition switch output (run/acc) fuse in the junction block. If OK, go to Step 5. If not OK, repair the open circuit to the ignition switch as required.

(5) Turn the ignition switch to the Off position. Disconnect and isolate the battery negative cable. Unplug the Seatbelt Control Timer Module (SCTM)

---
*8M Passive Restraint Systems - Page 15*
