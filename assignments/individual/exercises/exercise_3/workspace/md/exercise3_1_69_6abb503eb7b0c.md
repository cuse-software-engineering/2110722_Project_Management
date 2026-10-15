# Exercise 3: Cost management (function point, COCOMO II, earned value analysis)

2110722 Software Project Management — Exercise semester 1/2569 — 45 points

Submit your answer in a **pdf file**. Name the file by **your name and student ID**. *(Form box: StudentID and Name)*

## (23 points) Function point

For questions 1–5 the form has the same answer table: Which function (EI, EO, EQ, ILF, or EIF)? · What is the number of DETs and what are they? · If counting FTRs is applicable to this function, what is the number of FTRs and what are they? If not, write N/A. · If counting RETs is applicable to this function, what is the number of RETs and what are they? If not, write N/A. · Rating (Low, Average, or High)? · Value?

1. (4 points) A web admin uses data analytic software to collect interaction data per event (or hit such as pageview, button click) when it happens. Collected data in an event table include timestamp, user ID, session ID, page URL, event name etc. At the end of each week, the web admin displays a weekly report showing the activity level by day of the week, i.e. the number of hits, % of total hits, and the number of user sessions. Calculate the function point of this function of the software.

   *(Figure: "Activity Level by Day of the Week" with a Display button, and a report table with columns Day (1 Sun … 7 Sat), Hits, % of Total Hits, User Sessions, plus the rows Total Weekdays 9209 / 80.08% / 964 and Total Weekend 2290 / 19.91% / 232.)*

2. (4 points) The US Census Bureau hosts a web application that allows users to click on a location on the map (e.g. map location of Kansas City) to see some information about that location (i.e. city, state, population, and state coordinate). The US Census Bureau maintains its own state population data and obtains the state coordinate data from the Surveying and Mapping Section of the US Army [กรมแผนที่ทหาร]. Calculate the function point of this function of the application.

   *(Figure: a US map with cities; result text "Kansas City, Missouri: Population 435,146: Location: 39.1 N, 94.5 W".)*

3. (4 points) The Mor Prom [หมอพร้อม] application of the Ministry of Public Health (MOPH) is the government’s health application, first launched to provide the Covid vaccination service. Users provide personal data to register with this application, and the data are kept as part of the user data. Calculate the function point of this function of the application.

   *(Figure: two screenshots of the Mor Prom registration form "ลงทะเบียนผู้ใช้งาน หมอพร้อม" — คำนำหน้าชื่อ title (drop-down), ชื่อ first name, นามสกุล last name, เลขประจำตัวประชาชน national ID, วันที่เกิด/เดือนที่เกิด/ปีที่เกิด birth day/month/year (three drop-downs), เบอร์โทรศัพท์ phone number, เพศ gender (เพศชาย/เพศหญิง buttons); ที่อยู่ address (text area, label added by the lecturer), จังหวัด province, อำเภอ district, ตำบล sub-district (drop-downs), รหัสไปรษณีย์ postcode, เลือกโรงพยาบาล hospital (drop-down), กลุ่มเป้าหมาย target group (greyed out, pre-filled "ประชาชนทั่วไป"), and a บันทึก save button. Clear copies of all figures, taken from the Word version of the form, are in `problem/exercise3_1_69_6abb501a9ff35_media/`.)*

4. (4 points) The Mor Prom [หมอพร้อม] application stores the user data which consist of the user’s personal data, i.e. 15 data fields, and the information about vaccine shots that the user has received, i.e. date of vaccination, vaccine name, vaccine manufacturer, vaccine lot, and vaccination site. Calculate the function point of this function of the application.

5. (4 points) The Mor Prom [หมอพร้อม] application connects to the Organ Donation API of the Thai Red Cross to access users’ organ donation data. The organ donation data are maintained by the Thai Red Cross system and are only referenced by the Mor Prom application. The organ donation data consist of donor information and information about the donated organs. The donor information includes national ID, title, first name, last name, date of birth, occupation, address, tumbol, district, province, postcode, house phone, and mobile phone. For each donated organ, the information includes the donation date, donated organ, and witness name. Calculate the function point of this function of the application.

