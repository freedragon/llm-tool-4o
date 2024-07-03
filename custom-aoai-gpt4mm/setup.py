from setuptools import find_packages, setup

PACKAGE_NAME = "custom_aoai_gpt4mm"

setup(
    name=PACKAGE_NAME,
    version="0.0.5",
    description="Custom Azure OpenAI Multi-Model support LLM tool.",
    packages=find_packages(),
    entry_points={
        "package_tools": ["custom_aoai_gpt4mm = custom_aoai_gpt4mm.tools.utils:list_package_tools"],
    },
    include_package_data=True,   # This line tells setuptools to include files from MANIFEST.in
)