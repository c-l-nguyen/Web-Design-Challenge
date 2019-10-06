import pandas as pd

clinical_data_df = pd.read_csv("clinicaltrial_data.csv")
clinical_data_df.to_html("clinicaltrial_data.html",index=False)

mouse_df = pd.read_csv("mouse_drug_data.csv")
mouse_df.to_html("mouse_drug_data.html",index=False)