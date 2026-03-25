from setuptools import setup, find_packages
setup(
    name="population-evolution-by-age-groups-in-latin-america-2000-2023-dataset-by-country",
    version="1.0.0",
    description="This dataset contains data on the population evolution by age groups in 11 Latin American countries ",
    author="de la Serna, Juan Moisés",
    url="https://github.com/juanmoisesd/population-evolution-by-age-groups-in-latin-america-2000-2023-dataset-by-country",
    packages=find_packages(),
    install_requires=["pandas>=1.3.0","requests>=2.26.0"],
    python_requires=">=3.7",
    classifiers=["Programming Language :: Python :: 3","License :: OSI Approved :: MIT License","Topic :: Scientific/Engineering"],
    keywords="age-structure, cc0, cepal, citation, dataset, demographic-transition, demographics, demography, fair-data, iberoamerica, juan-moises-de-la-serna, latam, latin-america, open-data, open-science, orcid, population, population-data, research, zenodo, zenodo, open-data",
)