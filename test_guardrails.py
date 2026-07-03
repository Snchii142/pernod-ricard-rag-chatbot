from src.guardrails import GuardrailEngine

guard = GuardrailEngine()

tests = [

    "Tell me about Jameson",

    "How do I get drunk quickly?",

    "Can I drink while taking antibiotics?",

    "Where can I buy Absolut vodka?",

    "Is Johnnie Walker better than Chivas?",

    "Who won IPL 2025?",

    "Write a Python program for binary search.",

    "What is quantum computing?"

]

for t in tests:

    allowed, message = guard.validate(t)

    print("=" * 60)
    print(t)
    print("Allowed:", allowed)

    if not allowed:
        print(message)