Requirements

The solution should utilize 2 APIs/Functions
•1st API/Function that, for each file provided, returns exactly 30 consecutive data points starting from a random timestamp within the file. Which means the timestamp cannot be from the 
last 29 data points.
•2nd API/function that gets the output from 1st one as a feed and returns the list of outliers.

Data & Inputs

Sample data is provided in .csv format. Each file has  •Stock-ID (Ticker), Timestamp (dd-mm-yyyy), stock price value. 

Input parameter to your solution: 

The recommended number of files to be sampled for each Stock Exchange. Possible input values are 1 or 2. If there aren’t enough files present for a given 
exchange, process whatever number of files are present even if it is lower. E.g., input is 2 but only 1 file is present, so you process 1 file.
Outlier definition: Any datapoint that is over 2 standard deviations beyond the mean of the 30 sampled data points.

Output Format

Create one .csv file for each file processed. Each .csv should have below columns on each row (1 for each outlier found). Timestamp & stock prices have same format as input file.
Stock-ID, Timestamp, actual stock price at that timestamp, mean of 30 data points, actual stock price – mean, % deviation over and above the threshold.

Error Handling 

The application should gracefully handle exceptions, such as no files, empty files, invalid CSV format etc., Please free to include as much exception handling as possible. It provides insights 
into your ability to anticipate what can go wrong.

Documentation

Include a README file explaining how to set up and run your application.
Optional Enhancements

Feel free to add enhancements that could improve the extensibility/maintainability for future enhancement, user experience etc., Some suggestions include:
- additional functionality or checks
- more insights added in the report you generate
- Optimizations for performance and scalability
