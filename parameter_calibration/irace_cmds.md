install the package pyinstaller package: <br>
pip install pyinstaller <br>
generate target-runner.py: <br>
cd path\\to\\target-runner.py <br>
pyinstaller --onefile target-runner.py <br>

////////////////////////////////////////////////

commands on rsudio :<br>

library("irace")<br>
setwd("C:/Users/T480S/Documents/ESI/2CS-SIQ3/S2/OPTIM/BinPacking/parameter_calibration/AG")<br>
scenario <- readScenario(filename = "scenario.txt",scenario = defaultScenario())<br>
checkIraceScenario(scenario = scenario)<br>
irace.main(scenario = scenario)<br>