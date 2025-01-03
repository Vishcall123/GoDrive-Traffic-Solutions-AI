# GoDrive-Traffic-Solutions-AI
GoDrive is a prototype mobile application and AI developed to diminish the time spent waiting in interseciton-based-traffic.

**Problem**

Traffic in metropolitan Atlanta is an overwhelmingly large problem for many commuters. The average driver in Atlanta spends almost 77 hours each year in traffic, dimninishing from productive time they could be spending. On average, commutes are almost 39 minutes, and in suburban areas, much of this is caused by intersection-based traffic. Traffic at intersection continues for hundreds of cars in some locations, resulting in many drivers spending hours behind traffic lines. Intersections currently operate on time intervals - this project aimed to demonstrate a proof of concept of a more optimized neural network approach which could take over the timed intersections to create a more efficient solution to traffic.

**Methodology**

In the SurveyCreator.py file, using the PIL library, intersections with a set number of pedestrians and cars were programatically created with the intent of gaining testing situations to be evaluated and stored as training data. These surveys were exported and sent to various experienced engineers, who completed the surveys by indicating which lane of traffic should be allowed to pass. With the 400 data points procured through this survey, the Neural Network was trained and tested using PyTorch, obtaining an almost 80% accuracy.

**Results**

With this, the model was tested against a timing based model in the roadsim.py and pygamesim.py files, using the pygame library. Using a base intersection created programatically by the PIL library (shown as intersection.png), both the Neural Network and the timing-based model(s) were run against each other. In all situations but one, the Neural Network outperformed the timing-based model to clear the intersection faster by 8% on average (graph below).

![Neural Network vs  Timing Traffic Model  (1)](https://github.com/user-attachments/assets/08a2a536-991c-449a-8d82-4eaec5ade120)

With an 8% decrease in traffic times to clear an intersection, the time of commuting can be brought down by almost an hour for the average commuter in the suburbs. This decrease, while seemingly trivial, could represent a large decrease in emissions and an increase in productivity time for workers.

These data indicate that the future of traffic may lie in the realm of AI.
