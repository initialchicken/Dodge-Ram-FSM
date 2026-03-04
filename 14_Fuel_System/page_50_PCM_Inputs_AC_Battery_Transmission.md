# 14 - 50 FUEL SYSTEM BR

## DESCRIPTION AND OPERATION (Continued)

### AIR CONDITIONING (A/C) CONTROLS—PCM INPUT

The A/C control system information applies to factory installed air conditioning units.

**A/C SELECT SIGNAL:** When the A/C switch is in the ON position, an input signal is sent to the powertrain control module (PCM). The signal informs the PCM that the A/C has been selected. The PCM adjusts idle speed to a pre-programmed rpm through the idle air control (IAC) motor to compensate for increased engine load.

**A/C REQUEST SIGNAL:** Once A/C has been selected, the powertrain control module (PCM) receives the A/C request signal from the clutch cycling pressure switch. The input indicates that the evaporator pressure is in the proper range for A/C application. The PCM uses this input to cycle the A/C compressor clutch (through the A/C relay). It will also determine the correct engine idle speed through the idle air control (IAC) motor position.

If the A/C low-pressure switch or high-pressure switch opens (indicating a low or high refrigerant pressure), the PCM will not receive an A/C request signal. The PCM will then remove the ground from the A/C relay. This will deactivate the A/C compressor clutch.

If the switch opens, (indicating that evaporator is not in proper pressure range), the PCM will not receive the A/C request signal. The PCM will then remove the ground from the A/C relay, deactivating the A/C compressor clutch.

### AUTOMATIC SHUTDOWN (ASD) SENSE—PCM INPUT

A 12 volt signal at this input indicates to the PCM that the ASD has been activated. The ASD relay is located in the power distribution center (PDC). The PDC is located in the engine compartment. For the location of the relay within the PDC, refer to PDC cover.

This input is used only to sense that the ASD relay is energized. If the powertrain control module (PCM) does not see 12 volts at this input when the ASD should be activated, it will set a diagnostic trouble code (DTC).

### BATTERY VOLTAGE—PCM INPUT

The battery voltage input provides power to the Powertrain Control Module (PCM). It also informs the PCM what voltage level is being supplied by the generator once the vehicle is running.

The battery input also provides the voltage that is needed to keep the PCM memory alive. The memory stores Diagnostic Trouble Code (DTC) messages and speed control adaptive memory.

### BATTERY TEMPERATURE SENSOR—PCM INPUT

Provides a signal to the PCM corresponding to the battery temperature. Refer to Group 8C, Charging System for additional information.

### FUEL LEVEL SENSOR—PCM INPUT

The Powertrain Control Module (PCM) sends a 5 volt signal to the fuel level sensor (fuel gauge sending unit). The fuel level sensor will then return a signal to the PCM to indicate fuel level. A signal is then sent out from the PCM to the CCD bus circuits for fuel gauge operation.

### SPEED CONTROL SWITCHES—PCM INPUT

Six different speed control functions, using three momentary contact switches, are monitored through this multiplexed input. The resistance monitored at this input, in combination with the length of time the PCM measures the resistance, determines which switch feature has been selected. The three switches are: On/Off, Set/Coast, Cancel and Resume/Accelerate.

Refer to Group 8H, Vehicle Speed Control System for further speed control information.

### PARK/NEUTRAL POSITION SWITCH—PCM INPUT

The park/neutral switch provides an input to the powertrain control module (PCM). This will indicate that the automatic transmission is in Park, Neutral or a Drive gear selection. This input is used to determine speed control strategy and electrical operation of both the overdrive and torque converter solenoids. Refer to Group 21, Transmissions, for testing, replacement and adjustment information.

### TRANSMISSION TEMPERATURE SENSOR—PCM INPUT

The transmission temperature sensor is a variable, thermistor type. It reacts to temperature changes. At cold transmission oil temperatures, its resistance is high. As temperatures increase, its resistance will decrease.

The transmission temperature sensor is used on models equipped with an automatic transmission. Its purpose is to help control transmission fluid overheating. If transmission overheating has been determined by this sensor (temp. above approximately 280 degrees F), an input is sent to the powertrain control module (PCM). The PCM will then force a 4-3 downshift. Once transmission temperature has cooled below specifications, a 3-4 upshift will be allowed. An instrument panel mounted transmission temperature warning lamp is also used.