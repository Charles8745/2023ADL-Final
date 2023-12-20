
# ADL Final: m11203404 陳旭霖
以下內容包含:
* Contents description
* Build up environment
* Inference
* Human evaluation

## Contents description
- **Folder Dialogue_dataset:** This folder contains all generated dialogues and the Scenario Points (SP) for each dialogue.

- **Folder Human_evaluation_EXE:** The folder contains an executable file named "Human_evaluation.exe," which is designed for testers to assess Scenario Points for the conversation.

- **Folder Materials for reports:** The folder contains experimental results data utilized in the report.

- **Script Generate_dialogue.py:** This program is used to generate in-game dialogues.

- **Script Evaluate_Scenario_Points.py:** This code is used to iteratively assess all Scenario Points in dialogues within the dataset.

- **Script Oak_NPC.py:** This is the main program of the Game Agent, encompassing the entire architectural workflow. It enables users to engage in conversations with the Game Agent.


## Build up environment
- **Step1:** Please create and activate your venv(python=3.10.13) first

- **Step2:** install requirement.txt 
    ```
    pip install -r requirements.txt
    ```
## Inferance
- Execute Oak_NPC.py:
    ```
    python Oak_NPC.py -a <your openai api-key>
    ```
- Enter what you want to ask Oak
    ```
    trainer: <Type here>
    ```
- This is an example of a reply, where score is the Scenario Points for the previous conversation.
    ```
    trainer: Hi
    Oak: Hello there! Welcome to the Pokémon Training Center. How can I assist you today?
    score: 1
    ```
- If you want to leave the conversation, type ***exit***. After the conversation ends, a dialogue_log.json will be automatically saved to store conversation records.
    ```
    trainer: exit
    ```
## Human evaluation
- In the Human_evaluation_EXE folder, there is a Human_evaluation.exe execution file, which is used to allow testers to evaluate Scenario Points for 40 paragraphs of game dialogue. Below is an example of one of the conversations.
    ```
    Dialogue: 1

    trainer:
        Do Pokémon like to be petted, Professor Oak?
    Oak:
        Indeed! Many Pokémon enjoy being petted. It's a great way to bond with your Pokémon and strengthen your trainer-pokémon   
        relationship.

    Please enter 1 to 9: <Enter your evaluation>
    ```
## Contact
- Email: charles77778888asd@gmail.com 
- linkedin: www.linkedin.com/in/旭霖-陳-b34102277





