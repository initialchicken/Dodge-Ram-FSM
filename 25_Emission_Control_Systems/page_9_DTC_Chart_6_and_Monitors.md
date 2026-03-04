# DESCRIPTION AND OPERATION (Continued)

## DIAGNOSTIC TROUBLE CODE DESCRIPTIONS (Continued)

| Hex Code | Generic Scan Tool Code | DRB Scan Tool Display | Description of Diagnostic Trouble Code |
|----------|------------------------|----------------------|----------------------------------------|
| \*B6 | P0157 | O2 2/2 Voltage Low | Oxygen sensor input voltage maintained below normal operating range. |
| \*BA | P1398 | Mis-fire Adaptive Numerator at Limit | CKP sensor target windows have too much variation. |
| BC | P0751 | O/D Switch Pressed (LO) More Than 5 Min | Overdrive Off switch input too low for more than 5 minutes. |
| \*C0 | P1195 or P0133 | Cat Mon Slow O2 1/1 | A slow switching oxygen sensor has been detected in bank 1/1 during catalyst monitor test. |
| \*C1 | P0153 or P1196 | Cat Mon Slow O2 2/1 | A slow switching oxygen sensor has been detected in bank 2/1 during catalyst monitor test. |
| \*C2 | P0129 or P1197 | Cat Mon Slow O2 1/2 | A slow switching oxygen sensor has been detected in bank 1/2 during catalyst monitor test. |
| \*DE | P1694 | No Engine Bus Msgs Fit in Comp Module | |
| \*DF | P1693 | | |

---

## MONITORED SYSTEMS

There are new electronic circuit monitors that check fuel, emission, engine and ignition performance. These monitors use information from various sensor circuits to indicate the overall operation of the fuel, engine, ignition and emission systems and thus the emissions performance of the vehicle.

The fuel, engine, ignition and emission systems monitors do not indicate a specific component problem. They do indicate that there is an implied problem within one of the systems and that a specific problem must be diagnosed.

If any of these monitors detect a problem affecting vehicle emissions, the Malfunction Indicator (Check Engine) Lamp will be illuminated. These monitors generate Diagnostic Trouble Codes that can be displayed with the check engine lamp or a scan tool.

The following is a list of the system monitors:

- Misfire Monitor
- Fuel System Monitor
- Oxygen Sensor Monitor
- Oxygen Sensor Heater Monitor
- Catalyst Monitor
- Leak Detection Pump Monitor (if equipped)

All these system monitors require two consecutive trips with the malfunction present to set a fault.

Refer to the appropriate Powertrain Diagnostics Procedures manual for diagnostic procedures.

The following is an operation and description of each system monitor:

### OXYGEN SENSOR MONITOR

Effective control of exhaust emissions is achieved by an oxygen feedback system. The most important element of the feedback system is the O2S. The O2S is located in the exhaust path. Once it reaches operating temperature 300 degrees to 350 degrees C (572 degrees to 662 degrees F), the sensor generates a voltage that is inversely proportional to the amount of oxygen in the exhaust. The information obtained by the sensor is used to calculate the fuel injector pulse width. This maintains a 14.7 to 1 Air Fuel (A/F) ratio. At this mixture ratio, the catalyst works best to remove hydrocarbons (HC), carbon monoxide (CO) and nitrogen oxide (NOx) from the exhaust.

The O2S is also the main sensing element for the Catalyst and Fuel Monitors.

The O2S can fail in any or all of the following manners:

- slow response rate
- reduced output voltage
- dynamic shift
- shorted or open circuits

Response rate is the time required for the sensor to switch from lean to rich once it is exposed to a richer than optimum A/F mixture or vice versa. As the sensor starts malfunctioning, it could take longer to detect the changes in the oxygen content of the exhaust gas.

The output voltage of the O2S ranges from 0 to 1 volt. A good sensor can easily generate any output voltage in this range as it is exposed to different concentrations of oxygen. To detect a shift in the A/F mixture (lean or rich), the output voltage has to change beyond a threshold value. A malfunctioning sensor could have difficulty changing beyond the threshold value.

If there is an oxygen sensor (O2S) shorted to voltage DTC, as well as a O2S heater DTC, the O2S fault MUST be repaired first. Before checking the O2S fault, verify that the heater circuit is operating correctly.

---
*Chapter 25 - Emission Control Systems, Page 9*
