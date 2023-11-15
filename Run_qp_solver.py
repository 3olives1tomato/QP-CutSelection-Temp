import os
import pandas as pd
import threading
from TemporalSets import CutSolverT

solver= 'TemporalSets_lala'
print('Algorithm is ', solver)
sel_size = 100
n_clusters=100
dim = 3
cut_rounds = 20
termon = False
strategies = {1: 'feasibility', 2: 'optimality', 4: 'combined selection', 5: 'random'}
strat = 1

# Create a DataFrame to store results
cut_rounds_list = list(range(0, cut_rounds + 1))
data = {'Cut rounds': cut_rounds_list + ['time (sec)']}
df = pd.DataFrame(data)

# Define functions
def get_filenames_list():
    filenames_list = []
    file_path =os.path.join(os.getcwd(), r'boxqp_instances\filenames.txt') 
    with open(file_path, 'r') as file:
        for line in file:
            filenames_list.append(line.strip())
    return filenames_list

def process_filename(filename, all_results):
    csT=CutSolverT() 
    try:
        (sol, time, round_times, sep_times, nbs_sdp_cuts, nbs_tri_cuts,  vars_values, agg_list, n_cuts_added, n_replacements) = \
            csT.cut_select_algo(filename=filename,dim=dim, sel_size=sel_size, strat=strat, nb_rounds_cuts=cut_rounds, term_on=termon) 
        print('The original solution for file ', filename,' is',sol[-1], 'The time elapsed  is',time, 'The cut rounds are',len(nbs_sdp_cuts )-1)
        sol.append(time)
  
    except:
        sol=([0]*(cut_rounds+2))
    all_results[filename] = sol 

# Parallelize the processing of files in the folder
filenames_list = get_filenames_list()
threads = [] 
all_results = {} 
for filename in filenames_list:
    thread = threading.Thread(target=process_filename, args=(filename, all_results), daemon=True)
    thread.start()
    threads.append(thread)
    print('Threading', filename)
for thread in threads:
    thread.join()

# Add results to the DataFrame
for filename in filenames_list:
    df[filename] = all_results[filename]

results_folder = os.path.join(os.getcwd(), "Results_lala") # Check if the "Results" folder exists, if not, create it
if not os.path.exists(results_folder):
    os.makedirs(results_folder)

results_filename=solver+'_results.csv'
csv_file_path = os.path.join(results_folder, results_filename)
df.to_csv(csv_file_path, index=False)

print(df) # Display the DataFrame