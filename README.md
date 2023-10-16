## Create and Setup Virtual Environment
```
python3 -m venv $HOME/.virtualenvironments/WebScrape
/opt/homebrew/bin/python3 -m venv $HOME/.virtualenvironments/WebScrape
source $HOME/.virtualenvironments/WebScrape/bin/activate
pip install -r requirements.txt
deactivate
```

## Run code
```
source $HOME/.virtualenvironments/WebScrape/bin/activate
jupyter lab
```
- athlinks_scrape.ipynb - Get race results from Athlinks website
- athlinks_clean.ipynb - Clean results from Athlinks and save as Pandas pickle file
- Steamboat_Dist_analyze.ipynb - Analyze results of Steamboat race for 15K or 4 mile distance
- Steamboat_all_analyze.ipynb - Analyze counts of Steamboat race for 15K and 4 mile distance

Inside html_notebooks directory can view python code as webpages

## Export
### To HTML without showing python code
```
jupyter nbconvert Steamboat_Dist_analyze.ipynb --no-input --to html
```
### To HTML using preprocessor to not include cells marked skip_report
```
jupyter nbconvert Steamboat_Dist_analyze.ipynb --Exporter.preprocessors=\[\"preprocess.RemoveCellsWithNoTags\"\] --ClearOutputPreprocessor.enabled=False --no-input --to html
```


