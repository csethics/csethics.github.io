+++
date = "04 Feb 2021"
draft = false
title = "Week 2: Race After Technology"
author = "David Evans"
slug = "week2"
+++

## Readings

- Ruha Benjamin, [_Race After Technology_](https://www.ruhabenjamin.com/race-after-technology), Introduction and Chapter 1 
- John McWhorter, [_'Racist' Technology Is a Bug—Not a Crime_](https://time.com/4475627/is-technology-capable-of-being-racist/), Time Magazine, 12 September 2016

Optional additional readings:

- Aylin Caliskan, Joanna J. Bryson, Arvind Narayanan. [_Semantics derived automatically from language corpora contain human-like biases_](/docs/caliskan-language-biases.pdf), Science, 14 April 2017.
- Latanya Sweeney. [_Discrimination in Online Ad Delivery_](/docs/sweeney-discrimination-ads.pdf), ACM Queue, 2013.

**[On-Line Discussion](https://github.com/csethics/csethics.github.io/discussions/8)**

# Class Meetings

**Lead by Team 1**

[Slides for Week 2 [PDF]](https://www.dropbox.com/s/cmobu905e0yer28/week2-updated.pdf?dl=0)

# Blog Summary

**Written by Team 4**

Tuesday's class began with a discussion about names, inspired by Ruha
Benjamin's own "What's in a Name?" game which she plays with her
undergraduate students at Princeton. In their table groups, students
discussed the backgrounds and assumptions in a name &mdash; chosen or
imposed &mdash; in sharing the story behind their own name.

Our discussions found that some students with immigrant parents were
given common American-English names (often inspired by popular
musicians and actors), instead of names in other cultures and
languages like their parents. Several students reported that this was
intentional on their parents' parts in order to help their children
better fit into American society and make it easier for other people
to say their name. This exemplified the point Benjamin made in Chapter
1 of her book in describing how common white-sounding names are
considered the standard in the U.S.

Next, the class turned to the debate around free will and the
influence of algorithms on our decisions and behaviors. Students
centered discussion around Benjamin’s quote “The road to inequity is
paved with technical fixes.”

We discussed how Amazon, Facebook, Netflix, Spotify, YouTube, etc. all
recommend specific content (products, posts, tv shows, movies, music)
to users based on the data collected from them— only showing specific
content to people on these large platforms. As a result, it is made
harder to have “free will” to seek out specific content that is not
recommended for you by algorithms. This can lead to “echo chambers”
where users live in their own reverberating bubble of information, and
can lead people down radical political paths.

Another aspect of this discussion was acknowledging that small
“technical fixes” often only mask problems such as racism and gender
inequality by hiding it in the technology we use while not necessarily
addressing these issues in society. For example, sentencing algorithms
used to determine length of jail sentences (which we'll talk more
about in [Week 3](/week3)) and other legal criminal decisions in
court.

These sentencing algorithms often give the appearance of placing
sentences into unbiased hands because they take the decision away from
a judge, who can be seen as fallible or biased, and hands it to an
algorithm that is meant to not take into account race or other
identifiers that could lead to discrimination. The issue is, however,
that these algorithms then use factors associated heavily with race,
such as past criminal history, socioeconomic status, crime rates in a
person’s home area, to determine sentencing. The results are often
just as discriminatory as we’d expect from human decisions, in which
POC are sentenced to far longer prison stays than white people who
have committed comparable crimes.

Next, the class tackled the larger question of what technology is
truly racist and how we can determine between racism in tech and
advancements that have merely gone awry. Students began with an
example of the Twitter algorithm which crops photos attached to
tweets. The algorithm used to search for high contrast colors in
pictures to decide what portion of a photo to preview. This caused
pictures containing people of different races to be constantly cropped
to show the white person instead of a POC who is also in the
photo. Once Twitter became aware of this trend in its algorithm, it changed
it’s system to be a standard crop for all photos.

Another example of a case where it’s hard to determine responsibility
and intent behind racist outcomes in tech was Microsoft
TayTweets. TayTweets was the first bot of its kind launched on Twitter
as an experiment to see if AI could learn to interact on social media
like a real person. It’s design, however, left room for some
mistakes. Within a day or two of it’s launch, TayTweets was targeted
by trolls who taught it racist and bigoted phrases, and TayTweets
began repeating and using those phrases. (See James Mickens' [keynote
talk at USENIX Security 2018](https://youtu.be/ajGX7odA87k?t=1184) for
a entertaining summary of this unfortunate episode.)

During this discussion, some made an argument that since Microsoft had
good intentions in launching this new technology, and didn’t predict
the racist outcome, it’s really the companies that have followed and
created similar bots after seeing TayTweets’ poor outcome who should
be held accountable as they aren’t learning from racist mistakes and
taking actions to avoid them.

## Thursday's Class

Before the second class period, students were tasked with completing
an Implicit Association Test and finding a search query that displayed
bias in the results. Some groups argued that the measurement of speed
in the test results judged reaction time more than actual implicit
bias. Most of the group realized that they had a slight bias for one
or the other ethnicity, and discussed methods for taking into account
their own implicit bias, especially within technology. Some groups
came to the consensus that having ethnically diverse teams limits
implicit bias namely in the production of technology.

In group discussions on the second homework question, some students
discussed how it was very hard to find a specific query that displayed
bias. Several students thought that when searching “school children”,
the image results forced specific ethnic representation in the
results. In other words, it seemed that the search engine was
protecting its image by adding representation. Furthermore, students
wondered if changing geographic location to a low socioeconomic area
produces different results than a more affluent area.

The class then moved into discussing the optional readings. Key
mentions here were word embedding and its reflection of bias,
discrimination in ad delivery, good training data, quantifying bias
through sentiment analysis, and whether or not the developer has
responsibility to over correct social bias as opposed to simply being
aware and not reinforcing it. Some students reached a consensus that
it is not the role of software developers to over-correct for societal
biases, but rather to be aware and stop using a technology when it
does perpetuate it.
