install the package pyinstaller package:
pip install pyinstaller
generate target-runner.py:
cd path\\to\\target-runner.py
pyinstaller --onefile target-runner.py

////////////////////////////////////////////////

commands on rsudio :

library("irace")
setwd("C:/Users/T480S/Documents/ESI/2CS-SIQ3/S2/OPTIM/BinPacking/parameter_calibration/AG")
scenario <- readScenario(filename = "scenario.txt",scenario = defaultScenario())
checkIraceScenario(scenario = scenario)
irace.main(scenario = scenario)