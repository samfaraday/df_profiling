# DF_Profiling

Data Frame Profiling - A package that allows to easily profile your dataframe, 
              check for missing values, outliers, data types.
              <p> <ul><b>Import Lib</b>
                   <li>from  df_profiling  import  DF_Profiling </li></ul> 
                   <ul> <b>Profile your Data:</b>
                   <li> DF_Profiling.profiling("my_file.csv")</li></ul>
                   <p><b> <ul> <b>Either using Google Colab or Saving it as csv file, use the filter options to easily check for:
                   <li>Data Types</li>
                   <li>Counts</li>
                   <li>Missing Values Count</li>
                   <li>Missing Values Percentage</li>
                   <li> Min Value</li>
                   <li>Quartiles: 1st, 3rd</li>
                   <li>Median</li>
                   <li>Lower Bound Limits</li>
                   <li>Upper Bound Limits</li>
                   <li> Max Value</li>
                   <li> Unique Values</li>
                   <li> Spot Potential Outliers</li></ul>
                   <p><ul> <b>Save / Export your Analyses</b> 
                   <p><li> DF_Profiling.profiling("my_file.csv").to_csv("my_profiling.csv")</li></ul>
