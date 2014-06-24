RUN_NOTEBOOKS_DIR = run_notebooks
HTML_NOTEBOOKS_DIR = $(CURDIR)/../docs/notebooks/notebooks

notebooks := $(wildcard *.ipynb)
run_notebooks := $(addprefix $(RUN_NOTEBOOKS_DIR)/,$(notebooks))
notebook_html := $(patsubst %.ipynb,$(HTML_NOTEBOOKS_DIR)/%.html,$(notebooks))

.PHONY : clean all

all : $(notebook_html)

$(HTML_NOTEBOOKS_DIR)/%.html : $(RUN_NOTEBOOKS_DIR)/%.ipynb | $(HTML_NOTEBOOKS_DIR)
	ipython nbconvert --to=html --stdout $< > $@

$(RUN_NOTEBOOKS_DIR)/%.ipynb : %.ipynb | $(RUN_NOTEBOOKS_DIR)
	runipy --pylab --matplotlib --skip-exceptions $< $@

$(RUN_NOTEBOOKS_DIR) :
	mkdir -p $(RUN_NOTEBOOKS_DIR)

$(HTML_NOTEBOOKS_DIR) :
	mkdir -p $(HTML_NOTEBOOKS_DIR)

clean :
	rm -rf $(RUN_NOTEBOOKS_DIR)
	rm -rf $(HTML_NOTEBOOKS_DIR)
