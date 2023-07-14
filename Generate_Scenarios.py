import json
import time

import pandas as pd
import os

from SocialScenarioGPT import generate_scenario

df_2016 = pd.read_csv('Dataset/ROCStories__spring2016.csv')
df_2017 = pd.read_csv('Dataset/ROCStories_winter2017.csv')

# Using pandas.concat() Method
data = [df_2016, df_2017]
df_rocstories = pd.concat(data, ignore_index=True, sort=False)
df = df_rocstories.sample(n=100, replace=True, random_state=1)

times = []

for index, row in df.iterrows():
    scenario_description = " ".join([row['sentence1'], row['sentence2'], row['sentence3'], row['sentence4'], row['sentence5']])
    scenario_name = "test_" + row['storytitle']
    start_time = time.time()
    for i in range(10):
        try:
            generate_scenario(scenario_name, scenario_description)
        except Exception as e:
            print(e)
            continue
        else:
            break
    final_time = (time.time() - start_time)
    print("--- %s minutes ---" % ((time.time() - start_time) / 60))
    times.append(final_time)

    with open("Data/time_spent.json", "w") as f:
        average_time = sum(times)/len(times)
        json_times = json.dumps({"average_time": average_time, "times": times})
        f.write(json_times)


