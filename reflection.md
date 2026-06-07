# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
  The game looked clean, with no immediately visible bugs. The UI was very straight forward. If you guessed the correct number, then you knew once you hit it.
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").
  The hints were displaying the opposite of what they were supposed to. i.e. Expected 'higher' and got 'lower'
  The total attempts number was not accurate. It displayed that I have no more attempts when I still had 1 attempt left.
  The new game button does not work. It does nothing instead of clearing history and only resets attempts, but does not actually start a new game.

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
| 50 | 'higher' hint | 'lower' hint | Nothing added to the history tracker |
| 90 | 'lower' hint | 'higher' hint | Previous input added to history, but not current input |
| 64 | 'correct guess' | 'correct guess' | previous added to history, not current. |

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
