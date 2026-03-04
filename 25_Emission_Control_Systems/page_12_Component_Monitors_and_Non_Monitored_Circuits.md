# DESCRIPTION AND OPERATION (Continued)

## COMPONENT MONITORS

There are several components that will affect vehicle emissions if they malfunction. If one of these components malfunctions the Malfunction Indicator Lamp (Check Engine) will illuminate.

Some of the component monitors are checking for proper operation of the part. Electrically operated components now have input (rationality) and output (functionality) checks. Previously, a component like the Throttle Position sensor (TPS) was checked by the PCM for an open or shorted circuit. If one of these conditions occurred, a DTC was set. Now there is a check to ensure that the component is working. This is done by watching for a TPS indication of a greater or lesser throttle opening than MAP and engine rpm indicate. In the case of the TPS, if engine vacuum is high and engine rpm is 1600 or greater and the TPS indicates a large throttle opening, a DTC will be set. The same applies to low vacuum if the TPS indicates a small throttle opening.

All open/short circuit checks or any component that has an associated limp in will set a fault after 1 trip with the malfunction present. Components without an associated limp in will take two trips to illuminate the MIL.

Refer to the Diagnostic Trouble Codes Description Charts in this section and the appropriate Powertrain Diagnostic Procedure Manual for diagnostic procedures.

## NON-MONITORED CIRCUITS

The PCM does not monitor the following circuits, systems and conditions that could have malfunctions causing driveability problems. The PCM might not store diagnostic trouble codes for these conditions. However, problems with these systems may cause the PCM to store diagnostic trouble codes for other systems or components. For example, a fuel pressure problem will not register a fault directly, but could cause a rich/lean condition or misfire. This could cause the PCM to store an oxygen sensor or misfire diagnostic trouble code.

### FUEL PRESSURE

The fuel pressure regulator controls fuel system pressure. The PCM cannot detect a clogged fuel pump inlet filter, clogged in-line fuel filter, or a pinched fuel supply or return line. However, these could result in a rich or lean condition causing the PCM to store an oxygen sensor or fuel system diagnostic trouble code.

### SECONDARY IGNITION CIRCUIT

The PCM cannot detect an inoperative ignition coil, fouled or worn spark plugs, ignition cross firing, or open spark plug cables.

### ENGINE COMPRESSION

The PCM cannot detect uneven, low, or high engine cylinder compression.

### EXHAUST SYSTEM

The PCM cannot detect a plugged, restricted or leaking exhaust system, although it may set a fuel system fault.

### FUEL INJECTOR MECHANICAL MALFUNCTION

The PCM cannot determine if a fuel injector is clogged, the needle is sticking or if the wrong injector is installed. However, these could result in a rich or lean condition causing the PCM to store a diagnostic trouble code for either misfire, an oxygen sensor, or the fuel system.

### EXCESSIVE OIL CONSUMPTION

Although the PCM monitors engine exhaust oxygen content when the system is in closed loop, it cannot determine excessive oil consumption.

### AIR FILTER RESTRICTION

The PCM cannot detect a clogged or restricted air cleaner inlet or filter element.

### VACUUM LEAKS

The PCM cannot detect leaks or restrictions in the vacuum circuits of vacuum assisted engine control system devices. However, these could cause the PCM to store a MAP sensor diagnostic trouble code and cause a high idle condition.

### PCM SYSTEM GROUND

The PCM cannot determine a poor system ground. However, one or more diagnostic trouble codes may be generated as a result of this condition. The module should be mounted to the body at all times, also during diagnostic.

### CONNECTOR DAMAGE

The PCM may not be able to determine spread or damaged connector pins. However, it might store diagnostic trouble codes as a result of spread connector pins.

## HIGH AND LOW LIMITS

The PCM compares input signal voltages from each input device with established high and low limits for the device. If the input voltage is not within limits and other criteria are met, the PCM stores a diagnostic trouble code in memory. Other diagnostic trouble code criteria might include engine RPM limits or input voltages from other sensors or switches that must be present before verifying a diagnostic trouble code condition.

---
*Chapter 25 - Emission Control Systems, Page 12*
