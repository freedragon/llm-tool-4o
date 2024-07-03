# llm-tool-4o
AI Studio PromptFlow custom tool sample

```bash
python promptflow/scripts/tool/generate_tool_package_template.py --destination my-vision-llm --package-name my-vision-llm --tool-name my-vision-llm --function-name my-vision-tool
```

* Promptflow에서 사용할 수 있는  Custom Tool을 제작하는데 필요한 정보를 정리한 리포 입니다. Azure OpenAI GPT-4V Preview툴을 변경한 커스텀 툴의 소스 코드는 아래 URL을 참고 하세요. (리포 아래 서브 폴더)  
    https://github.com/freedragon/llm-tool-4o/tree/master/custom-aoai-gpt4mm 
* LLM툴을 커스터 마이징 하는 방법은 아래 문서를 우선 참고 하세요.  
    [Create and Use Tool Package](https://microsoft.github.io/promptflow/how-to-guides/develop-a-tool/create-and-use-tool-package.html)

커스텀 툴 제작을 위한 순서는 대략 다음과 같습니다:

1. 아나콘다 또는 파이썬 가상환경 등의 방식으로 개발 환경을 우선 셋팅 했다고 보고,
2. Custom Tool을 제작하는데 사용 되는 주요 패키지들을 설치 합니다.
```bash
# 프롬프트 플로우 기본 패키지
pip install promptflow

# 유닛 테스트 용 패키지 설치
pip install pytest pytest-mock

# PyPi 업로드 영 패키지 설치
pip install twine
```
3. 툴의 제작에 필요한 파일들이 저장될 폴더를 만들고 해당 폴더로 디렉토리를 변경 합니다.
4. 아래 명령을 수행해서 promptflow의 소스 코드를 다운로드 합니다. 
```bash
git clone https://github.com/microsoft/promptflow.git
```
[!WARNING] 여기서 한가지 문제가, AI Studio, 파이썬의 모듈과 깃헙에 저장된 코드들의 버젼이 완전히 일치하지 않습는 부분 입니다. 오류의 형태에 따라서 패키지를 다운그레이드 할 수 있습니다.

5. 소스코드가 같은 폴더에 다운로드 했다고 가정하고, 다음 명령을 수행하면 Took을 만들 수 있는 프로젝트 템플릿이 만들어 집니다. 만일 폴더에 destionation 폴더 (아래에서 hello-world-proj)와 같은 이름의 폴더가 있으면 오류가 발생 합니다.
```bash
python D:\proj\github\promptflow\scripts\tool\generate_tool_package_template.py --destination hello-world-proj --package-name hello-world --tool-name hello_world_tool --function-name get_greeting_messagename>
```
6. 생성 된 폴더의 구조는 대략 다음과 같습니다. 주로 변경이 필요한 부분은 ```hello_world_tool.py```, ```hello_world_tool.yaml```와 ```test_hello_world_tool.py``` 파일들입니다만, 소스코드나 설정등이 변경 되면 ```setup.py``` 파일의 버젼 역시 변경을 해 주어야 빌드된 패키지 파일의 업로드 및 설치이 용이 해 집니다.

```markdown
hello-world-proj/    
│    
├── hello_world/    
│   ├── tools/    
│   │   ├── __init__.py    
│   │   ├── hello_world_tool.py    
│   │   └── utils.py    
│   ├── yamls/    
│   │   └── hello_world_tool.yaml    
│   └── __init__.py    
│    
├── tests/     
│   ├── __init__.py    
│   └── test_hello_world_tool.py    
│    
├── MANIFEST.in    
│    
└── setup.py  
```
7. 코드의 유닛테스트 가 필요한 경우 ```test_hello_world_tool.py```을 업데이트 하고 아래 명령을 수행 합니다. (프로젝트 폴더에서 실행 되어야 합니다.
```bash
pytest tests
```
8. 배포가 준비 된 상태에서 아래 명령을 프로젝트 폴더에서 수행 하면 ```dist``` 폴더가 생성 되고, 휠(WHL) 파일과 Tar.gz파일이 생성 됩니다. 패키지의 업로드는 별도의 명령을 사용 합니다.
```bash
python setup.py sdist bdist_wheel
```
9. 실제 PyPi에 dist 폴더의 내용을 업로드 해 볼 수 도 있겠습니다만, 우선 테스트를 위해서 test.pypi.org에 계정을 만들고 업로드 및 설치 테스트를 해 볼 수 있습니다. 사용법과 구조는 거의 동일 하지만, 공식적인 사이트와 테스트 사이트가 제종 됩니다.
패키지 업로드 명령과 다음과 같습니다. 위에서 설치한 twine 명령을 사용 합니다.
```bash
twine upload --repository testpypi dist/* 
```
아래 문서도 참고 하세요.

[How to Create and Upload Your First Python Package to PyPI (freecodecamp.org)](https://www.freecodecamp.org/news/how-to-create-and-upload-your-first-python-package-to-pypi/)

다음은 실제 실행 결과 샘플 입니다.
```bash
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
test.pypi.org에 업로드 된 패키지 설치 방법은 아래와 같습니다. 패키지 이름이 custom-tool-pkg로 가정한 샘플 입니다.

```bash
pip install --index-url https://test.pypi.org/simple/ --no-deps custom-tool-pkg 
```

### 제작한 툴을 AI Studio에서 리스트 되고 사용 가능 하도록 하는 방법

아래 문서에서 새로 만들어진 도구들을 AI Studio 나 VS Code를 이용해서 설정 및 테스트 하는 방법등에 대해 설명하고 있습니다.

[사용자 지정 도구 패키지 만들기 및 사용](https://learn.microsoft.com/ko-kr/azure/machine-learning/prompt-flow/how-to-custom-tool-package-creation-and-usage?view=azureml-api-2)
[Custom tool package creation and usage](https://learn.microsoft.com/en-us/azure/machine-learning/prompt-flow/how-to-custom-tool-package-creation-and-usage?view=azureml-api-2)

#### 첫번째 방법은 특정 프롬프트 플루우에서만 사용 하도록 프로젝트 내에 파이썬의 requirements.txt에 지정하는 방법 입니다.
1. 컴퓨트 세션을 시작하고, 플로우가 저장된 폴더에 requirements.txt 파일을 만들고
2. 파일에 새로 제작된 툴의 패키지 이름을 리스트 합니다.
3. 필요하면 버젼 역시 지정 합니다. (예을 들어, my-tool-pbckage==0.0.1)

![requirements.txt 수장 방법 (AI Studio)](https://learn.microsoft.com/en-us/azure/machine-learning/prompt-flow/media/how-to-custom-tool-package-creation-and-usage/install-package-on-compute-session.png?view=azureml-api-2)

이 방식의 문제점은 툴을 사용하는 모든 플로우를 위해서 폴더에 requirements.txt 파일을 저장해야 하고, 프로젝트나 툴의 종류가 많아지면 관리할 곳이 많아지는 문제등이 있겠습니다.

#### 플로우가 실행 되는 도커 이미지에 추가 하는 방법

AI Studio (또는 AzureML Studio)에서 플로우를 실행하는 환경이 컨테이너 환경이고, 이 환경에서 실행 되는 이미지에 도구를 기본적으로 포함 하도록 도커 이미지를 다시 만들어서 등록 하는 방법 입니다.

아래의 두개 문서의 내용을 참고 하세요. 첫번째 문서는: 

1. 개별 요구 조건에 맞는 이미지를 제작하는 방법에 대해서, 
> [컴퓨팅 세션에 대한 기본 이미지 사용자 지정](https://learn.microsoft.com/ko-kr/azure/machine-learning/prompt-flow/how-to-customize-session-base-image?view=azureml-api-2)
> [Customize base image for compute session](https://learn.microsoft.com/en-us/azure/machine-learning/prompt-flow/how-to-customize-session-base-image?view=azureml-api-2)

2. 두번째는 이들 이미지를 실행 되는 컴퓨팅 환경의 기본 이미지로 설정 하는 방법에 대해서 설명하고 있습니다.
> [컴퓨팅 세션의 기본 이미지 변경](https://learn.microsoft.com/ko-kr/azure/machine-learning/prompt-flow/how-to-manage-compute-session?view=azureml-api-2&tabs=cli#change-the-base-image-for-compute-session)
> [Change the base image for compute session](https://learn.microsoft.com/en-us/azure/machine-learning/prompt-flow/how-to-manage-compute-session?view=azureml-api-2&tabs=cli#change-the-base-image-for-compute-session)


### 기타 주요 링크들

[How to Create and Upload Your First Python Package to PyPI (freecodecamp.org)](https://www.freecodecamp.org/news/how-to-create-and-upload-your-first-python-package-to-pypi/)

[Create and Use Tool Package](https://microsoft.github.io/promptflow/how-to-guides/develop-a-tool/create-and-use-tool-package.html)

[ChatWithPdf sample document:](https://github.com/microsoft/promptflow/blob/main/examples/tutorials/e2e-development/chat-with-pdf.md)

https://github.com/microsoft/promptflow/tree/main/examples/tools/tool-package-quickstart/my_tool_package
