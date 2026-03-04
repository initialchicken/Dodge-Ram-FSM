# DESCRIPTION AND OPERATION (Continued)

### OXYGEN SENSOR HEATER MONITOR

Effective control of exhaust emissions is achieved by an oxygen feedback system. The most important element of the feedback system is the O2S. The O2S is located in the exhaust path. Once it reaches operating temperature 300 degrees to 350 degrees C (572 degrees to 662 degrees F), the sensor generates a voltage that is inversely proportional to the amount of oxygen in the exhaust. The information obtained by the sensor is used to calculate the fuel injector pulse width. This maintains a 14.7 to 1 Air Fuel (A/F) ratio. At this mixture ratio, the catalyst works best to remove hydrocarbons (HC), carbon monoxide (CO) and nitrogen oxide (NOx) from the exhaust.

The voltage readings taken from the O2S sensor are very temperature sensitive. The readings are not accurate below 300 degrees C. Heating of the O2S sensor is done to allow the engine controller to shift to closed loop control as soon as possible. The heating element used to heat the O2S sensor must be tested to ensure that it is heating the sensor properly.

The O2S sensor circuit is monitored for a drop in voltage. The sensor output is used to test the heater by isolating the effect of the heater element on the O2S sensor output voltage from the other effects.

### LEAK DETECTION PUMP MONITOR (IF EQUIPPED)

The leak detection assembly incorporates two primary functions: it must detect a leak in the evaporative system and seal the evaporative system so the leak detection test can be run.

The primary components within the assembly are: A three port solenoid that activates both of the functions listed above; a pump which contains a switch, two check valves and a spring/diaphragm; a canister vent valve (CVV) seal which contains a spring loaded vent seal valve.

Immediately after a cold start, between predetermined temperature thresholds limits, the three port solenoid is briefly energized. This initializes the pump by drawing air into the pump cavity and also closes the vent seal. During non test conditions the vent seal is held open by the pump diaphragm assembly which pushes it open at the full travel position. The vent seal will remain closed while the pump is cycling due to the reed switch triggering of the three port solenoid that prevents the diaphragm assembly from reaching full travel. After the brief initialization period, the solenoid is de-energized allowing atmospheric pressure to enter the pump cavity, thus permitting the spring to drive the diaphragm which forces air out of the pump cavity and into the vent system. When the solenoid is energized and de-energized, the cycle is repeated creating flow in typical diaphragm pump fashion. The pump is controlled in 2 modes:

**Pump Mode:** The pump is cycled at a fixed rate to achieve a rapid pressure build in order to shorten the overall test length.

**Test Mode:** The solenoid is energized with a fixed duration pulse. Subsequent fixed pulses occur when the diaphragm reaches the switch closure point.

The spring in the pump is set so that the system will achieve an equalized pressure of about 7.5" H2O. The cycle rate of pump strokes is quite rapid as the system begins to pump up to this pressure. As the pressure increases, the cycle rate starts to drop off. If there is no leak in the system, the pump would eventually stop pumping at the equalized pressure. If there is a leak, it will continue to pump at a rate representative of the flow characteristic of the size of the leak. From this information we can determine if the leak is larger than the required detection limit (currently set at .040" orifice by CARB). If a leak is revealed during the leak test portion of the test, the test is terminated at the end of the test mode and no further system checks will be performed.

After passing the leak detection phase of the test, system pressure is maintained by turning on the LDP's solenoid until the purge system is activated. Purge activation in effect creates a leak. The cycle rate is again interrogated and when it increases due to the flow through the purge system, the leak check portion of the diagnostic is complete.

The canister vent valve will unseal the system after completion of the test sequence as the pump diaphragm assembly moves to the full travel position.

Evaporative system functionality will be verified by using the stricter evap purge flow monitor. At an appropriate warm idle the LDP will be energized to seal the canister vent. The purge flow will be clocked up from some small value in an attempt to see a shift in the O2 control system. If fuel vapor, indicated by a shift in the O2 control, is present the test is passed. If not, it is assumed that the purge system is not functioning in some respect. The LDP is again turned off and the test is ended.

### MISFIRE MONITOR

Excessive engine misfire results in increased catalyst temperature and causes an increase in HC emissions. Severe misfires could cause catalyst damage. To prevent catalytic converter damage, the PCM monitors engine misfire.

The Powertrain Control Module (PCM) monitors for misfire during most engine operating conditions (positive torque) by looking at changes in the crankshaft speed. If a misfire occurs the speed of the crankshaft will vary more than normal.

### CATALYST MONITOR

To comply with clean air regulations, vehicles are equipped with catalytic converters. These converters reduce the emission of hydrocarbons, oxides of nitrogen and carbon monoxide.

---
*Chapter 25 - Emission Control Systems, Page 10*
