import sys
import json

if __name__ == '__main__':
    results_file_name = sys.argv[1]
    csv_file = open(results_file_name.split('.json')[0]+'.csv','w')
    csv_file.write('name,solutionFF,solutionBF,solutionNF,solutionWF,solutionFFD,solutionBFD,exact_solution,timeFF,timeBF,timeNF,timeWF,timeFFD,timeBFD\n')
    results_file = open(results_file_name,'r')
    data = json.load(results_file)
    for instance in data:
        csv_file.write(instance['name'].split('.')[0]+','+str(instance['results']['FirstFit'][0]['num_bins'])+','+str(instance['results']['BestFit'][0]['num_bins'])+ ',' +str(instance['results']['NextFit'][0]['num_bins'])+','+ str(instance['results']['WorstFit'][0]['num_bins'])+','+str(instance['results']['FirstFitDec'][0]['num_bins'])+',' + str(instance['results']['BestFitDec'][0]['num_bins'])+ ',' + str(instance['solution']) +','+str(instance['results']['FirstFit'][0]['execution_time']).split(':')[2]+','+ str(instance['results']['BestFit'][0]['execution_time']).split(':')[2]+ ',' + str(instance['results']['NextFit'][0]['execution_time']).split(':')[2]+','+ str(instance['results']['WorstFit'][0]['execution_time']).split(':')[2]+','+str(instance['results']['FirstFitDec'][0]['execution_time']).split(':')[2]+','+ str(instance['results']['BestFitDec'][0]['execution_time']).split(':')[2]+'\n')
