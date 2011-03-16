Cereal nutritional fact visualization written in Tornado and Protovis

Assignment 3 for CS194 Data Sciences at UC Berkeley

## Visualizations in DataFlakes

The first is a bar graph showing the nutritional facts for cereals grouped by the shelf they sell on, showing that cereals on the bottom shelf are often times a healthier choice.

The second visualization is a scatter plot which tells consumers which words to look for and avoid in cereal names. For example, a cereal with "Wheat" in its name probably has less sugar than a cereal with "Crisp" in its name.

Lastly, we use a donut chart to show the makeup of an individual cereal. With these charts, it's easy to see which cereals have the most sugar and which contain the highest amounts of fiber.

## Visualization techniques

Using a grouped bar graph for the first visualization made sense because we were comparing the same data across three different groups. A scatter plot is great at encoding multiple dimensions of data, so graphing sugar, calories, cereal count, and name in a coherent matter is easy. Lastly, a donut-chart is a great way to show parts that make up a whole without causing the problems of pie charts.

## Data Transformation

The cereal data need to be first organized into a structured format before being cleaned to remove erroneous data. Lastly, in some instances the data need to be normalized so comparisons were correct.
