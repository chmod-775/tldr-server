FROM continuumio/miniconda3

MAINTAINER Patrick Kelley <pakelley@protonmail.com>

SHELL ["/bin/bash", "-c"]

ENV LANG=C.UTF-8 LC_ALL=C.UTF-8

WORKDIR /app/

RUN conda config --add channels conda-forge
# RUN conda uninstall nltk idna # FIXME: Gross hack, I'll deal with this later
RUN conda install -c pkelley tldr-server
# RUN conda config --prepend pkgs_dirs /condapkgs
# RUN conda env create -q -n tessie-filter
# RUN echo "# Activate the conda env for the app." >> /etc/bash.bashrc
# RUN echo "source activate tessie-filter" >> /etc/bash.bashrc

RUN mkdir src
COPY ./tldr-server/ ./src/

CMD python src/app.py
