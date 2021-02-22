+++
date = "22 Feb 2021"
draft = false
title = "Week 3"
slug = "week3"
+++

16/18 February  

**Lead: Team 2**

**Reading assignment:** (for everyone)

- Ruha Benjamin, [_Race After Technology_](https://www.ruhabenjamin.com/race-after-technology), Chapters 2 and 3.
- Julia Angwin, Jeff Larson, Surya Mattu and Lauren Kirchner, [_Machine Bias (Risk Assessments in Criminal Sentencing)_](https://www.propublica.org/article/machine-bias-risk-assessments-in-criminal-sentencing), ProPublica, 23 May 2016.

Optional additional readings:
- Cynthia Rudin. [_Stop explaining black box machine learning models for high stakes decisions and use interpretable models instead_](https://csethics.github.io/docs/rudin2019.pdf). Nature, May 2019.
- Cynthia Rudin, Caroline Wang, and Beau Coker. [_The Age of Secrecy and Unfairness in Recidivism Prediction_](https://hdsr.mitpress.mit.edu/pub/7z10o269/release/4), Harvard Data Science Review, 2020.

Response assignments for **Team 3** and **Team 5**: By **1:59pm** on **Monday, 15 February** (note the slightly extended deadline from the usual Sunday evening response to avoid having a deadline on Valentine's Day), post a response to the
_Race After Technology_ (RAT) reading and the ProPublica article that does at least one of these options:

1. Briefly explain the findings of the ProPublica article and how it ties into Benjamin's discussion of default discrimination. How can developers avoid creating algorithms such as this recidivism risk scores assessment? Discuss how you might approach this issue as a developer informed by the two readings.
2. Respond to something in one of the readings that you found interesting or surprising.
3. Identify something in one of the readings that you disagree with, and explain why.
4. Respond constructively to something someone else posted.

Response assignments for **Team 1** and **Team 4**: By **10:59pm** on **Monday, 15 February**, post a response to the readings that either (1) responds constructively to one of the initial postings, or (2) does any of the options above, but without duplicating points that were already made.

# Class Meetings

**Lead by Team 2**

[Slides for Week 3 [PDF]](https://www.dropbox.com/s/v21v7lnn5inrn26/week3-updated.pdf?dl=0)

# Blog Summary

**Written by Team 5**

## Tuesday’s Class 

We began Tuesday’s class with a warm up discussion at each table about
the following questions: What is the difference between institutional
racism and individual racism? Is one more harmful than the others? How
does technology support/propagate both?

Our discussions found that institutional racism reaches more people on
a bigger scale but often is limited by legal boundaries and pushback
from within the society. Individual racism, on the other hand, can be
more targeted and often is experienced more acutely by
individuals. Technology has supported institutional racism by enabling
data collection that help institutions in making more effective racist
policies. Social media as a piece of technology has also propagated
individual racism by allowing racist trolls to have a voice in society
and go after individuals that they would not be able to in real life.

We then went into discussion groups to talk about the dilemma
companies face to bring products to market quickly and testing
properly.  We discussed issues such as Google not being able to
recognize darker-colored faces as well as lighter-colored ones.
Students raised the point that population demographics are important
considerations when testing their product.

Smaller companies are often targeting a smaller subset of the
population whereas large companies are aiming for a bigger market
should ensure its testing and data collection match up to
reality. There is also an economic cost for collecting a larger
dataset, which is a price that not every company can pay. No
company/project has an unlimited budget. There are times when we have
to decide whether to sidetrack the entire development trajectory in
pursuit of inclusivity. Companies are profit-driven so it becomes a
matter of aligning financial interest with anti-racism
interests.

Voice technology presents a similar dilemma as facial recognition
technology, since American English is typically treated as the
standard that is accepted whereas accents and other languages are
often accounted for as afterthoughts. Here, the costs of training
voice assistants to support multiple languages and ways of speaking
are clearly high, and even large companies have not done this (and
there does not seem to be any public outrage about it, compared to
what has happened with face recognition).

We then discussed in groups the issues of using ML and AI in a use
case with paramount importance such as criminal justice.  We all
generally agreed that the Machine bias article is more technical than
RAT. A lot of technical mistakes were made, which begs the question of
what kind of engineering process took place. Criminal justice is also
still a context where it is important that humans are responsible for
decisions, and human judgment and justification cannot be replaced by
algorithms.


## Thursday’s Class

We began Thursdays class with a discussion on the homework assignment:
examples of “glitches” of varying intentionality from the book or
elsewhere. Examples included Google correlating images of Black people
with gorillas, which was discussed to not stem from malicious intent,
but rather a lack of holistic testing, similarly to Twitter’s images
consistently focusing on subjects with lighter skin. Additionally, the
innovation of Polaroid pictures and facial recognition AI in order to
improve surveillance of Black citizens in Apartheid South Africa and
China exemplify development as the result of malicious intent.

We reviewed optional reading number one: “Stop explaining black box
machine learning models for high stakes decisions and use
interpretable models instead” by Cynthia Rudin. Here are a couple of
points from the reading we went over:

- Black Box Machine Learning Models which give the power to the computer to make decisions/connect variables and other factors in their decision making that are not necessarily readable by humans vs interpretable models.
- Argument: Interpretable models should be used instead of trying to explain the decision making process of the black-box model. Interpretable models can be difficult to develop, but the pros can outweigh the uncertainty within the black-box models.
- It can be difficult to reduce black-box models into 3-5 simple rules, but in some cases, a few simple rules can perform as well as a complex black-box model.
  - CORELS was an interpretable machine learning model that reduced COMPAS model to three simple rules that produced the same scores
  
- Black box models find hidden patterns within these calculations, and if we want to move forward with interpretable models, we need to make sure they are also finding these.
- Some issues with black box models are that they combine variables in ways humans do not understand and explanations for these models are often unreliable and misleading.
 
Then, in groups, we created an interpretable model for determining
whether an incoming first year student will become a CS major. Common
parameters included whether or not the student had prior exposure
through courses in high school such as AP Computer Science or a
relative who is a software engineer. This algorithm could result in
bias due to less affluent students not having access to these courses
or exposure to the field through their family. Other parameters
suggested that the school the student enrolled in was a sufficient
determiner, as transfering from the Nursing school or the A-school is
less likely. A big question about this exercise is about how the model
will be used &mdash; if it would impact the opportunities students
have, certain features that may be useful in predictions would result
in unacceptable biases; if the goal is just to estimate the number of
CS majors in the incoming class, maybe this isn't an issue, and
learning about the factors that impact major decisions could be
helpful for a program to reconsider how it is treating students that
might not match the "model's expectations".

It is also important to note that exposure to technology leads to a
bias due to the digital divide between those without access to
computers, and the current demographics or culture of CS may lead to
further discouragement of those without exposure to the field or in
marginalized communities. It is important to note what the model is
being used for, as some use cases may lead to worse outcomes with
bias. For example, using the algorithm to encourage student enrollment
would escalate the biases, but using the algorithm to determine where
enrollment is lacking would decrease the biases.


We reviewed optional reading number two: “The Age of Secrecy and
Unfairness in Recidivism Prediction” Here are a couple of points from
the reading we went over:

- Argument: “The focus on the question of fairness is misplaced, as these algorithms fail to meet a more important and yet readily obtainable goal: transparency”
- ProPublica had a flawed analysis that claimed the proprietary prediction model COMPAS is racially biased
- Lack of transparency allows errors to “propagate and results in damage to society”
- Findings from this: 
  - Reconstructed COMPAS model for Broward County to study
  - The model “does not seem to depend linearly on the defendant’s age despite statements to the contrary by the creator”
  - Found that COMPAS scores performed equally well with or without direct knowledge of race: contradicts ProPublica’s claim
- Examples of bias:
  - Bryan Row given a COMPAS violent score of 1 despite history including trafficking cocaine and battery of a pregnant woman
  - Glenn Rodriguez: denied parole bc of miscalculated COMPAS score due to human error

We then in groups discussed the importance of transparency and the
outcome of an algorithm. Some groups explained that there is little
incentive for companies to be transparent due to the profitability of
complex, black boxed algorithms. Other groups added that transparency
alone may not lead to change if the algorithms are not critiqued by
the public, emphasizing that developers need to use transparency to
investigate bias. Lastly, transparency alone is not sufficient: a
transparent model may incorporate bias, and the process to produce the
model may be biased. Just because a model appears to be "fair",
doesn't mean it is, and fairness tests may be able to identify biases
not obvious in a transparent model.

