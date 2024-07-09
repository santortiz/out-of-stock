<img heigth="8" src="https://i.imgur.com/3mimh4M.png" alt="guane">

<h1 align="center">🛠️ Out of Stock Problem 🤖</h1>

<p align="center">Predicting the Countdown - Estimating the Out-of-Stock Horizon for Retail Inventory</p>

<p align="center">
  <a href="https://www.guane.com.co/">guane enterprises</a> 
  <br> <br>
  <a href="#about">About</a> •
  <a href="#data-description">Data Description</a> •
  <a href="#life-cycle">Life Cycle</a> •
  <a href="#project-features">Project Features</a> •
  <a href="#contribute">Contribute</a> •
  <a href="#authors">Authors</a> •
  <a href="#license">License</a>
  <br> <br>
  <a href="https://img.shields.io/badge/version-0.0.1-blue.svg?cacheSeconds=2592000">
    <img src="https://img.shields.io/badge/version-0.0.1-blue.svg?cacheSeconds=2592000" alt="Version" height="18">
  </a>
  <a  href="[https://twitter.com/guaneAI](https://twitter.com/guaneAI)"  target="_blank">
    <img  alt="Twitter: GuaneAI"  src="https://img.shields.io/twitter/follow/guaneAI.svg?style=social"/>
  </a>
</p>


---

## About

The logistics department at retail industry, is responsible for transporting thousands of products daily throughout Latin America. Achieving precise sales predictions is vital to ensuring a superior delivery experience for customers. The essence of this commercial challenge is encapsulated in the Data Challenge task: using past sales data from a selection of marketplace listings, the goal is to forecast the time it will take for stock of a specific item to be completely depleted.

The objective is to estimate the time required for an item's stock to be sold out, a concept known in inventory management as 'days of inventory'. When assessing the test set, you will be provided with the designated stock level for the item, and it is your job to predict the amount of days it will last until it is fully depleted. Predictions can range from 1 to 30 days. The evaluation of submissions will utilize the [Ranked Probability Score (RPS)](https://syllepsis.live/2022/01/22/ranked-probability-score-in-python/#:~:text=The%20purpose%20of%20the%20ranked,in%20question%20is%20ranked%2Fordered.) as its metric. The RPS is a quadratic scoring rule that assesses how well the estimated cumulative distribution function of a probabilistic forecast aligns with the actual observed cumulative distribution, across a finite set of possible outcomes.

As a data scientist, it is extremely important to propose the predictive task for the problem, which best fits the problem and which delivers the greatest added value to our client. Be careful and propose an approach thinking at all times that the solution will be intended for inventory managers of companies in the retail sector.

The idea of this test, more than obtaining a model with the greatest precision, is to evaluate the ability to propose solutions while maintaining the best coding practices. Before being good data scientists, we must be excellent software developers, so it all adds up 😉. 

Success and good luck!


---

## Data Description

### items_metadata.jsonl

In the `items_metadata.jsonl` file, which is a JSON Lines (`.jsonl`) file containing metadata for various stock-keeping units (SKUs), you'll find a series of dictionaries. Each dictionary holds metadata about a specific SKU. Here's a breakdown of what each field represents:

Column Descriptions:

- **sku**: This is the acronym for 'stock-keeping unit.' It serves as a unique identifier for each distinguishable inventory item.

- **item_id**: This identifier is unique to a listing, but a single listing can have multiple SKUs linked to it. For instance, both the "t-shirt X, size M color Black" and "t-shirt X, size M, color Red" SKUs would have the same item_id, which corresponds to "t-shirt X."

- **item_domain_id**: Each listing is categorized within a 'domain' on e-commerce. A domain groups similar listings together. Taking the example of "t-shirt X," it might belong to a domain like MLB_SPORT_TSHIRT*S, which clusters sport t-shirts within Brazil's e-commerce site.

- **item_title**: This is the title of the listing, which is at the item level. So, all SKUs under "t-shirt X" would have a common title, such as "Sports T-shirt X."

- **site_id**: This indicates the specific store site a listing is associated with. The site IDs like MLB, MLA, and MLM correspond to the country-specific sites for Brazil, Argentina, and Mexico, respectively.

- **product_id**: Some listings have a product ID, although this field can be null. This ID helps to group the same products sold by different sellers. If several sellers are offering "t-shirt X," e-commerce assigns the same product_id to unify these listings under a single catalog entry.

- **product_family_id**: Similar to the product_id, this might also be null for some listings. It represents a broader cataloging system, grouping products into families. For "t-shirt X" sold by various vendors, the same product_family_id would be assigned to facilitate categorization at a higher hierarchy level.

This metadata is crucial for tasks that involve understanding the assortment of products, managing inventory, and providing insights into the range of items available on the store platform.

### train.csv

The training dataset features a collection of columns that contain detailed information about each SKU's sales performance, pricing, and logistics options for a given date. Below is an explanation of each column:

**Column Descriptions:**

- **sku**: Stock Keeping Unit. This unique identifier represents a specific item and its variations (like size, color, etc.).
  
- **date**: The format is YYYY-MM-DD, indicating the specific day the data was recorded.
  
