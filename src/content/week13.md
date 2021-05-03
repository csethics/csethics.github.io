+++
date = "04 Feb 2021"
draft = false
title = "Week 13"
slug = "week13"
+++

## Week 13: End-to-end Encryption

Lead: **Team 5**  
Blog: **Team 3**

**Required Readings and Viewings** (for everyone): 

-  Harold Abelson, Ross Anderson, Steven M. Bellovin, Josh Benaloh, Matt Blaze, Whitfield Diffie, John Gilmore, Matthew Green, Susan Landau, Peter G. Neumann, Ronald L. Rivest, Jeffrey I. Schiller, Bruce Schneier, Michael A. Specter, Daniel J. Weitzner. [_Keys under doormats: mandating insecurity by requiring government access to all data and communications_](https://academic.oup.com/cybersecurity/article/1/1/69/2367066). Journal of Cybersecurity. November 2015. [[Web Version](https://academic.oup.com/cybersecurity/article/1/1/69/2367066)] [[PDF](https://csethics.github.io/docs/doormats.pdf)]

- Matt Green. [_Can end-to-end encrypted systems detect child sexual abuse imagery?_](https://blog.cryptographyengineering.com/2019/12/08/on-client-side-media-scanning/). December 2019.

- Department of Justice, [_International Statement: End-To-End Encryption and Public Safety_](https://www.justice.gov/opa/pr/international-statement-end-end-encryption-and-public-safety). 11 October 2020.

**Optional Additional Readings**
- Jon Brodkin, [_Apple cut backup end-to-end encryption plans after FBI complained_](https://arstechnica.com/tech-policy/2020/01/apple-reportedly-nixed-plan-for-end-to-end-encryption-in-iphone-backups/). Ars Technica, January 2020.
- Bill Goodwin, [_Government puts Facebook under pressure to stop end-to-end encryption over child abuse risks_](https://www.computerweekly.com/news/252499496/Government-puts-Facebook-under-pressure-to-stop-end-to-end-encryption). Computer Weekly, 18 April 2021.
- Jack Karsten, [_Alternative Perspectives on Encryption_](https://www.brookings.edu/blog/techtank/2016/05/12/alternative-perspectives-on-encryption/). Brookings. May 2016.
- Matt Blaze, [Testimony to House Committee Hearing on _Deciphering the Debate over Encryption_](https://docs.house.gov/meetings/IF/IF02/20160419/104812/HHRG-114-IF02-Wstate-BlazeM-20160419-U3.pdf), April 2016.

**Response prompts:**  
Post a response to the readings that does at least one of these options by **10:59pm** on **Sunday, 25 April** (Team 2 and Team 4) or **5:59pm** on **Monday, 26 April** (Team 1 and Team 3):

Post a response to the readings that does at least one of these options:

1. Do you believe public safety can be protected without compromising privacy or cyber security?
2. Is end-to-end encryption beneficial to protect personal privacy, or is there too much risk if law enforcement has no access to communications?
3. Respond to something in one of the readings/ videos that you found interesting or surprising.
4. Identify something in one of the readings/ videos that you disagree with or are skeptical about, and explain why.
5. Respond constructively to something someone else posted.

# Discussion

[Week 13: End-to-end Encryption](https://github.com/csethics/csethics.github.io/discussions/39)

# Blog Summary

**Team 3**

### Tuesday, 27 April

We started week 13 discussing encryption and the challenges that
end-to-end (E2E) encryption poses on societal safety and security. E2E
encryption is defined as the process of data being transmitted in an
encrypted form to another device where only that second device is able
to decrypt it. In the intermediary transmission process, no outsider
can see exactly what was sent. However, E2E encryption is not perfect;
if the decryption key is compromised, so is the message.

On Tuesday, one of the first discussions we had was questioning what
role the government has in providing security for people while
preserving their citizens' privacy. Some proposed solutions in this
week’s reading discussed topics such as allowing the government to
require encryption keys or backdoors where government agencies are
able to access suspected bad actors’ hardware. Many issues abound in
our discussion - for example, what happens if the government gets
hacked? Given the history of the vulnerabilities within the government
and other companies demonstrate that if a backdoor exists it may be
accessed by those who should not have access. This topic urges us to
consider the tradeoff between the risks E2E encryption poses to
national security and the risks associated with creating
vulnerabilities in our technology.

We also discussed some of the possible risks that policymakers may
have overlooked in the demand for exceptional access, as it sets a
precedent of overriding security protocols. These protocols exist to
protect societies’ civil liberties and privacy. We also explored
possible ways that the government could have exceptional access
without negatively impacting the open nature of the internet. As it
was noted, many tech companies already have built-in backdoors in
their technology for various reasons, such as updates. However, would
requiring more access create too high of a barrier to entry that it
would prevent entrepreneurial pursuits from coming to fruition?

In [one of the readings](https://www.justice.gov/opa/pr/international-statement-end-end-encryption-and-public-safety), the Department of Justice (DOJ)
supported strong encryption because of its crucial role in ensuring
personal data, privacy, intellectual property, trade secrets, and
cybersecurity. The DOJ frequently works with tech companies to embed
public safety into system designs and engages with legal experts
regarding design decisions. However, E2E encryption poses challenges
by undermining companies’ ability to identify and create the
appropriate response to violations of their terms of service. This
includes issues such as child exploitation, violent crimes, and
radicalization. As a result, many of our discussions this week were
centered on whether or not public safety and privacy can coexist. As
we noted, there will always be a trade-off between privacy and safety
because increased privacy can lead to possible crises and threats to
public safety, while more safety can sometimes only be achieved with a
loss of personal privacy. This is a trade-off that differs depending
on what perspective someone is viewing a problem from and might be
more focused on safeguards to their privacy. However, tech companies
arguably only care about the bottom line in the end, which may or may
not be aligned with privacy ideals.

A few possible solutions were discussed such as only allowing E2E
encryption on private messaging systems as opposed to all social media
platforms. Another idea was that E2E encryption should only be used if
everyone in the subspaces of that platform is an adult so that any
activity involving minors can be easily moderated. However, even in
these cases, the solutions are only very specific to certain scenarios
it is challenging to safeguard in a generalized way against threats to
public safety such as violence, exploitation of minors and other
vulnerable populations, and other illegal activities.

We then discussed a specific case of encrypted devices with the debate
of security versus privacy in the Apple iPhone case following the San
Bernardino shooting. In 2016, Apple refused to bypass the self-wipe
mechanism for the FBI after they requested their assistance in
obtaining evidence in the investigation after the tragedy. Apple
declined to cooperate with the FBI because the company didn’t want to
set a precedent of giving up private data. Because Apple took a stand
in supporting their user’s privacy rights, Apple in this case had
similar interests in protecting privacy as everyday users. In 2018,
Apple created a plan for E2E encryption for all iPhone backups but
ceded to the FBI after the agency lodged a complaint against
them. Nowadays, only certain Apple services have E2E encryption, where
some data can still be decrypted for law enforcement when deemed
necessary by the government.

## Thursday 29 April

On Thursday, we discussed former Attorney General William Barr’s open
letter to Facebook, which called for companies to work with law
enforcement to design systems that would allow them access when
needed. Barr argued that E2E encryption protects criminals and impedes
law enforcement’s ability to protect public safety and national
security. The related discussion question asked if there is a way to
implement these techniques while preserving the security of end-to-end
encryption. For the most part, groups agreed that allowing exceptional
access to the government would inherently create vulnerabilities and
make such systems more susceptible to hacking. We also talked about
the use of image scanning systems meant to detect child sexual abuse
imagery (CSAI) and discussed whether this process could be subject to
abuse. The class agreed that image scanning would require a lot of
trust in the creators of the algorithm, since there’s no way to prove
that it is without fault, and it relies on individuals not knowing how
it works so that it can’t be fooled by criminals. It was also
mentioned that there isn’t much of a legal remedy if an image is found
to be illegal since, under E2E encryption, it would not be possible to
access the plaintext image.

Next, an overview of the Brookings article, [_Alternative Perspectives
on
Encryption_](https://www.brookings.edu/blog/techtank/2016/05/12/alternative-perspectives-on-encryption/),
was given. In this article, four experts gave their views on E2E
encryption. The first was Niam Yaraghi, who compared online spaces to
private homes, in that online spaces should have a way to break the
front door lock. Yaraghi argues that encryption methods that do not
allow government access are a threat, stating that “unbreakable locks
do not ensure privacy, they create chaos.” We talked about this
viewpoint and the comparison between online spaces and homes. One
group called it a false comparison, since going into an online space
gives the person being searched very little awareness of the
situation, whereas in a home you can see everything that’s going on
and know that your property is being searched.

Another group also worried that the bar to obtain a warrant to search
an online space would be a lot lower due to the fact that it’s much
easier to use a backdoor than to physically go into someone’s
home. The next expert was Scott Andes, who argued that backdoors in
software affect competitiveness, since compromising privacy reflects
poorly on companies. This led to a discussion on whether a company’s
competitiveness should be factored into conversations regarding the
regulation of encryption. The third expert was Walter Valdivia, who
asserted that users don’t expect all-or-nothing privacy and that a
balance can be found. Valdivia supported layered encryption designed
with government officials, which aligned with the previously-discussed
Department of Justice viewpoint. The last expert, Darrell West, was
against backdoor access for law enforcement. He argued that it would
create a risky precedent globally, especially in countries that are
disposed to surveilling and censoring their citizens.

Group 5 posed the question of whether the global precedent should be
considered when making national laws. Several classmates agreed that
the U.S. may not hold the same weight that it used to when it comes to
setting global legal precedents, but the class seemed split on how
other nations might respond to increasing governmental oversight on
communications.
	
This week’s topic concluded with three final discussion questions:

- Should the government not be or be precluded from accessing content in order to preserve national security? What should be the extent?

- How have the discussions this week impacted your stance on the benefits and drawbacks of end-to-end encryption? Do you feel the same as before?

- Given the articles we have read, do you think that the pros of end-to-end encryption outweigh the cons or vice versa? Why or why not?

Most students agreed that the readings and discussions on E2E
encryption were thought-provoking and made them question their
preliminary views, or at least increased their understanding of the
different perspectives on the topic. There are strong arguments for
both sides and many expressed their wish to find a middle ground that
maintains privacy without threatening security.



