# PR Police Boilerplate

## Overview

Simple PR Police Bot that does the following:

1. Reviews the changed code on three criteria: PEP-8 compliance, security considerations, and possible bugs.
2. Puts in-line comments as needed. This is an imperfect feature at the moment and needs more work.
3. Gives a verdict of either CONDITIONALLY ACCEPTED or REJECTED depending on whether there is an immediate security concern. If REJECTED, then the pipline will register as FAILED.
4. Generates unit tests for the new code.

## File Structure

1. All PR Police files are in `pr_police`.
    * workflows naturally contains the Github action workflow
    * `app.py` contains the script to serve the LLM locally
    * `review.py` is what the workflow calls to forward the PR code diff to the LLM
    * `send.py` is just a test script to check if the model is operational
    * `setup.sh` is for first-time set up on machines that will be used as runners
2. All actual project files will be placed anywhere but the `pr_police` folder.

## Set up

1. Ensure that your intended runner has [Ollama](https://ollama.com/download) and [Python](https://www.python.org/downloads/) installed.
2. Next, make sure that the repository has the `.github` folder and `pr_police` folder as these contain the scripts needed. There is no need to change anything in these files.
3. [Register the machine as a runner](https://docs.github.com/en/actions/how-tos/manage-runners/self-hosted-runners/add-runners) for the repository. It should be a simple matter of just following the instructions on the documentation. At the end of it all, the machine should now be actively polling requests from Github.
4. Once done, open the terminal and run `ollama run qwen2.5-coder:7b`. If you have changed the model to use, obviously change this command accordingly as well.
5. Do `pip install -r requirements.txt` to install the dependencies.
6. Open up another terminal and `cd pr_police` then `uvicorn app:app --reload` to launch the app that forwards requests from Github to the model running via Ollama. This app acts like a middleman to pass along requests to and from the model and Github.

After the above, the PR Police Bot should now be enabled for the repository.

To summarize, the runner will have the following components running:
1. Ollama server for the LLM.
2. FastAPI app for the middleman application that routes requests and responses between Github and the LLM.
3. Github Runner server that polls for requests/responses from Github.

Now, is there a more optimal way? Good question. Let's see, as this is a WIP! :)

## Improvement Points

1. Is there a more optimal way to set-up the flow without compromising the fact that we are running this entirely for free? I.e., what can we do given that we adhere to the principle of "less is more"?
2. Is there a more optimal way to do prompt engineering for the model?
3. How can we measure model performance?
4. Do we need to go beyond prompt engineering and use techniques like fine-tuning or RAG? And if we do, for what reason do we do it?