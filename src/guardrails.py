"""
Rule-based Guardrails for the Pernod Ricard RAG Chatbot.
"""

import re


class GuardrailEngine:

    def __init__(self):

        self.competitors = [
            "johnnie walker",
            "jack daniels",
            "jim beam",
            "bacardi",
            "smirnoff",
            "captain morgan",
            "bombay sapphire",
            "tanqueray",
            "dewars"
        ]

        self.medical_keywords = [
            "pregnant",
            "pregnancy",
            "medicine",
            "medication",
            "antibiotic",
            "doctor",
            "disease",
            "health",
            "blood pressure",
            "diabetes",
            "cancer",
            "covid",
            "hospital"
        ]

        self.sales_keywords = [
            "buy",
            "purchase",
            "discount",
            "coupon",
            "cheap",
            "price",
            "delivery",
            "where can i buy",
            "order online"
        ]

        self.unsafe_keywords = [
            "get drunk",
            "blackout",
            "drink and drive",
            "underage drinking",
            "drink fast",
            "strongest alcohol",
            "kill someone",
            "suicide",
            "overdose"
        ]
        self.off_topic_keywords = [
            "python",
            "java",
            "c++",
            "javascript",
            "weather",
            "ipl",
            "cricket",
            "football",
            "quantum",
            "politics",
            "president",
            "prime minister",
            "stock market",
            "bitcoin",
            "leetcode"
        ]
    # -----------------------------------------

    def check_age(self, age):

        if age is None:
            return True, ""

        if age < 21:

            return (
                False,
                "I'm unable to provide alcohol-related information for users below the legal drinking age."
            )

        return True, ""

    # -----------------------------------------

    def check_competitor(self, query):

        q = query.lower()

        for brand in self.competitors:

            if brand in q:

                return (
                    False,
                    "I'm designed to answer questions related to Pernod Ricard and its brands."
                )

        return True, ""

    # -----------------------------------------

    def check_medical(self, query):

        q = query.lower()

        for word in self.medical_keywords:

            if word in q:

                return (
                    False,
                    "For medical advice regarding alcohol consumption, please consult a qualified healthcare professional."
                )

        return True, ""

    # -----------------------------------------

    def check_sales(self, query):

        q = query.lower()

        for word in self.sales_keywords:

            if word in q:

                return (
                    False,
                    "I'm unable to assist with purchasing, pricing or promotional requests."
                )

        return True, ""

    # -----------------------------------------

    def check_responsible_drinking(self, query):

        q = query.lower()

        for word in self.unsafe_keywords:

            if word in q:

                return (
                    False,
                    "Pernod Ricard promotes responsible drinking and cannot assist with requests encouraging harmful alcohol consumption."
                )

        return True, ""

    # -----------------------------------------
    def check_scope(self, query):

        q = query.lower()

        for word in self.off_topic_keywords:

            if word in q:

                    return (
                    False,
                    "I'm designed to answer questions related to Pernod Ricard, its brands and responsible alcohol information."
                    )

        return True, ""


    def validate(self, query, age=None):

        checks = [

            self.check_age(age),

            self.check_competitor(query),

            self.check_medical(query),

            self.check_sales(query),

            self.check_scope(query),

            self.check_responsible_drinking(query)

        ]

        for passed, message in checks:

            if not passed:

                return False, message

        return True, ""