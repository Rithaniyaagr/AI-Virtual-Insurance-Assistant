AI-Powered Virtual Insurance Assistant for Gig Delivery Workers
1. Delivery Workers We Chose
Our project focuses on food delivery workers, especially those working for platforms like Swiggy and Zomato. These workers are part of India's gig economy and depend on daily deliveries for their income. However, their earnings are highly affected by external conditions such as weather, pollution, or emergencies.
________________________________________
2. The Problem They Face
Delivery partners face several challenges that affect their income and safety:
•	Heavy rain or storms make deliveries dangerous or impossible.
•	Severe air pollution (high AQI) can harm their health if they work outdoors.
•	Natural disasters or government restrictions can stop deliveries completely.
•	When such events happen, delivery workers lose their daily earnings because they cannot work.
Currently, most gig workers do not have simple and affordable insurance protection for these unexpected situations.
________________________________________
3. Our Solution
We propose an AI-powered Intelligent Virtual Insurance Assistant (Chatbot) designed specifically for gig delivery workers.
The system will provide micro-insurance services where workers can subscribe to a low-cost insurance plan. The chatbot will help workers:
•	Understand insurance policies in simple language
•	Check coverage details
•	Track claim status
•	Receive alerts when risky conditions are expected
•	Automatically receive payouts when certain conditions occur
The assistant will be available through a mobile/web interface so workers can interact using natural language.
Example interaction:
Worker:
"Will I get insurance if it rains heavily today?"
AI Assistant:
"If rainfall exceeds 80 mm in your city, you will automatically receive a payout of ₹300."
This makes insurance easy, transparent, and accessible for gig workers.
________________________________________
4. Weekly Premium
The insurance model will follow a small weekly subscription system.
Example:
•	Delivery workers pay ₹30 per week as a premium.
•	The AI system dynamically adjusts the premium depending on risk factors such as:
o	Weather forecast
o	Pollution levels
o	Historical delivery disruptions
o	Seasonal risks
This ensures that pricing is fair and affordable for workers.
________________________________________
5. When Payout Happens
The system will use automatic triggers for insurance payouts. When certain real-world conditions are detected, payouts will happen automatically without manual claims.
Example triggers:
•	Rainfall greater than 80 mm
•	AQI greater than 400
•	Cyclone or extreme weather alert
•	Government-announced lockdown or curfew
•	Natural disaster warnings
When these conditions occur, the system automatically transfers compensation to workers.
Example payout:
•	Rainfall > 80 mm → ₹300 payout
•	AQI > 400 → ₹200 payout
•	Government curfew → ₹500 payout
This ensures workers receive support when they cannot work.
________________________________________
6. How AI Will Be Used
Artificial Intelligence will play several roles in the system:
1.	Natural Language Understanding
The chatbot understands user questions about insurance, claims, and payments.
2.	Risk Prediction
AI analyzes weather, pollution, and historical data to predict risky days.
3.	Dynamic Pricing
AI adjusts weekly premium pricing based on predicted risks.
4.	Fraud Detection
AI identifies suspicious claims or abnormal activity.
5.	Automated Assistance
The chatbot provides 24/7 support for workers.
________________________________________
7. Technology We Will Use
We plan to use the following technology stack:
Frontend
•	React.js (Web interface)
Backend
•	Python (Flask / FastAPI)
AI / Chatbot
•	Natural Language Processing (NLP)
•	OpenAI / HuggingFace models
APIs
•	Weather API (for rainfall data)
•	AQI API (for pollution levels)
Database
•	Firebase / MongoDB
Payments (Future Phase)
•	Razorpay test mode
Cloud Deployment
•	AWS / Google Cloud
________________________________________
Future Development (Next Phases)
In future phases, we plan to build:
•	A working chatbot interface
•	AI-based risk prediction model
•	Automatic insurance payout simulation
•	User dashboard for delivery workers
•	Integration with payment gateways
The goal is to create a simple, affordable, and AI-driven insurance system for India's gig economy workers.

 Adversarial Defense & Anti-Spoofing Strategy

 Why we added this
While thinking about real-world usage, we realized that GPS alone is not reliable. There are apps that can fake location, and if many users coordinate, they can trigger false payouts. So we changed our approach — instead of trusting only location, we try to understand the user’s actual situation.


1. How we tell real users and fake ones apart

We don’t just check “where the user is”, we check if their behavior makes sense.

- If someone is really stuck in bad weather, their movement will look natural (slow movement, stops, delays)
- But if someone is spoofing, we may see:
  - no movement at all
  - sudden jumps in location
  - unrealistic speed

We also compare GPS with phone sensors:
- If GPS says the person is moving, but the phone is actually still → something is wrong

We also check weather:
- If user claims heavy rain, we verify with weather data
- We also compare with nearby users to see if others are facing the same condition

Devices using fake GPS apps or modified systems are treated as risky.

 2. What data we look at (not just GPS)

To make better decisions, we use multiple small signals together:

- Phone sensors (accelerometer, gyroscope)
- Network info (IP vs GPS mismatch, signal issues)
- Cell tower location as backup
- Weather API data
- User’s past activity (movement history, claim frequency)

We also try to detect patterns:
- If many users are doing the exact same thing at the same time, it could be a coordinated attempt

 3. Making sure genuine users are not affected

We don’t want honest delivery partners to suffer because of strict checks.

So instead of rejecting claims directly:

- We mark suspicious cases as:
  → “Under Review” (no need for user to worry)

- If network is bad (which is common during heavy weather):
  - we allow some delay
  - we don’t immediately block the claim

- Only if needed, we may ask for simple proof like a photo

Most checks happen in the background without disturbing the user.

Handling group attacks

A single fake claim is easy to manage, but group attacks are more dangerous.

So we monitor:
- multiple users claiming the same thing at the same time
- similar patterns across accounts

If such behavior is detected, the system becomes stricter automatically.



 Final outcome

- Reduces fake claims due to GPS spoofing  
- Protects the system from large losses  
- Still keeps the experience smooth for genuine users  


 In short

GPS can be faked, but consistent behavior is hard to fake.

So our system focuses more on behavior than just location.


