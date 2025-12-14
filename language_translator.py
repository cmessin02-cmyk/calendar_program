from translate import Translator

def main():
    print("Simple CLI Language Translator")
    print("Example: Hola → English\n")

    text = input("Enter text to translate: ").strip()

    if not text:
        print("No text entered.")
        return

    try:
        translator = Translator(to_lang="en", provider="mymemory")
        translation = translator.translate(text)
        print("\nTranslated text:")
        print(translation)

    except Exception as e:
        print("\nTranslation failed.")
        print("Reason:", e)

if __name__ == "__main__":
    main()
