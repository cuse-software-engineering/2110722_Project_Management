# Function Point Languages Table — QSM Software Project Estimation

*Chapter 7 (Project Cost Management) reference document: a printout of QSM's "Function Point Languages Table" web page (https://www.qsm.com/resources/function-point-languages-table), listing gearing factors (SLOC per function point) by programming language. Printed 9/28/26, 2:35 PM. The page has no highlighting; bold text below is bold in the original.*

## Page 1

## Version 5.0

The QSM Function Points Languages Table contains updated function point language gearing factors for 37 distinct programming languages/technologies. The data supporting release 5.0 was drawn from 2192 recently completed function point projects from the QSM database. The sample included 126 languages, 37 of which had sufficient data to be included in the table.

[Learn more about QSM's function point analysis] *(button)*

**Release 5 features and observations:**

- 3 new technologies added
- 32 gearing factors updated
- The range (minimum/maximum values) for each language has grown smaller with each release of the table. This trend continued with release 5.
- Average and median values for most languages have decreased since the last update.

Environmental factors can result in significant variation in the source statements per function point. For this reason, QSM recommends that organizations collect both code counts and final function point counts for completed software projects and incorporate this data into project estimates. Where there is no completed project data available for estimation, we provide the following industry gearing factor information (where sufficient project data exists):

- Average
- Median
- Range (low - high)

These three measures should allow software estimators to assess the amount of variation, the central tendency, and any skew to the distribution of gearing factors for each language.

[Additional information](#more-information-on-using-gearing-factors) on gearing factors and recommendations on using this table.

Request gearing factors *(link)* for languages not found in the table.

## Pages 2–3 — QSM SLOC/FP Data

\* Languages with updated gearing factors.
\+ New languages for which gearing factor data was not previously reported.

**QSM SLOC/FP Data**

| Language | Avg | Median | Low | High |
|---|---:|---:|---:|---:|
| ABAP (SAP) \* | 28 | 18 | 16 | 60 |
| ASP\* | 51 | 54 | 15 | 69 |
| Assembler \* | 119 | 98 | 25 | 320 |
| Brio + | 14 | 14 | 13 | 16 |
| C \* | 97 | 99 | 39 | 333 |
| C++ \* | 50 | 53 | 25 | 80 |
| C# \* | 54 | 59 | 29 | 70 |
| COBOL \* | 61 | 55 | 23 | 297 |
| Cognos Impromptu Scripts + | 47 | 42 | 30 | 100 |
| Cross System Products (CSP) + | 20 | 18 | 10 | 38 |
| Cool:Gen/IEF \* | 32 | 24 | 10 | 82 |
| Datastage | 71 | 65 | 31 | 157 |
| Excel \* | 209 | 191 | 131 | 315 |
| Focus \* | 43 | 45 | 45 | 45 |
| FoxPro | 36 | 35 | 34 | 38 |
| HTML \* | 34 | 40 | 14 | 48 |
| J2EE \* | 46 | 49 | 15 | 67 |
| Java \* | 53 | 53 | 14 | 134 |
| JavaScript \* | 47 | 53 | 31 | 63 |
| JCL \* | 62 | 48 | 25 | 221 |
| LINC II | 29 | 30 | 22 | 38 |
| Lotus Notes \* | 23 | 21 | 19 | 40 |
| Natural \* | 40 | 34 | 34 | 53 |
| .NET \* | 57 | 60 | 53 | 60 |
| Oracle \* | 37 | 40 | 17 | 60 |
| PACBASE \* | 35 | 32 | 22 | 60 |
| Perl \* | 24 | 15 | 15 | 60 |
| PL/I \* | 64 | 80 | 16 | 80 |
| PL/SQL \* | 37 | 35 | 13 | 60 |
| Powerbuilder \* | 26 | 28 | 7 | 40 |
| REXX \* | 77 | 80 | 50 | 80 |
| Sabretalk \* | 70 | 66 | 45 | 109 |
| SAS \* | 38 | 37 | 22 | 55 |
| Siebel \* | 59 | 60 | 51 | 60 |
| SLOGAN \* | 75 | 75 | 74 | 75 |
| SQL \* | 21 | 21 | 13 | 37 |
| VB.NET \* | 52 | 60 | 26 | 60 |
| Visual Basic \* | 42 | 44 | 20 | 60 |

*(Rows ABAP (SAP) through HTML are on page 2; J2EE through Visual Basic are on page 3.)*

## Page 4

## More Information on Using Gearing Factors

**What is a gearing factor?** The gearing factor is simply the average number of new plus modified (Effective) Source Lines of Code per function point in the completed project. Gearing factors are calculated by dividing the effective code count for a completed project by the final function point count. SLOC counts represent logical, not physical line counts.

**What if the language I am using is not in the table?** If you do not see the language you need in the table, you may substitute a gearing factor from a comparable language. The uncertainty range for the estimated gearing factor may be increased to allow for any additional risk introduced by using a substitute. You may also contact QSM *(link)* to see if revised information is available.

**Should I use the average or the median?** In a perfectly symmetrical distribution of gearing factors, the average and the median will be identical or very close. The average is obtained by summing the gearing factors and then dividing by the number of gearing factors included in that sum. Although its purpose is to measure "central tendency", the average can be pulled up or down by extreme data values (or outliers). The median, on the other hand, is simply the data point that lies in the center of an ordered list of gearing factors. One half of the data points will lie above (and one half below) the median. When the data set is skewed (biased either toward the high or low end by extreme data values), the median may be a more accurate indicator of the central tendency.

**How should I use the range?** The range simply shows lowest and highest gearing factors for each language. The range can be combined with the average and median, to choose a "most likely" gearing factor for estimation. The range can be useful as a starting point for choosing an uncertainty range around your "most likely" estimate of the gearing factor.

**Where does the data come from?** The gearing factors in this table were drawn from 2192 recently completed function point projects in the QSM database *(link)*. As mixed-language projects are not a reliable source of gearing factors, only single-language projects are used.

## Page 5

**QSM offers Function Point Analysis Consulting Services *(link)*. Contact us *(link)* for more information.**

## Recommended Resources

*(Three resource cards:)*

- **An Analysis of Function Point Trends** — An in-depth analysis of completed projects in the QSM software project database using function points to track trends in productivity, schedule, and staffing since 2000. *Read article →*
- **Simplified Function Point Analysis (SiFP)** — The IFPUG standards for counting function points provide your business with a reliable, efficient, and accurate software project size estimation method. *Read blog post →*
- **Counting Function Points for Agile / Iterative Software Development** — This article highlights the importance of consistent terminology, and the application of rules, in creating consistent Function Point counts across a variety of development projects. *Read article →*