- **sold_quantity**: This column shows the total number of units sold for the SKU on the specified date.
  
- **current_price**: It reflects the price of the SKU at the given time, which is subject to change over different dates.
  
- **currency**: The currency in which the SKU's price is denoted. The dataset includes several Latin American currencies, with possible values being ARG (Argentine Peso), DOL (US Dollar), MEX (Mexican Peso), and REA (Brazilian Real).
  
- **listing_type**: This indicates the marketing tier of the SKU for the given date. 'Classic' or 'premium' listings differ in their visibility on the platform and the commission fee charged to the seller. Items with a 'premium' listing often have added benefits, such as the option for buyers to pay in installments without an interest rate.
  
- **shipping_logistic_type**: Specifies the logistics approach used for delivering the SKU on that date. The options include 'fulfillment' (where the e-commerce handles the entire logistics), 'cross_docking' (where the product is temporarily stored at a e-commerce facility before being shipped), and 'drop_off' (where the seller is responsible for delivering the product to a carrier).
  
- **shipping_payment**: Indicates whether the buyer was entitled to free shipping or had to pay for it on that specific date for the SKU in question.
  
- **minutes_active**: This metric captures the total minutes the SKU was listed and available for purchase on the platform on the given date.

Understanding these variables is essential for analyzing sales patterns, pricing strategies, and logistical preferences, which could help in forecasting sales and inventory management.

### test.csv

In the `test_data.csv` file that is provided for testing your predictions, you will encounter a simplified structure compared to the training dataset. Here are the descriptions for the columns present in this test dataset:

**Column Descriptions:**

- **sku**: This column contains the unique identifier for each stock keeping unit (SKU). This is the same SKU for which you have analyzed historical sales data in the training dataset. Your task is to use this identifier to make predictions regarding the inventory levels.

- **target_stock**: This is the inventory level for the corresponding SKU. It represents the number of units that you need to estimate how long will last before running out. This is essentially the 'inventory days' you need to predict, based on the SKU's sales history and other factors you've analyzed.

In essence, for each SKU listed in the `test_data.csv` file, you are expected to predict the number of days it will take for the target stock to go from the specified level to zero, given your model's understanding of that SKU's sales dynamics. This prediction will then be used to measure the accuracy of your forecasting model against actual sales data, likely with a metric such as the Ranked Probability Score as mentioned earlier.


---

## Life Cycle

As a proposal for the data science life cycle, [OSEMN](https://towardsdatascience.com/5-steps-of-a-data-science-project-lifecycle-26c50372b492) is mainly proposed. Standing for Obtain, Scrub, Explore, Model, and iNterpret, OSEMN is a five-phase life cycle.

<img heigth="8" src="https://i.imgur.com/tDP8VUd.png" alt="guane"><br>

Other good option is [Microsoft TDSP: The Team Data Science Process](https://learn.microsoft.com/en-us/azure/architecture/data-science-process/overview) combines many modern agile practices with the life cycle. It has five steps: Business Understanding, Data Acquisition and Understanding, Modeling, Deployment, and Customer Acceptance.

The important thing is that if you think they should be combined and form their own life cycle, feel free to do so.


---

## Project Features

`out-of-stock-modeling` is built on `Python 3.9` with [pandas](https://pandas.pydata.org/), [numpy](https://numpy.org/) and [scikit-learn](https://scikit-learn.org/stable/), [matplotlib](https://matplotlib.org/), [seaborn](https://seaborn.pydata.org/), [plotly](https://plotly.com/python/)  among others, to preprocess the data, build the machine learning models, and visualize the results. 

For development, the library use:

- Formatting with [black](https://github.com/psf/black)
- Import sorting with [isort](https://github.com/timothycrosley/isort)
- Linting with [flake8](http://flake8.pycqa.org/en/latest/)
- Git hooks that run all the above with [pre-commit](https://pre-commit.com/)
- Testing with [pytest](https://docs.pytest.org/en/latest/)
- Dependency management with [Pipenv](https://pipenv-es.readthedocs.io/es/latest/)


---

## Contribute

First, make sure that before enabling pipenv, you must have `Python 3.9` installed. If it does not correspond to the version you have installed, you can create a conda environment with:

```sh
# Create and activate python 3.9 virutal environment
$ conda create -n py39 python=3.9
$ conda activate py39
```

Now, you can managament the project dependencies with `Pipenv`. To create de virtual environment and install all dependencies follow:

```sh
# Install pipx if pipenv and cookiecutter are not installed
$ python3 -m pip install pipx
$ python3 -m pipx ensurepath

# Install pipenv using pipx
$ pipx install pipenv

# Create pipenv virtual environment
$ pipenv shell

# Install dependencies
$ pipenv install --dev
```

Once the dependencies are installed, we need to notify `Jupyter` of this new `Python` environment by creating a kernel:

```sh
$ ipython kernel install --user --name KERNEL_NAME
```

Finally, before making any changes to the library, be sure to review the [GitFlow](https://www.atlassian.com/es/git/tutorials/comparing-workflows/gitflow-workflow) guide and make any changes outside of the `master` branch.


---

## License

Copyright 2023 © guane enterprises. All rights reserved.
