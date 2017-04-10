- PostgreSQL account: tw2579

- URL of webapp: http://35.185.42.95:8111

- Description:

  This database project is designed for people like students and teachers to get a comprehensive 
  and connected knowledge graph, such as math, physics konwledge. The 7 entities of this project 
  are knowledge, events, axiom, theorem, courses, reference and scientists. users can search any 
  keyword with respect to specific entity, and related information will be shown, by searching on
  those related information, the network will get extended.
  
  Concretely, we showed all the information according to an entity at the top of each entity page, 
  and we provide method to search through a relationship according to that entity. If the search 
  result is not empty, we will jump to the new entity page and user can search further. Honestly, 
  user can get any information from database with suitable queries or some combination of queries.
  
  New Feature:
  
  - User can insert new information(course and their relationships) into the Knowledge Graph.
  - We also provided three complicated example which has real world meaning. When encoutering wro
  ng input or there is no matching information in database, an corresponding error message will sh
  ow on the webpage. 


- Interesting Operations:
 
  1. Interesting Queries
  There is a example page containing 3 interesting examples. In example 1 and example 3, users can 
  input according to hints. For all these three queries database will do corresponding complex que
  ries and show interesting results. 
  
  The page is interesting because firstly the query is a complecated query. However, we do not nee
  d to deal with this complexity during coding in python, but simply pass a long string into the 
  database query. Secondly, these three examples have real world understanding and usage. They are 
  queries usefull to user and are meaningful to be answered. 
  
  2. Course Page
  In course page, we have three queries about knowledge, prerequisite and reference according to a 
  specific course. We can also insert new courses and new prerequisite into the database. 
  
  This page is interesting because it covers most interesting operations according to course. When 
  we add a new course, we also need the course to have a specific knowledge it covered. We will re
  turn information of either one or both of them are successful. 
  

