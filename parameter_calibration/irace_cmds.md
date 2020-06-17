install the package pyinstaller package: <br>
pip install pyinstaller <br>
generate target-runner.py: <br>
cd path\\to\\target-runner.py <br>
pyinstaller --onefile target-runner.py <br>

////////////////////////////////////////////////

commands on rsudio :<br>

library("irace")<br>
setwd("C:/Users/kaout/OneDrive/Bureau/BinPacking/parameter_calibration/RT")<br>
scenario <- readScenario(filename = "scenario.txt",scenario = defaultScenario())<br>
checkIraceScenario(scenario = scenario)<br>
irace.main(scenario = scenario)<br>