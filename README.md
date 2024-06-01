## K-Means Customer Segmentation

This project performs K-Means clustering on a customer mall dataset to identify customer segments based on their annual income and spending score.

##Description

This code implements K-Means clustering to segment customers in a mall dataset. It uses the "Mall_Customers.csv" file, which is assumed to contain data on annual income, spending score, and potentially other customer attributes. The code performs the following steps:

1. Data Loading and Preprocessing:
    - Loads the CSV data into a pandas DataFrame.
    - Selects relevant features (annual income and spending score) for clustering.
    - Scales the features using StandardScaler for better clustering results.

2. Elbow Method for Optimal Clusters:
    - Calculates the Within-Cluster Sum of Squares (WCSS) for different K values (number of clusters).
    - Uses the elbow method to identify the optimal number of clusters based on the WCSS plot.

3. K-Means Clustering:
    - Performs K-Means clustering on the scaled data using the chosen optimal number of clusters.
    - Assigns cluster labels to each data point.

4. Analysis and Visualization:
    - Prints the cluster centers in the original feature scale.
    - Prints the distribution of data points across the identified clusters.
    - Visualizes the clusters using a scatter plot, where different colors represent different customer segments.

##Usage

1. Prerequisites:
   - Python 3.x with pandas, scikit-learn, and matplotlib libraries installed.
2. Running the Script:
   - Save the code as `customer_segmentation.py`.
   - Ensure the "Mall_Customers.csv" file is in the same directory.
   - Run the script from your terminal using `python customer_segmentation.py`.

##Output

The script will print the following:

- Cluster centers for each feature (annual income and spending score).
- The number of customers belonging to each cluster.
- A scatter plot visualizing the clusters and their centroids.

##Note:

- This code assumes the "Mall_Customers.csv" file has a specific format. You may need to modify the data loading and preprocessing steps if your data is structured differently.
- The chosen number of clusters (5 in this example) can be adjusted based on the specific dataset and the desired level of segmentation.
