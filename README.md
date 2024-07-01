# llm-tool-4o
AI Studio PromptFlow custom tool sample

https://microsoft.github.io/promptflow/how-to-guides/develop-a-tool/customize_an_llm_tool.html

How to Create and Upload Your First Python Package to PyPI (freecodecamp.org) 
https://www.freecodecamp.org/news/how-to-create-and-upload-your-first-python-package-to-pypi/

Create and Use Tool Package
https://microsoft.github.io/promptflow/how-to-guides/develop-a-tool/create-and-use-tool-package.html

Create your own tool package
Your tool package should be a python package. To try it quickly, just use my-tools-package 0.0.1 and skip this section.

Prerequisites
Create a new conda environment using python 3.9 or 3.10. Run below command to install PromptFlow dependencies:

pip install promptflow
Install Pytest packages for running tests:

pip install pytest pytest-mock
Clone the PromptFlow repository from GitHub using the following command:

git clone https://github.com/microsoft/promptflow.git
Create custom tool package
Run below command under the root folder to create your tool project quickly:

python <promptflow github repo>\scripts\tool\generate_tool_package_template.py --destination <your-tool-project> --package-name <your-package-name> --tool-name <your-tool-name> --function-name <your-tool-function-name>
For example:

python D:\proj\github\promptflow\scripts\tool\generate_tool_package_template.py --destination hello-world-proj --package-name hello-world --tool-name hello_world_tool --function-name get_greeting_message
This auto-generated script will create one tool for you. The parameters destination and package-name are mandatory. The parameters tool-name and function-name are optional. If left unfilled, the tool-name will default to hello_world_tool, and the function-name will default to tool-name.

https://github.com/microsoft/promptflow/tree/main/examples/tools/tool-package-quickstart/my_tool_package
