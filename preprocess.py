from nbconvert.preprocessors import Preprocessor

class RemoveCellsWithNoTags(Preprocessor):
  def preprocess(self, notebook, resources):
      executable_cells = []
      for cell in notebook.cells:
          if cell.metadata.get('tags'):
              if "skip_report" in cell.metadata.get('tags'):
                  continue
          executable_cells.append(cell)
      notebook.cells = executable_cells
      return notebook, resources

# Need to escape the [ and " and ] for zsh on macos
# jupyter nbconvert Steamboat_Dist_analyze.ipynb --no-input --to html
# jupyter nbconvert Steamboat_Dist_analyze.ipynb --Exporter.preprocessors=\[\"preprocess.RemoveCellsWithNoTags\"\] --ClearOutputPreprocessor.enabled=False --no-input --to html
