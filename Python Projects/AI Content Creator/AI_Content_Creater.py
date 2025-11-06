import datetime

class AIContentCreator:
    def __init__(self, version="1.0"):
        self.version = version

    # Generate content with topic, points, style
    def generate(self, topic, *points, **options):
        if topic.strip() == "":
            raise ValueError("Topic cannot be empty!")

        content = f"\n=== AI Generated Content ===\nTopic: {topic}\n"

        # Add bullet points if provided
        if points:
            for point in points:
                content += f"- {point}\n"
        else:
            content += "- Content coming soon...\n"

        # Style option
        style = options.get("style", "neutral")
        content += f"\n[Written in {style} style]\n"

        # Add version info
        content += f"\nGenerated with AI Content Creator v{self.version}"

        return content

    # Save generated content to a text file
    def save_to_file(self, topic, content, filename="generated_content.txt"):
        try:
            with open(filename, "a") as f:
                f.write(f"\n\n--- Generated on {datetime.datetime.now()} ---\n")
                f.write(f"Topic: {topic}\n")
                f.write(content)
                f.write("\n--- End of content ---\n")
        except Exception as e:
            print("Error while saving content:", e)
        finally:
            print("Saving process finished.")

    # Simple menu system
    def menu(self):
        print("\nChoose Content Type:")
        print("1. Blog")
        print("2. Caption")
        print("3. Email")

        choice = input("Enter choice (1/2/3): ")

        topic = input("Enter topic: ")
        if choice == "1":
            content = self.generate(topic, "Introduction", "Main Body", "Conclusion", style="formal")
        elif choice == "2":
            caption = lambda t: f"🔥 Hot take on {t}! #trending"
            content = caption(topic)
        elif choice == "3":
            content = self.generate(topic, "Greeting", "Main Message", "Closing", style="casual")
        else:
            content = "Invalid choice!"

        print(content)
        self.save_to_file(topic, content)


# ----------------- Run the App -----------------
app = AIContentCreator()

while True:
    app.menu()
    again = input("\nDo you want to generate more content? (y/n): ")
    if again.lower() != "y":
        print("Exiting AI Content Creator. Goodbye!")
        break
