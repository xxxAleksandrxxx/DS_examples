It's a final project of [Data Visualization with Python cource by IBM](https://www.coursera.org/learn/python-for-data-visualization#modules)  

## Task description:
Create Dashboard with Plotly and Dash

As a data scientist, you have been given a task to prepare a report on your finding from Automobile Sales data analysis.
You decided to develop a dashboard representing two main reports:  
1. Yearly Automobile Sales Statistics
2. Recession Period Statistics

### Requirements to create the expected Dashboard
- Two dropdown menus: For choosing report type and year
- Each dropdown will be designed in a division  
    >The second dropdown (for selecting the year) should be enabled only if when the user selects “Yearly Statistics report” from the previous dropdown, else it should be disabled only.
- Layout for adding graphs
- Callback functions to return to the layout and display graphs.
    - First callback will be required to take the input for the report type and set the years dropdown to be enabled to take the year input for “Years Statistics Report”, else this dropdown be put on disabled.
    - In the second callback you will fetch the value of report type and year and return the required graphs appropriately for each type of report
- The four plots to be displayed in 2 rows, 2 column representation


## Result
Check web-app [here](https://atomobile-market-analitics.onrender.com)
