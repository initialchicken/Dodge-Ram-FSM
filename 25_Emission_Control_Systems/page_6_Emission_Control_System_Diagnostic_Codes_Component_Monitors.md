# BR — EMISSION CONTROL SYSTEM 25 - 7

## DESCRIPTION AND OPERATION (Continued)

| Generic Scan Tool P-Code | DRB Scan Tool Display | Description of Diagnostic Trouble Code |
|---|---|---|
| P1683 (g) | Spd ctrl pwr rly, or s/c 12v driver circuit | An open or shorted condition detected in the speed control servo power control circuit. |
| P1688 (a), (c) | Internal Fuel Injection Pump Controller Failure | Internal problem within the fuel injection pump. Low power, engine derated, or engine stops. |
| P1689 (a), (c) | No Communication Between ECM and Injection Pump Module | Data link circuit failure between ECM and fuel injection pump. Low power, engine derated, or engine stops. |
| P1690 (b), (c) | Fuel Injection Pump CKP Sensor Does Not Agree With ECM CKP Sensor | Problem in fuel sync signal. Possible injection pump timing problem. Low power, engine derated, or engine stops. |
| P1691 (c), (g) | Fuel Injection Pump Controller Calibration Error | Internal fuel injection pump failure. Low power, engine derated, or engine stops. |
| P1692 (e), (g) | DTC Set In ECM | A "Companion DTC" was set in both the ECM and PCM. |
| P1693 (e), (g) | DTC Detected in PCM/ECM or DTC Detected in ECM | A "Companion DTC" was set in both the ECM and PCM. |
| P1694 (b), (e) | No CCD Messages received from ECM | Bus communication failure to PCM. |
| P1698 (e), (g) | No CCD Messages received from PCM | Bus communication failure to PCM. A "Companion DTC" was set in both the ECM and PCM. |
| P1740 (b) | TCC OR O/D Solenoid Performance | Problem detected in transmission convertor clutch and/or overdrive circuits (diesel engine with 4-speed auto. trans. only). |
| P1756 (b) | Governor Pressure Not Equal to Target @ 15-20 PSI | Governor sensor input not between 10 and 25 psi when requested (4-speed auto. trans. only). |
| P1757 (b) | Governor Pressure Above 3 PSI In Gear With 0 MPH | Governor pressure greater than 3 psi when requested to be 0 psi (4-speed auto. trans. only). |
| P1762 (b) | Governor Press Sen Offset Volts Too Low or High | Sensor input greater or less than calibration for 3 consecutive Neutral/Park occurrences (4-speed auto. trans. only). |
| P1763 (b) | Governor Pressure Sensor Volts Too HI | Voltage greater than 4.89 volts (4-speed auto. trans. only). |
| P1764 (b) | Governor Pressure Sensor Volts Too Low | Voltage less than .10 volts (4-speed auto. trans. only). |
| P1765 (b) | Trans 12 Volt Supply Relay Ctrl Circuit | Current state of solenoid output port is different than expected (4-speed auto. trans. only). |
| P1899 (b) | P/N Switch Stuck in Park or in Gear | Incorrect input state detected for the Park/Neutral switch (3 or 4-speed auto. trans. only). |

## COMPONENT MONITORS

There are several electrical components that will affect vehicle emissions if they malfunction. If one of these components is malfunctioning, a Diagnostic Trouble Code (DTC) will be set by either the Powertrain Control Module (PCM) or the Engine Control Module (ECM). The Malfunction Indicator Lamp (MIL) will then be illuminated when the engine is running (the MIL is displayed on the instrument panel as the CHECK ENGINE lamp).

These electrically operated components have input (rationality) and output (functionality) checks. A check is done by one or more components to check the operation of another component.

Example: The Intake Manifold Air Temperature (IAT) sensor is used to monitor intake manifold air temperature over a period of time after a cold start. If the temperature has not risen to a certain specification during a specified time, a Diagnostic Trouble Code (DTC) will be set for a problem in the manifold air heater system.

All open/short circuit checks, or any component that has an associated limp-in will set a DTC and trigger the MIL after 1 trip with the malfunction