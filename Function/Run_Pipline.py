import pandas as pd

df_Pipeline = pd.read_csv("Running_Pipline.csv")
f = open("Running_Function.sh", "w")
for i in df_Pipeline.index:
	f.write("cd "+str(df_Pipeline["FileName"][i])+"\n")
	f.write("python Test*.py\n")
	f.write("cd ..\n")
f.close()



