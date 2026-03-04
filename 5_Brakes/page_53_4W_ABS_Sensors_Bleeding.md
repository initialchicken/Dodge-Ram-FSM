# BRAKES 5-53

## DESCRIPTION AND OPERATION (Continued)

During antilock braking, solenoid valve pressure modulation occurs in three stages, pressure decrease, pressure hold, and pressure increase. The valves are all contained in the valve body portion of the HCU.

**Pressure Decrease**

The inlet valve is closed and the outlet valve is opened during the pressure decrease cycle.

A pressure decrease cycle is initiated when speed sensor signals indicate high wheel slip at one or more wheels. At this point, the CAB closes the inlet to prevent the driver from further increasing the brake pressure and locking the brakes. The CAB then opens the outlet valve, which also opens the return circuit to the accumulators. Fluid pressure is allowed to bleed off (decrease) as needed to prevent wheel lock.

Once the period of high wheel slip has ended, the CAB closes the outlet valve and begins a pressure increase or hold cycle as needed.

**Pressure Hold**

Both solenoid valves are closed in the pressure hold cycle. Fluid apply pressure in the control channel is maintained at a constant rate. The CAB maintains the hold cycle until sensor inputs indicate a pressure change is necessary.

**Pressure Increase**

The inlet valve is open and the outlet valve is closed during the pressure increase cycle. The pressure increase cycle is used to counteract unequal wheel speeds. This cycle controls re-application of fluid apply pressure due to changing road surfaces or wheel speed.

### WHEEL SPEED SENSOR

The ABS brake system uses 3 wheel speed sensors. A sensor is mounted to each front steering knuckles. The third sensor is mounted on top of the rear axle differential housing. The sensor is a magnet coil that is mounted over a tone wheel front/exciter ring rear with an air gap between them.

The sensors measure the wheel speed by monitoring the rotation of the tone wheels front/exciter ring rear. As the teeth of the tone wheels front/exciter ring rear move through the magnetic field of the sensor an AC voltage is generated. This signal frequency increases or decreases proportionally to the speed of the wheel. The CAB monitors these signals for changes in wheel deceleration. If the CAB detects a sudden wheel or wheels deceleration within a predetermined amount the CAB will activate the ABS system.

### ABS WARNING LAMP

The amber ABS warning lamp is located in the instrument cluster. The lamp illuminates at start-up to perform a self check. The lamp goes out when the self check program determines the system is operating normal. If an ABS component exhibits a fault the CAB will illuminate the lamp and register a trouble code in the microprocessor. The lamp is controlled by the CAB. The CAB controls the lamp by directly grounding the circuit.

---

## DIAGNOSIS AND TESTING

### ANTILOCK BRAKES

The ABS brake system performs several self-tests every time the ignition switch is turned on and the vehicle is driven. The CAB monitors the systems input and output circuits to verify the system is operating correctly. If the on board diagnostic system senses that a circuit is malfunctioning the system will set a trouble code in its memory.

> **NOTE:** An audible noise may be heard during the self-test. This noise should be considered normal.

> **NOTE:** The MDS or DRB III scan tool is used to diagnose the ABS system. For additional information refer to the Antilock Brake section in Group 8W. For test procedures refer to the Chassis Diagnostic Manual.

---

## SERVICE PROCEDURES

### BLEEDING ABS BRAKE SYSTEM

ABS system bleeding requires conventional bleeding methods plus use of the DRB scan tool. The procedure involves performing a base brake bleeding, followed by use of the scan tool to cycle and bleed the HCU pump and solenoids. A second base brake bleeding procedure is then required to remove any air remaining in the system.

1. Perform base brake bleeding. Refer to base brake section for procedure.

2. Connect scan tool to the Data Link Connector.

3. Select ANTILOCK BRAKES, followed by MISCELLANEOUS, then ABS BRAKES. Follow the instructions displayed. When scan tool displays TEST COMPLETE, disconnect scan tool and proceed.

4. Perform base brake bleeding a second time. Refer to base brake section for procedure.

5. Top off master cylinder fluid level and verify proper brake operation before moving vehicle.
