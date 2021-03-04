# GlossaryMaker
Python application that allows you to create and update a glossary of English words.

By default it will provide translations in Russian, but you can change it in the main.py changing TARGET_LANGUAGE global variable

All the code needed located in main.py scrypt, hook-build needed only for executable compiling with PyInstaller, and if you will, don't forget to add ` --additional-hooks-dir "C:/Code/PYTHON/GlossaryMaker"` to your build request.
Althrough, there is an exe executable file, so you can directly launch it from windows, no compilation needed.
textDivider.py is just a tool to quickly decompose text to separate unique words.

The run process is straight forward.
When you'll launch an app, it will suggest you to enter words, separated by endlines and when you finish you'll just need to double enter.
If there won't be a glossary.xlsx file in the app directory, it will one and store data there. If there will be one, it will append new data.

Program makes transcrypt on it's own, using https://github.com/mphilli/English-to-IPA library, but for transaltion and example sentences it uses web services, so you should be aware of getting banned or restricted because of large number of requests.
