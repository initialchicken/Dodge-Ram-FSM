# DIAGNOSIS AND TESTING (Continued)

### INSTRUMENT CLUSTER FAILURE MESSAGE

| Message | Description | Correction |
|---------|-------------|------------|
| 110 | A failure has been identified in the cluster CPU, RAM, or EEPROM. | Replace the faulty cluster. |
| 900 | The CCD data bus is not operational. | 1. Check the CCD data bus connections at the cluster. 2. Check the cluster fuses. 3. Check the CCD data bus bias. 4. Check the CCD data bus voltage. 5. Check the CCD data bus terminations. |
| 920 | The cluster is not receiving a vehicle speed message from the PCM. | 1. Check the PCM software level and reflash if required. 2. Use a DRB scan tool to verify that the vehicle speed message is being sent by the PCM. |
| 921 | The cluster is not receiving a distance pulse message from the PCM. | 1. Check the PCM software level and reflash if required. 2. Use a DRB scan tool to verify that the distance pulse message is being sent by the PCM. |
| 940 | The cluster is not receiving an airbag lamp-on message from the ACM. | 1. Check the CCD data bus connections at the ACM. 2. Check the ACM fuse. |
| 950 | The cluster is not receiving an ABS lamp-on message from the CAB. | 1. Check the CCD data bus connections at the CAB. 2. Check the CAB fuse. |
| 999 | An error has been discovered. | 1. Record the failure message. 2. Depress the trip odometer reset button to continue the Self-Diagnostic Test. |

Each of the red indicators are illuminated by a Light Emitting Diode (LED). If an LED fails to illuminate during this test, the instrument cluster must be replaced. Following the bulb check test, the instrument cluster Self-Diagnostic Test will automatically proceed as described in Step 8.

- (8) The instrument cluster will perform a gauge actuator test. In this test the instrument cluster circuitry positions each of the gauge needles at three different calibration points, then returns the gauge needles to their relaxed positions. If an individual gauge does not respond properly, or does not respond at all during the gauge actuator test, the instrument cluster should be removed. However, check that the gauge terminal pins are properly inserted through the spring-clip terminal pin receptacles on the instrument cluster circuit board before considering instrument cluster replacement. If the gauge terminal connections are OK, replace the faulty instrument cluster.

- (9) The Self-Diagnostic Test is now completed. The instrument cluster will automatically exit the self-diagnostic mode and return to normal operation at the completion of the test, if the ignition switch is turned to the Off position during the test, or if a vehicle speed message indicating that the vehicle is moving is received from the PCM on the CCD data bus during the test.

- (10) Go back to Step 1 to repeat the test, if required.

### COOLANT TEMPERATURE GAUGE

If the problem being diagnosed is related to coolant temperature gauge accuracy, be certain to confirm that the problem is with the gauge and not with cooling system performance. The actual engine coolant temperature should be checked with a test gauge or thermometer and compared to the instrument cluster coolant temperature gauge readings before you proceed with gauge diagnosis. Refer to Group 7 - Cooling System for more information. Refer to Group 8W - Wiring Diagrams for circuit descriptions and diagrams.

---
*8E_Insturment_Panel_Systems - Page 14*
