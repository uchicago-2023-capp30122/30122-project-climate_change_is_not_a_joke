# <b>Climate Change is not a joke</b>
## <b>CAPP 122 Course Project | Winter 2023</b>
### <b>Team Members: Nadir Khan, Bob Surridge, Rob Mccormick, Kayecee Palisoc</b>


<p>
The 2015 Paris Agreement (ratified on Nov 2016) on climate change was a historic step forward in the global effort to combat the impacts of climate change. Multilateral development banks (MDBs) have an important role to play in supporting the implementation of the Paris Agreement, specifically in the Asia Pacific region, which is particularly vulnerable to the impacts of climate change. MDBs have a critical role to play in providing financial and technical assistance to developing countries to support the implementation of the Paris Agreement. The goal of this project is to conduct a comparative analysis of the funding patterns of major MDBs in the Asia Pacific region after the Paris Agreement.
</p>

<p>
The dashboad has six parts:
</p>

<p><b>1. Interactive Map</b> -shows the summarized information per country. Details will be shown when user hovers through the map on the right. Filters on the left side allow user to view different cuts metrics based on data source and the time interval (pre/post Paris Agreement) </p>

![Alt Text](https://github.com/uchicago-capp122-spring23/30122-project-climate_change_is_not_a_joke/blob/main/project_tracker/dashboard_screenshots/1.Map.png)



<p><b>2. Regression Plots</b> -examine the effects of the Paris Agrement on Climate related project investments. Detailed Statisical analysis results can be found in the StatResults file</p>

![Alt Text](https://github.com/uchicago-capp122-spring23/30122-project-climate_change_is_not_a_joke/blob/main/project_tracker/dashboard_screenshots/2.Regression.png)


<p><b>3. Histogram</b> -shows the distibution of commitment amount and project count</p>

![Alt Text](https://github.com/uchicago-capp122-spring23/30122-project-climate_change_is_not_a_joke/blob/main/project_tracker/dashboard_screenshots/3.Histogram.png)


<p><b>4. Country Level Deep dive</b> -this includes total cumulative funding amount per country, with GDP per capita and GAIN index information. To compare values between two countries, select the country name on the filters</p>

![Alt Text](https://github.com/uchicago-capp122-spring23/30122-project-climate_change_is_not_a_joke/blob/main/project_tracker/dashboard_screenshots/4.GDP_Vulnerability%20Datatable.png)


<p><b>5. Project-level graphs</b> -shows the overall project details of the  selected in Country Level filter. This has breakdown of count between pre and post Paris agreement, and a plot showing the count and funding amount over time</p>

![Alt Text](https://github.com/uchicago-capp122-spring23/30122-project-climate_change_is_not_a_joke/blob/main/project_tracker/dashboard_screenshots/5.project_plots.png)


<p><b>6. Data Table</b> -a table showing the individual project details of the selected country</p>

![Alt Text](https://github.com/uchicago-capp122-spring23/30122-project-climate_change_is_not_a_joke/blob/main/project_tracker/dashboard_screenshots/6.project_datatable.png)

### <b> Documentation </b>

<p>insert documentation texts here</p>


### <b> Instructions to execute project codes </b>
<p>NOTE: All codes to be run from within the project root directory</p>

<p> Setting up Virtual Environment and installing required packages:

1. Clone this repo
2. From within project root directory <b>30122-project-climate_change_is_not_a_joke</b> run `poetry install` (takes ~2 minutes for all packages to install)
3. Activate the virtual environment through `poetry shell`

Viewing WebApp:

1. Run `python3 -m project_tracker` (takes ~30 seconds)
2. Follow the generated URL link (eg: http://0.0.0.0:3004/) by clicking <b>Open in Browser</b> or by copying and pasting in your browser (On Mac, use <b>⌘</b> and click <b>Follow link</b> on the link generated)
3. The website may take a few seconds to load all figures

</p>












