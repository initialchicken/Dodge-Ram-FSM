# DESCRIPTION AND OPERATION (Continued)

### CATALYST MONITOR (Continued)

To comply with clean air regulations, vehicles are equipped with catalytic converters. These converters reduce the emission of hydrocarbons, oxides of nitrogen and carbon monoxide. The catalyst works best when the Air Fuel (A/F) ratio is at or near the optimum of 14.7 to 1.

### FUEL SYSTEM MONITOR

The PCM is programmed to maintain the optimum air/fuel ratio of 14.7 to 1. This is done by making short term corrections in the fuel injector pulse width based on the O2S sensor output. The programmed memory acts as a self calibration tool that the engine controller uses to compensate for variations in engine specifications, sensor tolerances and engine fatigue over the life span of the engine. By monitoring the actual fuel-air ratio with the O2S sensor (short term) and multiplying that with the program long-term (adaptive) memory and comparing that to the limit, it can be determined whether it will pass an emissions test. If a malfunction occurs such that the PCM cannot maintain the optimum A/F ratio, then the MIL will be illuminated.

### CATALYST EFFICIENCY MONITOR

To comply with clean air regulations, vehicles are equipped with catalytic converters. These converters reduce the emission of hydrocarbons, oxides of nitrogen and carbon monoxide.

Normal vehicle miles or engine misfire can cause a catalyst to decay. A meltdown of the ceramic core can cause a reduction of the exhaust passage. This can increase vehicle emissions and deteriorate engine performance, driveability and fuel economy.

The catalyst monitor uses dual oxygen sensors (O2S's) to monitor the efficiency of the converter. The dual O2S's sensor strategy is based on the fact that as a catalyst deteriorates, its oxygen storage capacity and its efficiency are both reduced. By monitoring the oxygen storage capacity of a catalyst, its efficiency can be indirectly calculated. The upstream O2S is used to detect the amount of oxygen in the exhaust gas before the gas enters the catalytic converter. The PCM calculates the A/F mixture from the output of the O2S. A low voltage indicates high oxygen content (lean mixture). A high voltage indicates a low content of oxygen (rich mixture).

When the upstream O2S detects a lean condition, there is an abundance of oxygen in the exhaust gas. A functioning converter would store this oxygen so it can use it for the oxidation of HC and CO. As the converter absorbs the oxygen, there will be a lack of oxygen downstream of the converter. The output of the downstream O2S will indicate limited activity in this condition.

As the converter loses the ability to store oxygen, the condition can be detected from the behavior of the downstream O2S. When the efficiency drops, no chemical reaction takes place. This means the concentration of oxygen will be the same downstream as upstream. The output voltage of the downstream O2S copies the voltage of the upstream sensor. The only difference is a time lag (seen by the PCM) between the switching of the O2S's.

To monitor the system, the number of lean-to-rich switches of upstream and downstream O2S's is counted. The ratio of downstream switches to upstream switches is used to determine whether the catalyst is operating properly. An effective catalyst will have fewer downstream switches than it has upstream switches i.e., a ratio closer to zero. For a totally ineffective catalyst, this ratio will be one-to-one, indicating that no oxidation occurs in the device.

The system must be monitored so that when catalyst efficiency deteriorates and exhaust emissions increase to over the legal limit, the MIL (check engine lamp) will be illuminated.

### TRIP DEFINITION

The term "Trip" has different meanings depending on what the circumstances are. If the MIL (Malfunction Indicator Lamp) is OFF, a Trip is defined as when the Oxygen Sensor Monitor and the Catalyst Monitor have been completed in the same drive cycle.

When any Emission DTC is set, the MIL on the dash is turned ON. When the MIL is ON, it takes 3 good trips to turn the MIL OFF. In this case, it depends on what type of DTC is set to know what a "Trip" is.

For the Fuel Monitor or Mis-Fire Monitor (continuous monitor), the vehicle must be operated in the "Similar Condition Window" for a specified amount of time to be considered a Good Trip.

If a Non-Continuous OBDII Monitor, such as:

- Oxygen Sensor
- Catalyst Monitor
- Purge Flow Monitor
- Leak Detection Pump Monitor (if equipped)
- EGR Monitor (if equipped)
- Oxygen Sensor Heater Monitor

fails twice in a row and turns ON the MIL, re-running that monitor which previously failed, on the next start-up and passing the monitor is considered to be a Good Trip.

If any other Emission DTC is set (not an OBDII Monitor), a Good Trip is considered to be when the Oxygen Sensor Monitor and Catalyst Monitor have been completed; or 2 Minutes of engine run time if the Oxygen Sensor Monitor or Catalyst Monitor have been stopped from running.

It can take up to 2 Failures in a row to turn on the MIL. After the MIL is ON, it takes 3 Good Trips to turn the MIL OFF. After the MIL is OFF, the PCM will self-erase the DTC after 40 Warm-up cycles. A Warm-up cycle is counted when the ECT (Engine Coolant Temperature Sensor) has crossed 160 degrees F and has risen by at least 40 degrees F since the engine has been started.

---
*Chapter 25 - Emission Control Systems, Page 11*
