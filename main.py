# Conversational AI with Gemini & PDF Export
# Author: Your Name
# Description:
# This script allows users to interact with Google's Gemini model in a Q&A loop,
# and saves the entire conversation (history) into a PDF file.

from google import genai
from google.genai import types
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet


# Initialize Gemini client
client = genai.Client(api_key="YOUR_API_KEY_HERE")

# Initialize conversation history
history = ""

while True:
    # Take user input
    user_ques = input("Ask The Question: ")

    # Generate model response
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=user_ques + history
    )
    model_ans = response.text

    # Print response in console
    print(model_ans)

    # Update history
    history += (
        "\nQuestion: " + user_ques +
        "\nAnswer: " + model_ans + ".\n"
    )

    # Ask user whether to continue
    while True:
        continue_choice = input(
            "Enter 'y' to continue the session or 'n' to terminate it: "
        ).lower()

        if continue_choice in ["y", "n"]:
            break
        else:
            print("Invalid input! Please enter 'y' or 'n'.")

    if continue_choice == "n":
        break

# Save conversation to PDF
pdf = SimpleDocTemplate("gemini_convo.pdf")
styles = getSampleStyleSheet()
story = [Paragraph(history, styles["Normal"])]
pdf.build(story)

print("✅ Conversation saved to gemini_convo.pdf")
