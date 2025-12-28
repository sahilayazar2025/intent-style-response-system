Intent-Aware and Style-Adaptive Response System

# Overview of this project:
This project is a simple system that understands what type of
question a user is asking and responds in different styles.

The goal of this project is to show how user intent can be identified
using basic logic and how the same response can be presented in different
communication styles.

This task will be focusing on clarity and simplicity rather than complex models.
A rule based approach was used to keep the system simple and easy to understand. This avoids using complex models while still keeping the core idea of the task at hand.

# Purpose of the user's query.
The system classifies the user's queries into the following types:
1) Academic - questions related to learning 
2) Technical - questions related to coding or errors
3) Entertainment - questions related to fun 
4) Personal - questions related to feelings
5) General - queries that do not fall into the above four

# Response Styles
Available styles by the system:
- Overconfident Genius
- Nervous Intern
- Sarcastic Reviewer
- Calm Professor

# Run through on how the system works
1. The user enters a text query
2. The system checks for keywords to identify the purpose
3. A response style is selected based on the purpose
4. The response style is applied using predefined templates
5. The final response is shown to the user

#Example
Input:
Explain neural networks

Detected Intent:
Academic

Response (Calm Professor):
Let’s go through this step by step.
