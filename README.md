# 📊 CLI Language Analyzer

A lightweight command-line tool for linguistic analysis, written in Python.

## 🐍 Why Python?

We chose Python over C for this project because linguistic analysis is fundamentally about high-level string manipulation, not raw memory management.

While C is performant, implementing Unicode-aware string parsing is notoriously difficult. A character in C is just a byte, but a character in human language (like 'ř' or 'ö') can be multiple bytes. Python handles Unicode natively, allowing us to focus on the linguistic logic rather than reinventing text encoding parsers.

This tool achieves in 60 lines of readable Python what would require hundreds of lines of complex, error-prone code in C.

## 🚀 Usage

Since the script includes a shebang, you can run it directly on Linux.

1. Make the script executable:
```chmod +x main.py```

2. Run the analyzer:
```./main.py [flags] [file]```

## ⚙️ Flags & Options

* **-c, --count**: Show the total word count (tokens).
* **-u, --unique**: Show the number of unique words (types).
* -h, --help: Display the help message.

## 💡 Examples

Get the total word count:
```./main.py -c essay.txt```

Get the size of your vocabulary (unique words):
```./main.py -u essay.txt```

Get both statistics at once:
```./main.py -cu essay.txt```

## ⚠️ Limitation: CJK Support

Please note that this tool relies on whitespace to identify word boundaries.

* Supported: English, Czech, German, Russian, Korean (languages that use spaces).
* Not Supported: Standard Japanese, Chinese (languages without spaces).

If you use this tool on a standard Japanese text (e.g., "私は猫が好き"), it will count the entire sentence as 1 word. To analyze Japanese, you must manually insert spaces between words before running this tool.

## 📜 License

This project is open source and distributed under the GPLv3 License.
