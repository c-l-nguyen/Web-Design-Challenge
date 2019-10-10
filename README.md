# Web-Design-Challenge
A web visualization dashboard created using HTML/CSS in Bootstrap to summarize pharmaceutical analysis done in pandas. The link address is https://c-l-nguyen.github.io/Web-Design-Challenge/. The original analysis that generated the plots and summaries is at https://github.com/c-l-nguyen/pymaceuticals.


This project demonstrates the use of HTML and CSS within a Bootstrap framework to produce a navigable website hosted on a personal Github Page. A custom Bootswatch theme (https://bootswatch.com/pulse/) was used to help develop the site. 

The contents of the site are as follows:

* A landing page containing:
    * An explanation of the Pymaceuticals project.
    * Links to each visualizations page.
* Four visualization pages, each with:
    * A descriptive title and heading tag.
    * The plot/visualization itself for the selected comparison across drug types.
    * A paragraph describing the plot and its significance.
* A "Comparisons" page that:
    * Contains all of the visualizations on the same page so we can easily visually compare them.
    * Uses a bootstrap grid for the visualizations.
* Two "Data" pages that display the data used in the visualizations:
    * The clinical trial data that shows tumor volume measurements and number of metastatic sites taken during the time of the experiment
    * The mouse drug data the shows the mouse ID and which Pymaceutical drug it was exposed to
    
The directory structure is as follows:

* **/WebVisualizations**
    * **/Resources**: contains the CSV data tables used in the analysis and HTML versions of those tables
    * **/assets**: contains CSS style documents and non-visualization pictures
    * **/pages**: contains every non-landing page HTML file
    * **/visualization**: contains the visualization plots used for webpages
* index.html: the landing page
* README.md: the README document
