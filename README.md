# GlossaryMaker
Python application to create and update a glossary of English words.

By default, it will provide translations in Russian, but you can change it in the main.py changing the TARGET_LANGUAGE global variable

All the code needed located in main.py script, hook-build needed only for executable compiling with PyInstaller, and if you will, don't forget to add `--additional-hooks-dir "path_to_project_dir/GlossaryMaker"` to your build request. Although, there is an exe executable file, so you can directly launch it from windows, no compilation needed. textDivider.py is just a tool to quickly decompose text to separate unique words.

The run process is straight forward. When you'll launch an app, it will suggest you enter words, separated by endlines and when you finish you'll just need to double enter. If there won't be a glossary.xlsx file in the app directory, it will make one and store data there. If there will be one, it will append new data.

The program makes a transcript on its own, using https://github.com/mphilli/English-to-IPA library, but for translation and example sentences it uses web services, so you should be aware of getting banned or restricted because of the large number of requests.
