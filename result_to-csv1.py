import sys
import json

if __name__ == '__main__':
    results_file_name = sys.argv[1]
    csv_file = open(results_file_name.split('.json')[0]+'.csv','w')
    csv_file.write('name,solution_AG,exact_solution,Temps_exec\n')
    results_file = open(results_file_name,'r')
    data = json.load(results_file)
    for instance in data:
        csv_file.write(instance['name'].split('.')[0]+','+str(instance['results']['GA'][0]['num_bins'])+ ',' + str(instance['solution']) +','+str(instance['results']['GA'][0]['execution_time_in_seconds'])+'\n')
