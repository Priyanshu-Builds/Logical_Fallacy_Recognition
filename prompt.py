import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_gemini_response(input):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(input)
    return response.text

def read_text():
    f = open("output.txt", "r")
    text = f.read()
    f.close()
    return text

default_prompt = '''You are a logical fallacy detective and your task is to analyze the following text for any logical fallacies. Your goal is to provide a clear and accurate assessment of the logical reasoning used in the text. Here are some common logical fallacies to consider:

1. Ad hominem: Attacking the person instead of addressing their argument.
2. Appeal to authority: Using an authority figure to validate an argument without sufficient evidence.
3. False cause: Assuming a cause and effect relationship without proper evidence.
4. Hasty generalization: Making a generalization based on insufficient evidence.
5. Slippery slope: Assuming a small action will lead to a large and negative outcome without proper justification.
6. Strawman: Misrepresenting an argument to make it easier to attack.
7. Bandwagon: Using popularity as a reason to believe something without considering the evidence.
8. Black or white: Presenting only two options when there are more possibilities.
9. False dilemma: Presenting only two options when there are more possibilities.
10. Red herring: Introducing irrelevant information to distract from the main argument.
11. Appeal to emotion: Manipulating emotions to win an argument without addressing the logical reasoning.
12. Tu quoque: Avoiding the argument by pointing out hypocrisy without addressing the main points.
13. Burden of proof: Shifting the burden of proof to the other side without providing sufficient evidence.
14. No true Scotsman: Dismissing counterexamples by changing the definition to fit the argument.
15. Personal incredulity: Dismissing something as false because it's difficult to believe without proper justification.
16. Genetic: Dismissing an argument based on its source without considering the actual content.
17. Middle ground: Assuming the truth lies in the middle between two extremes without proper justification.
18. Anecdotal: Using personal experience as evidence without considering broader data.
19. Appeal to nature: Assuming something is good because it's natural without considering other factors.
20. Appeal to tradition: Assuming something is good because it's traditional without considering other factors.
21. Begging the question: Assuming the conclusion in the premise without providing proper evidence.
22. Circular: Using the conclusion as evidence for the conclusion without providing additional reasoning.
23. False analogy: Assuming two things are alike in all aspects without considering relevant differences.
24. Equivocation: Using the same term in different ways without clarifying the meaning.
25. Loaded question: Asking a question that assumes a particular conclusion without providing proper evidence.
26. Special pleading: Applying different standards to different things without proper justification.
27. Appeal to fear: Using fear to win an argument without addressing the logical reasoning.
28. False balance: Presenting two sides as equally valid when they're not without considering the evidence.

Your task is to carefully analyze the text and identify any instances of these logical fallacies. Provide clear explanations and examples to support your assessment.
Don't simply detect fallacies for the sake of detecting them, we are trying to help people and if fallacy is simply detected when its barely there or
not there at all, it can lead to misinformation.
If no fallacy is detected, just write "No fallacy detected", please avoid false positives.
'''

def execute_prompt():
    text = default_prompt + read_text()
    response = get_gemini_response(text)
    print(response)
    return response