# Import any necessary modules below.
import math
import pandas as pd

# 1. Write the code that reads the given amzn.csv using one of the Pandas
# function, creates a dataframe containing all the data in amzn.csv, and
# assign the dataframe to the variable named 'df'. [10 pts]
df = pd.read_csv("amzn.csv")


# 2. Write the code that converts the values in 'Close/Last' column into
# float data type. For example, the string value, "$176.53" must be converted
# into a float number 176.53. Create a new column with converted value inside
# 'df' whose name is 'Close_float'. [10 pts]
df["Close_float"] = df["Close/Last"].apply(lambda x: float(x.strip("$")))


# 3. Write the code that calculates "volatility" using the values stored in
# the column 'Close_float' in 'df'. "Volatility" is calculated by
# the standard deviation of log returns multiplied by sqrt(252); 252 is
# the number of trading days per year. Assign the calculated volatility
# value into the variable vol. [10 pts]
log_returns = (df["Close_float"] / df["Close_float"].shift(1)).apply(
    lambda x: math.log(x)
)
vol = log_returns.std() * math.sqrt(252)


# 4. Write the code that calculates the "maximum profit" a trader can expect
# if they traded AMZN stock during the time in the data set. To achieve
# "maximum profit", a trader must buy the stock on the day when the close price
# was the lowest, and sell the stock on the day when the close price was the
# highest. Assign the maximum profit value into the variable max_profit.
# [30 pts]
df["daily_profit"] = df["Close_float"] - df["Close_float"].shift(1)
df["cumulative_profit"] = df["daily_profit"].cumsum()
max_profit = df["cumulative_profit"].max()
print("Volatility:", vol)
print("Maximum Profit:", max_profit)