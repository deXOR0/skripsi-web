<br/>
<p align="center">
  <h3 align="center">Jakarta Air Pollution Prediction</h3>

  <p align="center">
    Data Mining-based Web Application for Air Pollution Prediction in DKI Jakarta 
    <br/>
    <br/>
    <a href="https://skripsi-aqf.up.railway.app/">Visit Website</a>
  </p>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB.svg?style=for-the-badge&logo=Python&logoColor=white" />
  <img src="https://img.shields.io/badge/Django-092E20.svg?style=for-the-badge&logo=Django&logoColor=white" />
  <img src="https://img.shields.io/badge/pandas-150458.svg?style=for-the-badge&logo=pandas&logoColor=white" />
  <img src="https://img.shields.io/badge/NumPy-013243.svg?style=for-the-badge&logo=NumPy&logoColor=white" />
  <img src="https://img.shields.io/badge/PostgreSQL-4169E1.svg?style=for-the-badge&logo=PostgreSQL&logoColor=white" />
  <img src="https://img.shields.io/badge/Railway-0B0D0E.svg?style=for-the-badge&logo=Railway&logoColor=white" />
  <img src="https://img.shields.io/badge/Bootstrap-7952B3.svg?style=for-the-badge&logo=Bootstrap&logoColor=white" />
</p>

## Table Of Contents

* [About the Project](#about-the-project)
* [Built With](#built-with)
* [Getting Started](#getting-started)
  * [Prerequisites](#prerequisites)
  * [Installation](#installation)
* [Usage](#usage)
* [Authors](#authors)
* [Acknowledgements](#acknowledgements)

## About The Project

![Screen Shot](https://cdn.discordapp.com/attachments/846612997836505088/1072950943261392966/index.jpg)

This application was built as my team's undergraduate thesis. The purpose of this application is to display the air pollution level in DKI Jakarta and educate people about the danger and health risks that can be caused by air pollution. 

Some visualizations are provided to make it easily digestible by the general public. There is a geomap to display current air pollution levels across various districts in DKI Jakarta,  an ISPU index that explains what the current air pollution level means, the latest air pollution levels with a 12-hour prediction into the future, pollution level ranking between all the districts, and historical air pollution level data.

The prediction is made by using a SARIMAX model built on Python which is updated every hour to ensure data actuality.

## Built With

The Jakarta Air Pollution Prediction app was built using Python and the Django framework. It also includes a machine learning algorithm to predict future air pollution levels using the SARIMAX model of time series analysis.

* [Python](https://www.python.org/)
* [Django](https://www.djangoproject.com/)
* [Pandas](https://pandas.pydata.org/)
* [Numpy](https://numpy.org/)
* [Psycopg2](https://www.psycopg.org/docs/)
* [PostgreSQL](https://www.postgresql.org/)
* [Pytz](https://pypi.org/project/pytz/)
* [Statsmodels](https://www.statsmodels.org/stable/index.html)

## Getting Started

To get started, clone this repository through your favorite Git client, or by using 
```
git clone https://github.com/deXOR0/skripsi-web.git
```

### Prerequisites

Make sure you have these set up before you run the application
* Python
* pip
* postgresql@14
* venv

### Installation

1. Create a virtual environment inside the project's directory
    ```
    python -m venv venv
    ```

2. Activate the virtual environment
   ```
   source venv/bin/activate
   ```
   For Windows users
   ```
   . venv\Scripts\activate
   ```

3. Install the dependencies
   ```
   python -m pip install -r requirements.txt
   ```

4. Create a .env file to provide the necessary environment variables needed
    ```
    echo SECRET_KEY=""\\n\
      DATABASE_NAME=""\\n\
      DATABASE_USER=""\\n\
      DATABASE_PASSWORD=""\\n\
      DATABASE_HOST=""\\n\
      DATABASE_PORT=""\\n\
      MODE="dev" > .env
    ```

5. Fill in the environment variables' value

6. Provision a PostgreSQL database and fill in the credentials to the environment variables

## Usage

To run the application you can start a local server with hot reloading enabled by entering this command
```
python manage.py runserver
```

To run it in production enter the command
```
gunicorn skripsi_aqf.wsgi --timeout 300
```

## Authors

* **Atyanta Awesa Pambharu** - *Back-end Engineer, Machine Learning Engineer* - [Atyanta Awesa Pambharu](https://github.com/deXOR0/) - *Built the back end and the machine learning model*
* **Adie Satriyo Nirbito** - *Front-end Engineer, Machine Learning Engineer* - [Adie Satriyo Nirbito](https://github.com/Asabito/) - *Built the front end and the machine learning model*
* **Luthfie Hafizh Anugerah** - *Machine Learning Engineer* - [Luthfie Hafizh Anugerah](https://github.com/LuthfieHafizh) - *Built the machine learning model*

## Acknowledgements

* Dr. Eka Miranda, S.Kom., MMSI.
* [ritvikmath](https://github.com/ritvikmath/Time-Series-Analysis/)
* [Timon Florian Godt](https://medium.com/@timonfloriangodt/forecasting-hourly-electricity-consumption-with-arimax-sarimax-and-lstm-part-i-cc652cdd905a)
