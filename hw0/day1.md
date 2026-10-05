# Day 1 "before" snapshot

Write your own, even if you worked in a pair. Keep it: we come back to it at mid-quarter (Week 6) and at the end (Week 11). Your prompts go in `ai_log.md`, not here.

**Name:** Solomiia Kleban
**Partner (if any):**

## Before we prompted

### 1. Who is it for, and what do they want to do?

It's for people/students who want to do historical research about how in different centuries people perceived and represented animals through artwork. 

**"The user can..." sentences:**
1. The user can type the specific animal and year they want the artwork to be from into the search bar. Afterward, they will see animal art and move through it using the next and previous buttons. 

2. They can also type an animal and just move the cursor on the timeline to choose the specific year they want to make research, without typing it on the search bar. 

### 2. Our sketch

Put the photo in this `hw0` folder, then change the filename below to match:

![sketch](sketch.jpg)

### 3. Our prediction

We expected the app would  look like a sketch, with the art pictures, the timeline, and the search bar that moves right and left to show the year requested in the search bar.

## What we got

### 4. What the AI made

Put the screenshot in this `hw0` folder, then change the filename below to match:

![screenshot](screenshot.png) 

### 5. Sketch vs. app

- **Matches our sketch:**
After running, AI matched the search bar, mostly the timeline, and the next and previous buttons. 
- **Different from our sketch:**
Claude made the search bar too long and used a grid background. It also didn't include artwork.
- **The AI decided** (something we never said): AI decided to add the line “Type an animal to begin, for example, horse, owl, or lion.” instead of the art, or at least an art space to imitate it. But I suppose that AI thought that the artwork would be shown after a person searches for the specific animal. And also AI added the cancelation button near the search bar that we never asked for.


### 6. What did I keep, change, or reject, and why?
I kept the title and the caption under the artwork because they fit my app. Also, I added the artwork space, changed the size of the search bar, and used different colors, such as nude with brown, and dark red. I moved everything toward the center of the app page, moved the timeline and the artwork space more down, and rejected the grid background. I think that all these changes made the app look closer to the main idea and a sketch.


### 7. Explain back

Pick one part of the code. In your own words, what does it do?

$('prev').onclick = () => step(-1);
$('next').onclick = () => step(1);

I think that this part allows the user to click the previous and next buttons next to the artwork to change the art. step(-1) means to move back by one artwork, and step(1) means to move forward.

## Looking ahead

### 8. What does it do? Does it work? What broke?
The app helps students to fine a specific animal artwork by year of creation, so it is easier to find art and make a history research. However, the app doesn't show the artwork after typing an animal, but only the text "Could not reach the museum API (Failed to fetch). Open this file in your browser with internet on and try again." The only thing that works is the year and a timeline. After typing a year, the cursor on it will move to the right year. I think that Au couldn't connect the API correctly, so it doesn't work as intended. 


### 9. How much do I understand about how it works? (0–100%)

**My number:**
70%

**Why that number:**
I understand how the app suppose to work but I still need to understnad more about the code behind it, so I feel more confident about correcting what AI made or making better predictions about my future apps. 


### 10. What would I need to know to tell whether it's *well designed or well built*?
To tell whether it is well designed, I  need to actually see someone using my app and giving me feedback. To tell whether it is well built, I need to gain a better understanding of reading a code and how API works.


### 11. What do I hope to be able to do by week 10?
I hope to be able to make presentable and suitable apps for users. I also hope to gain more experience in reading and tracing code to make apps that work and don't break.

