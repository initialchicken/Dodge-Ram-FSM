# BR EMISSION CONTROL SYSTEM 25 - 3

## DESCRIPTION AND OPERATION (Continued)

### DIAGNOSTIC TROUBLE CODES

A Diagnostic Trouble Code (DTC) indicates that either the Powertrain Control Module (PCM), or the Engine Control Module (ECM) has recognized an abnormal condition in the system. Certain DTC's will set a "Companion DTC", meaning the same code will be set in the opposite module (ECM or PCM).

DTC's are the results of a system or circuit failure, but do not directly identify the failed component or components.

Technicians must retrieve stored DTC's by connecting the DRB III scan tool (or an equivalent scan tool) to the 16-way data link connector (Fig. 3).

**NOTE: For a list of DTC's, refer to the following charts.**

### OBTAINING DTC's

**WARNING: APPLY PARKING BRAKE AND/OR BLOCK WHEELS BEFORE PERFORMING ANY TEST ON AN OPERATING ENGINE.**

(1) Connect the DRB scan tool to data link (diagnostic) connector.

(2) Turn the ignition switch on, access Read Fault Screen. Record all the DTC's shown on the DRB scan tool.

(3) To erase DTC's, use the Erase Trouble Code data screen on the DRB scan tool.

(4) Certain DTC's are stored as "Companion DTC's". They must be erased from both the ECM and PCM.

(a) CHECK ENGINE lamp (Malfunction Indicator Lamp or MIL) illuminated during engine operation if this DTC was recorded (CARB and/or EPA requirements).

(b) CHECK ENGINE lamp (Malfunction Indicator Lamp or MIL) illuminated during engine operation if this DTC was recorded (CARB requirements only).

(c) ECM may derate engine power, degrade engine performance or put fuel system into "Limp-In" mode if this DTC was recorded.

(d) CHECK GAUGES lamp illuminated during engine operation if this DTC was recorded.

(e) Companion DTC recorded (DTC recorded in both ECM and PCM).

(f) Water-In-Fuel warning lamp illuminated if this DTC was recorded.

(g) CHECK ENGINE lamp (Malfunction Indicator Lamp or MIL) not illuminated during engine operation if this DTC was recorded.

### DIAGNOSTIC TROUBLE CODE (DTC) DESCRIPTIONS

| Generic Scan Tool P-Code | DRB Scan Tool Display | Description of Diagnostic Trouble Code |
|---|---|---|
| P0112 (b), (c) | Intake Air Temperature (IAT) Sensor Voltage Low | Intake manifold air temperature sensor voltage input below the minimum acceptable voltage. |
| P0113 (b), (c) | Intake Air Temperature (IAT) Sensor Voltage High | Intake manifold air temperature sensor voltage input above the maximum acceptable voltage. |
| P0117 (b), (c) | Engine Coolant Temperature (ECT) Sensor Voltage Too Low | Engine coolant temperature sensor voltage input below minimum acceptable voltage. |
| P0118 (b), (c) | Engine Coolant Temperature (ECT) Sensor Voltage Too High | Engine coolant temperature sensor voltage input above maximum acceptable voltage. |
| P0121 (a), (c) | Accel. Position Sensor Volts Do Not Agree w/idle Validation Sig | Problem detected in APPS idle validation circuit |
| P0122 (a), (c) | Accelerator Position Sensor (APPS) Signal Voltage Too Low | APPS voltage input below the minimum acceptable voltage |
| P0123 (a), (c) | Accelerator Position Sensor (APPS) Signal Voltage Too High | APPS voltage input above the maximum acceptable voltage. |
| P0125 (b) | Engine is Cold Too Long | Engine does not reach operating temperature. |
| P0168 (c), (g) | Decreased Engine Performance Due To High Injection Pump Fuel Temp | Fuel temperature is above the engine protection limit. Engine power will be derated. |
| P0177 (f), (g) | Water In Fuel | Excess water found in fuel by water-in-fuel sensor |
