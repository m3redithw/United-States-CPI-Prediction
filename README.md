![inflation](https://user-images.githubusercontent.com/105242871/188526013-4313105f-5b16-4330-814d-2f1499d2bc45.png)

# United States Inflation Prediction
by [**Meredith Wang**](https://www.linkedin.com/in/m3redithw/)

Sep 2022

<a href="#"><img alt="Python" src="https://img.shields.io/badge/Python-013243.svg?logo=python&logoColor=white"></a>
<a href="#"><img alt="Pandas" src="https://img.shields.io/badge/Pandas-150458.svg?logo=pandas&logoColor=white"></a>
<a href="#"><img alt="NumPy" src="https://img.shields.io/badge/Numpy-2a4d69.svg?logo=numpy&logoColor=white"></a>
<a href="#"><img alt="Matplotlib" src="https://img.shields.io/badge/Matplotlib-8DF9C1.svg?logo=matplotlib&logoColor=white"></a>
<a href="#"><img alt="seaborn" src="https://img.shields.io/badge/seaborn-65A9A8.svg?logo=pandas&logoColor=white"></a>
<a href="#"><img alt="math" src="https://img.shields.io/badge/math-adcbe3.svg?logo=plotly&logoColor=white"></a>
<a href="#"><img alt="sklearn" src="https://img.shields.io/badge/sklearn-4b86b4.svg?logo=scikitlearn&logoColor=white"></a>
<a href="#"><img alt="SciPy" src="https://img.shields.io/badge/SciPy-1560bd.svg?logo=scipy&logoColor=white"></a>


The United States' inflation is at its highest in nearly 40 years, as the COVID-19 pandemic has caused both supply and demand-side shocks, with a disrupted supply chain, unprecedented levels of government fiscal stimulus, shifts in consumer spending, a decline in labor force participation, and presistent business uncertainty.

***

## 🏁   Project Goals
▪️ Identify economic trends in the United States from 1957 to 2022.

▪️ Construct an ML model that predict **CPI** ('all_items_value') for future recent years.

***

## :memo:   Initial Questions
▪️ Is there trend or seasonality in `all_items_value` we can find?

▪️ Does CPI follow a specific pattern each month over the years?

▪️ Do `food_values`, `energy_value`, `apparel_value`, `gasoline_value`, `medical value`, `transportation value` have distinct trends or do they all follow the same pattern?

***

## :open_file_folder:   Data Dictionary
**Variable** |    **Value**    | **Meaning**
---|---|---
*Year* | Datetime object | The year of the data source
*Month* | Integer ranging from 1-12 | The month of the data source
*All Items Value* | Float | All items CPI in U.S. city average, seasonally adjusted
*Apparel Value* | Float | Apparel items CPI in U.S. city average, seasonally adjusted
*Food Value* | Float | Food CPI in U.S. city average, seasonally adjusted
*Energy Value* | Float | Energy CPI in U.S. city average, seasonally adjusted
*Gasoline Value* | Float | Gasoline CPI in U.S. city average, seasonally adjusted
*Medical Value* | Float | Medical CPI in U.S. city average, seasonally adjusted
*Transportation Value*| Float | Transportation CPI in U.S. city average, seasonally adjusted

***

## 📊   Data Context
We have monthly data from 1957 to 2022 CPI for All Urban Consumers. 3 **datetime** objects and 14 **numerical** variables.

***

## :placard:   Project Plan / Process
#### :one:   Data Acquisition

- Gather data from [BLS Beta Labs](https://beta.bls.gov/labs/)

#### :two:   Data Preparation

<details>
<summary> Data Cleaning</summary>

- **Join Tables:**
    - All 8 tables on joined on time index
    
    - Merging and concatenation are done in Microsoft Excel.
    
- **Rename Column**
     ```sh
     df = df.rename(columns={'period': 'month'})
     ```
    
- **Convert Datatype**
     ```sh
     df['label'] = pd.to_datetime(df['label'], infer_datetime_format=True)
     df['year'] =  pd.to_datetime(df['year']).dt.to_period('Y')
     df['month'] = df['month'].str.replace('M', '')
     ```
    
- Create function `get_data` to clean and prepare data with steps above

- Import [prepare.py](prepare.py)

- Test prepare function

- Call the function, and store the cleaned data in the form of dataframe
</details>

<details>
<summary> Data Splitting</summary>

- Using percentage-based method to split data into **train, validate, test**

- Check the size of each dataset
     ```sh
     train.shape, validate.shape, test.shape
     ```
</details>

***

#### :three:   Exploratory Analysis
- Ask questions to find trend or seasonality in `all_items_value`

- Resample by month and explore commonality in values over time

- Using visualizations to better understand the relationship between features

***

#### :four:    Modeling Evaluation
- Using **Last Observed Value** to make prediction and calculate model's RMSE on validate dataset

- Using **Simple Average** to make prediction and calculate model's RMSE on validate dataset

- Using **Moving Average** to make prediction and calculate model's RMSE on validate dataset

- Using **Holt's Linear Trend** to make prediction

- Pick the model with lowest RMSE and evaluate on test dataset

***

## 	♻️   Steps to Reproduce
- [x] You will to go to BLS Beta Labs to acquire the data
- [x] Clone my repo (including the **prepare.py**) 
- [x] Libraries used are pandas, numpy, datetime, math, matplotlib, seaborn, statsmodels, sklearn
- [x] Follow instructions in [eda](eda.ipynb) workbook and README file
- [x] Good to run report :smile_cat:

***

## 🔆   Conclusion

▪️ The machine learning model: Holt's Linear Trend is expected to predict housing prices within variance of **35** on average on future unseen data

▪️ The inflation rate for the United States for the next year is predicted to be 8.5%
population, etc.)

▪️ Develop machine learning models with higher accuracy (lower RMSE) with these additonal data and make better predictions.

▪️ Collect data on previous years to analyze the general trend of each area, and determine what features drive the housing prices the most.
