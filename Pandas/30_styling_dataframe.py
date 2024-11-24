# import pandas as pd

# # Create dataframe
# data = {'Name' : ['Alice', 'Bob', 'Charlie', 'David'], 'Score': [85,90,78,92]}
# df = pd.DataFrame(data)

# # Applying styles to highlight scores above 80
# styled_df = df.style.applymap(lambda x:'background-color : yellow' if isinstance (x, int) and x > 80 else '')

# # Displaying the styled Dataframe (use.render() if exporting to HTML)
# print('Styled dataframe with condiotinal formatting')


import pandas as pd

# Create dataframe
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David'], 'Score': [85, 90, 78, 92]}
df = pd.DataFrame(data)

# Applying styles to highlight scores above 80
styled_df = df.style.map(
    lambda x: 'background-color: yellow' if isinstance(x, int) and x > 80 else ''
)

# Save styled DataFrame to HTML
styled_df.to_html("styled_dataframe.html")

# Displaying the styled Dataframe
print("Styled dataframe with conditional formatting has been saved to 'styled_dataframe.html'.")
