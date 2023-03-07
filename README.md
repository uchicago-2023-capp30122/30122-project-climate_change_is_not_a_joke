# <b>Climate Change is not a joke</b>
## <b>CAPP 122 Course Project | Winter 2023</b>
### <b>Team Members: Nadir Khan, Bob Surridge, Rob Mccormick, Kayecee Palisoc</b>


<p>
The 2015 Paris Agreement (ratified on Nov 2016) on climate change was a historic step forward in the global effort to combat the impacts of climate change. Multilateral development banks (MDBs) have an important role to play in supporting the implementation of the Paris Agreement, specifically in the Asia Pacific region, which is particularly vulnerable to the impacts of climate change. MDBs have a critical role to play in providing financial and technical assistance to developing countries to support the implementation of the Paris Agreement. The goal of this project is to conduct a comparative analysis of the funding patterns of major MDBs in the Asia Pacific region after the Paris Agreement, specifically the World Bank and Asian Development Bank.
</p>

<p>
The dashboad has six parts:
</p>

<p><b>1. Interactive Map</b> -shows the summarized information per country. Details will be shown when user hovers through the map on the right. Filters on the left side allow user to view different metrics (count, funding amount, climate funding proportion) based on funding source source and the time interval (pre/post Paris Agreement) </p>

![Alt Text](https://github.com/uchicago-capp122-spring23/30122-project-climate_change_is_not_a_joke/blob/main/project_tracker/dashboard_screenshots/1.Map.png)


<p><b>2. Regression Plots</b> -examine the effects of the Paris Agrement on Climate related project investments. Detailed Statisical analysis results can be found in the <a href = "https://github.com/uchicago-capp122-spring23/30122-project-climate_change_is_not_a_joke/blob/main/project_tracker/Documentation/Statistical%20Model%20and%20Comparative%20Data%20Analysis.pdf">Statistical Model and Comparative Data Analysis file</a></p>

![Alt Text](https://github.com/uchicago-capp122-spring23/30122-project-climate_change_is_not_a_joke/blob/main/project_tracker/dashboard_screenshots/2.Regression.png)


<p><b>3. Histogram</b> -shows the distibution of commitment amount and project count</p>

![Alt Text](https://github.com/uchicago-capp122-spring23/30122-project-climate_change_is_not_a_joke/blob/main/project_tracker/dashboard_screenshots/3.Histogram.png)


<p><b>4. Country Level Deep dive</b> -this includes total cumulative funding amount per country, with GDP per capita and GAIN index information. To compare values between two countries, select the country name on the filters</p>

![Alt Text](https://github.com/uchicago-capp122-spring23/30122-project-climate_change_is_not_a_joke/blob/main/project_tracker/dashboard_screenshots/4.GDP_Vulnerability_Datatable.png)


<p><b>5. Project-level graphs</b> -shows the overall project details of the  selected in Country Level filter. This has breakdown of project status between pre and post Paris agreement, and a plot showing the count and funding amount over time</p>

![Alt Text](https://github.com/uchicago-capp122-spring23/30122-project-climate_change_is_not_a_joke/blob/main/project_tracker/dashboard_screenshots/5.project_plots.png)


<p><b>6. Data Table</b> -shows the individual project details of the selected country, user can also be directed to the project page through the project url on the last column</p>

![Alt Text](https://github.com/uchicago-capp122-spring23/30122-project-climate_change_is_not_a_joke/blob/main/project_tracker/dashboard_screenshots/6.project_datatable.png)

### <b> Documentation </b>

<p><b>Software Architecture</b></p>

<p>This diagram showcases the high-level architecture of the project software. The data is loaded from two different portals, then cleaned and aggregated, and added to a dashboard module and backend database. The dashboard produces the visualization shown on the right.</p>  

![Alt Text](https://github.com/uchicago-capp122-spring23/30122-project-climate_change_is_not_a_joke/blob/main/project_tracker/Documentation/Software%20Architecture.JPG)

<p><b>Application Architecture</b></p>

<p>This diagram showcases the software architecture for the web application. This application features three different pathways (project_tracker, graphs, and load_and_clean) that all connect to the __main__.py module, which runs the dashboard application.</p>  

![Alt Text](https://github.com/uchicago-capp122-spring23/30122-project-climate_change_is_not_a_joke/blob/main/project_tracker/Documentation/Application%20Structure.JPG)

<p><b>Project Folder Structure</b></p>

<p>This figure showcases the folder structure, including all modules and file data, for the final project</p> 

![Alt Text](https://github.com/uchicago-capp122-spring23/30122-project-climate_change_is_not_a_joke/blob/main/project_tracker/Documentation/Folder%20Structure.jpg)

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
  
(Optional) Scraping Data from the Asian Development Bank Data Library:

To view sample data web-scrape from the ADB Data Library:
1. Run `python3 -m project_tracker.load_and_clean.draft_crawler`
2. Sample dataset created is stored in <b>project_tracker/data/raw/adb_projects.json</b>

</p>












