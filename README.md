# Data Analysis - Hypothesis Testing
In this project, I have used the dataset (```data.csv```), to examin a case study finding a correlation between students' academic performance and social media. This dataset contains students' gender, ages, the spent time on social media, and their Grage Point Average (GPA). The goal of this project is to apply the hypothesis testing methodology and check whether time spent on social media, gender and age affect the students' GPA or not.


<br>

## Getting Started
This project is consists of statistical analysis and modeling them with plots and diagrams. To do so, it's important to acquire some certain required and essential library packages to be able to run the project. These packages are:

### Dependencies
- [ThinkStats2 by Prof. Allen B. Downey](https://github.com/AllenDowney/ThinkStats2). <br>
   _Note: The link's repository is downloadable as ThinkStats2 package. You can find also his book as a guideline reference._
- [Matplotlib](https://github.com/matplotlib/matplotlib)
- [NumPy](https://github.com/numpy/numpy)
- [SciPy](https://github.com/scipy/scipy)


<br>

## Explanation
In this project, I'm going to try to answer 3 main question:
1. Is there any significant correlation between the numbers of minutes that college students spent on Facebook and their academic performance represented by (GPA)? 
2. Is there any significant correlation between the time spent on Facebook and the student’s age? 
3. Is there any significant significant difference between male and female college students in relation to the use of Facebook in regard to time spent on Facebook?

Each part of the project will be contributing to answer the previous questions. To answer them, I will apply **Hypothesis Test** and **Regression**. First, for hypothesis testing, we need to follow the following steps:

<ul>
  <li>For each question, if it is necessary, state stated null hypothesis and alternative hypothesis, and justify why the null hypothesis is accepted or rejected. For example, in a case, if you want to know whether defendant is innocent or not your null hypothesis and alternative hypothesis are like: <br><br>
<pre>
 <i>H0: defendant is innocent</i>
 <i>H1: defendant is guilty</i>
</pre>
   Where <i>H0</i> is null and <i>H1</i> is alternative hypothesis.
  </li>
</ul>

- Make assumptions and meet test requirements. We have information for 120 students so we can use mean for the level of measurement. We can use normal distribution as a sample distribution and we can make ```alpha = 0.05```.
- Select the sampling distribution (normal distribution) and establish the critical region
- Compute the test statistic like using formula for normal distribution, finding mean, standard deviation, plotting CDF etc.
- Finally, Make a decision and interpret the results.


<br>

### Part [ 1 ] - Hypothesis Test
In this part, I'm going to apply hypothesis test to the above three questions. The goal of classical hypothesis testing is to answer the question, “Given a sample and an apparent effect, what is the probability of seeing such an effect by chance?” 

To do so, after importing the data, we define our hypothesis as below (the example below is for the first question):
<pre>
<i>H0</i>: time spend on media does not have effect on GPA.
<i>H1</i>: time spend on media end up decrease in GPA.
</pre>

After stating the hypothesis test, we find the mean for both spent time and GPA attributes. Then, finally, we find the p-value in order to make assumptions about the our hypothesis.


<br>

### Part [ 2 ] - Regression
In the first part, we measure the correlation for the strength and sign of a relationship, but not the slope. In this part we will measure slope for a relationship. We will model the relationships by useing linear fit and regression. To do so, I plotted the scatter plot of GPA and time spend in social media. You may testify it by running the script, or see it in screenshots folder. I have inserted a fitted line to the scatterplot to provide a better understanding to the visualized data.


<br>

## Screenshots
Below screeshot examples of Normal Distribution plot, and couple of scatter plot comparisons:


<br>
<p>
   <em>Normal Distribution Showing the Rejection Region</em>
   <br><br>
   <img style="max-width: 100%;height: 450px;" src="/screenshots/ND.png" alt>
</p>



<br>

<p>
   <em>Data Distribution for the Time Spent vs Student's GPA</em>
   <br><br>
   <img style="max-width: 100%;height: 450px;" src="/screenshots/TimevsGPA.png" alt>
</p>



<br>

<p>
   <em>Data Distribution for the Time Spent on Social Media for Males vs Females</em>
   <br><br>
   <img style="max-width: 100%;height: 450px;" src="/screenshots/MvsFM.png" alt>
</p>
