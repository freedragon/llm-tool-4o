# llm-tool-4o
AI Studio PromptFlow custom tool sample

python promptflow/scripts/tool/generate_tool_package_template.py --destination my-vision-llm --package-name my-vision-llm --tool-name my-vision-llm --function-name my-vision-tool

 
```
(pf-tools) freedragon@yonghp-030221:~/work/pf-tools/prompty-qs/my-vision-llm$ twine upload --repository testpypi dist/* 
Uploading distributions to https://test.pypi.org/legacy/ 
Uploading my_vision_llm-0.0.1-py3-none-any.whl 
100% ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 6.2/6.2 kB • 00:00 • ? 
Uploading my_vision_llm-0.0.1.tar.gz 
100% ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 4.7/4.7 kB • 00:00 • ? 
View at: 
https://test.pypi.org/project/my-vision-llm/0.0.1/ 
(pf-tools) freedragon@yonghp-030221:~/work/pf-tools/prompty-qs/my-vision-llm$ 
```

How to Create and Upload Your First Python Package to PyPI (freecodecamp.org)  
https://microsoft.github.io/promptflow/how-to-guides/develop-a-tool/customize_an_llm_tool.html
```
pip install --index-url https://test.pypi.org/simple/ --no-deps basicpkg 
```

How to Create and Upload Your First Python Package to PyPI (freecodecamp.org) 
https://www.freecodecamp.org/news/how-to-create-and-upload-your-first-python-package-to-pypi/

Create and Use Tool Package
https://microsoft.github.io/promptflow/how-to-guides/develop-a-tool/create-and-use-tool-package.html

**ChatWithPdf sample document:**
https://github.com/microsoft/promptflow/blob/main/examples/tutorials/e2e-development/chat-with-pdf.md

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