6. (3 points) Suppose an application has the following number of functions of various sizes.

   | | No. of low | No. of average | No. of high |
   |---|---|---|---|
   | External Input (EI) | 3 | 1 | 0 |
   | External Output (EO) | 1 | 0 | 0 |
   | External Inquiry (EQ) | 2 | 1 | 0 |
   | Internal Logical File (ILF) | 5 | 0 | 0 |
   | External Interface File (EIF) | 1 | 0 | 0 |

   Calculate the unadjusted function points of this application.

   | | Low | Average | High | Total |
   |---|---|---|---|---|
   | External Input (EI) | ……*3 = …… | ……*4 = …… | ……*6 = …… | |
   | External Output (EO) | ……*4 = …… | ……*5 = …… | ……*7 = …… | |
   | External Inquiry (EQ) | ……*3 = …… | ……*4 = …… | ……*6 = …… | |
   | Internal Logical File (ILF) | ……*7 = …… | ……*10 = …… | ……*15 = …… | |
   | External Interface File (EIF) | ……*5 = …… | ……*7 = …… | ……*10 = …… | |
   | | | | Unadjusted FP | |

## (8 points) COCOMO II Post-architecture Model

1. Suppose the application size is 67 function points. If the application is written in Javascript and the average gearing factor is ……, the application size is …… KLOC. (See gearing factor here https://www.qsm.com/resources/function-point-languages-table)

2. Scale Factor (SF) (Rate SF as you see fit.) — table with Rating and Score columns for PREC, FLEX, RESL, TEAM, PMAT and Σ SF.

3. Effort Multipliers (EM) (Rate EM as you see fit.) — table with Rating and Score columns for the product factors (RELY, DATA, CPLX, RUSE, DOCU), platform factors (TIME, STOR, PVOL), personnel factors (ACAP, PCAP, PCON, APEX, PLEX, LTEX), project factors (TOOL, SITE, SCED) and Π EM.

Show how you calculate for the following. (แทนค่าในสมการให้ดูด้วย)

4. E = ……
5. Project effort PM = …… person-months
6. Nominal effort PM_NS = …… person-months
7. Calendar time to develop TDEV is …… months
8. Staff size required to do the amount of work in 5. during the calendar time in 7. is …… persons

## (6 points) Cost estimation

Show your calculations for the following.

Suppose the estimated effort for the project is 5 person-months. The project has a fixed number of staff that will be working on the project and agile methodology (Scrum) is used. The distribution of the project effort on different project activities and on different sprint activities is shown in the table below.

| Project Activity | % of Project Effort PM | Sprint Activity | % of Sprint Effort |
|---|---|---|---|
| Management | 10% | | |
| Analysis | 10% | | |
| Sprint 1 | 20% | Analysis / Design / Implementation / Testing / Management | 5 / 15 / 50 / 20 / 10 |
| Sprint 2 | 20% | Analysis / Design / Implementation / Testing / Management | 5 / 15 / 50 / 20 / 10 |
| Sprint 3 | 20% | Analysis / Design / Implementation / Testing / Management | 5 / 15 / 50 / 20 / 10 |
| Sprint 4 | 20% | Analysis / Design / Implementation / Testing / Management | 5 / 15 / 50 / 20 / 10 |

In the table below, show how to calculate % of project effort of each project activity, activity effort in person-months, activity labor cost, and total project labor cost. (แสดงการคำนวณให้ดูด้วย)

| Project Activity | % of Project Effort PM | Activity Effort (Person-Months) | Average Activity Labor Cost Per Person-Month (THB) | Activity Labor Cost (THB) |
|---|---|---|---|---|
| Management | | | 90,000 | |
| Analysis | | | 50,000 | |
| Design | | | 50,000 | |
| Implementation | | | 30,000 | |
| Testing | | | 30,000 | |
| Total Project Labor Cost | | | | |

## (8 points) Earned Value Analysis

Assume we are through the second month of a one-year project that has a total budget of 1,200,000 bahts. The amount budgeted for the first two months is 230,000 bahts, but the work that has been finished in these two months is worth 200,000 bahts of the budget. The actual cost for the first two months is 250,000 bahts. (แสดงการคำนวณให้ดูด้วย)

Budget at completion (BAC) = …… · Planned Value (PV) = …… · Earned Value (EV) = …… · Actual Cost (AC) = …… · Cost Variance (CV) = …… · Schedule Variance (SV) = …… · Cost Performance Index (CPI) = …… · Schedule Performance Index (SPI) = …… · Estimate at completion (EAC) = …… · Estimated time to complete = …… · Estimated to complete (ETC) = …… · To complete the project with the original budget, To-complete performance index (TCPI) = ……

1. Considering the Cost Performance Index (CPI) and Schedule Performance Index (SPI), how is the project doing?
   - [ ] under budget  - [ ] on budget  - [ ] over budget
   - [ ] ahead of schedule  - [ ] on schedule  - [ ] behind schedule
2. If the team continues to perform at the current cost efficiency, the cost of completing the project would be ……
3. If the team continues to perform at the current schedule efficiency, the time of completing the project would be ……
4. Considering the To-complete performance index (TCPI), is the original budget reasonable for completing the project? Why? ……
