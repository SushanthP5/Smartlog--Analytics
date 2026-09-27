"""
Course Title: Python Essentials (Dr. D. Lakshmi)
Platform: VITyarthi Project Ingestion Portal
Project Title: SmartLog Analytics System
Author: Sushanth P(Freshman, B.Tech CSE AIML)
Institution: VIT Bhopal University

"""

import sys

class SystemConfig:
    """Stores basic system settings and configurations."""
    BANNER_TEXT = "VIT BHOPAL UNIVERSITY - VITYARTHI PROJECT EVALUATION"
    TOP_CHAR_COUNT = 5
    MIN_LENGTH = 1


class DataIngestionModule:
    """
    MODULE 1: DATA INTAKE AND SANITATION
    Functional Requirement 1: Checks for valid inputs and cleans whitespace.
    Non-Functional Requirement: Reliability and Error Handling.
    """
    
    @staticmethod
    def validate_input(text_data):
        """Checks if the user input meets basic rules."""
        if not text_data or not isinstance(text_data, str):
            raise ValueError("Input Error: The provided data must be a valid text string.")

        
        cleaned_text = text_data.strip()
        if len(cleaned_text) < SystemConfig.MIN_LENGTH:
            raise ValueError("Input Error: Text content cannot be blank or empty.")
            
        return cleaned_text

    @classmethod
    def sanitize_text(cls, raw_input_text):
        """Cleans trailing spaces and normalizes line breaks."""
        print("\n[INFO] Starting Module 1: Ingesting raw input text...")
        
        # Run input validation check
        validated_text = cls.validate_input(raw_input_text)
        
        # Convert multi-line strings into a clean single line space format
        processed_text = " ".join(validated_text.splitlines())
        
        print("[INFO] Module 1 execution completed successfully.")
        return processed_text


class TextProcessingEngine:
    """
    MODULE 2: LINGUISTIC ANALYTICS ENGINE
    Functional Requirement 2: Scans text to calculate character and word statistics.
    Non-Functional Requirement: Efficiency (Processes data in a single clean loop).
    """
    
    @staticmethod
    def analyze_text_metrics(clean_text):
        """Calculates totals for characters, words, spaces, vowels, and consonants."""
        print("\n[INFO] Starting Module 2: Running text analytics engine...")
        
        # Initializing the summary dictionary
        results = {
            'total_characters': len(clean_text),
            'alphanumeric_chars': 0,
            'numeric_digits': 0,
            'blank_spaces': 0,
            'vowels': 0,
            'consonants': 0,
            'word_count': 0,
            'unique_words': 0
        }
        
        vowels_list = set("aeiouAEIOU")
        
        # Single-pass loop to count characters efficiently
        for char in clean_text:
            if char.isalnum():
                results['alphanumeric_chars'] += 1
            if char.isdigit():
                results['numeric_digits'] += 1
            if char.isspace():
                results['blank_spaces'] += 1
                
            if char.isalpha():
                if char in vowels_list:
                    results['vowels'] += 1
                else:
                    results['consonants'] += 1
                    
        # Splitting text into basic word lists
        words = clean_text.split()
        results['word_count'] = len(words)
        results['unique_words'] = len(set(words))
        
        print("[INFO] Module 2 metrics calculated successfully.")
        return results


class ReportingModule:
    """
    MODULE 3: STATISTICAL REPORTING DASHBOARD
    Functional Requirement 3: Finds character density maps and prints results.
    Non-Functional Requirement: Usability (Presents a clear console output).
    """
    
    @staticmethod
    def get_character_frequency(text_data):
        """Counts how many times each character appears and finds the top dense entries."""
        print("\n[INFO] Starting Module 3: Generating character frequency maps...")
        frequency_dict = {}
        
        for char in text_data:
            if char.isalnum():
                lower_char = char.lower()
                frequency_dict[lower_char] = frequency_dict.get(lower_char, 0) + 1
                
        # Sort characters based on frequency counts in descending order
        sorted_items = sorted(frequency_dict.items(), key=lambda x: x[1], reverse=True)
        return sorted_items[:SystemConfig.TOP_CHAR_COUNT]

    @staticmethod
    def print_final_report(metrics, top_characters):
        """Outputs a clean academic table layout summarizing all metrics."""
        print("\n" + "="*65)
        print(f" {SystemConfig.BANNER_TEXT} ")
        print("="*65)
        print("                       PROJECT RESULTS SUMMARY                   ")
        print("-"*65)
        print(f"  Total Character Count        : {metrics['total_characters']} units")
        print(f"  Total Word Count             : {metrics['word_count']} tokens")
        print(f"  Unique Vocabulary Words      : {metrics['unique_words']} unique units")
        print(f"  Alphanumeric Characters      : {metrics['alphanumeric_chars']}")
        print(f"  Numerical Digits Found       : {metrics['numeric_digits']}")
        print(f"  Blank Space Gaps             : {metrics['blank_spaces']}")
        print(f"  Vowel Density Count          : {metrics['vowels']}")
        print(f"  Consonant Balance Count      : {metrics['consonants']}")
        print("-"*65)
        print(f"  TOP {SystemConfig.TOP_CHAR_COUNT} MOST FREQUENT ALPHANUMERIC CHARACTERS:")
        
        if not top_characters:
            print("  [Notice] No alphanumeric characters were found in the text input.")
        else:
            for rank, (char, count) in enumerate(top_characters, 1):
                print(f"   Rank {rank} -> Character [{char}] appears {count} times")
        print("="*65)
        print("  [Status] Code Execution Pipeline Completed Successfully.")
        print("="*65 + "\n")


class MainProgramController:
    """Manages the main program lifecycle loop and interface inputs."""
    
    @classmethod
    def start_pipeline(cls):
        print("*" * 65)
        print(f" {SystemConfig.BANNER_TEXT} ")
        print(" Main Application Workflow: Active Terminal Mode ")
        print("*" * 65)
        print("\nPlease paste your text dataset or log files below.")
        print("When you are done, hit Enter, then use the following keys to process:")
        print(" - Windows Users: Press Ctrl + Z and then hit Enter.")
        print(" - Mac / Linux Users: Press Ctrl + D.\n")
        
        try:
            # Reads data from terminal until standard EOF trigger is hit
            user_text_input = sys.stdin.read()
            
            # Executing Module 1
            cleaned_text = DataIngestionModule.sanitize_text(user_text_input)
            
            # Executing Module 2
            calculated_metrics = TextProcessingEngine.analyze_text_metrics(cleaned_text)
            
            # Executing Module 3
            frequent_chars = ReportingModule.get_character_frequency(cleaned_text)
            
            # Visualizing the final dashboard
            ReportingModule.print_final_report(calculated_metrics, frequent_chars)
            
        except ValueError as val_error:
            print(f"\n[ERROR] Input Check Failed: {val_error}")
        except Exception as general_error:
            print(f"\n[ERROR] An unexpected pipeline issue occurred: {general_error}")
        finally:
            print("[INFO] Program process shut down safely.")

if __name__ == "__main__":
    MainProgramController.start_pipeline()
